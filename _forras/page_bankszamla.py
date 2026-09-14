# -*- coding: utf-8 -*-
"""Dijmentes bankszamlak aloldal az eaglz.hu-n (Zoe oldalarol atemelve)."""
from build_sub import build
import port_back

css, body, modal, js = port_back.port('bankszamla.html')


# ── a nyitoresz a tobbi aloldallal azonos vazat kovesse ────────────────
LONG = (u'A számlavezetési díj minden hónapban elmegy, magától. Nem érkezik róla csekk, nem kell dönteni róla. '
        u'Ezért van, hogy a legtöbb család soha nem számolta össze, mennyi ez egy évben. '
        u'Most négy nagybank verseng egyszerre az új ügyfelekért: 0 Ft havi számlavezetés, mellé akár 100 000 Ft ajándék jóváírás.')
SHORT_LEAD = (u'A számlavezetési díj minden hónapban elmegy, magától, ezért a legtöbb család soha nem számolta össze, '
              u'mennyi ez egy évben. Most négy nagybank verseng egyszerre az új ügyfelekért.')
body = body.replace(LONG, SHORT_LEAD)
body = body.replace(
    u'<a href="#dijkimutatas" class="btn btn-ghost">Mennyit fizetek most?</a>',
    u'<a href="#dijkimutatas" class="btn btn-ghost">Mennyit fizetek most?</a>'
    u'<a href="index.html#advisors" class="btn btn-ghost">Díjmentes konzultációt kérek</a>')
body = body.replace(
    u'</div>\n      <div class="hero-trust">',
    u'</div>\n      <p class="sub-upd">Az oldalon szereplő banki feltételek a <b data-upd></b> állapotot tükrözik, '
    u'és tájékoztató jellegűek.</p>\n      <div class="hero-trust">')

# ── cimkek egyertelmusitese ────────────────────────────────────────────
# A bank egyszeri bonusza es a szamlara elvart havi bejovo osszeg ket
# kulon dolog: ne alljon mindketto "jovairas" neven egymas mellett.
body = body.replace(u'<span>Jóváírás</span>', u'<span>Elvárt havi jóváírás</span>')
body = body.replace(u'<div class="bk-gift">', u'<div class="bk-gift"><span class="bk-gift-l">Egyszeri bónusz</span>')
body = body.replace(u'<div class="bk-gift is-max">', u'<div class="bk-gift is-max"><span class="bk-gift-l">Egyszeri bónusz</span>')
# a nulla szamlavezetesi dij nem jelent teljesen koltsegmentes bankolast
body = body.replace(u'<div><span>Havi díj</span><b>0 Ft</b></div>',
                    u'<div><span>Havi számlavezetési díj</span><b>0 Ft</b><i>a tranzakciós költségekről lentebb</i></div>')

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
