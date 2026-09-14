# -*- coding: utf-8 -*-
"""
Szovegaudit: hosszu kotojelek (– —) kigyomlalasa minden forrasbol.

Szabalyok, sorrendben:
  1. szam–szam            -> szam-szam            (20–100 -> 20-100)
  2. </b> – szoveg        -> </b>: szoveg         (definicios felsorolas)
  3. CSS content:'–'      -> content:'•'          (listajel)
  4. JS '—' helyorzo      -> 'nincs'
  5. " – " / " — " prozaban -> ", "
  6. minden marado – —    -> -
Futtatas: python3 audit_text.py <fajl> [<fajl> ...]
"""
import io, re, sys

RULES = [
    (re.compile(u'(\\d)\\s?[–—]\\s?(\\d)'),        u'\\1-\\2'),
    (re.compile(u'</b>\\s?[–—]\\s'),                u'</b>: '),
    (re.compile(u"content:\\s*'[–—]'"),             u"content:'•'"),
    (re.compile(u'"[–—]"'),                         u'"•"'),
    (re.compile(u"\\?'[–—]'"),                      u"?'nincs'"),
    (re.compile(u'\\s[–—]\\s'),                     u', '),
    (re.compile(u'[–—]'),                           u'-'),
]

def fix(s):
    for rx, rep in RULES:
        s = rx.sub(rep, s)
    return s

if __name__ == '__main__':
    for f in sys.argv[1:]:
        s = io.open(f, encoding='utf-8').read()
        before = s.count(u'–') + s.count(u'—')
        t = fix(s)
        if t != s:
            io.open(f, 'w', encoding='utf-8').write(t)
        print('%-40s %3d -> %d' % (f, before, t.count(u'–') + t.count(u'—')))
