# -*- coding: utf-8 -*-
"""Lakastakarek aloldal az eaglz.hu-n (Zoe oldalarol atemelve, kalkulatorral)."""
from build_sub import build
import port_back

css, body, modal, js = port_back.port('lakastakarek.html')

BODY = (u'<div id="khead" hidden></div><div id="scrollBar" hidden></div><span id="year" hidden></span>'
        u'<nav id="nav" hidden></nav><button id="burger" hidden type="button"></button><div id="mobileMenu" hidden></div>\n'
        u'<div class="zpage">\n' + body + u'\n' + modal + u'\n</div>')

LEGAL = (u'<b>*</b> Az oldalon szereplő adatok tájékoztató jellegűek, a <b>2026. szeptemberi</b> állapotot tükrözik, és nem minősülnek '
         u'ajánlattételnek, ajánlattételi felhívásnak vagy befektetési tanácsadásnak. A kalkulátor egyszerűsített modellel számol: a kamatbónusz, '
         u'a betéti kamat, a számlanyitási és a havi díjak alapértéke tájékoztató piaci nagyságrend, amit a látogató szabadon átállíthat; '
         u'egyik érték sem egy konkrét lakás-takarékpénztár ajánlata. A lakás-takarékpénztári szerződések feltételeit (bónusz mértéke és feltételei, '
         u'megtakarítási idő, díjak, lakáscélú felhasználás szabályai) a mindenkori üzletszabályzatok és általános szerződési feltételek tartalmazzák. '
         u'Az újonnan kötött szerződésekhez 2018. október 16-tól állami támogatás nem jár. A logók az adott vállalatok tulajdonát képezik. '
         u'Adatok érvényessége: <b data-upd></b>.')

build('lakastakarek.html',
      u'Lakástakarék 2026: megéri még állami támogatás nélkül? | EAGLZ Finance',
      u'Lakástakarék állami támogatás nélkül: hogyan működik, mire használható, mit hoz valójában. Kalkulátor, ami a díjak levonása után évesített hozamot számol.',
      BODY, LEGAL,
      u'A kalkulátor becslés. A három ajánlat konkrét.',
      u'Egy rövid beszélgetésen megnézzük, mire és mikor fog kelleni a pénz, és hogy a lakástakarék-e ehhez a jó eszköz. Ha igen, mind a három szolgáltatót kiszámoljuk. Ha nem, azt is megmondjuk.',
      extra_js=js, extra_css=css, use_landing=False)
