/* ══════════════════════════════════════════════════════════════════════
   EAGLZ kozos viselkedesreteg  ·  minden oldalon ugyanaz
   ----------------------------------------------------------------------
   1. kalkulatorok: csuszka + kozvetlen szambevitel, szinkronban
   2. ertekhatarok es mertekegyseg lathatoan, ertheto hibaallapottal
   3. visszaallitas az alapertekekre
   4. tablazatok mobilon: jelzett, billentyuzettel is gorgetheto sav
   5. parbeszedablakok: fokusz be, Escape-re zar, fokusz vissza
   ══════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var HU = function (n, step) {
    var d = (step && step < 1) ? (String(step).split('.')[1] || '').length : 0;
    return Number(n).toLocaleString('hu-HU', { minimumFractionDigits: d, maximumFractionDigits: d });
  };
  var num = function (s) { return parseFloat(String(s).replace(/[^\d.,-]/g, '').replace(/\s/g, '').replace(',', '.')); };

  /* ── 1-3. kalkulator-mezok ──────────────────────────────────────────── */
  function unitOf(rng) {
    var b = document.getElementById(rng.id + '_v');
    var txt = b ? b.textContent : '';
    var u = txt.replace(/[\d\s., -]/g, '').trim();
    if (u === 'MFt' || /M\s*Ft/.test(txt)) u = 'Ft';
    return { el: b, unit: u };
  }

  function enhance(rng) {
    if (rng.dataset.uiDone) return;
    rng.dataset.uiDone = '1';
    var lab = document.querySelector('label[for="' + rng.id + '"]') ||
              (rng.previousElementSibling && rng.previousElementSibling.tagName === 'LABEL'
                ? rng.previousElementSibling : null);
    if (!lab) return;
    var info = unitOf(rng);
    var min = parseFloat(rng.min), max = parseFloat(rng.max), step = parseFloat(rng.step) || 1;

    var box = document.createElement('span');
    box.className = 'rng-box';
    var inp = document.createElement('input');
    inp.type = 'text';
    inp.inputMode = 'numeric';
    inp.className = 'rng-num';
    inp.id = rng.id + '_num';
    inp.setAttribute('aria-label', (lab.childNodes[0] ? lab.childNodes[0].textContent.trim() : 'Érték') + ' számmal');
    inp.value = HU(rng.value, step);
    box.appendChild(inp);
    if (info.unit) {
      var u = document.createElement('span');
      u.className = 'rng-unit';
      u.textContent = info.unit;
      box.appendChild(u);
    }
    if (info.el) { info.el.classList.add('rng-orig'); }
    lab.appendChild(box);

    var host = rng.parentNode;
    var mm = document.createElement('div');
    mm.className = 'rng-minmax';
    mm.innerHTML = '<span>' + HU(min, step) + (info.unit ? ' ' + info.unit : '') + '</span>' +
                   '<span>' + HU(max, step) + (info.unit ? ' ' + info.unit : '') + '</span>';
    var err = document.createElement('span');
    err.className = 'f-err';
    err.id = rng.id + '_err';
    if (rng.nextSibling) { host.insertBefore(mm, rng.nextSibling); } else { host.appendChild(mm); }
    if (mm.nextSibling) { host.insertBefore(err, mm.nextSibling); } else { host.appendChild(err); }

    function say(msg) {
      err.textContent = msg || '';
      err.classList.toggle('on', !!msg);
      inp.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (msg) { inp.setAttribute('aria-describedby', err.id); }
    }

    rng.addEventListener('input', function () {
      if (document.activeElement !== inp) inp.value = HU(rng.value, step);
      say('');
    });

    inp.addEventListener('input', function () {
      var v = num(inp.value);
      if (isNaN(v)) { say('Írj be egy számot.'); return; }
      if (v < min) { say('A legkisebb beállítható érték ' + HU(min, step) + (info.unit ? ' ' + info.unit : '') + '.'); return; }
      if (v > max) { say('A legnagyobb beállítható érték ' + HU(max, step) + (info.unit ? ' ' + info.unit : '') + '.'); return; }
      say('');
      rng.value = Math.round(v / step) * step;
      rng.dispatchEvent(new Event('input', { bubbles: true }));
      rng.dispatchEvent(new Event('change', { bubbles: true }));
    });

    inp.addEventListener('blur', function () {
      var v = num(inp.value);
      if (isNaN(v)) v = parseFloat(rng.value);
      v = Math.min(max, Math.max(min, v));
      rng.value = (Math.round(v / step) * step).toFixed(String(step).split('.')[1] ? String(step).split('.')[1].length : 0);
      inp.value = HU(rng.value, step);
      say('');
      rng.dispatchEvent(new Event('input', { bubbles: true }));
      rng.dispatchEvent(new Event('change', { bubbles: true }));
    });
  }

  function resetButtons() {
    var groups = [];
    document.querySelectorAll('input[type=range]').forEach(function (r) {
      var g = r.closest('.sc-in, .hw-pane, .calc-panel, .calc-in, .fld-wrap, .sc');
      if (g && groups.indexOf(g) === -1) groups.push(g);
    });
    groups.forEach(function (g) {
      if (g.querySelector('.calc-reset')) return;
      var fields = [].slice.call(g.querySelectorAll('input[type=range], input[type=number]'));
      if (!fields.length) return;
      var defaults = fields.map(function (f) { return f.value; });
      var segs = [].slice.call(g.querySelectorAll('.sc-seg button, .hw-tabs button'));
      var segOn = segs.map(function (s) { return s.classList.contains('on'); });
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'calc-reset';
      b.innerHTML = '<svg class="ic" aria-hidden="true" focusable="false"><use href="#i-refresh"></use></svg> Alapértékek visszaállítása';
      b.addEventListener('click', function () {
        fields.forEach(function (f, i) {
          f.value = defaults[i];
          f.dispatchEvent(new Event('input', { bubbles: true }));
          f.dispatchEvent(new Event('change', { bubbles: true }));
        });
        segs.forEach(function (s, i) { if (segOn[i] && !s.classList.contains('on')) s.click(); });
      });
      g.appendChild(b);
    });
  }

  /* ── 4. tablazatok mobilon ──────────────────────────────────────────── */
  function tables() {
    document.querySelectorAll('.tbl-wrap, .table-wrap, .ctab-wrap').forEach(function (w) {
      var over = w.scrollWidth > w.clientWidth + 2;
      w.classList.toggle('is-scroll', over);
      if (over) {
        if (!w.hasAttribute('tabindex')) {
          w.setAttribute('tabindex', '0');
          w.setAttribute('role', 'region');
          w.setAttribute('aria-label', 'Táblázat, oldalra görgethető');
        }
        if (!w.previousElementSibling || !w.previousElementSibling.classList.contains('tbl-hint')) {
          var h = document.createElement('div');
          h.className = 'tbl-hint';
          h.innerHTML = '<svg class="ic" aria-hidden="true" focusable="false"><use href="#i-transfer"></use></svg> Húzd oldalra a táblázatot a többi oszlopért';
          w.parentNode.insertBefore(h, w);
        }
      } else if (w.previousElementSibling && w.previousElementSibling.classList.contains('tbl-hint')) {
        w.previousElementSibling.remove();
      }
      w.addEventListener('scroll', function () {
        w.classList.toggle('at-end', w.scrollLeft + w.clientWidth >= w.scrollWidth - 4);
      }, { passive: true });
    });
  }

  /* ── 5. parbeszedablakok ────────────────────────────────────────────── */
  var lastOpener = null;
  function dialogs() {
    document.addEventListener('click', function (e) {
      var t = e.target.closest('[data-adv], [data-page], .adv-card, .svc-card');
      if (t) lastOpener = t;
    }, true);

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      var open = document.querySelector('.adv-modal.on, .svc-modal.on, .imp-modal.on, .modal.on, [data-modal].on');
      if (open) {
        var close = open.querySelector('.adv-m-close, .svc-modal-close, .imp-close, .m-close, [data-close]');
        if (close) close.click();
      }
    });

    var mo = new MutationObserver(function (list) {
      list.forEach(function (m) {
        var el = m.target;
        if (!el.classList || !el.classList.contains('on')) return;
        if (!/modal/.test(el.className)) return;
        el.setAttribute('role', 'dialog');
        el.setAttribute('aria-modal', 'true');
        var f = el.querySelector('h2, h3, .adv-m-name, [tabindex="-1"], button, a');
        if (f) { try { f.focus({ preventScroll: true }); } catch (x) { f.focus(); } }
        var back = function () {
          if (!el.classList.contains('on') && lastOpener) {
            try { lastOpener.focus(); } catch (x) {}
            mo2.disconnect();
          }
        };
        var mo2 = new MutationObserver(back);
        mo2.observe(el, { attributes: true, attributeFilter: ['class'] });
      });
    });
    document.querySelectorAll('[class*="modal"]').forEach(function (el) {
      mo.observe(el, { attributes: true, attributeFilter: ['class'] });
    });
  }

  function init() {
    document.querySelectorAll('input[type=range]').forEach(enhance);
    resetButtons();
    tables();
    dialogs();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
  window.addEventListener('resize', function () { clearTimeout(window.__tblT); window.__tblT = setTimeout(tables, 200); });
})();
