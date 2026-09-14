# -*- coding: utf-8 -*-
"""
A theme.css reteg es az Archivo betutipus beillesztese egy kesz HTML-be.
Mindket oldalcsalad (EAGLZ, tanacsadoi oldalak) ugyanezt hivja.
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
THEME = io.open(os.path.join(HERE, 'theme.css'), encoding='utf-8').read()

FONT_LINK = ('<link href="https://fonts.googleapis.com/css2?'
             'family=Archivo:wght@400;500;600;700;800'
             '&family=Space+Grotesk:wght@400;500;600;700;800'
             '&family=Poppins:wght@400;500;600'
             '&display=swap" rel="stylesheet">')

_OLD_FONT = re.compile(r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">')


def apply(html):
    """Betutipus-link csere + theme.css az utolso stiluslapkent."""
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
    return html
