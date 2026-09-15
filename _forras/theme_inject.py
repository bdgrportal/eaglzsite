# -*- coding: utf-8 -*-
"""
A theme.css reteg es az Archivo betutipus beillesztese egy kesz HTML-be.
Mindket oldalcsalad (EAGLZ, tanacsadoi oldalak) ugyanezt hivja.
"""
import io, os, re
import icons
import cleanup

HERE = os.path.dirname(os.path.abspath(__file__))
THEME = (io.open(os.path.join(HERE, 'theme.css'), encoding='utf-8').read() + icons.CSS
         # a harmonia reteg mindig utolso: ez hozza kozos nevezore a
         # sugarakat, kereteket, arnyekokat, a tipografiai skalat es a ritmust
         + io.open(os.path.join(HERE, 'harmonia.css'), encoding='utf-8').read())
UI_JS = (io.open(os.path.join(HERE, 'ui.js'), encoding='utf-8').read()
         + '\n' + io.open(os.path.join(HERE, 'mozgas.js'), encoding='utf-8').read())

FONT_LINK = ('<link href="https://fonts.googleapis.com/css2?'
             'family=Archivo:wght@400;500;600;700;800'
             '&family=Space+Grotesk:wght@400;500;600;700;800'
             '&family=Poppins:wght@400;500;600'
             '&display=swap" rel="stylesheet">')

_OLD_FONT = re.compile(r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">')


_HEAD_TAG = re.compile(r'(<h[123][^>]*>)(.*?)(</h[123]>)', re.S)
_TAGSPLIT = re.compile(r'(<[^>]+>)')
_HYPH = re.compile(r'(?<!\S)(\S*[^\s-]-[^\s-]\S*)(?!\S)')


def nowrap_hyphens(html):
    """Cimsorokban a kotojeles szo ne torjon meg a kotojelnel ("2026-" / "ban")."""
    def one(m):
        parts = _TAGSPLIT.split(m.group(2))
        for i, t in enumerate(parts):
            if i % 2 == 0 and '-' in t:
                # csak a rovid osszetett szo marad egyben: a hosszu
                # amugy is kilogna a keskeny kepernyorol
                parts[i] = _HYPH.sub(
                    lambda h: ('<span class="nb">%s</span>' % h.group(1))
                    if len(h.group(1)) <= 18 else h.group(1), t)
        return m.group(1) + ''.join(parts) + m.group(3)
    return _HEAD_TAG.sub(one, html)


def apply(html):
    """Betutipus-link csere + theme.css az utolso stiluslapkent."""
    html = nowrap_hyphens(html)
    if 'family=Archivo' not in html:
        if _OLD_FONT.search(html):
            html = _OLD_FONT.sub(FONT_LINK, html, count=1)
        else:
            html = html.replace('</head>', FONT_LINK + '\n</head>', 1)
    block = '<style id="eaglz-theme">\n' + THEME + '\n</style>'
    if 'id="eaglz-theme"' in html:
        # mar van benne egy korabbi valtozat: frissitjuk
        html = re.sub(r'<style id="eaglz-theme">.*?</style>', lambda m: block, html, count=1, flags=re.S)
    else:
        html = html.replace('</head>', block + '\n</head>', 1)
    if '<body' in html:
        html = finish(html)
    return html


NOSCRIPT = ('<noscript><style>'
            '.reveal{opacity:1!important;transform:none!important}'
            '.hw-pane,.faq-a{display:block!important}'
            '.count{visibility:visible!important}'
            '</style></noscript>')


BUILD = None


def build_id():
    """Egyedi azonosito minden generalashoz, hogy egy pillantassal lathato
    legyen, melyik valtozat van fent (nezd meg a forrasban: eaglz-build)."""
    global BUILD
    if BUILD is None:
        import datetime
        BUILD = datetime.datetime.now().strftime('%Y-%m-%d-%H%M')
    return BUILD


def finish(html):
    """Zaro menet egy kesz oldalon: cimsor-tordeles + ikonrendszer + JS nelkuli eset."""
    html = nowrap_hyphens(html)
    html = cleanup.apply(html)
    html = icons.apply(html)
    if '<noscript><style>' not in html and '<body' in html:
        i = html.index('>', html.index('<body')) + 1
        html = html[:i] + '\n' + NOSCRIPT + html[i:]
    if 'name="eaglz-build"' not in html and '</head>' in html:
        html = html.replace('</head>',
                            '<meta name="eaglz-build" content="%s">\n</head>' % build_id(), 1)
    if 'id="eaglz-ui"' not in html and '</body>' in html:
        html = html.replace('</body>', '<script id="eaglz-ui">\n' + UI_JS + '\n</script>\n</body>', 1)
    return html
