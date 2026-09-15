/* ══════════════════════════════════════════════════════════════════════
   EAGLZ mozgásréteg  ·  minden oldalon a theme után fut
   ----------------------------------------------------------------------
   1. négyzetrácsos háttér besorolása: csak egyszínű szekciókra kerül
   2. finom felúszás görgetéskor, szekción belül lépcsőzve
   3. az első képernyőn látható elemek azonnal a helyükön vannak
   Minden viselkedés kikapcsol, ha a látogató csökkentett mozgást kért.
   ══════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var halk = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── 1. rács-besorolás ───────────────────────────────────────────────
     Csak akkor kap rácsot a szekció, ha nincs saját háttérképe és nem
     áttetsző. A világos és a sötét felület más erősségű rácsot kap. */
  function racs() {
    var sorok = document.querySelectorAll('section, .section, footer');
    for (var i = 0; i < sorok.length; i++) {
      var el = sorok[i];
      if (el.classList.contains('h-racs-vilagos') || el.classList.contains('h-racs-sotet')) continue;
      var st = window.getComputedStyle(el);
      if (st.backgroundImage && st.backgroundImage !== 'none') continue;
      var szin = st.backgroundColor || '';
      var m = szin.match(/rgba?\(([^)]+)\)/);
      if (!m) continue;
      var r = m[1].split(',').map(function (x) { return parseFloat(x); });
      if (r.length > 3 && r[3] < 0.9) continue;            // áttetsző: hagyjuk
      var vil = (0.2126 * r[0] + 0.7152 * r[1] + 0.0722 * r[2]) / 255;
      if (el.getBoundingClientRect().height < 80) continue;
      el.classList.add(vil > 0.6 ? 'h-racs-vilagos' : 'h-racs-sotet');
    }
  }

  /* ── 2. felúszás ─────────────────────────────────────────────────────
     A kiválasztott blokkok a nézetbe érve úsznak fel. Egy szekción belül
     az egymás utáni elemek kis késleltetést kapnak, így a sor nem
     egyszerre villan be, de nem is válik lassúvá: legfeljebb hat lépés. */
  var VALASZTO = [
    '.section-title', '.section-sub', '.sec-head', '.label-chip',
    '.tile', '.box', '.hub-c', '.fw-card', '.nstep', '.faq-item', '.kpi',
    '.rel-c', '.eo-tile', '.onl-card', '.card', '.scf', '.sav-item',
    '.ben-c', '.gd-c', '.adv-c', '.stat-item', '.docitem',
    '.midcta-box', '.cta-box', '.tbl-wrap', '.graph-light', '.art > p',
    '.art > h3', '.art > ul', '.toc'
  ].join(',');

  function elokeszit() {
    var elemek = document.querySelectorAll(VALASZTO);
    var csoportSzamlalo = new WeakMap();
    var lista = [];
    for (var i = 0; i < elemek.length; i++) {
      var el = elemek[i];
      if (el.closest('.ehead, .mhead, .mmob, .mega, [class*="modal"], .fablak')) continue;
      var doboz = el.getBoundingClientRect();
      if (doboz.height === 0 && doboz.width === 0) continue;
      var szulo = el.parentElement || document.body;
      var n = (csoportSzamlalo.get(szulo) || 0);
      csoportSzamlalo.set(szulo, n + 1);
      el.style.transitionDelay = Math.min(n, 5) * 55 + 'ms';
      el.classList.add('h-be');
      lista.push(el);
    }
    return lista;
  }

  function indit() {
    if (halk || !('IntersectionObserver' in window)) return;
    var lista = elokeszit();
    var also = window.innerHeight * 1.25;

    /* az első képernyő tartalma ne villanjon: azonnal látszik */
    lista.forEach(function (el) {
      if (el.getBoundingClientRect().top < also) {
        el.style.transitionDelay = '0ms';
        el.classList.add('h-lat');
      }
    });

    var figyelo = new IntersectionObserver(function (bejegyzesek) {
      bejegyzesek.forEach(function (b) {
        if (!b.isIntersecting) return;
        b.target.classList.add('h-lat');
        figyelo.unobserve(b.target);
      });
    }, { rootMargin: '300px 0px 300px 0px', threshold: 0.01 });

    lista.forEach(function (el) {
      if (!el.classList.contains('h-lat')) figyelo.observe(el);
    });

    /* biztonsági háló: ha bármi félrecsúszna, 6 másodperc után minden látszik */
    window.setTimeout(function () {
      lista.forEach(function (el) { el.classList.add('h-lat'); });
    }, 3000);
  }

  function start() {
    try { racs(); } catch (e) { /* a háttér sose akassza meg az oldalt */ }
    try { indit(); } catch (e) { /* a mozgás sem */ }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
  window.addEventListener('resize', function () {
    clearTimeout(window.__hRacsT);
    window.__hRacsT = window.setTimeout(function () { try { racs(); } catch (e) {} }, 250);
  });
})();
