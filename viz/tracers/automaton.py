"""code-viz automaton loader and simulator.

Full manual: the header of code-viz (`code-viz readme`, or README.md), sections 7 Kinds of visualization, 8 Reading the viewer (automaton), 14 Trace format.

Reads a finite automaton drawn in Graphviz DOT (the course's files/dotty/*.dot style: a start
arrow from an invisible node, accepting states as doublecircle, edge labels as input symbols,
comma separated, with "ε", "eps" or "epsilon" for epsilon moves) and simulates it on an input
string, recording the set of current states after each symbol (NFA and ε-NFA aware).

Usage:  python3 automaton.py FILE.dot --input abba > trace.json

PIPELINE
  driver.py for viz=automaton examples and the .dot files in viz/manifest.json; the viewer also
  re-simulates in the browser when the input box is edited (the same logic in JavaScript).

TRACE FIELDS WRITTEN
  kind "automaton", language "dot", source, input, automaton: {states, start, accept, edges:
  [[from, to, symbol]]}, graph (DOT), accepted, stdout, error, truncated, and steps:
  {read, rest, states}.

OPTIONS  --input TEXT.   ENVIRONMENT  none.

EXAMPLE  python3 automaton.py files/dotty/ends_in_ab.dot --input abab > t.json

LIMITS AND KNOWN PROBLEMS
  - Only the DOT conventions above are understood; other start or accept markings are missed.
"""
import json
import re
import sys

EPS = {"ε", "eps", "epsilon", "λ", "e"}


def parse_dot(text):
    states, accept, edges, start, hidden = set(), set(), [], None, set()
    body = re.sub(r"//.*|/\*.*?\*/", "", text, flags=re.S)
    # node defaults: "node [shape = doublecircle]; q2 q3;" style
    shape = None
    for stmt in re.split(r";|\n", body):
        s = stmt.strip()
        if not s or s.startswith(("digraph", "graph", "}", "{", "rankdir", "size", "label", "fontname")):
            m = re.match(r"(?:di)?graph\s+\S*\s*\{\s*(.*)", s)
            if not m:
                continue
            s = m.group(1).strip()
            if not s:
                continue
        m = re.match(r"node\s*\[(.*)\]\s*(.*)", s)
        if m:
            sh = re.search(r"shape\s*=\s*\"?(\w+)", m.group(1))
            shape = sh.group(1) if sh else shape
            for n in re.findall(r"\"([^\"]+)\"|([A-Za-z0-9_]+)", m.group(2)):
                name = n[0] or n[1]
                states.add(name)
                if shape == "doublecircle":
                    accept.add(name)
            continue
        m = re.match(r"\"?([^\"\s\[]+)\"?\s*->\s*\"?([^\"\s\[]+)\"?\s*(\[(.*)\])?", s)
        if m:
            a, b, attrs = m.group(1), m.group(2), m.group(4) or ""
            lab = re.search(r"label\s*=\s*\"([^\"]*)\"|label\s*=\s*(\S+)", attrs)
            label = (lab.group(1) if lab and lab.group(1) is not None else (lab.group(2) if lab else "")).strip()
            if a in hidden or a.lower() in ("start", "__start", "init", "s0start", "empty", "null", "qi") and not label:
                start = b
                states.add(b)
                continue
            states.update([a, b])
            for sym in [x.strip() for x in label.split(",")] if label else [""]:
                edges.append([a, b, sym])
            continue
        m = re.match(r"\"?([^\"\s\[]+)\"?\s*\[(.*)\]", s)
        if m:
            n, attrs = m.group(1), m.group(2)
            if n in ("edge", "node", "graph"):
                continue  # attribute defaults, not states
            if re.search(r"shape\s*=\s*\"?(point|none|plaintext)", attrs) or "invis" in attrs:
                hidden.add(n)
                continue
            states.add(n)
            if "doublecircle" in attrs:
                accept.add(n)
            continue
        if shape == "doublecircle":
            for n in re.findall(r"\"([^\"]+)\"|([A-Za-z0-9_]+)", s):
                name = n[0] or n[1]
                if name not in ("node", "edge"):
                    accept.add(name)
                    states.add(name)
    states -= hidden
    if start is None:
        cands = sorted(states)
        start = next((q for q in cands if q in ("q0", "0", "s0", "S", "start")), cands[0] if cands else None)
    return {"states": sorted(states), "start": start, "accept": sorted(accept), "edges": edges}


def closure(states, edges):
    seen, todo = set(states), list(states)
    while todo:
        q = todo.pop()
        for a, b, s in edges:
            if a == q and s in EPS and b not in seen:
                seen.add(b)
                todo.append(b)
    return seen


def simulate(auto, inp):
    cur = closure({auto["start"]}, auto["edges"])
    steps = [{"read": None, "rest": inp, "states": sorted(cur)}]
    for i, ch in enumerate(inp):
        nxt = {b for a, b, s in auto["edges"] if a in cur and s == ch}
        cur = closure(nxt, auto["edges"])
        steps.append({"read": ch, "rest": inp[i + 1:], "states": sorted(cur)})
    accepted = bool(cur & set(auto["accept"]))
    return steps, accepted


if __name__ == "__main__":
    a = sys.argv
    text = open(a[1], encoding="utf-8", errors="replace").read()
    inp = a[a.index("--input") + 1] if "--input" in a else ""
    auto = parse_dot(text)
    steps, ok = simulate(auto, inp)
    json.dump({"version": 1, "kind": "automaton", "language": "dot", "source": text, "automaton": auto,
               "input": inp, "steps": steps, "stdout": ("accepted" if ok else "rejected") + "\n", "error": None,
               "truncated": False}, sys.stdout)
