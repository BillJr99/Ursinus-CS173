/* code-viz modes (modes.js): the mode tabs, the URL arguments, and switching between modes.

   Full manual: the header of code-viz (`code-viz readme`, or README.md), section 21 Modes and URL
   arguments; sections 22 (Explain) and 23 (Simulate) for the two modes beside Run.

   WHAT IT DOES
   An example can be shown in up to three modes. Run is the original viewer (viewer.js). Explain
   (mode-explain.js) walks through a tour, and Simulate (mode-simulate.js) replays a recorded
   terminal session. viz/index.json lists each example's modes; an entry without "modes" is Run only.
   This file draws one tab per mode the example has data for, in the header, and switches between
   them whatever mode the link opened in. Each mode keeps its own place (Run's trace step, the tour
   step, the session step), so going back to a tab returns to where it was.

   URL ARGUMENTS (old ones unchanged, so every link and QR code already handed out still works)
     #<id>               the example           ?student=1     student mode
     ?step=N             Run: trace step N      ?mode=run|explain|simulate   the mode to open in
     &t=N                Explain: tour step N   &s=N           Simulate: session step N
     &tour=<name>        Explain: a named tour (viz/tours/<id>--<name>.json)
   With no mode, the viewer opens in Run when there is a trace, else Explain, else Simulate. A mode
   the example has no data for opens the best one it has, with a one-line note above the code.

   HOW THE MODES PLUG IN
   mode-explain.js and mode-simulate.js call CVIZ_MODES.register(name, mode). A mode has
     label                 the tab text
     show(ctx)             draw it; ctx = {id, meta, V (viewer.js internals), pos, params, note}
     go(to)                move: a step number, or "+1" / "-1"
     pos()                 its current place (kept while another tab shows)
     url()                 its URL arguments for the QR code ({t: 3}, {s: 2, ...})
     hide()                (optional) undo anything it changed outside #example
   The Run mode is this file's own small adapter around viewer.js's showTrace and render.
*/
(function () {
  "use strict";
  const ORDER = ["run", "explain", "simulate", "terminal"];
  const LABEL = { run: "Run", explain: "Explain", simulate: "Simulate", terminal: "Terminal" };
  const registry = {};
  const params = new URLSearchParams(location.search);
  const cur = { id: null, meta: null, modes: [], mode: null, pos: {} };

  // Fetch JSON that may be gzipped (published traces and sessions are .json.gz).
  async function fetchJson(path) {
    const r = await fetch(path, { cache: "no-store" });
    if (!r.ok) throw new Error("missing " + path);
    const buf = await r.arrayBuffer();
    const b = new Uint8Array(buf);
    if (b[0] === 0x1f && b[1] === 0x8b) {
      return JSON.parse(await new Response(new Blob([buf]).stream().pipeThrough(new DecompressionStream("gzip"))).text());
    }
    return JSON.parse(new TextDecoder().decode(b));
  }

  // Run mode: viewer.js as it always was.
  registry.run = {
    label: LABEL.run,
    async show(ctx) {
      const V = ctx.V;
      // Coming back to Run keeps what was there, including an Edit-and-run result.
      if (V.state.trace && V.state.trace.id === ctx.id && ctx.pos !== undefined) {
        document.getElementById("list").hidden = true; document.getElementById("example").hidden = false;
        V.state.step = ctx.pos; V.renderCode(V.state.trace.source || ""); V.render(); return;
      }
      const t = V.expand(await V.loadTrace(ctx.id));
      V.showTrace(t, ctx.meta);
      if (ctx.pos !== undefined) { V.state.step = ctx.pos; V.render(); }
    },
    go() { /* viewer.js moves the Run mode itself */ },
    pos() { return window.CVIZ_VIEWER.state.step; },
    url() { const s = window.CVIZ_VIEWER.state.step; return s ? { step: s } : {}; },
  };

  function V() { return window.CVIZ_VIEWER; }

  function tabs() {
    const bar = document.getElementById("modetabs");
    if (!bar) return;
    bar.innerHTML = "";
    const shown = ORDER.filter((m) => cur.modes.includes(m) && registry[m]);
    bar.hidden = shown.length < 2;
    for (const m of shown) {
      const b = document.createElement("button");
      b.textContent = registry[m].label || LABEL[m];
      b.className = "modetab" + (m === cur.mode ? " on" : "");
      b.setAttribute("aria-pressed", m === cur.mode ? "true" : "false");
      b.title = { run: "Run: step through what the code does (key 1)", explain: "Explain: a guided walkthrough of the code (key 2)",
                  simulate: "Simulate: replay the recorded terminal session (key 3)", terminal: "Terminal: play commands and output (key 4)" }[m];
      b.onclick = () => switchTo(m);
      bar.appendChild(b);
    }
  }

  function note(text) {
    const n = document.getElementById("modenote");
    if (!n) return;
    n.textContent = text || "";
    n.hidden = !text;
  }

  // The best mode an example has: the one asked for if it exists, else Run, Explain, Simulate.
  function pick(asked) {
    const have = ORDER.filter((m) => cur.modes.includes(m) && registry[m]);
    if (asked && have.includes(asked)) return { mode: asked, fell: false };
    return { mode: have[0] || "run", fell: !!asked };
  }

  async function show(mode, first) {
    const v = V();
    if (cur.mode && cur.mode !== mode && registry[cur.mode]) {
      cur.pos[cur.mode] = registry[cur.mode].pos();
      if (registry[cur.mode].hide) registry[cur.mode].hide();
    }
    cur.mode = mode;
    v.state.mode = mode;
    document.body.dataset.mode = mode;
    tabs();
    let pos = cur.pos[mode];
    if (first) {
      const key = { run: "step", explain: "t", simulate: "s", terminal: "s" }[mode];
      if (params.has(key)) pos = Number(params.get(key)) || 0;
    }
    try {
      await registry[mode].show({ id: cur.id, meta: cur.meta, V: v, pos, params, fetchJson, note });
    } catch (e) {
      // A mode whose data failed to load: say so and fall back to another one the example has.
      const rest = ORDER.filter((m) => m !== mode && cur.modes.includes(m) && registry[m]);
      cur.modes = cur.modes.filter((m) => m !== mode);
      if (rest.length) { note(`${LABEL[mode]} could not load for this example (${e.message || e}); showing ${LABEL[rest[0]]}.`); return show(rest[0], false); }
      document.getElementById("list").hidden = false;
      document.getElementById("example").hidden = true;
      document.getElementById("list").innerHTML = `<p class="err">No data for ${v.esc(cur.id)}.</p>`;
    }
  }

  async function open(id, meta, modes) {
    cur.id = id; cur.meta = meta; cur.modes = modes.slice(); cur.pos = {};
    if (cur.mode && registry[cur.mode] && registry[cur.mode].hide) registry[cur.mode].hide();
    cur.mode = null;
    note("");
    const asked = params.get("mode");
    const p = pick(asked && ORDER.includes(asked) ? asked : null);
    if (p.fell) note(`This example has no ${LABEL[asked]} view; showing ${LABEL[p.mode]}.`);
    await show(p.mode, true);
  }

  function switchTo(mode) {
    if (!cur.id || mode === cur.mode || !cur.modes.includes(mode) || !registry[mode]) return;
    note("");
    V().stop();
    show(mode, false);
  }

  window.CVIZ_MODES = {
    register(name, mode) { registry[name] = Object.assign({ label: LABEL[name] }, mode); },
    open, switchTo, fetchJson,
    go(to) { if (cur.mode && registry[cur.mode]) registry[cur.mode].go(to); },
    clear() { if (cur.mode && registry[cur.mode] && registry[cur.mode].hide) registry[cur.mode].hide(); cur.id = null; cur.mode = null; V().state.mode = "run"; const b = document.getElementById("modetabs"); if (b) b.hidden = true; note(""); },
    currentId() { return cur.id; },
    urlState() {
      if (!cur.mode || !registry[cur.mode]) return {};
      const u = registry[cur.mode].url() || {};
      return cur.mode === "run" && !params.has("mode") ? u : Object.assign({ mode: cur.mode }, u);
    },
  };
})();
