/* code-viz viewer: figures an example drew (matplotlib plots, turtle and ezgraphics drawings).

   Full manual: the header of code-viz (`code-viz readme`, or README.md), sections 7 (Figures) and 14
   (Trace format).

   A trace may carry "figures": [{"png": base64 PNG, "at": output offset}] (tracers/driver.py with
   tracers/cviz_mplbackend.py). viewer.js calls cvizFigures.show(trace, container, outLength, all)
   after it draws the Output panel: in a stepped trace (env, c) a figure appears once the printed
   output so far reaches its "at" offset, which is when the program showed it; otherwise (plain,
   agent, and at the last step) every figure shows. Each figure is an <img> with alt text "Figure N";
   clicking one opens it full size in a new tab. "figures_dropped" (figures over the size cap) is
   reported under the images. Styles are injected here so viewer.css needs no change. */
(function () {
  const css = ".cviz-figures{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 0}" +
    ".cviz-figures img{max-width:100%;height:auto;border:1px solid var(--line,#8884);border-radius:4px;background:#fff;cursor:zoom-in}" +
    ".cviz-figures .note{font-size:.85em;opacity:.75;width:100%}";
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  let shownFor = null, shownCount = -1;
  function show(t, box, outLen, all) {
    if (!box) return;
    const figs = (t && t.figures) || [];
    const vis = all ? figs : figs.filter((f) => (f.at || 0) <= outLen);
    box.hidden = !figs.length;
    if (shownFor === t && shownCount === vis.length) return;  // unchanged: keep the images (no flicker)
    shownFor = t; shownCount = vis.length;
    box.className = "cviz-figures";
    box.textContent = "";
    vis.forEach((f, i) => {
      const img = document.createElement("img");
      img.src = "data:image/png;base64," + f.png;
      img.alt = "Figure " + (i + 1);
      img.title = "Figure " + (i + 1) + " (click to open full size)";
      img.addEventListener("click", () => {
        const a = document.createElement("a"); a.href = img.src; a.target = "_blank"; a.rel = "noopener"; a.click();
      });
      box.appendChild(img);
    });
    if (figs.length && !vis.length) {
      const n = document.createElement("span"); n.className = "note"; n.textContent = "Figures appear when the program shows them.";
      box.appendChild(n);
    }
    if (t.figures_dropped) {
      const n = document.createElement("span"); n.className = "note";
      n.textContent = t.figures_dropped + " more figure(s) not kept (size cap).";
      box.appendChild(n);
    }
  }
  window.cvizFigures = { show };
})();
