# -*- coding: utf-8 -*-
"""
Fooldal-atrendezes (landing-logika), a step2 utan, a theme elott.

  1. a "8 terulet, egy kezben" szekcio torolve
  2. az "Ennyi penzt sporolhatsz meg" szekcio a helyere kerul
  3. a video-szekcio kap cimet es alcimet
  4. a zaro CTA es a lead-urlap egy blokkba olvad
  5. a lablec: a kozossegi ikonok a brand-sor jobb oldalara
  6. a hub alatti jogi megjegyzes: kozepre (a theme kulon kezeli)
"""
import re


def _section(S, sec_id):
    """(start, end) a <section ... id="x"> blokkra."""
    i = S.index('id="%s"' % sec_id)
    i = S.rfind('<section', 0, i)
    j = S.index('</section>', i) + len('</section>')
    return i, j


def apply(S):
    # 1) 8 terulet torlese
    i, j = _section(S, 'services')
    S = S[:i] + S[j:]

    # 2) savings a for-whom utan
    i, j = _section(S, 'savings')
    sav = S[i:j]
    S = S[:i] + S[j:]
    _, k = _section(S, 'for-whom')
    S = S[:k] + '\n\n' + sav + S[k:]

    # 3) video-szekcio fejlec
    old = ('<div style="text-align:center;"><div class="label-chip chip-teal" style="text-transform:uppercase;letter-spacing:.12em;">'
           'Ügyfeleink visszajelzései</div></div>')
    new = ('<div style="text-align:center;">'
           '<div class="label-chip chip-teal">Ügyfeleink visszajelzései</div>'
           '<h2 class="section-title">Akik már végigcsinálták velünk.</h2>'
           '<p class="section-sub">Hallgass bele ügyfeleink véleményébe!</p>'
           '</div>')
    assert old in S, 'video fejlec'
    S = S.replace(old, new, 1)

    # gorgetesi tipp a videosav ala
    S = S.replace('</div>\n    <div style="text-align:center;margin-top:2rem;">\n<div class="apt-btn-wrap">',
                  '</div>\n    <div class="vid-hint">húzd oldalra a többi véleményhez</div>\n    <div style="text-align:center;margin-top:2rem;">\n<div class="apt-btn-wrap">', 1)
    # a videok kozotti CTA: egyseges gomb-burkolo
    S = S.replace('<div style="text-align:center;margin-top:2rem;">\n<div class="apt-btn-wrap">',
                  '<div class="sec-cta">\n<div class="apt-btn-wrap">', 1)

    # 4) CTA + lead osszeolvasztasa
    ci, cj = _section(S, 'cta')
    li, lj = _section(S, 'lead')
    lead = S[li:lj]
    m = re.search(r'<div class="lead-box">(.*?)</div>\s*</div>\s*</section>', lead, re.S)
    assert m, 'lead-box'
    lead_inner = m.group(1)
    # a lead-box belseje: chip-burkolo, cim, alcim, form, trust
    lead_inner = lead_inner.replace('<div style="text-align:center;"><div class="label-chip chip-teal">Vagy írj, és visszahívunk</div></div>',
                                    '<div class="lead-kicker">Vagy írj, és visszahívunk</div>', 1)
    lead_inner = re.sub(r'<h2 class="lead-title"[^>]*>', '<h3 class="lead-title">', lead_inner, count=1).replace('</h2>', '</h3>', 1) \
        if '<h2 class="lead-title"' in lead_inner else lead_inner
    lead_inner = re.sub(r'<p class="lead-sub"[^>]*>', '<p class="lead-sub">', lead_inner, count=1)

    cta = S[ci:cj]
    # a CTA belso oszlopai: bal (szoveg + gombok) + jobb (urlap-kartya)
    cta = cta.replace('<div class="cta-inner">', '<div class="cta-inner cta-merged">', 1)
    cta = cta.replace('<div style="display:flex;flex-direction:column;align-items:center;gap:.75rem;flex-shrink:0;">',
                      '<div class="cta-actions">', 1)
    # a bal oszlop: a cim-blokk es a gombok egy burkoloba
    cta = cta.replace('<div class="cta-inner cta-merged">\n        <div>', '<div class="cta-inner cta-merged">\n        <div class="cta-left"><div>', 1)
    # a gombok utan zarjuk a bal oszlopot, es jon a jobb oszlop
    k = cta.index('<div class="cta-actions">')
    k2 = cta.index('</div>\n      </div>', k)      # a cta-actions vege
    k2 += len('</div>')
    right = ('\n        </div>\n        <div class="cta-right lead-box" id="lead">' + lead_inner + '</div>')
    cta = cta[:k2] + right + cta[k2:]
    S = S[:ci] + cta + S[cj:]
    # a regi lead szekcio torlese (a poziciok elcsusztak, ujra keressuk)
    li, lj = _section(S, 'lead') if 'id="lead"' in S[S.index('</section>', ci):] else (None, None)
    # a lead id most a CTA-n belul is szerepel: a KULSO szekciot keressuk
    m = re.search(r'<section id="lead">.*?</section>', S, re.S)
    if m:
        S = S[:m.start()] + S[m.end():]

    # 5) lablec: kozossegi ikonok a brand-sorba
    fs = re.search(r'<div class="footer-social">.*?</div>\s*(?=<div class="footer-inner">)', S, re.S)
    if fs:
        social = fs.group(0)
        S = S[:fs.start()] + S[fs.end():]
        S = S.replace('<div class="footer-links">', social.strip() + '\n      <div class="footer-links">', 1)
        # sorrend: brand | linkek | social  -> a social a linkek utan
        S = re.sub(r'(<div class="footer-social">.*?</div>)\s*(<div class="footer-links">.*?</div>)',
                   r'\2\n      \1', S, count=1, flags=re.S)

    S = advisors_and_form(S)
    S = lead_js(S)
    S = online_block(S)
    return S


# ══════════════════════════════════════════════════════════════════════
#  Tanacsadoi kartyak, parbeszedablak es kapcsolatfelveteli urlap
# ══════════════════════════════════════════════════════════════════════
def advisors_and_form(S):
    # ── 1. szakterulet a kartyan is, ne csak a megnyitasa utan ──────────
    S = S.replace(
        "'<div class=\"adv-role\">'+_esc(empty ? 'Csatlakozz a csapathoz' : a.role)+'</div>'+",
        "'<div class=\"adv-role\">'+_esc(empty ? 'Csatlakozz a csapathoz' : a.role)+'</div>'+"
        "(empty ? '' : '<div class=\"adv-tags-mini\">'+((a.tags||[]).filter(function(t){return !_isPh(t);})"
        ".slice(0,2).map(function(t){return '<span>'+_esc(t)+'</span>';}).join(''))+'</div>')+", 1)

    # ── 2. utvonal annak, aki nem tud valasztani ────────────────────────
    S = S.replace('<div class="adv-hint" id="advHint"></div>',
                  '<div class="adv-hint" id="advHint"></div>\n'
                  '    <div class="adv-help">\n'
                  '      <div>\n'
                  '        <div class="adv-help-t">Nem tudod, kit válassz?</div>\n'
                  '        <div class="adv-help-s">Írd meg, miben segítsünk, és mi keressük meg hozzá a megfelelő '
                  'szakértőt a csapatból. Ugyanaz a díjmentes első beszélgetés.</div>\n'
                  '      </div>\n'
                  '      <a class="hact hact-primary" href="#lead">Segítsetek szakértőt választani</a>\n'
                  '    </div>', 1)

    # ── 3. parbeszedablak: fokusz be es vissza ──────────────────────────
    S = S.replace("function openAdv(i){\n  var a = ADVISORS[i]; if(!a) return;",
                  "var _advOpener = null;\nfunction openAdv(i){\n  var a = ADVISORS[i]; if(!a) return;\n"
                  "  _advOpener = document.activeElement;", 1)
    S = S.replace("function closeAdv(){\n  document.getElementById('advOverlay').classList.remove('active');\n"
                  "  document.body.style.overflow = '';\n}",
                  "function closeAdv(){\n  var ov = document.getElementById('advOverlay');\n"
                  "  if(!ov.classList.contains('active')) return;\n"
                  "  ov.classList.remove('active');\n  document.body.style.overflow = '';\n"
                  "  if(_advOpener){ try{ _advOpener.focus(); }catch(e){} _advOpener = null; }\n}", 1)
    # nyitas utan a fokusz a parbeszedablak cimere kerul
    S = S.replace("document.getElementById('advOverlay').classList.add('active');",
                  "document.getElementById('advOverlay').classList.add('active');\n"
                  "  var _mn = document.getElementById('advMName');\n"
                  "  if(_mn){ _mn.setAttribute('tabindex','-1'); setTimeout(function(){ try{ _mn.focus({preventScroll:true}); }catch(e){ _mn.focus(); } }, 30); }")

    # ── 4. urlap: cimkek, hibajelzes, allapotok ─────────────────────────
    F = [('leadName',  u'Név', 'text',  'name',  True,  u'Írd be a neved.'),
         ('leadPhone', u'Telefonszám', 'tel', 'tel', True, u'Adj meg egy telefonszámot, amin elérünk.'),
         ('leadEmail', u'E-mail cím', 'email', 'email', True, u'Adj meg egy érvényes e-mail címet.'),
         ('leadTopic', u'Téma', 'text', 'off', False, '')]
    for fid, label, typ, ac, req, _err in F:
        old_lbl = u'<label>%s%s</label>' % (label, u' *' if req else u'')
        new_lbl = (u'<label for="%s">%s%s</label>' % (fid, label, u' <span class="f-req" aria-hidden="true">*</span>' if req else u''))
        S = S.replace(old_lbl, new_lbl, 1)
        if req:
            S = S.replace(u'<input type="%s" id="%s" required autocomplete="%s">' % (typ, fid, ac),
                          u'<input type="%s" id="%s" required autocomplete="%s" aria-required="true" '
                          u'aria-describedby="%s_err"><span class="f-err" id="%s_err"></span>' % (typ, fid, ac, fid, fid), 1)
    S = S.replace(u'<label>Üzenet</label><textarea id="leadMsg"',
                  u'<label for="leadMsg">Üzenet</label><textarea id="leadMsg"', 1)
    S = S.replace('<div class="lead-status" id="leadStatus"></div>',
                  '<div class="f-status" id="leadStatus" role="status" aria-live="polite"></div>', 1)
    return S


LEAD_JS = u"""
/* ── kapcsolatfelveteli urlap: mezoszintu ellenorzes es allapotok ──────── */
(function(){
  var F = {
    leadName:  { msg:'Írd be a neved.',                         ok:function(v){ return v.trim().length >= 2; } },
    leadPhone: { msg:'Adj meg egy telefonszámot, amin elérünk.', ok:function(v){ return v.replace(/[^\\d+]/g,'').length >= 7; } },
    leadEmail: { msg:'Adj meg egy érvényes e-mail címet.',       ok:function(v){ return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(v.trim()); } }
  };
  function mark(id, bad){
    var el = document.getElementById(id), er = document.getElementById(id + '_err');
    if(!el || !er) return;
    el.setAttribute('aria-invalid', bad ? 'true' : 'false');
    er.textContent = bad ? F[id].msg : '';
    er.classList.toggle('on', !!bad);
  }
  Object.keys(F).forEach(function(id){
    var el = document.getElementById(id);
    if(!el) return;
    el.addEventListener('blur', function(){ mark(id, el.value && !F[id].ok(el.value)); });
    el.addEventListener('input', function(){ if(el.getAttribute('aria-invalid')==='true' && F[id].ok(el.value)) mark(id,false); });
  });

  /* aloldalrol hozott tema ne vesszen el: ?tema=... vagy #lead?tema=... */
  var t = (location.search + location.hash).match(/tema=([^&#]+)/);
  var box = document.getElementById('leadTopic');
  if(t && box && !box.value){ try{ box.value = decodeURIComponent(t[1].replace(/\\+/g,' ')); }catch(e){} }

  window.leadSubmit = function(e){
    e.preventDefault();
    if(document.getElementById('leadWebsite').value) return false;   /* rejtett csapda */
    var bad = false;
    Object.keys(F).forEach(function(id){
      var el = document.getElementById(id);
      var wrong = !F[id].ok(el.value);
      mark(id, wrong);
      if(wrong && !bad){ bad = true; el.focus(); }
    });
    var st  = document.getElementById('leadStatus');
    var btn = document.getElementById('leadSendBtn');
    var form= document.getElementById('leadForm');
    function say(cls, txt){ st.className = 'f-status on ' + cls; st.textContent = txt; }
    if(bad){ say('bad', 'Nézd át a pirossal jelölt mezőket.'); return false; }
    if(!document.getElementById('leadGdpr').checked){
      say('bad', 'A küldéshez el kell fogadnod az adatkezelési tájékoztatót.');
      document.getElementById('leadGdpr').focus(); return false;
    }
    btn.disabled = true; form.classList.add('is-sending');
    say('', 'Küldés folyamatban...');
    fetch(LEAD_URL, {
      method:'POST',
      headers:{ 'apikey':LEAD_KEY, 'Authorization':'Bearer '+LEAD_KEY,
                'Content-Type':'application/json', 'Prefer':'return=minimal' },
      body: JSON.stringify({
        name:    document.getElementById('leadName').value.trim(),
        phone:   document.getElementById('leadPhone').value.trim(),
        email:   document.getElementById('leadEmail').value.trim(),
        topic:   document.getElementById('leadTopic').value.trim(),
        message: document.getElementById('leadMsg').value.trim()
      })
    }).then(function(r){
      btn.disabled = false; form.classList.remove('is-sending');
      if(r.ok){
        say('ok', 'Megkaptuk. 24 órán belül jelentkezünk a megadott elérhetőségen.');
        form.reset();
      } else {
        say('bad', 'A küldés nem sikerült. Próbáld újra, vagy hívj minket. Amit beírtál, megmaradt.');
      }
    }).catch(function(){
      btn.disabled = false; form.classList.remove('is-sending');
      say('bad', 'Nem sikerült elérni a szervert. Ellenőrizd a kapcsolatot, és próbáld újra. Amit beírtál, megmaradt.');
    });
    return false;
  };
})();
"""


def lead_js(S):
    """A regi beküldő fuggveny cserejе a mezoszintu valtozatra."""
    i = S.index('function leadSubmit(e){')
    j = S.index('\n}\n', S.index('return false;', i)) + len('\n}\n')
    S = S[:i] + LEAD_JS + S[j:]
    # az adatkezelesi tajekoztato a valodi (impresszum) tartalomra mutat
    S = S.replace(u'<span>Hozzájárulok, hogy a megadott adataimat a kapcsolatfelvétel céljából kezeljék.',
                  u'<span>Hozzájárulok, hogy a megadott adataimat a kapcsolatfelvétel céljából kezeljék '
                  u'(<a href="#" onclick="openImp();return false;">adatkezelési tájékoztató</a>).', 1)
    S = S.replace(u' Az adatokat harmadik félnek nem adjuk át, és kérésre töröljük.',
                  u' Az adatokat harmadik félnek nem adjuk át, és kérésre töröljük.', 1)
    return S


# ══════════════════════════════════════════════════════════════════════
#  Helyorzok es nem mukodo hivatkozasok
# ══════════════════════════════════════════════════════════════════════
def placeholders(S):
    import re
    # 1. lablec "Kapcsolat": a kitoltetlen mailto helyett a valodi urlap
    S = S.replace(u'<a href="mailto:INFO_EMAIL_IDE">Kapcsolat</a>',
                  u'<a href="#lead">Kapcsolat</a>', 1)

    # 2. kozossegi ikonok: ures (#) hivatkozas nem maradhat aktiv.
    #    Amelyikhez van valodi cim, az marad; a tobbi kikerul.
    def soc(m):
        return '' if 'href="#"' in m.group(0) else m.group(0)
    S = re.sub(r'<a href="[^"]*" class="fsoc-btn"[^>]*>.*?</a>', soc, S, flags=re.S)
    S = re.sub(r'<div class="footer-social">\s*</div>', '', S, flags=re.S)

    # 3. impresszum: a kitoltetlen sorok ne latszodjanak nyers helyorzokent
    def row(m):
        return '' if '_IDE' in m.group(0) else m.group(0)
    S = re.sub(r'<dt>.*?</dt>\s*<dd>.*?</dd>', row, S, flags=re.S)
    S = re.sub(r'<div class="imp-row">.*?</div>\s*</div>', row, S, flags=re.S)
    return S


# ══════════════════════════════════════════════════════════════════════
#  Online kotes sav: egyseges kartyak (a ket szinu valtakozas megszunik)
# ══════════════════════════════════════════════════════════════════════
def online_block(S):
    import re
    i = S.find('<section id="online"')
    if i == -1:
        return S
    g0 = S.index('<div style="display:grid;grid-template-columns:1fr 1fr;gap:.6rem;">', i)
    g1 = S.index('</div>\n  </div>\n</section>', g0)
    block = S[g0:g1]
    cards = re.findall(r'<a href="([^"]+)"[^>]*>\s*<span[^>]*>(.*?)</span>\s*<span[^>]*>(.*?)</span>\s*</a>',
                       block, re.S)
    if not cards:
        return S
    out = ['<div class="onl-grid">']
    for href, ico, label in cards:
        out.append('<a class="onl-card" href="%s" target="_blank" rel="noopener">'
                   '<span class="onl-i">%s</span><span class="onl-t">%s</span>'
                   '<svg class="ic onl-go" aria-hidden="true" focusable="false"><use href="#i-arrow-up-right"></use></svg>'
                   '</a>' % (href, ico.strip(), re.sub(r'\s+', ' ', label).strip()))
    out.append('</div>')
    return S[:g0] + '\n      '.join(out) + S[g1:]
