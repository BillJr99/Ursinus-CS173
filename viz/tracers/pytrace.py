"""code-viz Python step tracer.

Full manual: the header of code-viz (`code-viz readme`, or README.md), sections 8 Reading the viewer (env, Python), 9 Student mode, 14 Trace format.

Runs one Python program under sys.settrace and records, for every line executed in the program
itself: the line, the call stack (each frame's local variables), the objects those variables point
to (lists, dicts, tuples, sets, instances, functions and their closures), and the output so far.
Pure Python with no imports beyond the standard library, so the same file runs in the runner
container and in the browser (Pyodide) for live editing.

Usage:  python3 pytrace.py PROGRAM.py [--max-steps N] [--setup SETUP.py] > trace.json
In Pyodide: trace_source(code_string, max_steps) returns the trace as a dict.

PIPELINE
  Called by driver.py in the python runner (viz=env, lang=python), and by the viewer in the
  browser through Pyodide when someone presses Edit and Run (teacher or student mode).

TRACE FIELDS WRITTEN
  kind "env", language "python", source, stdout, error, truncated, and steps:
  {line, event (line|return|exception), stack: [{id, func, line, vars: {name: value}}],
   heap: {ref: object}, out (stdout so far), ret?, zombies? (frames kept alive by a closure)}.
  A value is {"p": primitive} or {"r": ref}; objects are {t: list|tuple|set|dict, items},
  {t: function, name, params, closure, parent} or {t: instance, class, attrs}. code-viz compacts
  heap per step on the site (heap_ids plus changed objects); the viewer expands it on load.

OPTIONS  --max-steps N (default 800).  --setup FILE: a label's setup= code, run first in the same
         globals, untraced and with its output discarded (trace_source(..., setup=) in Pyodide).   ENVIRONMENT  none.

EXAMPLES
  python3 pytrace.py closures.py > closures.json
  python3 pytrace.py loop.py --max-steps 2000 > loop.json
  # in the browser (what the viewer does):  json.dumps(pytrace.trace_source(code, 800))

LIMITS AND KNOWN PROBLEMS
  - Only the program's own lines are traced; library internals are not.
  - Large data structures make large traces; the step cap (800) cuts long runs (truncated=true).
  - input() reads the job's input text; with none it raises EOFError, which shows as an error.
"""
import io
import json
import sys
import types

PRIMS = (int, float, bool, str, type(None), complex)
ADDR = __import__("re").compile(r" at 0x[0-9a-fA-F]+")   # memory addresses change on every run
SKIP_NAMES = {"__builtins__", "__name__", "__doc__", "__package__", "__loader__", "__spec__",
              "__file__", "__cached__", "__annotations__"}


class Tracer:
    def __init__(self, filename, max_steps=800):
        self.filename = filename
        self.max_steps = max_steps
        self.steps = []
        self.out = io.StringIO()
        self.frame_ids = {}
        self.next_frame = 1
        self.zombies = {}      # frame id -> last snapshot of a returned frame whose cells live on
        self.truncated = False
        self.refs = {}         # id(object) -> (stable ref number, the object)

    # ---- encoding ----------------------------------------------------------------------------
    def enc(self, v, heap, depth=0):
        if isinstance(v, PRIMS):
            if isinstance(v, float) and v != v:
                return {"p": "nan"}
            if isinstance(v, str) and len(v) > 200:
                return {"p": v[:200] + "..."}
            if isinstance(v, complex):
                return {"p": repr(v)}
            return {"p": v}
        ref = self.ref(v)
        if ref not in heap and depth < 6 and len(heap) < 400:
            heap[ref] = None  # reserve, so cycles terminate
            heap[ref] = self.enc_obj(v, heap, depth + 1)
        return {"r": ref}

    def enc_obj(self, v, heap, depth):
        if isinstance(v, (list, tuple, set, frozenset)):
            items = list(v)[:60]
            kind = type(v).__name__
            return {"t": kind, "items": [self.enc(x, heap, depth) for x in items], "more": max(0, len(v) - 60)}
        if isinstance(v, dict):
            items = list(v.items())[:60]
            return {"t": "dict", "items": [[self.enc(k, heap, depth), self.enc(x, heap, depth)] for k, x in items],
                    "more": max(0, len(v) - 60)}
        if isinstance(v, types.FunctionType):
            code = v.__code__
            params = list(code.co_varnames[:code.co_argcount])
            closure = {}
            if v.__closure__:
                for name, cell in zip(code.co_freevars, v.__closure__):
                    try:
                        closure[name] = self.enc(cell.cell_contents, heap, depth)
                    except ValueError:
                        closure[name] = {"p": "<unset>"}
            parent = v.__qualname__.rsplit(".<locals>.", 1)[0] if ".<locals>." in v.__qualname__ else None
            return {"t": "function", "name": v.__name__, "params": params, "closure": closure, "parent": parent,
                    "line": code.co_firstlineno}
        if isinstance(v, (types.BuiltinFunctionType, types.ModuleType, type)):
            return {"t": "builtin", "name": getattr(v, "__name__", repr(v))}
        if hasattr(v, "__dict__"):
            attrs = {k: self.enc(x, heap, depth) for k, x in list(vars(v).items())[:40] if not k.startswith("__")}
            return {"t": "instance", "class": type(v).__name__, "attrs": attrs}
        return {"t": "other", "repr": ADDR.sub("", repr(v))[:200]}

    # ---- snapshots ---------------------------------------------------------------------------
    def ref(self, v):
        """A small, stable number for an object (1, 2, ... in the order first seen), not id(v), so the
        same program gives the same trace on every build. The object is kept alive so its id is
        never reused for another object during the run."""
        k = id(v)
        if k not in self.refs:
            self.refs[k] = (len(self.refs) + 1, v)
        return self.refs[k][0]

    def fid(self, frame):
        k = id(frame)
        if k not in self.frame_ids or self.frame_ids[k][1] is not frame:
            # keep the frame, so a later frame cannot reuse its id and inherit its number
            self.frame_ids[k] = (self.next_frame, frame)
            self.next_frame += 1
        return self.frame_ids[k][0]

    def snapshot(self, frame, event, retval=None):
        if len(self.steps) >= self.max_steps:
            self.truncated = True
            raise _Stop()
        heap = {}
        stack = []
        f = frame
        while f is not None:
            if f.f_code.co_filename == self.filename:
                loc = {}
                for k, x in list(f.f_locals.items()):
                    if k in SKIP_NAMES or (f.f_code.co_name == "<module>" and isinstance(x, types.ModuleType)):
                        continue
                    loc[k] = self.enc(x, heap)
                stack.append({"id": self.fid(f), "func": "global" if f.f_code.co_name == "<module>" else f.f_code.co_name,
                              "line": f.f_lineno, "vars": loc})
            f = f.f_back
        stack.reverse()
        step = {"line": frame.f_lineno, "event": event, "stack": stack,
                "heap": {str(k): v for k, v in heap.items() if v is not None}, "out": len(self.out.getvalue())}
        if event == "return":
            step["ret"] = self.enc(retval, heap)
            step["heap"] = {str(k): v for k, v in heap.items() if v is not None}
            # keep a returned frame whose variables a live closure still captures
            if any(isinstance(h, dict) and h.get("t") == "function" and h.get("parent") == frame.f_code.co_name
                   for h in heap.values()) or frame.f_code.co_freevars or frame.f_code.co_cellvars:
                self.zombies[self.fid(frame)] = stack[-1] if stack else None
        if self.zombies:
            # a returned frame stays on screen only while a function on the heap still captures from it
            live = {s["id"] for s in stack}
            parents = {h.get("parent") for h in step["heap"].values() if isinstance(h, dict) and h.get("t") == "function" and h.get("closure")}
            keep = [(k, z) for k, z in self.zombies.items() if z and k not in live and z.get("func") in parents]
            step["zombies"] = [z for k, z in keep[-4:]]
        self.steps.append(step)

    def trace(self, frame, event, arg):
        if frame.f_code.co_filename != self.filename:
            return None  # do not trace library code
        if event in ("line", "return", "exception", "call"):
            if event == "call":
                return self.trace
            self.snapshot(frame, event, arg if event == "return" else None)
        return self.trace


class _Stop(Exception):
    pass


def run_setup(setup, g):
    """Run setup code (a label's setup= blocks) in globals g, untraced and with its output discarded,
    so the traced program starts where the page's earlier cells left off. Returns an error or None."""
    old = sys.stdout
    sys.stdout = io.StringIO()
    try:
        exec(compile(setup, "<setup>", "exec"), g)
    except BaseException as e:
        return f"setup: {type(e).__name__}: {e}"
    finally:
        sys.stdout = old
    return None


def trace_source(src, max_steps=800, filename="<program>", setup=None):
    t = Tracer(filename, max_steps)
    code = compile(src, filename, "exec")
    g = {"__name__": "__main__", "__builtins__": __builtins__}
    if setup:
        err = run_setup(setup, g)
        if err:
            return {"version": 1, "kind": "env", "language": "python", "source": src, "steps": [],
                    "stdout": "", "error": err, "truncated": False}
    old, old_argv = sys.stdout, sys.argv
    sys.stdout = t.out
    import os
    import shlex
    sys.argv = [filename] + shlex.split(os.environ.get("CVIZ_ARGS", ""))  # the label's args=, else none
    error = None
    try:
        sys.settrace(t.trace)
        exec(code, g)
    except _Stop:
        pass
    except SystemExit:
        pass
    except BaseException as e:  # the program's own error is part of the trace
        error = f"{type(e).__name__}: {e}"
    finally:
        sys.settrace(None)
        sys.stdout, sys.argv = old, old_argv
    return {"version": 1, "kind": "env", "language": "python", "source": src, "steps": t.steps,
            "stdout": t.out.getvalue(), "error": error, "truncated": t.truncated}


def main(argv):
    path = argv[1]
    max_steps = int(argv[argv.index("--max-steps") + 1]) if "--max-steps" in argv else 800
    src = open(path, encoding="utf-8").read()
    setup = open(argv[argv.index("--setup") + 1], encoding="utf-8").read() if "--setup" in argv else None
    sys.setrecursionlimit(5000)
    result = trace_source(src, max_steps, filename=path, setup=setup)
    json.dump(result, sys.__stdout__)


if __name__ == "__main__":
    main(sys.argv)
