"""code-viz SQL tracer (sqltrace.py): run an SQL script statement by statement in SQLite and record,
after every statement, every table's contents, which tables changed, and the result of a query.

Full manual: the header of code-viz (`code-viz readme`, or README.md), sections 7 Kinds of
visualization (sql) and 14 Trace format.

WHERE IT RUNS
  In the python runner container (driver.py, viz=sql), and in the reader's browser: the viewer loads
  this file into Pyodide (with Pyodide's sqlite3 package) for student mode's Edit and run. It uses the
  Python standard library only (sqlite3, json, re), so both places run the same code.

HOW IT WORKS
  The script is split into complete statements with sqlite3.complete_statement (so semicolons inside
  strings and triggers are handled), keeping each statement's first line number. Each statement runs
  in an in-memory database (or a fresh database file when --db is given). After it runs, the tracer
  reads every user table (sqlite_master, type 'table', not sqlite_*), up to MAX_ROWS rows per table,
  and records:
    {"line": first line, "end": last line, "sql": statement text, "kind": "query" | "change" | "schema" | "other",
     "result": {"columns": [...], "rows": [[...]], "more": bool} (for statements that return rows),
     "changes": rows changed (INSERT/UPDATE/DELETE), "tables": {name: {"columns": [...], "rows": [...], "more": bool}},
     "changed": [names of tables whose contents or columns differ from the step before],
     "error": message or absent, "out": length of stdout so far}
  and, at the top level, "start_tables": every table before the first statement (after setup=).
  A statement that fails records its error and the script carries on, as the sqlite3 shell does.
  stdout is what the sqlite3 shell would print in its default list mode (columns joined by "|"),
  so the expected output can be compared with `sqlite3 db < script.sql`.

SETUP
  With setup= (earlier SQL blocks on the same page that create the tables this block uses, section 4),
  the setup statements run first, unrecorded, and their tables appear in the first step.

LIMITS
  SQLite's dialect only: MySQL or PostgreSQL syntax (AUTO_INCREMENT, SERIAL, ENGINE=, stored procedures)
  fails at that statement and is reported there; `label --try` skips blocks that fail. Values are
  shown as SQLite returns them (bytes as hex). At most MAX_ROWS rows per table and per result, and at
  most --max-steps statements.

USAGE
  python3 sqltrace.py script.sql [--setup setup.sql] [--max-steps 400]   # prints the trace as JSON
  trace_source(src, setup=None)                                            # the same, from Python (Pyodide)
"""
import argparse
import json
import re
import sqlite3
import sys

MAX_ROWS = 50


def split_statements(src):
    """[(first line, last line, statement text)] for each complete statement; comments-only text is skipped."""
    out, buf, start = [], [], None
    for n, line in enumerate(src.split("\n"), 1):
        if start is None and not line.strip():
            continue
        if start is None:
            start = n
        buf.append(line)
        text = "\n".join(buf)
        if sqlite3.complete_statement(text):
            body = strip_comments(text).strip()
            if body:
                out.append((start, n, text.strip()))
            buf, start = [], None
    rest = "\n".join(buf)
    if strip_comments(rest).strip():   # a last statement without its semicolon: run it anyway
        out.append((start, start + len(buf) - 1, rest.strip()))
    return out


def strip_comments(text):
    text = re.sub(r"/\*.*?\*/", " ", text, flags=re.S)
    return re.sub(r"--[^\n]*", " ", text)


def shown(v):
    if isinstance(v, bytes):
        return "x'" + v.hex() + "'"
    return v


def cell(v):
    """How the sqlite3 shell prints a value in list mode."""
    if v is None:
        return ""
    if isinstance(v, float) and v == int(v) and abs(v) < 1e15:
        return f"{v:.1f}"
    if isinstance(v, bytes):
        return v.decode("utf-8", "replace")
    return str(v)


def snapshot(con):
    tables = {}
    names = [r[0] for r in con.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
    for name in names:
        q = '"' + name.replace('"', '""') + '"'
        cols = [r[1] for r in con.execute(f"PRAGMA table_info({q})")]
        rows = con.execute(f"SELECT * FROM {q} LIMIT {MAX_ROWS + 1}").fetchall()
        tables[name] = {"columns": cols, "rows": [[shown(v) for v in r] for r in rows[:MAX_ROWS]],
                        "more": len(rows) > MAX_ROWS}
    return tables


def kind_of(sql):
    w = strip_comments(sql).strip().split(None, 1)
    w = w[0].upper() if w else ""
    if w in ("SELECT", "WITH", "VALUES", "PRAGMA", "EXPLAIN"):
        return "query"
    if w in ("INSERT", "UPDATE", "DELETE", "REPLACE", "UPSERT"):
        return "change"
    if w in ("CREATE", "DROP", "ALTER"):
        return "schema"
    return "other"


def trace_source(src, setup=None, max_steps=400, db=":memory:"):
    con = sqlite3.connect(db, isolation_level=None)   # autocommit, like the sqlite3 shell
    if setup:
        for _, _, s in split_statements(setup):
            try:
                con.execute(s)
            except sqlite3.Error:
                pass
    steps, out, prev = [], [], snapshot(con)
    start = prev                 # the tables before the first statement (after setup=), for the first "before"
    truncated = False
    error = None
    for first, last, sql in split_statements(src):
        if len(steps) >= max_steps:
            truncated = True
            break
        step = {"line": first, "end": last, "sql": sql, "kind": kind_of(sql)}
        try:
            cur = con.execute(sql)
            if cur.description:
                cols = [d[0] for d in cur.description]
                rows = cur.fetchmany(MAX_ROWS + 1)
                step["result"] = {"columns": cols, "rows": [[shown(v) for v in r] for r in rows[:MAX_ROWS]],
                                  "more": len(rows) > MAX_ROWS}
                for r in rows[:MAX_ROWS]:
                    out.append("|".join(cell(v) for v in r) + "\n")
            elif cur.rowcount is not None and cur.rowcount >= 0 and step["kind"] == "change":
                step["changes"] = cur.rowcount
        except sqlite3.Error as e:
            step["error"] = str(e)
            line = f"Parse error near line {first}: {e}\n" if isinstance(e, sqlite3.OperationalError) else f"Runtime error near line {first}: {e}\n"
            out.append(line)
            error = error or f"line {first}: {e}"
        tabs = snapshot(con)
        step["tables"] = tabs
        step["changed"] = sorted(n for n in set(tabs) | set(prev) if tabs.get(n) != prev.get(n))
        step["out"] = len("".join(out))
        steps.append(step)
        prev = tabs
    con.close()
    return {"version": 1, "kind": "sql", "language": "sql", "source": src, "steps": steps,
            "stdout": "".join(out), "error": error, "truncated": truncated, "start_tables": start}


def main():
    ap = argparse.ArgumentParser(description="Trace an SQL script in SQLite, statement by statement.")
    ap.add_argument("file")
    ap.add_argument("--setup")
    ap.add_argument("--max-steps", type=int, default=400)
    a = ap.parse_args()
    src = open(a.file, encoding="utf-8").read()
    setup = open(a.setup, encoding="utf-8").read() if a.setup else None
    json.dump(trace_source(src, setup, a.max_steps), sys.stdout)


if __name__ == "__main__":
    main()
