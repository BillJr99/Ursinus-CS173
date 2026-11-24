/* code-viz Simulate mode (mode-simulate.js): replay a recorded terminal session as if it ran live.

   Full manual: the header of code-viz (`code-viz readme`, or README.md), section 23 Simulate mode,
   sessions and recording; section 21 for the tabs and URL arguments.

   WHAT IT SHOWS
   A session (viz/sessions/<id>.json.gz) was run for real and recorded by `code-viz record`: each
   command with its terminal output as timestamped chunks (`cast`), its exit status, its time, and
   what Docker looked like afterwards. Nothing is guessed: every character on the screen is recorded.
     left    a real terminal emulator (xterm.js 5.3.0, pinned, from jsDelivr, loaded on first use),
             so colors, cursor moves, \r progress bars, `clear` and full-screen programs look as they
             did live. The screen persists from command to command, with scrollback.
             Next command (Space or the right arrow) reveals the next command line by line,
             then plays its output at the recorded pace; 0.5x (Slow), 1x, fast and instant set the speed. Back
             (<, left arrow) and jumping (the slider, Home, &s=N) rebuild the exact screen at that
             point at once from the recording. Pressing Next while a command is still playing
             finishes it at once.
             Below the terminal students can type the next command themselves: the recorded command
             (spacing aside) plays exactly as Next would; anything else gets a hint, never output.
     right   the docker ps table, a diagram of containers grouped by network with published ports and
             mounted folders, images, volumes and the watched folders' files, as they were when the
             current command finished.
   Recorded "what if" branches appear as buttons beside the speed control; a branch replays the main
   line up to its branch point, then its own recorded commands.

   PHONES: the terminal keeps the recorded width (100 columns) and scales its font to fit the box,
   down to 9 px; below that it scrolls sideways inside its own box, never the page.

   If xterm.js cannot load (offline before first use), the terminal falls back to plain text.

   URL: ?mode=simulate&s=N#<id> opens with commands 0..N already run (N from 0); without s it opens
   at the first prompt, before anything has run. &branch=<name> opens on a branch.
*/
(function () {
  "use strict";
  const XTERM = "https://cdn.jsdelivr.net/npm/xterm@5.3.0/";
  const PROMPT = "\x1b[1;32m$\x1b[0m ";
  const SPEEDS = { "0.5x (Slow)": 0.5, "1x": 1, fast: 4, instant: 0 };
  const S = { sess: null, id: null, step: -1, branch: "", speed: "1x", pacing: "line", term: null, xtermTried: false, token: 0, playing: false };
  const V = () => window.CVIZ_VIEWER;
  const el = (id) => document.getElementById(id);
  const norm = (c) => String(c || "").trim().replace(/\s+/g, " ");

  function steps() {
    const s = S.sess;
    if (!S.branch) return s.steps || [];
    const b = (s.branches || []).find((x) => x.name === S.branch);
    return b ? (s.steps || []).slice(0, b.after).concat(b.steps || []) : (s.steps || []);
  }
  const castOf = (st) => (st.cast && st.cast.length ? st.cast : [[0, (st.output || "").replace(/\n/g, "\r\n")]]);
  const outOf = (st) => castOf(st).map((c) => c[1]).join("");

  // ---------- the terminal ----------
  async function loadXterm() {
    if (window.Terminal || S.xtermTried) return !!window.Terminal;
    S.xtermTried = true;
    try {
      const css = document.createElement("link"); css.rel = "stylesheet"; css.href = XTERM + "css/xterm.css"; document.head.appendChild(css);
      await new Promise((ok, bad) => { const s = document.createElement("script"); s.src = XTERM + "lib/xterm.js"; s.onload = ok; s.onerror = bad; document.head.appendChild(s); });
    } catch (e) { /* offline: plain-text fallback */ }
    return !!window.Terminal;
  }

  function fit() {
    // Keep the recorded width; scale the font so it fits the box (not under 9 px), else scroll inside it.
    const box = el("simterm"); if (!box || !S.term) return;
    const cols = (S.sess.recorded && S.sess.recorded.cols) || 100;
    const w = box.clientWidth || 600;
    const size = Math.max(9, Math.min(14, Math.floor(w / (cols * 0.62))));
    if (S.term.options.fontSize !== size) S.term.options.fontSize = size;
  }

  function makeTerm() {
    const box = el("simterm");
    if (S.term) { S.term.dispose(); S.term = null; }
    box.innerHTML = "";
    if (!window.Terminal) { S.term = null; box.classList.add("plainterm"); return; }
    box.classList.remove("plainterm");
    const rec = S.sess.recorded || {};
    S.term = new window.Terminal({ cols: rec.cols || 100, rows: rec.rows || 30, scrollback: 5000, disableStdin: true,
      convertEol: false, cursorBlink: false, fontSize: 13, fontFamily: "ui-monospace, Menlo, Consolas, monospace",
      theme: { background: "#1d2330", foreground: "#e6e9ef", cursor: "#e6e9ef" } });
    S.term.open(box);
    fit();
  }

  // Everything the terminal showed up to and including command k, then the waiting prompt.
  function screenData(k) {
    const list = steps();
    let d = "";
    for (let i = 0; i <= k && i < list.length; i++) {
      const out = outOf(list[i]);
      d += PROMPT + list[i].cmd + "\r\n" + out + (out && !/\n$/.test(out) ? "\r\n" : "");
    }
    return d + PROMPT;
  }

  function plainScreen(k) {
    const esc = V().esc, list = steps();
    let h = "";
    for (let i = 0; i <= k && i < list.length; i++) {
      h += `<div class="tline"><span class="prompt">$</span> ${esc(list[i].cmd)}</div>`;
      if (list[i].output) h += `<div class="tout">${esc(list[i].output.replace(/\n$/, ""))}</div>`;
    }
    return h + '<div class="tline"><span class="prompt">$</span></div>';
  }

  function drawInstant(k) {
    S.token++; S.playing = false;
    if (S.term) { S.term.reset(); S.term.write(screenData(k)); }
    else el("simterm").innerHTML = plainScreen(k);
    S.step = k;
    panels();
  }

  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  // Reveal command k at the prompt, then play its original output chunks.
  async function play(k) {
    const list = steps(), st = list[k];
    if (!st) return;
    const f = SPEEDS[S.speed];
    if (!S.term || f === 0 || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return drawInstant(k);
    const my = ++S.token, line = S.pacing === "line";
    S.playing = true;
    el("next").textContent = "Finish command";
    // Budget as for character typing, plus 90 ms to read each revealed line at 1x.
    const perChar = Math.min(35, 1500 / Math.max(1, st.cmd.length));
    // Keep ANSI-bearing commands opaque, and don't split CRLF or alter command bytes.
    const parts = /[\x1b\x80-\x9f]/.test(st.cmd) ? [st.cmd] :
      st.cmd.match(line ? /[^\n]*\n|[^\n]+/g : /\r\n|[\s\S]/gu) || [];
    for (const part of parts) {
      if (my !== S.token) return;
      S.term.write(part);
      await sleep(([...part].length * perChar + (line ? 90 : 0)) / f);
    }
    if (my !== S.token) return;
    S.term.write("\r\n");
    let last = 0;
    for (const [t, data] of castOf(st)) {
      const gap = Math.min(Math.max(0, t - last), 2) / f;    // long pauses shortened to 2 s at 1x
      last = t;
      if (gap > 0.01) await sleep(gap * 1000);
      if (my !== S.token) return;
      S.term.write(data);
    }
    const out = outOf(st);
    S.term.write((out && !/\n$/.test(out) ? "\r\n" : "") + PROMPT);
    S.playing = false;
    S.step = k;
    panels();
  }

  // ---------- the right side and the step controls ----------
  function diagram(state) {
    const esc = V().esc, cs = state.containers || [];
    if (!cs.length) return '<p class="note">No containers.</p>';
    const nets = {};
    for (const c of cs) for (const n of (c.networks && c.networks.length ? c.networks : ["(no network)"])) (nets[n] = nets[n] || []).push(c);
    let h = '<div class="netdiag">';
    for (const [n, list] of Object.entries(nets)) {
      h += `<div class="net"><div class="netname">network ${esc(n)}</div>`;
      for (const c of list) {
        h += `<div class="ctr ${/^up|running/i.test(c.status || "") ? "up" : "down"}"><b>${esc(c.name)}</b><span class="img">${esc(c.image || "")}</span>`;
        for (const p of c.ports || []) h += `<span class="tag port" title="published port">${esc(p)}</span>`;
        for (const m of c.mounts || []) h += `<span class="tag mount" title="mounted folder">${esc(m)}</span>`;
        h += "</div>";
      }
      h += "</div>";
    }
    return h + "</div>";
  }

  function panels() {
    const esc = V().esc, list = steps(), n = list.length, st = list[S.step];
    el("next").textContent = "Next command";
    el("slider").min = 0; el("slider").max = n; el("slider").value = S.step + 1;
    el("stepinfo").textContent = S.step < 0 ? `${n} command${n === 1 ? "" : "s"}, none run yet` : `command ${S.step + 1} of ${n}`;
    el("paneltitle").textContent = S.step < 0 ? "Before the first command" : "After this command";
    el("output").textContent = st ? `took ${st.duration != null ? st.duration + " s" : "?"}, exit ${st.exit}` : "";
    if (!st) { el("panel").innerHTML = '<p class="note">Nothing has run yet. Choose Next command (Space) or type the first command.</p>'; }
    else {
      const state = st.state || {};
      let h = st.note ? `<p class="tournote">${esc(st.note)}</p>` : "";
      const cs = state.containers || [];
      h += '<div class="panel-sub">docker ps -a</div>' + (cs.length
        ? '<table class="dps"><tr><th>name</th><th>image</th><th>status</th><th>ports</th></tr>' +
          cs.map((c) => `<tr><td>${esc(c.name)}</td><td>${esc(c.image || "")}</td><td>${esc(c.status || "")}</td><td>${esc((c.ports || []).join(", "))}</td></tr>`).join("") + "</table>"
        : '<p class="note">No containers.</p>');
      h += '<div class="panel-sub">Containers, networks, ports and mounts</div>' + diagram(state);
      if ((state.images || []).length) h += `<div class="panel-sub">Images</div><p class="mono">${state.images.map(esc).join("<br>")}</p>`;
      if ((state.volumes || []).length) h += `<div class="panel-sub">Volumes</div><p class="mono">${state.volumes.map(esc).join("<br>")}</p>`;
      for (const [dir, files] of Object.entries(state.files || {})) h += `<div class="panel-sub">Files in ${esc(dir)}</div><pre class="mono">${files.length ? files.map(esc).join("\n") : "(empty)"}</pre>`;
      el("panel").innerHTML = h;
    }
    const nxt = list[S.step + 1], box = el("simcmd");
    if (box) { box.disabled = !nxt; box.placeholder = nxt ? "Type the next command and press Enter" : "That was the last command"; }
  }

  function tryCommand() {
    const box = el("simcmd"), hint = el("simhint"), list = steps(), nxt = list[S.step + 1];
    if (!box || !nxt || S.playing) return;
    const typed = norm(box.value);
    if (!typed) return;
    if (typed === norm(nxt.cmd)) { box.value = ""; hint.textContent = ""; play(S.step + 1); return; }
    const want = norm(nxt.cmd).split(" "), got = typed.split(" ");
    let k = 0; while (k < want.length && k < got.length && want[k] === got[k]) k++;
    hint.textContent = `That is not the command that was recorded here. Hint: it starts with "${want.slice(0, Math.max(1, Math.min(k + 1, 3))).join(" ")}".`;
  }

  function extra() {
    const x = el("extra"); x.innerHTML = "";
    const mk = (label, on, title, fn) => { const b = document.createElement("button"); b.textContent = label; b.className = on ? "on" : ""; b.title = title || ""; b.onclick = fn; x.appendChild(b); };
    for (const sp of Object.keys(SPEEDS)) mk(sp, S.speed === sp, "Playback speed for the next command", () => { S.speed = sp; extra(); });
    const label = document.createElement("label"), pacing = document.createElement("select");
    label.textContent = "Command pacing ";
    pacing.setAttribute("id", "simulate-pacing");
    for (const [value, text] of [["line", "Line by line"], ["character", "Character by character"]]) {
      const option = document.createElement("option"); option.value = value; option.textContent = text; pacing.append(option);
    }
    pacing.value = S.pacing;
    pacing.onchange = () => { S.pacing = pacing.value; };
    label.append(pacing); x.append(label);
    const bs = S.sess.branches || [];
    if (bs.length) {
      x.appendChild(Object.assign(document.createElement("span"), { className: "sep" }));
      mk("main", !S.branch, "The session as recorded", () => { S.branch = ""; extra(); drawInstant(-1); });
      for (const b of bs) mk("what if: " + (b.title || b.name), S.branch === b.name, b.description || "", () => { S.branch = b.name; extra(); drawInstant(-1); });
    }
  }

  function chrome(on) {
    for (const id of ["edit", "reset", "play"]) { const b = el(id); if (b) b.style.display = on ? "none" : ""; }
    const next = el("next");
    next.textContent = on ? "Next command" : ">";
    next.title = on ? "Next command (Space or right arrow)" : "Next step (right arrow)";
    el("setupbox").hidden = true;
    const f = el("figures"); if (f) f.hidden = true;
    el("code").hidden = on;
    const t = el("simterm"); if (t) t.hidden = !on;
    const sim = el("simbar"); if (sim) sim.hidden = !on;
    document.querySelectorAll(".panel-title").forEach((p) => { if (p.textContent === "Code" || p.textContent === "Terminal") p.textContent = on ? "Terminal" : "Code"; });
  }

  window.addEventListener("resize", () => { if (document.body.dataset.mode === "simulate") fit(); });

  window.CVIZ_MODES.register("simulate", {
    async show(ctx) {
      const fresh = S.id !== ctx.id || !S.sess;
      if (fresh) {
        S.sess = await ctx.fetchJson("sessions/" + encodeURIComponent(ctx.id) + ".json.gz");
        S.id = ctx.id; S.step = -1; S.branch = "";
      }
      // The URL's branch applies when the session opens; a tab switch keeps the branch on screen.
      if (fresh) { const b = ctx.params.get("branch") || ""; S.branch = (S.sess.branches || []).some((x) => x.name === b) ? b : ""; }
      el("list").hidden = true; el("example").hidden = false;
      el("title").textContent = `${S.sess.title || ctx.id}  ·  simulate`;
      if (ctx.meta.page_url) { el("pagelink").href = ctx.meta.page_url; el("pagelink").textContent = "Open the page this session is on"; }
      else el("pagelink").textContent = "";
      el("editor").hidden = true;
      chrome(true);
      await loadXterm();
      makeTerm();
      extra();
      const box = el("simcmd");
      if (box) { box.value = ""; box.onkeydown = (e) => { if (e.key === "Enter") { e.preventDefault(); tryCommand(); } }; }
      const hint = el("simhint"); if (hint) hint.textContent = "";
      drawInstant(ctx.pos !== undefined ? Math.max(-1, Math.min(ctx.pos, steps().length - 1)) : -1);
    },
    go(to) {
      if (!S.sess) return;
      const n = steps().length;
      const hint = el("simhint"); if (hint) hint.textContent = "";
      if (to === "+1") {
        if (S.playing) return drawInstant(Math.min(S.step + 1, n - 1));   // finish the command that is playing
        if (S.step < n - 1) play(S.step + 1);
        return;
      }
      if (to === "-1") return drawInstant(Math.max(-1, (S.playing ? S.step + 1 : S.step) - 1));
      drawInstant(Math.max(-1, Math.min(n - 1, Number(to) - 1)));        // slider and Home/Last: 0 = before the first command
    },
    pos() { return S.step; },
    url() { const u = {}; if (S.step >= 0) u.s = S.step; if (S.branch) u.branch = S.branch; return u; },
    hide() { S.token++; S.playing = false; chrome(false); el("extra").innerHTML = ""; },
  });
})();
