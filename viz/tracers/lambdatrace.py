"""code-viz lambda-calculus step recorder.

Full manual: the header of code-viz (`code-viz readme`, or README.md), sections 13 Tips (Lambda predefined names), 14 Trace format (lambda).

Parses a lambda term and reduces it step by step, in normal order and in applicative order,
recording the term tree and which redex is reduced next at every step. Pure Python, so it also
runs in the browser (Pyodide).

Syntax: \\x.body or λx.body (several binders allowed: λx y.body), application by juxtaposition,
parentheses for grouping, identifiers of letters, digits, _ and '. Lines starting with # or -- are
comments. Definitions "NAME = term" on earlier lines are substituted into the last line, so a block
can define TRUE, FALSE, AND and then reduce AND TRUE FALSE.

Usage:  python3 lambdatrace.py TERMFILE [--max-steps N] > trace.json

PIPELINE
  Called by driver.py in the python runner (viz=lambda), and by the viewer in the browser
  (Pyodide) for Edit and Run, so lambda terms can be typed and reduced on a phone.

TRACE FIELDS WRITTEN
  kind "lambda", language "lambda", source, expression, definitions, prelude_used ({name: term}
  for each predefined name the term used), orders: {normal: steps, applicative: steps}, steps
  (= normal), stdout (the normal form), error, truncated. A step is {term, tree, redex}; a tree
  node is {k: var|lam|app, ...}; redex is a path of f/a/b moves, or null at normal form.

OPTIONS  --max-steps N (default 200).   ENVIRONMENT  none.

DIRECTIVES IN THE SOURCE
  NAME = term      a definition, substituted into the last line
  -- free: B C     keep these names as plain variables instead of the predefined combinators
  # or --         comment lines

EXAMPLES
  printf 'AND TRUE FALSE\n' > t.lam && python3 lambdatrace.py t.lam > t.json
  printf -- '-- free: B\nC K A B\n' > t.lam && python3 lambdatrace.py t.lam   # B stays a variable

LIMITS AND KNOWN PROBLEMS
  - Predefined names (PRELUDE, below) are substituted for any free name that matches, so a
    variable called B, C, I, K or S becomes that combinator unless the block says "-- free: B"
    or uses lowercase names. The viewer lists the predefined names a term used.
  - Reduction stops at max_steps (200); a diverging term (OMEGA, Y under applicative order)
    shows as truncated.
"""
import json
import re
import sys

TOKEN = re.compile(r"\s*(λ|\\|\.|\(|\)|=|[A-Za-z0-9_']+)")


class Var:
    def __init__(self, n): self.n = n
class Lam:
    def __init__(self, v, b): self.v, self.b = v, b
class App:
    def __init__(self, f, a): self.f, self.a = f, a


def tokens(s):
    out, i = [], 0
    s = s.strip()
    while i < len(s):
        m = TOKEN.match(s, i)
        if not m:
            raise SyntaxError(f"unexpected character {s[i]!r} at {i}")
        out.append(m.group(1))
        i = m.end()
    return out


def parse(toks):
    pos = [0]

    def peek():
        return toks[pos[0]] if pos[0] < len(toks) else None

    def eat(t=None):
        tok = peek()
        if t is not None and tok != t:
            raise SyntaxError(f"expected {t!r}, got {tok!r}")
        pos[0] += 1
        return tok

    def term():
        if peek() in ("λ", "\\"):
            eat()
            names = []
            while peek() not in (".", None):
                names.append(eat())
            eat(".")
            body = term()
            for n in reversed(names):
                body = Lam(n, body)
            return body
        t = atom()
        while peek() not in (None, ")"):
            if peek() in ("λ", "\\"):
                t = App(t, term())
                break
            t = App(t, atom())
        return t

    def atom():
        tok = peek()
        if tok == "(":
            eat("(")
            t = term()
            eat(")")
            return t
        if tok is None or tok in (")", ".", "="):
            raise SyntaxError(f"unexpected {tok!r}")
        eat()
        return Var(tok)

    t = term()
    if peek() is not None:
        raise SyntaxError(f"unexpected {peek()!r}")
    return t


def free(t):
    if isinstance(t, Var):
        return {t.n}
    if isinstance(t, Lam):
        return free(t.b) - {t.v}
    return free(t.f) | free(t.a)


def fresh(v, avoid):
    i = 1
    while f"{v}{i}" in avoid:
        i += 1
    return f"{v}{i}"


def subst(t, x, s):
    if isinstance(t, Var):
        return s if t.n == x else t
    if isinstance(t, App):
        return App(subst(t.f, x, s), subst(t.a, x, s))
    if t.v == x:
        return t
    if t.v in free(s):
        nv = fresh(t.v, free(s) | free(t.b) | {x})
        return Lam(nv, subst(subst(t.b, t.v, Var(nv)), x, s))
    return Lam(t.v, subst(t.b, x, s))


def find_redex(t, order, path=()):
    """Path (tuple of 'f'/'a'/'b') to the next redex, or None when in normal form."""
    if isinstance(t, App):
        if order == "applicative":
            for side, sub in (("f", t.f), ("a", t.a)):
                p = find_redex(sub, order, path + (side,))
                if p is not None:
                    return p
            if isinstance(t.f, Lam):
                return path
            return None
        if isinstance(t.f, Lam):
            return path
        p = find_redex(t.f, order, path + ("f",))
        return p if p is not None else find_redex(t.a, order, path + ("a",))
    if isinstance(t, Lam):
        return find_redex(t.b, order, path + ("b",))
    return None


def at(t, path):
    for p in path:
        t = getattr(t, p)
    return t


def replace(t, path, new):
    if not path:
        return new
    p, rest = path[0], path[1:]
    if isinstance(t, App):
        return App(replace(t.f, rest, new), t.a) if p == "f" else App(t.f, replace(t.a, rest, new))
    return Lam(t.v, replace(t.b, rest, new))


def show(t):
    if isinstance(t, Var):
        return t.n
    if isinstance(t, Lam):
        return f"λ{t.v}.{show(t.b)}"
    f = show(t.f) if not isinstance(t.f, Lam) else f"({show(t.f)})"
    a = show(t.a) if isinstance(t.a, Var) else f"({show(t.a)})"
    return f"{f} {a}"


def tree(t, path=()):
    p = "".join(path)
    if isinstance(t, Var):
        return {"k": "var", "n": t.n, "path": p}
    if isinstance(t, Lam):
        return {"k": "lam", "v": t.v, "b": tree(t.b, path + ("b",)), "path": p}
    return {"k": "app", "f": tree(t.f, path + ("f",)), "a": tree(t.a, path + ("a",)), "path": p}


def reduce_all(t, order, max_steps):
    steps = []
    for _ in range(max_steps):
        r = find_redex(t, order)
        steps.append({"term": show(t), "tree": tree(t), "redex": None if r is None else "".join(r)})
        if r is None:
            return steps, False
        red = at(t, r)
        t = replace(t, r, subst(red.f.b, red.f.v, red.a))
    return steps, True


# Standard Church encodings, used only for names a block does not define itself, so a block like
# "AND TRUE FALSE" or "SUCC TWO" reduces without spelling every definition out.
PRELUDE = {
    "TRUE": "λt f.t", "FALSE": "λt f.f", "AND": "λp q.p q p", "OR": "λp q.p p q", "NOT": "λp.p (λt f.f) (λt f.t)",
    "IF": "λb t f.b t f", "ZERO": "λf x.x", "ONE": "λf x.f x", "TWO": "λf x.f (f x)", "THREE": "λf x.f (f (f x))",
    "FOUR": "λf x.f (f (f (f x)))", "SUCC": "λn f x.f (n f x)", "PLUS": "λm n f x.m f (n f x)",
    "MULT": "λm n f.m (n f)", "ISZERO": "λn.n (λx.λt f.f) (λt f.t)", "PAIR": "λa b s.s a b",
    "FST": "λp.p (λa b.a)", "SND": "λp.p (λa b.b)", "I": "λx.x", "K": "λx y.x", "KI": "λx y.y",
    "S": "λx y z.x z (y z)", "C": "λf x y.f y x", "B": "λf g x.f (g x)", "OMEGA": "(λx.x x) (λx.x x)",
}


def worked_term(src):
    """A deck's worked reduction: the first line is the term, the following lines (->β ..., = ...)
    are the hand derivation with comments. Returns the term, or None if the block is not one."""
    lines = [l for l in src.splitlines() if l.strip()]
    if len(lines) < 2 or not all(re.match(r"^\s*(->|→|=)", l) for l in lines[1:]):
        return None
    return re.split(r"\s{2,}|#|->|→", lines[0].strip())[0].strip()


def load(src):
    """Returns (term, expression text, definitions, prelude names used). A comment line
    "-- free: B C" (or "# free: B C") keeps those names as plain variables instead of the
    predefined combinators, so `C K a B` can use B as a variable."""
    defs, last, keep_free = {}, None, set()
    w = worked_term(src)
    if w:
        src = w
    for line in src.splitlines():
        s = line.strip()
        fm = re.match(r"^(?:#|--)\s*free\s*:\s*(.+)$", s, re.I)
        if fm:
            keep_free.update(fm.group(1).replace(",", " ").split())
            continue
        if not s or s.startswith("#") or s.startswith("--"):
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_']*)\s*=\s*(.+)$", s)
        if m:
            defs[m.group(1)] = m.group(2)
        else:
            last = s
    if last is None and defs:
        last = list(defs)[-1]
    own = set(defs)
    for k, v in PRELUDE.items():
        if k not in keep_free:
            defs.setdefault(k, v)
    t = parse(tokens(last))
    used = sorted(n for n in free(t) if n in defs and n not in own and n in PRELUDE)
    for _ in range(20):  # expand definitions (outermost first), so names stay readable at step 0
        names = [n for n in free(t) if n in defs]
        if not names:
            break
        for n in names:
            t = subst(t, n, parse(tokens(defs[n])))
    return t, last, defs, used


def trace_source(src, max_steps=200):
    t, expr, defs, used = load(src)
    normal, cut1 = reduce_all(t, "normal", max_steps)
    applicative, cut2 = reduce_all(t, "applicative", max_steps)
    return {"version": 1, "kind": "lambda", "language": "lambda", "source": src, "expression": expr,
            "definitions": defs, "prelude_used": {n: PRELUDE[n] for n in used}, "orders": {"normal": normal, "applicative": applicative},
            "steps": normal, "stdout": normal[-1]["term"] + "\n", "error": None,
            "truncated": cut1 or cut2}


if __name__ == "__main__":
    a = sys.argv
    n = int(a[a.index("--max-steps") + 1]) if "--max-steps" in a else 200
    try:
        out = trace_source(open(a[1], encoding="utf-8").read(), n)
    except Exception as e:
        out = {"version": 1, "kind": "lambda", "error": f"{type(e).__name__}: {e}", "steps": [], "stdout": ""}
    json.dump(out, sys.stdout)
