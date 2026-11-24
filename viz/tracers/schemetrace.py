"""code-viz Scheme step recorder.

Full manual: the header of code-viz (`code-viz readme`, or README.md), sections 8 Reading the viewer (env, Scheme), 9 Student mode, 14 Trace format.

A small Scheme interpreter that records, for each procedure call and special form it evaluates,
the expression, the environment chain (each frame and its bindings) and the closures in it, so the
viewer can draw environment diagrams for binding, scope and closures. Pure Python, so it also runs
in the browser (Pyodide). The runner also runs the program in Guile; if the outputs differ the
trace is marked "approximate" and Guile's output is the one checked.

Supported: define (variables and procedures), lambda, let, let*, letrec, named let, if, cond, case,
when, unless, begin, set!, quote and ', and, or, numbers, strings, #t/#f, characters as strings,
and the usual list, arithmetic, comparison, string and output procedures.

Usage:  python3 schemetrace.py PROGRAM.scm [--max-steps N] > trace.json

PIPELINE
  Called by driver.py in the scheme runner (viz=env, lang=scheme), which also runs the program in
  Guile through cviz-repl.scm; and by the viewer in the browser (Pyodide) for Edit and Run.

TRACE FIELDS WRITTEN
  kind "env", language "scheme", source, stdout, error, truncated, approximate, and steps:
  {expr, note, env, chain: [env ids], frames: {id: {name, parent, vars}}, closures: {id: {name,
   params, env, body}}, out}. A value is {"p": printed} or {"c": closure id}. driver.py adds
  reference_stdout (Guile's output) and sets approximate when the two differ.

OPTIONS  --max-steps N (default 800).   ENVIRONMENT  none.

EXAMPLES
  python3 schemetrace.py closures.scm > closures.json
  # in the browser:  json.dumps(schemetrace.trace_source(code, 800))

LIMITS AND KNOWN PROBLEMS
  - A teaching subset, not full Scheme: no call/cc, macros, vectors or tail-call guarantees.
  - When its output differs from Guile's the trace is kept but marked approximate (2 CS374
    examples on 2026-11-14), and Guile's output is the one build --check compares.
"""
import json
import sys


class Sym(str):
    pass


class Nil:
    def __repr__(self): return "()"
NIL = Nil()


class Pair:
    def __init__(self, a, d): self.car, self.cdr = a, d


class Env:
    count = 0

    def __init__(self, parent=None, name="global"):
        Env.count += 1
        self.id, self.vars, self.parent, self.name = Env.count, {}, parent, name

    def find(self, k):
        e = self
        while e is not None:
            if k in e.vars:
                return e
            e = e.parent
        raise NameError(f"unbound variable: {k}")


class Closure:
    count = 0

    def __init__(self, params, rest, body, env, name="λ"):
        Closure.count += 1
        self.id, self.params, self.rest, self.body, self.env, self.name = Closure.count, params, rest, body, env, name


class Stop(Exception):
    pass


def tokenize(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == ";":
            while i < len(s) and s[i] != "\n":
                i += 1
        elif c.isspace():
            i += 1
        elif c in "()[]'`,":
            out.append(c if c not in "[]" else ("(" if c == "[" else ")"))
            i += 1
        elif c == '"':
            j, buf = i + 1, []
            while s[j] != '"':
                if s[j] == "\\":
                    j += 1
                    buf.append({"n": "\n", "t": "\t"}.get(s[j], s[j]))
                else:
                    buf.append(s[j])
                j += 1
            out.append(("str", "".join(buf)))
            i = j + 1
        else:
            j = i
            while j < len(s) and not s[j].isspace() and s[j] not in "()[]';":
                j += 1
            out.append(s[i:j])
            i = j
    return out


def read_all(src):
    toks = tokenize(src)
    pos = [0]

    def read():
        t = toks[pos[0]]
        pos[0] += 1
        if t == "(":
            items = []
            while toks[pos[0]] != ")":
                if toks[pos[0]] == ".":
                    pos[0] += 1
                    tail = read()
                    pos[0] += 1
                    return to_list(items, tail)
                items.append(read())
            pos[0] += 1
            return to_list(items)
        if t == "'":
            return to_list([Sym("quote"), read()])
        if isinstance(t, tuple):
            return t[1]
        if t == "#t" or t == "#true":
            return True
        if t == "#f" or t == "#false":
            return False
        if t.startswith("#\\"):
            return t[2:] if t[2:] not in ("space", "newline") else (" " if t[2:] == "space" else "\n")
        try:
            return int(t)
        except ValueError:
            try:
                return float(t)
            except ValueError:
                return Sym(t)
    exprs = []
    while pos[0] < len(toks):
        exprs.append(read())
    return exprs


def to_list(items, tail=NIL):
    out = tail
    for x in reversed(items):
        out = Pair(x, out)
    return out


def from_list(p):
    out = []
    while isinstance(p, Pair):
        out.append(p.car)
        p = p.cdr
    return out


def show(v, top=True):
    if v is True:
        return "#t"
    if v is False:
        return "#f"
    if v is NIL:
        return "()"
    if isinstance(v, Sym):
        return str(v)
    if isinstance(v, str):
        return v if top else '"' + v + '"'
    if isinstance(v, Pair):
        parts, p = [], v
        while isinstance(p, Pair):
            parts.append(show(p.car, False))
            p = p.cdr
        return "(" + " ".join(parts) + ("" if p is NIL else " . " + show(p, False)) + ")"
    if isinstance(v, Closure):
        return f"#<procedure {v.name}>"
    if callable(v):
        return "#<procedure>"
    if isinstance(v, float) and v.is_integer():
        return f"{v:.1f}"
    return str(v)


class Interp:
    def __init__(self, max_steps=600):
        self.out = []
        self.steps = []
        self.max_steps = max_steps
        self.envs = {}
        self.closures = {}
        self.g = Env()
        self.envs[self.g.id] = self.g
        self.install()

    def install(self):
        import math
        g = self.g.vars

        def num_fold(f, init):
            def h(*a):
                r = init if not a else a[0]
                for x in (a[1:] if a else []):
                    r = f(r, x)
                return r
            return h

        def sub(*a):
            return -a[0] if len(a) == 1 else num_fold(lambda x, y: x - y, 0)(*a)

        def div(*a):
            if len(a) == 1:
                return 1 / a[0]
            r = a[0]
            for x in a[1:]:
                r = r // x if isinstance(r, int) and isinstance(x, int) and r % x == 0 else r / x
            return r

        def cmp(f):
            return lambda *a: all(f(a[i], a[i + 1]) for i in range(len(a) - 1))

        def display(x, *_):
            self.out.append(show(x, True))
            return NIL

        def newline(*_):
            self.out.append("\n")
            return NIL

        def lst_append(*ls):
            items = []
            for l in ls[:-1]:
                items += from_list(l)
            return to_list(items, ls[-1] if ls else NIL)

        g.update({
            "+": num_fold(lambda x, y: x + y, 0), "-": sub, "*": num_fold(lambda x, y: x * y, 1), "/": div,
            "=": cmp(lambda x, y: x == y), "<": cmp(lambda x, y: x < y), ">": cmp(lambda x, y: x > y),
            "<=": cmp(lambda x, y: x <= y), ">=": cmp(lambda x, y: x >= y),
            "quotient": lambda a, b: int(a / b), "remainder": lambda a, b: a - b * int(a / b),
            "modulo": lambda a, b: a % b, "abs": abs, "min": min, "max": max, "sqrt": math.sqrt,
            "expt": lambda a, b: a ** b, "exact->inexact": float, "number?": lambda x: isinstance(x, (int, float)) and not isinstance(x, bool),
            "zero?": lambda x: x == 0, "even?": lambda x: x % 2 == 0, "odd?": lambda x: x % 2 == 1,
            "positive?": lambda x: x > 0, "negative?": lambda x: x < 0, "add1": lambda x: x + 1, "sub1": lambda x: x - 1,
            "not": lambda x: x is False, "eq?": lambda a, b: a is b or (isinstance(a, (int, str)) and a == b),
            "eqv?": lambda a, b: a is b or a == b, "equal?": lambda a, b: show(a) == show(b),
            "cons": Pair, "car": lambda p: p.car, "cdr": lambda p: p.cdr, "cadr": lambda p: p.cdr.car,
            "cddr": lambda p: p.cdr.cdr, "caddr": lambda p: p.cdr.cdr.car, "list": lambda *a: to_list(list(a)),
            "null?": lambda x: x is NIL, "pair?": lambda x: isinstance(x, Pair), "list?": lambda x: x is NIL or isinstance(x, Pair),
            "length": lambda l: len(from_list(l)), "append": lst_append, "reverse": lambda l: to_list(from_list(l)[::-1]),
            "list-ref": lambda l, i: from_list(l)[i], "symbol?": lambda x: isinstance(x, Sym),
            "string?": lambda x: isinstance(x, str) and not isinstance(x, Sym), "procedure?": lambda x: callable(x) or isinstance(x, Closure),
            "boolean?": lambda x: isinstance(x, bool), "string-append": lambda *a: "".join(a),
            "number->string": lambda n: show(n), "string-length": len, "display": display, "newline": newline,
            "write": lambda x, *_: (self.out.append(show(x, False)), NIL)[1],
        })
        g["map"] = lambda f, *ls: to_list([self.apply(f, list(xs)) for xs in zip(*[from_list(l) for l in ls])])
        g["filter"] = lambda f, l: to_list([x for x in from_list(l) if self.apply(f, [x]) is not False])
        g["apply"] = lambda f, *a: self.apply(f, list(a[:-1]) + from_list(a[-1]))
        g["for-each"] = lambda f, *ls: ([self.apply(f, list(xs)) for xs in zip(*[from_list(l) for l in ls])], NIL)[1]
        g["foldl"] = lambda f, init, l: _fold(self, f, init, from_list(l))
        g["foldr"] = lambda f, init, l: _foldr(self, f, init, from_list(l))
        g["reduce"] = lambda f, init, l: _fold(self, f, init, from_list(l)) if from_list(l) else init

    # ---- recording -----------------------------------------------------------------------------
    def enc(self, v):
        if isinstance(v, Closure):
            self.closures[v.id] = v
            return {"c": v.id}
        if isinstance(v, Pair) or v is NIL:
            return {"p": show(v, False)}
        if callable(v):
            return {"p": "#<builtin>"}
        if isinstance(v, (int, float, bool)):
            return {"p": show(v)}
        return {"p": show(v, False)}

    def record(self, expr, env, note):
        if len(self.steps) >= self.max_steps:
            raise Stop()
        chain, e = [], env
        while e is not None:
            chain.append(e.id)
            e = e.parent
        frames = {}
        for eid, e in self.envs.items():
            if e is self.g:
                vars_ = {k: self.enc(v) for k, v in e.vars.items() if not callable(v) or isinstance(v, Closure)}
            else:
                vars_ = {k: self.enc(v) for k, v in e.vars.items()}
            frames[str(eid)] = {"name": e.name, "parent": e.parent.id if e.parent else None, "vars": vars_}
        clos = {str(c.id): {"name": c.name, "params": c.params + ([". " + c.rest] if c.rest else []),
                            "env": c.env.id, "body": show(to_list(c.body), False)[:120]} for c in self.closures.values()}
        self.steps.append({"expr": show(expr, False)[:160], "note": note, "env": env.id, "chain": chain,
                           "frames": frames, "closures": clos, "out": len("".join(self.out))})

    # ---- evaluation ----------------------------------------------------------------------------
    def apply(self, f, args):
        if isinstance(f, Closure):
            env = Env(f.env, name=f.name)
            self.envs[env.id] = env
            for p, a in zip(f.params, args):
                env.vars[p] = a
            if f.rest:
                env.vars[f.rest] = to_list(args[len(f.params):])
            self.record(to_list([Sym(f.name)] + args), env, f"call {f.name}")
            r = NIL
            for b in f.body:
                r = self.eval(b, env)
            return r
        return f(*args)

    def eval(self, x, env):
        if isinstance(x, Sym):
            return env.find(x).vars[x]
        if not isinstance(x, Pair):
            return x
        head, rest = x.car, from_list(x.cdr)
        if head == "quote":
            return rest[0]
        if head == "if":
            self.record(x, env, "if")
            if self.eval(rest[0], env) is not False:
                return self.eval(rest[1], env)
            return self.eval(rest[2], env) if len(rest) > 2 else NIL
        if head == "define":
            if isinstance(rest[0], Pair):
                ps, tail = rest[0].cdr, None
                plist = []
                while isinstance(ps, Pair):
                    plist.append(ps.car)
                    ps = ps.cdr
                if isinstance(ps, Sym):
                    tail = ps
                env.vars[rest[0].car] = Closure(plist, tail, rest[1:], env, str(rest[0].car))
            else:
                v = self.eval(rest[1], env)
                if isinstance(v, Closure) and v.name == "λ":
                    v.name = str(rest[0])
                env.vars[rest[0]] = v
            self.record(x, env, f"define {show(rest[0].car if isinstance(rest[0], Pair) else rest[0])}")
            return NIL
        if head == "set!":
            v = self.eval(rest[1], env)
            env.find(rest[0]).vars[rest[0]] = v
            self.record(x, env, f"set! {rest[0]}")
            return NIL
        if head == "lambda":
            ps, plist, tail = rest[0], [], None
            if isinstance(ps, Sym):
                tail = ps
            else:
                while isinstance(ps, Pair):
                    plist.append(ps.car)
                    ps = ps.cdr
                if isinstance(ps, Sym):
                    tail = ps
            c = Closure(plist, tail, rest[1:], env)
            self.closures[c.id] = c
            return c
        if head == "begin":
            r = NIL
            for b in rest:
                r = self.eval(b, env)
            return r
        if head in ("let", "let*", "letrec"):
            if isinstance(rest[0], Sym):  # named let
                name, binds, body = rest[0], from_list(rest[1]), rest[2:]
                loop_env = Env(env, name=f"let {name}")
                self.envs[loop_env.id] = loop_env
                c = Closure([b.car for b in map(lambda p: p, binds)], None, body, loop_env, str(name))
                loop_env.vars[name] = c
                return self.apply(c, [self.eval(b.cdr.car, env) for b in binds])
            binds, body = from_list(rest[0]), rest[1:]
            e = Env(env, name=str(head))
            self.envs[e.id] = e
            for b in binds:
                e.vars[b.car] = self.eval(b.cdr.car, e if head != "let" else env)
                if isinstance(e.vars[b.car], Closure) and e.vars[b.car].name == "λ":
                    e.vars[b.car].name = str(b.car)
            self.record(x, e, str(head))
            r = NIL
            for b in body:
                r = self.eval(b, e)
            return r
        if head == "cond":
            for clause in rest:
                parts = from_list(clause)
                if parts[0] == "else" or self.eval(parts[0], env) is not False:
                    r = NIL
                    for b in parts[1:]:
                        r = self.eval(b, env)
                    return r
            return NIL
        if head in ("when", "unless"):
            c = self.eval(rest[0], env) is not False
            if c == (head == "when"):
                r = NIL
                for b in rest[1:]:
                    r = self.eval(b, env)
                return r
            return NIL
        if head == "and":
            r = True
            for b in rest:
                r = self.eval(b, env)
                if r is False:
                    return False
            return r
        if head == "or":
            for b in rest:
                r = self.eval(b, env)
                if r is not False:
                    return r
            return False
        if head == "case":
            key = self.eval(rest[0], env)
            for clause in rest[1:]:
                parts = from_list(clause)
                if parts[0] == "else" or any(show(key) == show(d) for d in from_list(parts[0])):
                    r = NIL
                    for b in parts[1:]:
                        r = self.eval(b, env)
                    return r
            return NIL
        f = self.eval(head, env)
        args = [self.eval(a, env) for a in rest]
        return self.apply(f, args)


def _fold(it, f, acc, items):
    for x in items:
        acc = it.apply(f, [x, acc])
    return acc


def _foldr(it, f, acc, items):
    for x in reversed(items):
        acc = it.apply(f, [x, acc])
    return acc


def trace_source(src, max_steps=600):
    Env.count = 0
    Closure.count = 0
    it = Interp(max_steps)
    error, truncated = None, False
    sys.setrecursionlimit(10000)
    try:
        for e in read_all(src):
            v = it.eval(e, it.g)
            # like the REPL (and cviz-repl.scm): print the value of a top-level expression
            if not (isinstance(e, Pair) and e.car in ("define", "set!", "display", "newline")) and v is not NIL and v is not None:
                it.out.append(show(v, False) + "\n")
            it.record(e, it.g, "top level")
    except Stop:
        truncated = True
    except Exception as e:
        error = f"{type(e).__name__}: {e}"
    return {"version": 1, "kind": "env", "language": "scheme", "source": src, "steps": it.steps,
            "stdout": "".join(it.out), "error": error, "truncated": truncated}


if __name__ == "__main__":
    a = sys.argv
    n = int(a[a.index("--max-steps") + 1]) if "--max-steps" in a else 600
    json.dump(trace_source(open(a[1], encoding="utf-8").read(), n), sys.stdout)
