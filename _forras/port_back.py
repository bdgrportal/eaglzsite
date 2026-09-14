# -*- coding: utf-8 -*-
"""
Tanacsadoi (Zoe-tipusu) aloldal -> EAGLZ aloldal.

A bankszamla.html es a lakastakarek.html Zoe oldalan keszult el eloszor.
Ez a modul a torzsuket, a sajat CSS-uket es a JS-uket emeli at az EAGLZ
vazba (build_sub), hogy az eaglz.hu-n is fussanak, Zoe oldalatol fuggetlenul.

A CSS-t egy .zpage burkolo ala scope-oljuk, igy nem utkozik az EAGLZ
alap-stilusokkal; a theme.css utana mindket oldalcsaladot ugyanugy huzza ra.
"""
import io, os, re

ZOE = '/home/claude/zoe'

# ── 1. CSS scope-olas ─────────────────────────────────────────────────
DROP_PREFIX = ('nav', '#nav', '.khead', '.scroll-bar', '.mmenu', '.mobile-menu', '.nav-', '.foot', 'footer',
               '.gd-', '.mtag', '.prod-', '.mstep', '.mm')
KEEP_MODAL = ()


def _scope_selector(sel, prefix):
    sel = sel.strip()
    if not sel:
        return None
    if sel.startswith(':root'):
        return None
    if sel in ('html', 'body') or sel.startswith('body.') or sel.startswith('body '):
        return prefix
    if sel.startswith('*'):
        return prefix + ' ' + sel
    for d in DROP_PREFIX:
        if sel.startswith(d) and not sel.startswith(KEEP_MODAL):
            return None
    return prefix + ' ' + sel


def _split_blocks(css):
    """Legfelso szintu (selector, body) parok, kapcsos zarojelek szamlalasaval."""
    i, n = 0, len(css)
    while i < n:
        j = css.find('{', i)
        if j == -1:
            break
        head = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == '{': depth += 1
            elif css[k] == '}': depth -= 1
            k += 1
        yield head, css[j + 1:k - 1]
        i = k


def scope_css(css, prefix='.zpage'):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out = []
    for head, body in _split_blocks(css):
        if head.startswith('@media') or head.startswith('@supports'):
            inner = scope_css(body, prefix)
            if inner.strip():
                out.append('%s{\n%s\n}' % (head, inner))
        elif head.startswith('@keyframes') or head.startswith('@font-face') or head.startswith('@-webkit-keyframes'):
            out.append('%s{%s}' % (head, body))
        elif head.startswith('@'):
            continue
        else:
            sels = [_scope_selector(s, prefix) for s in head.split(',')]
            sels = [s for s in sels if s]
            if sels and body.strip():
                out.append('%s{%s}' % (','.join(sels), body.strip()))
    return '\n'.join(out)


# Zoe valtozoi, amik az EAGLZ :root-bol hianyoznak, EAGLZ-palettara hangolva
VARS = u"""
.zpage{
  --navy-soft:#22436a; --teal-soft:#E8F5F3; --purple-ink:#6E4E9A; --gold-ink:#9A7100;
  --bg-alt:#FFFFFF; --gray-soft:#8FA0B3; --border-strong:rgba(27,56,88,.16);
  --shadow-sm:0 1px 2px rgba(12,29,48,.04),0 2px 8px rgba(12,29,48,.05);
  --shadow-md:0 4px 12px rgba(12,29,48,.06),0 12px 32px rgba(12,29,48,.07);
  --shadow-lg:0 8px 24px rgba(12,29,48,.09),0 24px 60px rgba(12,29,48,.10);
  --r-sm:10px; --r-md:14px; --r-lg:20px; --r-xl:26px; --nav-h:0px;
}
.zpage .section-sm{ padding-top:2.4rem; padding-bottom:2.4rem; }
"""


# ── 2. a torzs es a JS kiemelese ──────────────────────────────────────
SHELL_JS = u"""
/* EAGLZ-vaz: reveal, datum, ev */
(function(){
  var rv=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){ rv.forEach(function(e){e.classList.add('in');}); }
  else{
    var io=new IntersectionObserver(function(en){en.forEach(function(e,i){if(e.isIntersecting){var x=e.target;
      setTimeout(function(){x.classList.add('in');},Math.min(i*60,240));io.unobserve(x);}});},{threshold:.08,rootMargin:'0px 0px -30px 0px'});
    rv.forEach(function(e){io.observe(e);});
  }
  var y=document.getElementById('year'); if(y) y.textContent=new Date().getFullYear();
})();
"""


def extract(slug):
    s = io.open(os.path.join(ZOE, slug), encoding='utf-8').read()
    css = s[s.index('<style>') + 7:s.index('</style>')]

    # torzs: az elso <section>-tol a zaro CTA szekcioig
    b0 = s.index('<section', s.index('<body'))
    b1 = s.index('<section id="cta">')
    body = s[b0:b1]

    # a mail-modal (ha van) a lablec utan
    modal = ''
    if '<div class="overlay" id="mailOverlay"' in s:
        m0 = s.index('<div class="overlay" id="mailOverlay"')
        m1 = s.index('<script', m0)
        modal = s[m0:m1]

    # JS: a lablec utani sima <script> blokkok, a fejlec/burger/scrollbar reszek nelkul
    js, ld = [], []
    f1 = s.index('</footer>')
    for m in re.finditer(r'<script([^>]*)>(.*?)</script>', s[f1:], re.S):
        attrs, code = m.group(1), m.group(2)
        if 'ld+json' in attrs:
            ld.append('<script type="application/ld+json">' + code + '</script>')
            continue
        # a fejlec/burger/scrollbar kodot nem dobjuk el (benne van a reveal es a szamlalo is),
        # helyette a torzs elejen ures, rejtett elemek kapjak el a hivatkozasokat
        # a Zoe-fejlec resze egy nagyobb blokkban: kivagjuk a ket jelolo kozott
        a = code.find(u'/* ── fejléc, reveal ── */')
        b = code.find(u'/* ── e-mailben kérem ── */')
        if a != -1 and b != -1:
            code = code[:a] + code[b:]
        # a lablec ev / adatok sorai a sajat vazban vannak kezelve
        code = code.replace("document.getElementById('year').textContent=new Date().getFullYear();", "")
        js.append(code)
    js = '\n'.join(js) + SHELL_JS
    return css, body, modal, js, '\n'.join(ld)


def _hero_to_eaglz(body, quick):
    """Zoe vilagos bevezetoje -> EAGLZ sotet sub-hero."""
    m = re.search(r'<section id="intro" class="section-sm">.*?<div class="eyebrow[^"]*">(.*?)</div>\s*'
                  r'<h1 class="section-title big">(.*?)</h1>\s*<p class="section-sub wide">(.*?)</p>(.*?)</section>',
                  body, re.S)
    if not m:
        return body
    h1, lead, rest = m.group(2), m.group(3), m.group(4)
    facts = re.findall(r'<div class="hero-fact">(.*?)</div>', rest, re.S)
    chips = ''.join('<div class="sub-chip">%s</div>' % f.strip() for f in facts)
    chips += '<div class="sub-chip">📅 Adatok: <b data-upd></b></div>'
    qn = ''.join('<a href="%s" class="qn%s">%s</a>' % (h, ' on' if i == 0 else '', t) for i, (h, t) in enumerate(quick))
    qn += '<a href="index.html#advisors" class="qn">📅 Időpontot foglalok</a>'
    hero = (u'<section class="sub-hero">\n  <div class="container">\n'
            u'    <a href="index.html" class="sub-back">← Vissza a főoldalra</a>\n'
            u'    <h1 class="sub-h1">%s</h1>\n    <p class="sub-lead">%s</p>\n'
            u'    <div class="sub-chips">%s</div>\n    <div class="quicknav">%s</div>\n'
            u'  </div>\n</section>') % (h1, lead, chips, qn)
    return body[:m.start()] + hero + body[m.end():]


def _quicklinks(slug):
    """Az oldalon beluli horgonyok a Zoe-fejlecbol (khead-idx vagy nav-links)."""
    s = io.open(os.path.join(ZOE, slug), encoding='utf-8').read()
    head = s[:s.index('<section', s.index('<body'))]
    links = re.findall(r'<a href="(#[a-z0-9-]+)"[^>]*>([^<]+)</a>', head)
    out, seen = [], set()
    for h, t in links:
        t = t.strip()
        if h in seen or h == '#cta':
            continue
        seen.add(h); out.append((h, t))
    return out[:4]


def port(slug):
    css, body, modal, js, ld = extract(slug)
    body = _hero_to_eaglz(body, _quicklinks(slug))

    # ── torzs: linkek es hivatkozasok az EAGLZ oldalra ──
    body = body.replace('href="hitel.html', 'href="kalkulator.html')
    body = body.replace('href="#cta"', 'href="#cta"')            # az EAGLZ vazban is #cta a zaro CTA
    # Zoe altal beszurt landing-elemek (bizalmi sav, kozbenso CTA) maradnak, de a gomb legyen EAGLZ-s
    body = body.replace('<a class="btn btn-primary" href="#cta">📅 Időpontot foglalok</a>',
                        '<a class="apt-btn-inner" href="index.html#advisors">📅 Időpontot foglalok</a>')
    body = body.replace(u'Online vagy személyesen, ahogy neked jobb', u'Válassz tanácsadót és időpontot')
    body = body.replace(u'azt is megmondom.', u'azt is megmondjuk.')
    # egyes szam -> tobbes (egy csapat beszel)
    for a, b in [(u'Kiszámolom', u'Kiszámoljuk'), (u'megnézem', u'megnézzük'), (u'Megnézem', u'Megnézzük'),
                 (u'elmondom', u'elmondjuk'), (u'megmondom', u'megmondjuk'), (u'segítek', u'segítünk'),
                 (u'Segítek', u'Segítünk'), (u'kiszámolom', u'kiszámoljuk'), (u'nálam', u'nálunk'),
                 (u'velem', u'velünk'), (u'Velem', u'Velünk'), (u'hozzám', u'hozzánk'), (u'nekem', u'nekünk'),
                 (u'irodámban', u'irodánkban'), (u'ügyfeleim', u'ügyfeleink'), (u'tapasztalatom', u'tapasztalatunk'),
                 (u'Írj nekem', u'Írj nekünk'), (u'foglalj nálam', u'foglalj nálunk')]:
        body = body.replace(a, b)

    # ── JS: a Zoe-specifikus reszek ──
    js = js.replace("'angelcsev.zoe'", "'eaglz'").replace("'zoe-ltp'", "'eaglz-ltp'").replace("'zoe-bk'", "'eaglz-bk'")
    js = js.replace(u'24 órán belül küldöm', u'24 órán belül küldjük')

    # scope-olt CSS + hianyzo valtozok
    scoped = VARS + scope_css(css)

    return scoped, body + '\n' + ld, modal, js
