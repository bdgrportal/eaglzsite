# -*- coding: utf-8 -*-
"""
Landing-vaz az aloldalakra: bizalmi sav a hero ala, halk kozbenso CTA a
fo szekcio utan. Mindket oldalcsalad ezt hivja, csak a gomb es a link mas.
"""
import re

TRUST_ITEMS = [u'Díjmentes tanácsadás', u'MNB által felügyelt közvetítés',
               u'30+ pénzintézet és biztosító', u'Online vagy személyesen']


def trust_bar(tag=u''):
    items = u''.join(u'<span class="trust-i">%s</span>' % t for t in TRUST_ITEMS)
    if tag:
        items += u'<span class="trust-i tag">%s</span>' % tag
    return (u'\n<div class="trust" aria-label="Miért érdemes velünk">\n'
            u'  <div class="container">%s</div>\n</div>\n' % items)


def mid_cta(kicker, title, sub, btn_html, note=u''):
    return (u'\n<section class="midcta section" aria-label="Kapcsolat">\n'
            u'  <div class="container">\n'
            u'    <div class="midcta-box">\n'
            u'      <div>\n'
            u'        <div class="midcta-k">%s</div>\n'
            u'        <div class="midcta-t">%s</div>\n'
            u'        <div class="midcta-s">%s</div>\n'
            u'      </div>\n'
            u'      <div class="midcta-a">%s%s</div>\n'
            u'    </div>\n'
            u'  </div>\n'
            u'</section>\n') % (kicker, title, sub, btn_html,
                                (u'<span class="midcta-n">%s</span>' % note) if note else u'')


def inject(body, trust_html, mid_html, after_section=3):
    """
    A bizalmi sav mar nem kerul kulon savba: ugyanazt a datumot es
    dijmentesseg-allitast ismetelte, amit a nyitoresz es a zaro CTA is kimond.
    Csak a kozbenso felhivast tesszuk be, es azt sem ott, ahol a kalkulatornak
    mar van sajat konzultacios gombja: egy donteshez egy felhivas tartozik.
    """
    out = body
    ends = [m.end() for m in re.finditer(r'</section>', out)]
    if not ends:
        return out

    k = None
    m = re.search(r'<div class="sc(?: reveal)?" id=', out)
    if m:
        k = out.find('</section>', m.start())
        if k != -1:
            k += len('</section>')
            seg = out[m.start():k]
            # ha a kalkulator sajat maga kinal konzultaciot, a kozbenso CTA
            # eggyel lejjebb csuszik, hogy ne ket felhivas alljon egymas alatt
            if 'index.html#advisors' in seg or 'calccta' in seg:
                nxt = out.find('</section>', k)
                k = (nxt + len('</section>')) if nxt != -1 else k
    if k is None:
        idx = min(after_section, len(ends) - 2)   # a GYIK es a hero kozott maradjon
        k = ends[idx]
    return out[:k] + mid_html + out[k:]
