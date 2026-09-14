# -*- coding: utf-8 -*-
"""Szakmai aloldalak osszeepitese a meglevo vazbol."""
import io, os, re, sys

SRC = io.open('kalkulator_portal.html', encoding='utf-8').read()
SUBCSS = io.open('sub.css', encoding='utf-8').read()

# ── a vaz darabjai ──────────────────────────────────────────────────
HEAD_RAW = SRC[:SRC.index('<body>') + len('<body>')]
HEAD_RAW = HEAD_RAW.replace('</style>', '\n' + SUBCSS + '\n</style>', 1)

i = SRC.index('<div class="ehead" id="ehead">')
MMOB = '<div class="mmob" id="mmob"><div id="mmobHost"></div></div>'
assert MMOB in SRC, 'a mobil menu blokk nem a vart alakban van'
j = SRC.index(MMOB) + len(MMOB)
HEADER = SRC[i:j]

f0 = SRC.index('<footer>')
f1 = SRC.index('</footer>') + len('</footer>')
FOOTER = SRC[f0:f1]

# a fejlec-JS (mega-menu): az a script blokk, amelyik a megaHost-ot tolti
NAVJS = None
pos = f1
while True:
    s0 = SRC.find('<script>', pos)
    if s0 == -1: break
    s1 = SRC.index('</script>', s0) + len('</script>')
    blk = SRC[s0:s1]
    if 'megaHost' in blk:
        NAVJS = blk
        break
    pos = s1
assert NAVJS, 'nem talalom a mega-menu scriptet'

def head(title, desc, canonical, ogimg='assets/og-eaglz.png'):
    h = HEAD_RAW
    h = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, h, count=1, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">',
               '<meta name="description" content="%s">' % desc, h, count=1, flags=re.S)
    h = re.sub(r'<link rel="canonical" href=".*?">',
               '<link rel="canonical" href="%s">' % canonical, h, count=1, flags=re.S)
    if 'og:title' in h:
        h = re.sub(r'<meta property="og:title" content=".*?">',
                   '<meta property="og:title" content="%s">' % title, h, count=1, flags=re.S)
        h = re.sub(r'<meta property="og:description" content=".*?">',
                   '<meta property="og:description" content="%s">' % desc, h, count=1, flags=re.S)
        h = re.sub(r'<meta property="og:url" content=".*?">',
                   '<meta property="og:url" content="%s">' % canonical, h, count=1, flags=re.S)
    else:
        h = h.replace('<link rel="canonical" href="%s">' % canonical,
            '<link rel="canonical" href="%s">\n'
            '<meta property="og:type" content="article">\n'
            '<meta property="og:locale" content="hu_HU">\n'
            '<meta property="og:title" content="%s">\n'
            '<meta property="og:description" content="%s">\n'
            '<meta property="og:url" content="%s">\n'
            '<meta property="og:image" content="https://eaglz.hu/%s">\n'
            '<meta name="twitter:card" content="summary_large_image">' % (canonical, title, desc, canonical, ogimg), 1)
    return h

LEGAL_WRAP = u'''
<section class="section" style="background:var(--bg);padding-top:2.4rem;padding-bottom:2.4rem;">
  <div class="container">
    <div class="sub-note" style="max-width:900px;margin:0 auto;font-size:.72rem;">%s</div>
  </div>
</section>
'''

CTA = u'''
<section id="cta">
  <div class="container">
    <div class="cta-box">
      <div class="cta-inner">
        <div>
          <div class="cta-free">✓ Kötelezettségektől mentes és díjmentes</div>
          <h2 class="cta-title">%s</h2>
          <p class="cta-sub">%s</p>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center;gap:.75rem;flex-shrink:0;">
          <div class="apt-btn-wrap">
            <a href="index.html#advisors" class="apt-btn-inner" style="padding:1rem 2rem;">📅 Tanácsadót választok</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

import landing

MID_BTN = (u'<a class="apt-btn-inner" href="index.html#advisors">📅 Időpontot foglalok</a>')

def build(slug, title, desc, body, legal, cta_title, cta_sub, extra_js='', mid=None, extra_css='', use_landing=True):
    canonical = 'https://eaglz.hu/%s' % slug
    mid = mid or {}
    if use_landing:
      body = landing.inject(
          body,
          landing.trust_bar(u'Adatok: <b data-upd></b>'),
          landing.mid_cta(mid.get('k', u'Kérdésed van ehhez?'),
                          mid.get('t', u'30 perc, és a saját számaidat látod, nem egy példát.'),
                          mid.get('s', u'Díjmentes, kötelezettség nélkül. Ha kiderül, hogy a mostani megoldásod jó, azt is megmondjuk.'),
                          MID_BTN, u'Válassz tanácsadót és időpontot'))
    hd = head(title, desc, canonical)
    if extra_css:
        hd = hd.replace('<style id="eaglz-theme">', '<style id="page-css">\n' + extra_css + '\n</style>\n<style id="eaglz-theme">', 1)
    page = (hd + '\n\n' + HEADER + '\n' + body + '\n' +
            (CTA % (cta_title, cta_sub)) + (LEGAL_WRAP % legal) + '\n' + FOOTER + '\n' +
            NAVJS + '\n' + (('<script>\n' + extra_js + '\n</script>\n') if extra_js else '') +
            '</body>\n</html>\n')
    io.open(slug, 'w', encoding='utf-8').write(page)
    left = re.findall(r'\{\{[A-Z0-9_]+\}\}', page)
    print('%-26s %5d KB%s' % (slug, len(page)//1024, '   ⚠ ' + str(set(left)) if left else ''))
    return page
