// Click-to-zoom for screenshots in page content.
// Click an image to view it fit-to-screen, click again for full size (drag or
// scroll to pan). Esc, the × button, or clicking the backdrop closes it.
// Images inside links are left alone so they keep opening their link.
(() => {
  const HINT = 'Click to zoom in/out · Drag to pan · Esc to close';
  let overlay, view, caption;
  let zoomed = false;
  let drag = null;
  let suppressClick = false;

  document.querySelectorAll('.markdown-body img').forEach((img) => {
    if (!img.closest('a')) img.classList.add('img-zoomable');
  });

  document.addEventListener('click', (e) => {
    if (e.target.classList && e.target.classList.contains('img-zoomable')) open(e.target);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && overlay && overlay.classList.contains('is-open')) close();
  });

  function build() {
    overlay = document.createElement('div');
    overlay.className = 'img-zoom-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.innerHTML =
      '<button type="button" class="img-zoom-close" aria-label="Close">' +
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>' +
      '</button>' +
      '<img alt="" draggable="false">' +
      '<div class="img-zoom-caption"></div>';
    view = overlay.querySelector('img');
    caption = overlay.querySelector('.img-zoom-caption');
    document.body.appendChild(overlay);

    overlay.addEventListener('pointerdown', () => {
      suppressClick = false;
    });
    overlay.addEventListener('click', (e) => {
      if (suppressClick) {
        suppressClick = false;
      } else if (e.target === view) {
        toggleZoom(e);
      } else {
        close();
      }
    });

    // Mouse drag pans when zoomed; touch devices pan with native scrolling.
    view.addEventListener('pointerdown', (e) => {
      if (!zoomed || e.pointerType !== 'mouse' || e.button !== 0) return;
      drag = { x: e.clientX, y: e.clientY, left: overlay.scrollLeft, top: overlay.scrollTop };
      view.setPointerCapture(e.pointerId);
    });
    view.addEventListener('pointermove', (e) => {
      if (!drag) return;
      const dx = e.clientX - drag.x;
      const dy = e.clientY - drag.y;
      if (Math.abs(dx) + Math.abs(dy) > 4) overlay.classList.add('is-dragging');
      overlay.scrollLeft = drag.left - dx;
      overlay.scrollTop = drag.top - dy;
    });
    view.addEventListener('pointerup', () => {
      if (!drag) return;
      suppressClick = overlay.classList.contains('is-dragging');
      overlay.classList.remove('is-dragging');
      drag = null;
    });
  }

  function toggleZoom(e) {
    if (zoomed) {
      setZoom(false);
      return;
    }
    const r = view.getBoundingClientRect();
    const rx = (e.clientX - r.left) / r.width;
    const ry = (e.clientY - r.top) / r.height;
    // Full resolution, but at least 2x the fitted size so small images still grow.
    setZoom(true, Math.max(view.naturalWidth, r.width * 2));
    // Scroll so the point that was clicked stays under the cursor.
    overlay.scrollLeft = view.offsetLeft + rx * view.offsetWidth - e.clientX;
    overlay.scrollTop = view.offsetTop + ry * view.offsetHeight - e.clientY;
  }

  function setZoom(on, width) {
    zoomed = on;
    overlay.classList.toggle('is-zoomed', on);
    view.style.width = on ? `${width}px` : '';
  }

  function open(img) {
    if (!overlay) build();
    setZoom(false);
    view.src = img.currentSrc || img.src;
    view.alt = img.alt;
    caption.textContent = img.alt ? `${img.alt} — ${HINT}` : HINT;
    overlay.classList.add('is-open');
    document.documentElement.classList.add('img-zoom-lock');
  }

  function close() {
    overlay.classList.remove('is-open');
    document.documentElement.classList.remove('img-zoom-lock');
  }
})();
