// Zoomable full-page screenshot viewer for the version pages.
(function () {
  const viewer = document.getElementById("viewer");
  const shots = Array.from(document.querySelectorAll(".shot"));
  if (!viewer || !shots.length) return;

  const stage = document.getElementById("viewer-stage");
  const img = document.getElementById("viewer-img");
  const title = document.getElementById("viewer-title");
  const zoomLabel = document.getElementById("viewer-zoom");
  const openLink = document.getElementById("viewer-open");
  let index = 0;
  let scale = 1; // 1 = fit to the stage width

  function natural() { return img.naturalWidth || 1440; }
  function fitWidth() { return Math.min(natural(), stage.clientWidth - 48); }

  function applyZoom(next, anchorX, anchorY) {
    const prev = scale;
    scale = Math.min(4, Math.max(0.25, next));
    // Keep the point under the cursor (or the centre) steady while zooming.
    const ax = anchorX ?? stage.clientWidth / 2;
    const ay = anchorY ?? stage.clientHeight / 2;
    const cx = stage.scrollLeft + ax;
    const cy = stage.scrollTop + ay - 24;
    img.style.width = Math.round(fitWidth() * scale) + "px";
    const ratio = scale / prev;
    stage.scrollLeft = cx * ratio - ax;
    stage.scrollTop = cy * ratio - ay + 24;
    zoomLabel.textContent = Math.round((fitWidth() * scale / natural()) * 100) + "%";
  }

  function show(i) {
    index = (i + shots.length) % shots.length;
    const s = shots[index];
    title.textContent = s.dataset.title;
    openLink.href = s.dataset.full;
    img.alt = s.dataset.title;
    scale = 1;
    img.style.width = fitWidth() + "px";
    zoomLabel.textContent = "…";
    img.onload = () => applyZoom(1);
    img.src = s.dataset.full;
    stage.scrollTo(0, 0);
  }

  function open(i) {
    viewer.hidden = false;
    document.body.style.overflow = "hidden";
    show(i);
  }
  function close() {
    viewer.hidden = true;
    document.body.style.overflow = "";
    shots[index].focus();
  }

  shots.forEach((s, i) => s.addEventListener("click", () => open(i)));

  viewer.addEventListener("click", (e) => {
    const act = e.target.closest("[data-act]")?.dataset.act;
    if (act === "close") close();
    else if (act === "prev") show(index - 1);
    else if (act === "next") show(index + 1);
    else if (act === "in") applyZoom(scale * 1.25);
    else if (act === "out") applyZoom(scale / 1.25);
    else if (act === "fit") applyZoom(scale === 1 ? natural() / fitWidth() : 1);
  });

  document.addEventListener("keydown", (e) => {
    if (viewer.hidden) return;
    if (e.key === "Escape") close();
    else if (e.key === "ArrowRight") show(index + 1);
    else if (e.key === "ArrowLeft") show(index - 1);
    else if (e.key === "+" || e.key === "=") applyZoom(scale * 1.25);
    else if (e.key === "-") applyZoom(scale / 1.25);
    else if (e.key === "0") applyZoom(1);
  });

  // Ctrl/Cmd + wheel (and trackpad pinch, which browsers report as ctrl+wheel) zooms.
  stage.addEventListener("wheel", (e) => {
    if (!e.ctrlKey && !e.metaKey) return;
    e.preventDefault();
    const r = stage.getBoundingClientRect();
    applyZoom(scale * Math.exp(-e.deltaY * 0.0025), e.clientX - r.left, e.clientY - r.top);
  }, { passive: false });

  // Double-click toggles between fit and a 2x close-up at the clicked point.
  img.addEventListener("dblclick", (e) => {
    const r = stage.getBoundingClientRect();
    applyZoom(scale > 1 ? 1 : 2, e.clientX - r.left, e.clientY - r.top);
  });

  // Drag to pan with the mouse.
  let drag = null;
  stage.addEventListener("pointerdown", (e) => {
    if (e.pointerType !== "mouse" || e.button !== 0) return;
    drag = { x: e.clientX, y: e.clientY, l: stage.scrollLeft, t: stage.scrollTop };
    stage.classList.add("dragging");
  });
  window.addEventListener("pointermove", (e) => {
    if (!drag) return;
    stage.scrollLeft = drag.l - (e.clientX - drag.x);
    stage.scrollTop = drag.t - (e.clientY - drag.y);
  });
  window.addEventListener("pointerup", () => { drag = null; stage.classList.remove("dragging"); });

  // Two-finger pinch on touch screens.
  let pinch = null;
  stage.addEventListener("touchstart", (e) => {
    if (e.touches.length === 2) {
      const [a, b] = e.touches;
      pinch = { d: Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY), s: scale };
    }
  }, { passive: true });
  stage.addEventListener("touchmove", (e) => {
    if (!pinch || e.touches.length !== 2) return;
    e.preventDefault();
    const [a, b] = e.touches;
    const r = stage.getBoundingClientRect();
    const d = Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY);
    applyZoom(pinch.s * d / pinch.d, (a.clientX + b.clientX) / 2 - r.left, (a.clientY + b.clientY) / 2 - r.top);
  }, { passive: false });
  stage.addEventListener("touchend", () => { pinch = null; });

  window.addEventListener("resize", () => { if (!viewer.hidden) applyZoom(scale); });
})();
