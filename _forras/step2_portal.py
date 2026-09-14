# -*- coding: utf-8 -*-
"""2. lepes: portal-reteg rateve a meglevo oldalra. A tartalom valtozatlan marad."""
import re, io

S = io.open('index_assets.html', encoding='utf-8').read()
CSS = io.open('portal.css', encoding='utf-8').read()
JS  = io.open('portal.js',  encoding='utf-8').read()

# ─────────────────────────────────────────────── 1) CSS a </style> ele
assert '</style>' in S
S = S.replace('</style>', '\n' + CSS + '\n</style>', 1)

# ─────────────────────────────────────────────── 2) uj fejlec a regi nav helyere
HEAD = u'''<div class="ehead" id="ehead">
  <div class="mhead">
    <div class="mhead-in">
      <a class="elogo" href="#hero" aria-label="EAGLZ Finance">
        <img src="assets/eaglz-lockup-nav.png" alt="EAGLZ">
        <span>powered by OVB Gentischer Direction</span>
      </a>
      <div class="mnav" id="mnav" role="navigation" aria-label="Fő navigáció"></div>
      <a class="mhead-cta" href="#advisors">Időpontot foglalok →</a>
      <button class="mburger" id="mburger" aria-label="Menü" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div id="megaHost"></div>
</div>
<div class="mega-scrim" id="megaScrim"></div>
<div class="mmob" id="mmob"><div id="mmobHost"></div></div>
'''

i = S.index('<nav>')
j = S.index('</script>', S.index('<div class="mobile-menu"')) + len('</script>')
S = S[:i] + HEAD + S[j:]

# ─────────────────────────────────────────────── 3) hero ujraszerkesztese
old_hero_start = S.index('<section id="hero"')
old_hero_end   = S.index('</section>', S.index('<div class="eo-wrap">')) + len('</section>')
OLD = S[old_hero_start:old_hero_end]

# az orbit palya kiemelese, kesobb a partnersavba kerul
def _block(src, start_tag):
    """a start_tag-tol a hozza tartozo zaro </div>-ig, div-szamlalassal"""
    i = src.index(start_tag)
    depth, j = 0, i
    while True:
        no = src.find('<div', j + 1)
        nc = src.find('</div>', j + 1)
        if nc == -1: raise ValueError('nincs zaro div')
        if no != -1 and no < nc:
            depth += 1; j = no
        else:
            if depth == 0: return src[i:nc + len('</div>')]
            depth -= 1; j = nc
eo = _block(OLD, '<div class="eo-wrap">')

NEW_HERO = u'''<section id="hero" class="graph-dark">
  <div class="hero-video-bg">
    <iframe src="https://player.vimeo.com/video/610622896?background=1&autoplay=1&muted=1&loop=1&byline=0&title=0" allow="autoplay; fullscreen" title="EAGLZ"></iframe>
  </div>
  <div class="hero-video-overlay"></div>
  <div class="container">
    <div class="hero-grid">
      <div>
        <h1 class="hero-title">El tudod képzelni, hogy fél órában választ kapsz minden pénzügyi kérdésre?</h1>
        <p class="hero-lead">Az EAGLZ független pénzügyi tanácsadó csapata vagyunk. A célunk az, hogy az ügyfeleinknél a legjobb ajánlat nyerjen, ne az, amelyik először jön szembe.</p>
        <div class="ben">
          <div class="ben-c"><div class="ben-i">🏠</div><div><div class="ben-t">Több millió forint a lakáshiteleden</div><div class="ben-s">a hirdetett és az elérhető kamat különbségéből</div></div></div>
          <div class="ben-c"><div class="ben-i">🏦</div><div><div class="ben-t">Évi 20-100 ezer Ft a bankszámládon</div><div class="ben-s">0 forintos számlavezetéssel</div></div></div>
          <div class="ben-c"><div class="ben-i">🔑</div><div><div class="ben-t">3% fix kamat Otthon Starttal</div><div class="ben-s">ha jogosult vagy rá, 50 M Ft-ig</div></div></div>
          <div class="ben-c"><div class="ben-i">🤝</div><div><div class="ben-t">0 Ft, amibe ez neked kerül</div><div class="ben-s">a szolgáltató fizet minket, nem te</div></div></div>
        </div>
        <div class="hero-trust">
          <div class="hero-trust-item"><span>✓</span> Díjmentes</div>
          <div class="hero-trust-item"><span>✓</span> Online vagy személyesen</div>
          <div class="hero-trust-item"><span>✓</span> 30 fős szakértői csapat</div>
        </div>
      </div>

      <aside class="hw" aria-label="Gyorskalkulátor">
        <div class="hw-head"><b>Mennyit nyerhetsz rajta?</b></div>
        <div class="hw-tabs">
          <button type="button" class="on" data-pane="loan">Lakáshitel</button>
          <button type="button" data-pane="save">Megtakarítás</button>
          <button type="button" data-pane="quiz">Jár nekem?</button>
        </div>
        <div class="hw-body">

          <div class="hw-pane on" id="pane-loan">
            <div class="hw-f">
              <label class="hw-lab" for="w_amt">Hitelösszeg<b id="w_amt_v"></b></label>
              <input type="range" id="w_amt" min="1000000" max="100000000" step="500000" value="30000000">
            </div>
            <div class="hw-f">
              <label class="hw-lab" for="w_yrs">Futamidő<b id="w_yrs_v"></b></label>
              <input type="range" id="w_yrs" min="5" max="30" step="1" value="20">
            </div>
            <div class="hw-out">
              <div class="hw-row"><span>Törlesztő hirdetett kamattal</span><b id="w_m1"></b></div>
              <div class="hw-row"><span>Törlesztő egyedi bírálattal</span><b id="w_m2"></b></div>
              <div class="hw-hero"><span>Különbség a teljes futamidőn</span><b id="w_big"></b><i id="w_sub"></i></div>
            </div>
            <a class="hw-cta" href="#advisors">Kiszámoljuk pontosan, díjmentesen →</a>
            <div class="hw-fine">Tájékoztató számítás, nem pénzintézeti ajánlat. A pontos kamat egyedi bírálaton dől el. <a href="kalkulator.html">Részletes kalkulátorok →</a></div>
          </div>

          <div class="hw-pane" id="pane-save">
            <div class="hw-f">
              <label class="hw-lab" for="s_amt">Havi megtakarítás<b id="s_amt_v"></b></label>
              <input type="range" id="s_amt" min="5000" max="250000" step="5000" value="30000">
            </div>
            <div class="hw-f">
              <label class="hw-lab" for="s_yrs">Időtáv<b id="s_yrs_v"></b></label>
              <input type="range" id="s_yrs" min="3" max="35" step="1" value="15">
            </div>
            <div class="hw-out">
              <div class="hw-row"><span>Amit összesen befizetsz</span><b id="s_dep"></b></div>
              <div class="hw-row"><span>Amit a hozam hozzátesz</span><b id="s_gain"></b></div>
              <div class="hw-hero"><span>A végén a tiéd</span><b id="s_big"></b><i id="s_sub"></i></div>
            </div>
            <a class="hw-cta" href="#advisors">Nézzük meg az én célomra →</a>
            <div class="hw-fine">Tájékoztató számítás. A hozam nem garantált, és a választott eszköztől függ.</div>
          </div>

          <div class="hw-pane" id="pane-quiz">
            <div class="hw-q">
              <div class="hw-q-ico">🔑</div>
              <p><b>Otthon Start: 3% fix kamat, 50 millió forintig.</b> Nem mindenki jogosult rá, és a feltételek szigorúak. Két perc alatt kiderül, hogy te beleférsz-e.</p>
              <ul class="hw-qlist">
                <li>12 kérdés, regisztráció nélkül</li>
                <li>Azonnali eredmény, indoklással</li>
                <li>Megmutatja, min múlik, ha nem fér bele</li>
              </ul>
            </div>
            <a class="hw-cta" href="kviz.html">Kitöltöm a kvízt →</a>
            <div class="hw-fine">Előszűrő, nem hivatalos jogosultság-megállapítás.</div>
          </div>

        </div>
      </aside>
    </div>
  </div>
</section>'''

S = S[:old_hero_start] + NEW_HERO + S[old_hero_end:]

# ─────────────────────────────────────────────── 4) partnersav + hub a #stats utan
PARTNERS = u'''
<section id="partners">
  <div class="container">
    <div class="pt-in">
      <div>
        <div class="pt-lab">Partnereink</div>
        <div class="pt-title">Több mint 30 pénzintézet<br>és biztosító, egy kézben</div>
        <div class="pt-text">Nem egy szolgáltató terméklistájából válogatunk. Az ajánlatokat egymás mellé tesszük, és azt visszük végig, amelyik a te helyzetedben a legkedvezőbb. Az összehasonlítás és a teljes ügyintézés díjmentes.</div>
      </div>
      __EO__
    </div>
  </div>
</section>

<section id="hub" class="section" style="background:#fff;">
  <div class="container">
    <div style="text-align:center;margin-bottom:2.6rem;">
      <div class="label-chip chip-teal">Eszközök</div>
      <h2 class="section-title" style="text-align:center;">Számold ki magad, mielőtt beszélünk.</h2>
      <p class="section-sub" style="margin-left:auto;margin-right:auto;">Minden kalkulátorunk ingyenes, regisztráció nélkül működik, és azonnal ad eredményt. Egyik szám sem egy konkrét pénzintézet ajánlata: a csúszkák alapértéke tájékoztató piaci nagyságrend, amit te állítasz a saját számaidra.</p>
    </div>
    <div class="hub">
      <a class="hub-c" href="kalkulator.html">
        <div class="hub-top"><div class="hub-i">🧮</div><div><div class="hub-n">01</div><div class="hub-t">Lakáshitel kalkulátor</div></div></div>
        <div class="hub-d">A hirdetett és az egyedi bírálattal elérhető kamat különbsége forintban, a teljes futamidőre kivetítve.</div>
        <span class="hub-go">Számolok →</span>
      </a>
      <a class="hub-c" href="kalkulator.html">
        <div class="hub-top"><div class="hub-i">🔁</div><div><div class="hub-n">02</div><div class="hub-t">Hitelkiváltás</div></div></div>
        <div class="hub-d">A jelenlegi kamatodat sem kell tudnod: a törlesztődből visszaszámoljuk, és megmutatjuk a megtérülést.</div>
        <span class="hub-go">Számolok →</span>
      </a>
      <a class="hub-c" href="kalkulator.html">
        <div class="hub-top"><div class="hub-i">📊</div><div><div class="hub-n">03</div><div class="hub-t">Mennyi hitelt kaphatok?</div></div></div>
        <div class="hub-d">Az MNB adósságfék-szabálya (JTM) alapján, a jövedelmedből és a meglévő hiteleidből kiindulva.</div>
        <span class="hub-go">Számolok →</span>
      </a>
      <a class="hub-c" href="kviz.html">
        <div class="hub-top"><div class="hub-i">🔑</div><div><div class="hub-n">04</div><div class="hub-t">Otthon Start kvíz</div></div></div>
        <div class="hub-d">12 kérdés, 2 perc. Megmondja, jogosult lehetsz-e a 3 százalékos fix kamatra, és ha nem, akkor min múlik.</div>
        <span class="hub-go">Kitöltöm →</span>
      </a>
      <a class="hub-c" href="bankszamla.html">
        <div class="hub-top"><div class="hub-i">🏦</div><div><div class="hub-n">05</div><div class="hub-t">Díjmentes bankszámlák</div></div></div>
        <div class="hub-d">A 2026 őszi 0 forintos számlaajánlatok a feltételekkel együtt, és a váltás három lépése.</div>
        <span class="hub-go">Megnézem →</span>
      </a>
      <a class="hub-c" href="lakastakarek.html">
        <div class="hub-top"><div class="hub-i">🐖</div><div><div class="hub-n">06</div><div class="hub-t">Lakástakarék</div></div></div>
        <div class="hub-d">Megéri még állami támogatás nélkül? A kalkulátor évesített hozamot számol, a díjak levonása után.</div>
        <span class="hub-go">Megnézem →</span>
      </a>
      <a class="hub-c" href="nyugdij.html">
        <div class="hub-top"><div class="hub-i">🌅</div><div><div class="hub-n">07</div><div class="hub-t">Nyugdíj-kalkulátor</div></div></div>
        <div class="hub-d">Mennyi gyűlik össze a nyugdíjadra, és mennyit tesz hozzá a 20 százalékos adó-visszatérítés, ha időben kezded.</div>
        <span class="hub-go">Számolok →</span>
      </a>
      <a class="hub-c" href="gyermekjovo.html">
        <div class="hub-top"><div class="hub-i">👶</div><div><div class="hub-n">08</div><div class="hub-t">Gyermek-megtakarítás</div></div></div>
        <div class="hub-d">Babakötvény és oktatási alap: mennyi gyűlik össze 18 éves korára, havi pár ezer forintból.</div>
        <span class="hub-go">Számolok →</span>
      </a>
      <a class="hub-c" href="befektetesek.html">
        <div class="hub-top"><div class="hub-i">📦</div><div><div class="hub-n">09</div><div class="hub-t">Befektetés és TBSZ</div></div></div>
        <div class="hub-d">Mennyit visz el a hozamodból az adó és a költség, és mennyivel marad több TBSZ-en, öt év után.</div>
        <span class="hub-go">Számolok →</span>
      </a>
      <a class="hub-c" href="tamogatasok.html">
        <div class="hub-top"><div class="hub-i">💰</div><div><div class="hub-n">10</div><div class="hub-t">Állami támogatások 2026</div></div></div>
        <div class="hub-d">Otthon Start, CSOK Plusz, Falusi CSOK, Babaváró: mi él most, mi futott ki, és milyen sorrendben érdemes igényelni.</div>
        <span class="hub-go">Megnézem →</span>
      </a>
      <a class="hub-c" href="biztositasok.html">
        <div class="hub-top"><div class="hub-i">🛡️</div><div><div class="hub-n">11</div><div class="hub-t">Biztosítási útmutató</div></div></div>
        <div class="hub-d">KGFB-váltás az évfordulón, lakásbiztosítás alulbiztosítás nélkül, és a hét hiba, amitől nem fizet a biztosító.</div>
        <span class="hub-go">Megnézem →</span>
      </a>
      <a class="hub-c" href="vallalati.html">
        <div class="hub-top"><div class="hub-i">🏢</div><div><div class="hub-n">12</div><div class="hub-t">Vállalati megoldások</div></div></div>
        <div class="hub-d">Széchenyi Kártya Program, cafeteria-keretek és céges biztosítás a 2026-os feltételek szerint.</div>
        <span class="hub-go">Megnézem →</span>
      </a>
    </div>
    <p style="max-width:76ch;margin:1.8rem auto 0;text-align:center;font-size:.79rem;line-height:1.75;color:var(--gray);">
      A kalkulátorok tájékoztató jellegűek, egyszerűsített, annuitásos számítást használnak, és nem minősülnek ajánlatnak, ajánlattételi felhívásnak vagy THM-tájékoztatásnak. Az oldalon egyetlen pénzintézet ajánlata, kamata vagy THM-e sem szerepel; a logók az adott vállalatok tulajdonát képezik, feltüntetésük a hazai piac szemléltetését szolgálja. A naprakész banki kondíciók az <a href="https://hitelvalaszto.mnb.hu/termekkereso" target="_blank" rel="noopener" style="color:var(--teal-ink);font-weight:600;">MNB Termékkeresőjében</a> ellenőrizhetők. Adatok érvényessége: <b data-upd></b>.
    </p>
  </div>
</section>
'''.replace('__EO__', eo)

k = S.index('</section>', S.index('<section id="stats">')) + len('</section>')
S = S[:k] + '\n' + PARTNERS + S[k:]

# ─────────────────────────────────────────────── 5) JS a </body> ele
S = S.replace('</body>', '<script>\n' + JS + '\n</script>\n</body>', 1)


# ─────────────────────────────────────────────── 6) szamlalok: a cel ertekrol indulnak
S = re.sub(r'<span class="count" data-target="(\d+)">0</span>',
           lambda m: '<span class="count" data-target="%s">%s</span>' % (m.group(1), int(m.group(1))),
           S)
S = S.replace("function animateCount(el){\n    const target = +el.dataset.target;",
              "function animateCount(el){\n    const target = +el.dataset.target;\n    el.textContent = '0';")

import index_layout, theme_inject
S = index_layout.apply(S)
S = theme_inject.apply(S)
io.open('index_portal.html', 'w', encoding='utf-8').write(S)
print('index_portal.html:', len(S)//1024, 'KB')
for t in ['id="ehead"', 'id="mnav"', 'class="hw"', 'id="partners"', 'id="hub"', 'eo-wrap', '<nav>']:
    print('  %-18s %d' % (t, S.count(t)))
