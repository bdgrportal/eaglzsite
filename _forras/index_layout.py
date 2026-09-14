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
           '<p class="section-sub">Nem mi mondjuk, hogy megéri. Három ügyfelünk mondja el, mi változott, miután leültünk.</p>'
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

    return S
