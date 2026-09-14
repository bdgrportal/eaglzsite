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
    trust: az elso </section> (a hero) utan
    mid:   az N-edik </section> utan, de sosem a GYIK ele kozvetlenul,
           es ha van kalkulator (id="kalk" vagy .sc), akkor az azt tartalmazo
           szekcio utan.
    """
    ends = [m.end() for m in re.finditer(r'</section>', body)]
    if not ends:
        return body
    out = body[:ends[0]] + trust_html + body[ends[0]:]

    ends = [m.end() for m in re.finditer(r'</section>', out)]
    # kalkulator-szekcio vege
    k = None
    m = re.search(r'<div class="sc(?: reveal)?" id=', out)
    if m:
        k = out.find('</section>', m.start())
        if k != -1:
            k += len('</section>')
    if k is None:
        idx = min(after_section, len(ends) - 2)   # a GYIK es a hero kozott maradjon
        k = ends[idx]
    return out[:k] + mid_html + out[k:]
