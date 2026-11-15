/* code-viz Explain mode (mode-explain.js): step through a tour of one example.

   Full manual: the header of code-viz (`code-viz readme`, or README.md), section 22 Explain mode and
   the tour format; section 21 for the tabs and URL arguments.

   WHAT IT SHOWS
   The code on the left and a step card on the right. A tour is a list of steps
   (viz/tours/<id>.json, published by code-viz build with the code it explains):
     reveal   lines appear, added to the ones already shown; lines not yet revealed stay hidden
     focus    these lines are highlighted and the rest are dimmed
     predict  the card asks the question; "Show the answer" (or the next step) gives the answer
     run      the right side shows the program's state at that trace step, the same panel as Run
     stage    the code changes to the next stage of a build-up; only the changed lines are marked
   An unreviewed tour (reviewed: false) carries a "draft" badge. Code is syntax-highlighted with
   highlight.js 11.9.0 (pinned, loaded on first use); without it the code shows plain.

   URL: ?mode=explain&t=N#<id> opens at step N (from 0); &tour=<name> picks a named tour.
   The step controls, the slider and the presenter keys (Space, arrows, Home) move through the tour.
*/
(function () {
  "use strict";
  const HLJS = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/";
  const S = { tour: null, step: 0, id: null, name: "", traces: {}, prevCode: null, hl: null, hlTried: false };
  const V = () => window.CVIZ_VIEWER;
  const el = (id) => document.getElementById(id);

  function parse(spec) {
    const out = new Set();
    for (const part of String(spec || "").split(",")) {
      if (!part) continue;
      const [a, b] = part.split("-").map(Number);
      for (let n = Math.min(a, b || a); n <= Math.max(a, b || a); n++) out.add(n);
    }
    return out;
  }
  const linesOf = (s) => { const set = parse(s.lines); if (s.line) set.add(s.line); return set; };

  // highlight.js, loaded once; a failure (offline) just leaves the code plain.
  async function hljs() {
    if (S.hl || S.hlTried) return S.hl;
    S.hlTried = true;
    try {
      await new Promise((ok, bad) => { const s = document.createElement("script"); s.src = HLJS + "highlight.min.js"; s.onload = ok; s.onerror = bad; document.head.appendChild(s); });
      const css = document.createElement("link"); css.rel = "stylesheet"; css.href = HLJS + "styles/github.min.css"; document.head.appendChild(css);
      S.hl = window.hljs || null;
    } catch (e) { S.hl = null; }
    return S.hl;
  }
  const HL_LANG = { shell: "bash", js: "javascript", cpp: "cpp", c: "c", python: "python", java: "java", scheme: "scheme",
                    sql: "sql", haskell: "haskell", prolog: "prolog", ocaml: "ocaml", mips: "mipsasm", vhdl: "vhdl", yaml: "yaml", json: "json" };

  // Which code is showing at step i: the example's, or the latest stage's.
  function codeAt(i) {
    const t = S.tour;
    let code = t.code || "", lang = t.lang || "", id = S.id;
    for (let k = 0; k <= i; k++) {
      const s = t.steps[k];
      if (s.kind === "stage" && t.stages && t.stages[s.stage]) { code = t.stages[s.stage].code; lang = t.stages[s.stage].lang || lang; id = s.stage; }
    }
    return { code, lang, id };
  }

  // Lines revealed so far for the code showing at step i (null: no reveal steps, so all lines show).
  function revealedAt(i) {
    const t = S.tour;
    let set = null, stageStart = 0;
    for (let k = 0; k <= i; k++) if (t.steps[k].kind === "stage") stageStart = k;
    for (let k = stageStart; k <= i; k++) {
      const s = t.steps[k];
      if (s.kind === "reveal") { set = set || new Set(); for (const n of linesOf(s)) set.add(n); }
    }
    const anyReveal = t.steps.slice(stageStart).some((s) => s.kind === "reveal");
    return anyReveal ? (set || new Set()) : null;
  }

  // Lines that changed from one stage's code to the next (a longest-common-subsequence diff).
  function changed(oldCode, newCode) {
    const a = (oldCode || "").split("\n"), b = newCode.split("\n");
    const n = a.length, m = b.length;
    if (n * m > 400000) return new Set(b.map((_, j) => j + 1));
    const L = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
    for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--) L[i][j] = a[i] === b[j] ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
    const out = new Set();
    let i = 0, j = 0;
    while (j < m) {
      if (i < n && a[i] === b[j]) { i++; j++; }
      else if (i < n && L[i + 1][j] >= L[i][j + 1]) i++;
      else { out.add(j + 1); j++; }
    }
    return out;
  }

  function drawCode(code, lang) {
    const hl = S.hl, hlLang = HL_LANG[lang] || lang;
    const ok = hl && hlLang && hl.getLanguage && hl.getLanguage(hlLang);
    el("code").innerHTML = code.split("\n").map((l, i) => {
      const inner = ok ? hl.highlight(l, { language: hlLang, ignoreIllegals: true }).value : V().esc(l);
      return `<span class="ln" data-n="${i + 1}">${inner || " "}</span>`;
    }).join("");
  }

  async function trace(id) {
    if (!(id in S.traces)) {
      try { S.traces[id] = V().expand(await V().loadTrace(id)); } catch (e) { S.traces[id] = null; }
    }
    return S.traces[id];
  }

  async function render() {
    const v = V(), t = S.tour, n = t.steps.length;
    S.step = Math.max(0, Math.min(S.step, n - 1));
    const s = t.steps[S.step];
    el("slider").max = Math.max(0, n - 1); el("slider").value = S.step;
    el("stepinfo").textContent = `step ${S.step + 1} of ${n}`;
    const { code, lang, id } = codeAt(S.step);
    drawCode(code, lang);
    const fresh = S.prevCode !== null && S.prevCode !== code ? changed(S.prevCode, code) : new Set();
    S.prevCode = code;
    const shown = revealedAt(S.step);
    const focus = s.kind === "focus" || s.kind === "run" || s.kind === "predict" ? linesOf(s) : new Set();
    document.querySelectorAll("#code .ln").forEach((ln) => {
      const k = Number(ln.dataset.n);
      ln.classList.toggle("hid", !!shown && !shown.has(k));
      ln.classList.toggle("foc", focus.has(k));
      ln.classList.toggle("dim", focus.size > 0 && !focus.has(k));
      ln.classList.toggle("fresh", fresh.has(k));
    });
    const first = document.querySelector("#code .ln.foc") || document.querySelector("#code .ln.fresh");
    if (first) first.scrollIntoView({ block: "nearest" });
    // The card: title, the step's text, a predict question, and the draft badge.
    el("paneltitle").textContent = s.kind === "run" ? "Running" : "Explain";
    const badge = t.reviewed ? "" : ' <span class="badge draft" title="Drafted, not yet reviewed by the instructor">draft</span>';
    let card = `<div class="tourcard"><div class="tourhead">${v.esc(t.title)}${badge}</div>`;
    if (S.step === 0 && t.description) card += `<p class="tourdesc">${v.esc(t.description)}</p>`;
    if (s.title) card += `<h3>${v.esc(s.title)}</h3>`;
    if (s.description) card += `<p>${v.esc(s.description)}</p>`;
    if (s.kind === "predict") {
      card += `<p class="predict"><b>Predict:</b> ${v.esc(s.question || "")}</p>`;
      if (s.answer) card += `<button id="showanswer">Show the answer</button><p id="answer" class="answer" hidden>${v.esc(s.answer)}</p>`;
    }
    const prev = t.steps[S.step - 1];
    if (prev && prev.kind === "predict" && prev.answer && s.kind !== "predict") card += `<p class="answer"><b>Answer:</b> ${v.esc(prev.answer)}</p>`;
    card += "</div>";
    el("output").textContent = "";
    if (s.kind === "run") {
      const tr = await trace(id);
      const steps = tr ? v.stepsOf(tr) : [];
      const at = steps[Math.min(s.trace_step || 0, Math.max(0, steps.length - 1))];
      el("panel").innerHTML = "";
      if (tr && at) {
        const P = v.panels();
        (P[tr.kind] || P.plain)(tr, at, steps);
        el("panel").insertAdjacentHTML("afterbegin", card);
        let out = tr.stdout || "";
        if (typeof at.out === "number") out = out.slice(0, at.out);
        el("output").textContent = out;
        const cur = v.currentLine(tr, at);
        if (cur) { const ln = document.querySelector(`#code .ln[data-n="${cur}"]`); if (ln) ln.classList.add("cur"); }
      } else {
        el("panel").innerHTML = card + '<p class="note">The recorded run for this step did not load.</p>';
      }
    } else {
      el("panel").innerHTML = card;
    }
    const sa = el("showanswer");
    if (sa) sa.onclick = () => { el("answer").hidden = false; sa.hidden = true; };
  }

  function controls(on) {
    // Edit, Reset and Play belong to Run mode; Explain moves one step at a time.
    for (const id of ["edit", "reset", "play"]) { const b = el(id); if (b) b.style.display = on ? "none" : ""; }
    el("setupbox").hidden = true;
    const f = el("figures"); if (f) f.hidden = true;
  }

  window.CVIZ_MODES.register("explain", {
    async show(ctx) {
      const v = ctx.V;
      const name = ctx.params.get("tour") || "";
      const names = ctx.meta.tours || [""];
      S.name = names.includes(name) ? name : (names[0] || "");
      if (name && S.name !== name) ctx.note(`This example has no tour named "${name}"; showing its ${S.name ? '"' + S.name + '"' : "default"} tour.`);
      if (S.id !== ctx.id || !S.tour || S.loaded !== S.name) {
        S.tour = await ctx.fetchJson("tours/" + encodeURIComponent(ctx.id) + (S.name ? "--" + S.name : "") + ".json");
        S.id = ctx.id; S.loaded = S.name; S.traces = {}; S.prevCode = null; S.step = 0;
      }
      if (ctx.pos !== undefined) S.step = ctx.pos;
      await hljs();
      el("list").hidden = true; el("example").hidden = false;
      el("title").textContent = `${ctx.id}  ·  explain`;
      if (ctx.meta.page_url) { el("pagelink").href = ctx.meta.page_url; el("pagelink").textContent = "Open the page this example is on"; }
      else el("pagelink").textContent = "";
      el("editor").hidden = true; el("code").hidden = false;
      el("extra").innerHTML = "";
      controls(true);
      S.prevCode = null;
      await render();
    },
    go(to) {
      if (!S.tour) return;
      S.step = typeof to === "string" ? S.step + Number(to) : to;
      render();
    },
    pos() { return S.step; },
    url() { const u = { t: S.step }; if (S.name) u.tour = S.name; return u; },
    hide() {
      controls(false);
      document.querySelectorAll("#code .ln").forEach((ln) => ln.classList.remove("hid", "foc", "dim", "fresh"));
    },
  });
})();
