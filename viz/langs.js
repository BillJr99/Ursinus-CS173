/*
  code-viz viewer: SQL, MIPS and VHDL panels, and in-browser runs for SQL, MIPS and JavaScript
  (langs.js). Loaded by index.html before viewer.js, which looks up window.CVIZ for:
    CVIZ.panels[kind](t, s, steps)   the right-hand panel for a trace kind ("sql", "mips", "wave")
    CVIZ.lines[kind](t, s)           the source line to highlight at a step
    CVIZ.steps[kind](t)              the list of steps of a trace kind (when not t.steps)
    CVIZ.outKinds                    kinds whose steps carry "out" (output printed so far)
    CVIZ.run[lang](code, t, h)       student mode Edit and run in the browser for a language; h gives
                                     h.pyodide() (the viewer's Pyodide loader) and h.note(text)
  Java traces use the Python view ("env": frames and objects), so they need nothing here.

  Full manual: the header of code-viz (`code-viz readme`, or README.md), sections 7 Kinds of
  visualization and 8 Reading the viewer.

  SQL      the statement just run, its result (columns and rows) and every table, a changed table
           shown before and after the statement. Edit and run: tracers/sqltrace.py in Pyodide with
           Pyodide's sqlite3 package.
  MIPS     the instruction just run, all 32 registers plus hi and lo (the ones this instruction
           changed highlighted, values in decimal and hex), and memory: the static data words (with
           their labels), the heap and the stack words the program wrote, the ones written by this
           instruction highlighted. Edit and run: tracers/mipstrace.py in Pyodide (SPIM is not in
           the browser, so the recorded run's SPIM check does not apply to an edited program).
  VHDL     the testbench's signals over simulation time as a waveform (one-bit signals as high and
           low lines, vectors as labeled bus segments, U/X/Z marked), a cursor at the current
           change time, and every signal's value at that time. No browser run (GHDL needs the runner).
  JS       Edit and run in a Web Worker (console.log captured, stopped after 5 seconds).
*/
(function () {
  const C = (window.CVIZ = window.CVIZ || { panels: {}, lines: {}, steps: {}, run: {}, outKinds: [] });
  C.outKinds.push("sql", "mips");
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s === undefined || s === null ? "" : s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // ---------------------------------------------------------------- SQL
  function sqlTable(name, tb, cls) {
    if (!tb) return `<div class="sqltab ${cls || ""}"><h5>${esc(name)} <span class="note">(not there)</span></h5></div>`;
    const head = tb.columns.map((c) => `<th>${esc(c)}</th>`).join("");
    const rows = tb.rows.map((r) => `<tr>${r.map((v) => `<td>${v === null ? '<span class="note">NULL</span>' : esc(v)}</td>`).join("")}</tr>`).join("");
    return `<div class="sqltab ${cls || ""}"><h5>${esc(name)}</h5><table class="steps"><tr>${head}</tr>${rows || `<tr><td colspan="${tb.columns.length || 1}" class="note">no rows</td></tr>`}</table>${tb.more ? '<div class="note">more rows not shown</div>' : ""}</div>`;
  }
  C.lines.sql = (t, s) => (s ? s.line : null);
  C.panels.sql = function (t, s, steps) {
    $("paneltitle").textContent = "Tables";
    const panel = $("panel");
    if (!s) { panel.innerHTML = `<p class="err">${esc(t.error || "No statements ran.")}</p>`; return; }
    const i = steps.indexOf(s);
    const before = i > 0 ? steps[i - 1].tables : (t.start_tables || {});
    let h = `<div class="sqlstmt"><h5>Statement ${i + 1} of ${steps.length} <span class="badge">${esc(s.kind)}</span>` +
      (s.changes !== undefined ? `<span class="badge">${s.changes} row${s.changes === 1 ? "" : "s"} changed</span>` : "") + `</h5><pre>${esc(s.sql)}</pre>` +
      (s.error ? `<p class="err">${esc(s.error)}</p>` : "") + `</div>`;
    if (s.result) h += `<div class="sqlresult">${sqlTable("Result", s.result, "result")}</div>`;
    const names = Object.keys(s.tables);
    for (const n of (before ? Object.keys(before) : [])) if (!names.includes(n)) names.push(n);
    h += names.map((n) => {
      const changed = s.changed.includes(n);
      if (changed && before) return `<div class="sqlpair"><div class="sqlside"><div class="note">before</div>${sqlTable(n, before[n], "before")}</div><div class="sqlside"><div class="note">after</div>${sqlTable(n, s.tables[n], "after changed")}</div></div>`;
      return sqlTable(n, s.tables[n], changed ? "changed" : "");
    }).join("");
    panel.innerHTML = h;
  };
  C.run.sql = async function (code, t, h) {
    const py = await h.pyodide();
    h.note("loading SQLite (first time only) ...");
    await py.loadPackage("sqlite3");
    if (!py.FS.analyzePath("sqltrace.py").exists) py.FS.writeFile("sqltrace.py", await (await fetch("tracers/sqltrace.py")).text());
    h.note("running ...");
    py.globals.set("cviz_src", code);
    py.globals.set("cviz_setup", t.setup ? t.setup.source : null);
    return JSON.parse(py.runPython("import json, sqltrace; json.dumps(sqltrace.trace_source(cviz_src, setup=cviz_setup))"));
  };

  // ---------------------------------------------------------------- MIPS
  const REGS = ["zero", "at", "v0", "v1", "a0", "a1", "a2", "a3", "t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7",
    "s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "t8", "t9", "k0", "k1", "gp", "sp", "fp", "ra", "hi", "lo"];
  const hex = (v) => "0x" + (v >>> 0).toString(16).padStart(8, "0");
  const s32 = (v) => (v | 0);
  function mipsState(t, upto) {
    // registers and memory after step `upto` (cached per trace for playback)
    const c = t._mips || (t._mips = { at: -1, regs: (t.regs0 || []).slice(), mem: new Map() });
    if (upto < c.at) { c.at = -1; c.regs = (t.regs0 || []).slice(); c.mem = new Map(); }
    for (let i = c.at + 1; i <= upto; i++) {
      const s = t.steps[i];
      for (const k in s.regs) c.regs[Number(k)] = s.regs[k];
      for (const [a, size, v] of s.mem) for (let b = 0; b < size; b++) c.mem.set(a + b, (v >>> (8 * b)) & 0xff);
      c.at = i;
    }
    return c;
  }
  function memByte(t, c, a) {
    if (c.mem.has(a)) return c.mem.get(a);
    const base = (t.data && t.data.base) || 0x10010000, hx = (t.data && t.data.hex) || "";
    const off = a - base;
    return off >= 0 && off * 2 < hx.length ? parseInt(hx.substr(off * 2, 2), 16) : 0;
  }
  C.lines.mips = (t, s) => (s ? s.line : null);
  C.panels.mips = function (t, s, steps) {
    $("paneltitle").textContent = "Registers and memory";
    const panel = $("panel");
    if (!s) { panel.innerHTML = `<p class="err">${esc(t.error || "No instructions ran.")}</p>`; return; }
    const i = steps.indexOf(s), c = mipsState(t, i);
    const changed = new Set(Object.keys(s.regs).map(Number));
    const regs = REGS.map((n, k) => `<div class="mreg${changed.has(k) ? " cur" : ""}"><span class="rn">$${n}</span><span class="rv">${s32(c.regs[k] || 0)}</span><span class="rh">${hex(c.regs[k] || 0)}</span></div>`).join("");
    const wrote = new Set(s.mem.map((m) => m[0] - (m[0] % 4)));
    const labels = {};
    for (const [n, a] of Object.entries(t.labels || {})) if (a >= 0x10000000) (labels[a] = labels[a] || []).push(n);
    const base = (t.data && t.data.base) || 0x10010000, dlen = ((t.data && t.data.hex) || "").length / 2;
    const words = new Set();
    for (let a = base; a < base + Math.min(dlen, 256); a += 4) words.add(a);
    for (const a of c.mem.keys()) words.add(a - (a % 4));
    const rows = [...words].sort((x, y) => x - y).slice(0, 120).map((a) => {
      let w = 0, txt = "";
      for (let b = 0; b < 4; b++) { const v = memByte(t, c, a + b); w |= v << (8 * b); txt += v >= 32 && v < 127 ? String.fromCharCode(v) : "."; }
      const seg = a >= 0x7f000000 ? "stack" : a >= base + dlen ? "heap" : "data";
      return `<tr class="${wrote.has(a) ? "cur" : ""}"><td>${hex(a)}</td><td class="note">${seg}${labels[a] ? " " + esc(labels[a].join(", ")) : ""}</td><td>${s32(w)}</td><td>${hex(w)}</td><td><code>${esc(txt)}</code></td></tr>`;
    }).join("");
    panel.innerHTML = `<div class="mins"><b>${esc(s.ins)}</b> <span class="note">at ${hex(s.pc)}, line ${s.line}</span>` +
      (t.approximate ? ' <span class="badge">simulator output differs from SPIM; the output shown is SPIM\'s</span>' : "") + `</div>` +
      `<div class="colhead">Registers</div><div class="mregs">${regs}</div>` +
      `<div class="colhead">Memory (words)</div><table class="steps mmem"><tr><th>address</th><th></th><th>decimal</th><th>hex</th><th>bytes</th></tr>${rows}</table>`;
  };
  C.run.mips = async function (code, t, h) {
    const py = await h.pyodide();
    if (!py.FS.analyzePath("mipstrace.py").exists) py.FS.writeFile("mipstrace.py", await (await fetch("tracers/mipstrace.py")).text());
    h.note("running ...");
    py.globals.set("cviz_src", code);
    py.globals.set("cviz_in", t.input || "");
    return JSON.parse(py.runPython("import json, mipstrace; json.dumps(mipstrace.trace_source(cviz_src, cviz_in))"));
  };

  // ---------------------------------------------------------------- VHDL waveform
  const HIGH = new Set(["1", "H"]), LOW = new Set(["0", "L"]);
  function busText(v) {
    if (/^[01]+$/.test(v) && v.length > 4) return v + " (0x" + parseInt(v, 2).toString(16) + ")";
    return v;
  }
  function valueAt(sg, time) {
    let v = "U";
    for (const [tm, x] of sg.changes) { if (tm <= time) v = x; else break; }
    return v;
  }
  C.steps.wave = (t) => t.steps || [];
  C.panels.wave = function (t, s, steps) {
    $("paneltitle").textContent = "Waveform";
    const panel = $("panel");
    const sigs = t.signals || [];
    if (!sigs.length) {
      panel.innerHTML = t.analyzed_only ? `<p class="note">${esc(t.stdout)}</p>` : `<p class="err">${esc(t.error || "No signals recorded.")}</p>`;
      return;
    }
    const end = Math.max(t.end || 0, ...sigs.map((g) => (g.changes.length ? g.changes[g.changes.length - 1][0] : 0))) || 1;
    const W = 640, L = 110, RH = 26, H = sigs.length * RH + 24;
    const X = (tm) => L + (tm / end) * (W - L - 10);
    const now = s ? s.t : 0;
    let svg = `<svg class="wave" viewBox="0 0 ${W} ${H}" width="100%" preserveAspectRatio="xMinYMin meet">`;
    sigs.forEach((g, k) => {
      const y0 = 8 + k * RH, hi = y0 + 3, lo = y0 + RH - 9, mid = (hi + lo) / 2;
      svg += `<text x="4" y="${mid + 4}" class="wname">${esc(g.name)}</text>`;
      const ch = g.changes.length ? g.changes : [[0, "U"]];
      ch.forEach(([tm, v], j) => {
        const x1 = X(tm), x2 = X(j + 1 < ch.length ? ch[j + 1][0] : end);
        if (g.width === 1) {
          const y = HIGH.has(v) ? hi : LOW.has(v) ? lo : mid;
          const cls = HIGH.has(v) || LOW.has(v) ? "wl" : "wl wx";
          svg += `<line x1="${x1}" y1="${y}" x2="${x2}" y2="${y}" class="${cls}"/>`;
          if (j + 1 < ch.length) {
            const nv = ch[j + 1][1], ny = HIGH.has(nv) ? hi : LOW.has(nv) ? lo : mid;
            svg += `<line x1="${x2}" y1="${y}" x2="${x2}" y2="${ny}" class="wl"/>`;
          }
        } else {
          const bad = /[UXZuxz-]/.test(v);
          svg += `<polygon points="${x1 + 3},${hi} ${x2 - 3},${hi} ${x2},${mid} ${x2 - 3},${lo} ${x1 + 3},${lo} ${x1},${mid}" class="wb${bad ? " wx" : ""}"/>`;
          if (x2 - x1 > 30) svg += `<text x="${(x1 + x2) / 2}" y="${mid + 4}" class="wv">${esc(busText(v).slice(0, Math.floor((x2 - x1) / 7)))}</text>`;
        }
      });
    });
    svg += `<line x1="${X(now)}" y1="0" x2="${X(now)}" y2="${H - 16}" class="wcur"/><text x="${X(now)}" y="${H - 4}" class="wt">${esc(now)} fs</text>`;
    svg += `<text x="${L}" y="${H - 4}" class="wt">0</text><text x="${W - 10}" y="${H - 4}" class="wt" text-anchor="end">${esc(end)} fs</text></svg>`;
    const vals = sigs.map((g) => `<tr class="${s && s.changed.includes(g.name) ? "cur" : ""}"><td>${esc(g.name)}</td><td><code>${esc(busText(valueAt(g, now)))}</code></td></tr>`).join("");
    panel.innerHTML = `<div class="note">Testbench <b>${esc(t.top || "")}</b>, VHDL-${esc(t.std || "")}; simulation time in femtoseconds (1 ns = 1,000,000 fs). Each step is a time when a signal changed.</div>` +
      `<div class="wavebox">${svg}</div><div class="colhead">Values at ${esc(now)} fs</div><table class="steps">${vals}</table>`;
  };

  // ---------------------------------------------------------------- JavaScript (Web Worker)
  C.run.js = function (code) {
    return new Promise((ok) => {
      const src = "let out='';const log=(...a)=>{out+=a.map(x=>typeof x==='string'?x:JSON.stringify(x)).join(' ')+'\\n'};" +
        "console.log=log;console.info=log;console.warn=log;console.error=log;" +
        "onmessage=(e)=>{try{(new Function(e.data))();postMessage({out})}catch(err){postMessage({out,error:String(err)})}}";
      const w = new Worker(URL.createObjectURL(new Blob([src], { type: "text/javascript" })));
      const timer = setTimeout(() => { w.terminate(); ok({ kind: "plain", language: "js", source: code, steps: [], stdout: "", error: "stopped after 5 seconds" }); }, 5000);
      w.onmessage = (e) => { clearTimeout(timer); w.terminate(); ok({ kind: "plain", language: "js", source: code, steps: [], stdout: e.data.out, error: e.data.error || null }); };
      w.postMessage(code);
    });
  };
})();
