# -*- coding: utf-8 -*-
"""Dijmentes bankszamlak aloldal az eaglz.hu-n (Zoe oldalarol atemelve)."""
from build_sub import build
import port_back

css, body, modal, js = port_back.port('bankszamla.html')

BODY = (u'<div id="khead" hidden></div><div id="scrollBar" hidden></div><span id="year" hidden></span>'
        u'<nav id="nav" hidden></nav><button id="burger" hidden type="button"></button><div id="mobileMenu" hidden></div>\n'
        u'<div class="zpage">\n' + body + u'\n' + modal + u'\n</div>')

LEGAL = (u'<b>*</b> Az oldalon szereplő adatok tájékoztató jellegűek, a <b>2026. szeptemberi</b> állapotot tükrözik, és nem minősülnek '
         u'ajánlattételnek vagy ajánlattételi felhívásnak. A bankszámla-kondíciók a hitelintézetek mindenkori hirdetményei és kondíciós '
         u'listái szerint alakulnak, és év közben is változhatnak; a díjmentesség jellemzően feltételekhez (például rendszeres jóváírás, '
         u'elektronikus számlakivonat) kötött. A bankváltás díjmentességére és határidejére vonatkozó leírás a fizetési számla váltásáról '
         u'szóló jogszabályi rendelkezéseken alapul. A logók az adott vállalatok tulajdonát képezik, feltüntetésük a hazai piac szemléltetését '
         u'szolgálja. Adatok érvényessége: <b data-upd></b>.')

build('bankszamla.html',
      u'Díjmentes bankszámlák 2026: hol nem fizetsz számlavezetést | EAGLZ Finance',
      u'A 2026 őszi 0 forintos számlacsomagok feltételekkel együtt, a bankváltás három lépése, és amire figyelj, mielőtt váltasz.',
      BODY, LEGAL,
      u'Nézzük meg, mennyit fizetsz feleslegesen.',
      u'Egy díjmentes átnézésen kiderül, mennyi megy el most számlavezetésre, és melyik csomag illik a te bevételeidhez. Ha a mostani jó, azt is megmondjuk.',
      extra_js=js, extra_css=css, use_landing=False)
