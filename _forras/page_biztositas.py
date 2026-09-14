# -*- coding: utf-8 -*-
from build_sub import build

def faq_html(items):
    out = []
    for q, ps in items:
        body = ''.join('<p>%s</p>' % p for p in ps)
        out.append('<details class="faq-item"><summary class="faq-q">%s'
                   '<svg class="faq-chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                   'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>'
                   '</summary><div class="faq-a">%s</div></details>' % (q, body))
    return '\n      '.join(out)

BODY = u'''
<section class="sub-hero">
  <div class="container">
    <a href="index.html" class="sub-back">← Vissza a főoldalra</a>
    <h1 class="sub-h1">Biztosítások: <em>30+ biztosító egy kézben</em></h1>
    <p class="sub-lead">A biztosítás díja egyéni, ezért ezen az oldalon nincs kalkulátor. Ami van: mi ellen érdemes védekezni, mikor lehet váltani, mennyit lehet ezzel nyerni, és melyek azok a hibák, amiktől egy kár esetén nem fizet a biztosító.</p>
    <div class="sub-chips">
      <div class="sub-chip">🚗 KGFB váltás <b>évfordulón</b></div>
      <div class="sub-chip">🏠 Lakás, élet, egészség</div>
      <div class="sub-chip">📅 Adatok: <b data-upd></b></div>
    </div>
    <div class="quicknav">
      <a href="#online" class="qn on">⚡ Online kötés</a>
      <a href="#kgfb" class="qn">🚗 KGFB</a>
      <a href="#lakas" class="qn">🏠 Lakásbiztosítás</a>
      <a href="index.html#advisors" class="qn">📅 Időpontot foglalok</a>
    </div>
  </div>
</section>

<section class="section" style="background:#fff;padding-bottom:2.4rem;">
  <div class="container">
    <div class="toc">
      <div class="toc-t">Ezen az oldalon</div>
      <ol>
        <li><a href="#terkep">Biztosítási térkép</a></li>
        <li><a href="#kgfb">KGFB: mikor és hogyan válts</a></li>
        <li><a href="#lakas">Lakásbiztosítás</a></li>
        <li><a href="#szemelyi">Élet, baleset, egészség</a></li>
        <li><a href="#hibak">Hét hiba, amitől nem fizet a biztosító</a></li>
        <li><a href="#online">Amit most azonnal elintézhetsz</a></li>
        <li><a href="#gyik">Gyakori kérdések</a></li>
      </ol>
    </div>
    <div class="art" id="terkep">
      <h2>Előbb a kockázat, utána a termék</h2>
      <p class="lead">A legtöbb ember úgy köt biztosítást, hogy előbb megkérdezi, mennyibe kerül. Ez fordítva van: előbb azt kell tisztázni, <b>melyik kár tudná felborítani a családi költségvetést</b>, és csak utána jön a díj.</p>
      <p>Egy ellopott telefon kellemetlen. Egy kereső elvesztése, egy leégett tető vagy egy tartós keresőképtelenség viszont évekre visszavet. A biztosításnak az utóbbiakra kell szólnia, és a kicsiket inkább vállald magad, mert azokra a fedezet aránytalanul drága.</p>

      <div class="tiles">
        <div class="tile"><div class="tile-i">🚗</div><div class="tile-t">Gépjármű</div><div class="tile-d">KGFB kötelező, casco opcionális. Évfordulókor váltással sokat lehet nyerni, ugyanazzal a fedezettel.</div></div>
        <div class="tile"><div class="tile-i">🏠</div><div class="tile-t">Otthon és vagyon</div><div class="tile-d">Tűz, víz, vihar, betörés, felelősség. A leggyakoribb hiba itt az <b>elavult biztosítási összeg</b>.</div></div>
        <div class="tile"><div class="tile-i">❤️</div><div class="tile-t">Élet és hitelfedezet</div><div class="tile-d">Ha a családi bevétel egy vagy két emberen múlik, ez a legfontosabb fedezet. Lakáshitel mellé különösen.</div></div>
        <div class="tile"><div class="tile-i">🩹</div><div class="tile-t">Baleset</div><div class="tile-d">Maradandó egészségkárosodásra és kórházi napokra. Olcsó fedezet, gyakran hiányzik.</div></div>
        <div class="tile"><div class="tile-i">🩺</div><div class="tile-t">Egészség</div><div class="tile-d">Magánellátás, szűrés, gyorsabb diagnózis. Egyre nagyobb súllyal a várólisták miatt.</div></div>
        <div class="tile"><div class="tile-i">✈️</div><div class="tile-t">Utas és asszisztencia</div><div class="tile-d">Rövid távú, olcsó, és egy külföldi kórházi kezelésnél <b>milliós tétel</b> a különbség.</div></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ KGFB ═══ -->
<section id="kgfb" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">01</div>
      <h2 class="section-title">KGFB: mikor válthatsz, és mit nyersz vele</h2>
      <p class="section-sub">Ugyanaz a törvényi fedezet, bármelyik biztosítónál. A díj viszont jelentősen eltér, és évfordulókor ingyen lehet váltani.</p>
    </div>
    <div class="art">
      <div class="box warn">
        <span class="box-t">A legfontosabb szabály, amin a legtöbben elcsúsznak</span>
        A felmondásnak írásban <b>be kell érkeznie</b> a biztosítóhoz az évforduló előtti 30. napig. Nem a feladás, hanem a <b>beérkezés</b> dátuma számít. Egy nap csúszás egy évet jelent: a szerződés automatikusan folytatódik, és legközelebb csak jövőre válthatsz.
      </div>

      <h3>Mikor van az évfordulód?</h3>
      <p>Nincs többé egységes, országos kampányidőszak. A <b>2010. január 1. előtt</b> kötött szerződéseknél az évforduló egységesen január 1., ezeknél a felmondási határidő december 1. éjfél, és a november a kampányidőszak. A <b>2010 után</b> kötött szerződéseknél az évforduló a szerződéskötés dátumához igazodik, tehát egyénileg szóródik az év során.</p>
      <p>A saját évfordulódat a kötvényedből olvashatod ki. A biztosítónak egyébként kötelessége az évforduló előtt legalább 50 nappal értesíteni téged az új díjról, tehát a levél megérkezése egyben emlékeztető is.</p>

      <h3>Évközi megszűnés</h3>
      <p>Az évfordulón kívül három esetben szűnhet meg a szerződés:</p>
      <ul class="clean">
        <li><b>Érdekmúlás:</b> eladás, forgalomból kivonás, megsemmisülés, lopás. A tranzakció napjával.</li>
        <li><b>Díjnemfizetés:</b> 60 nap után. Ilyenkor viszont az évfordulóig <b>csak ugyanannál a biztosítónál</b> köthetsz újra, tehát ez nem a váltás útja.</li>
        <li><b>Közös megegyezés:</b> ritka, a biztosító hozzájárulása kell hozzá.</li>
      </ul>

      <h3>Bonus-malus dióhéjban</h3>
      <p>Kármentes évenként egy osztályt lépsz felfelé, A00-ból B01, majd tovább <b>B10-ig</b>, ami a legjobb. Okozott kár esetén visszasorolás következik, M01-től M04-ig. A megszerzett bonus-fokozat <b>átvihető másik biztosítóhoz</b>, és azonos kategóriájú csereautóra két éven belül is megmarad.</p>
      <p>Amit kevesen tudnak: a törvényi bonus-malus mellett a biztosítók <b>saját károkozói pótdíjat</b> is alkalmazhatnak, egymástól eltérő mértékben. Ezért kárt követően különösen érdemes több ajánlatot összevetni: ugyanazzal az előzménnyel nagyon eltérő díjakat kaphatsz.</p>

      <div class="box info">
        <span class="box-t">Kártérítési limitek</span>
        A KGFB törvényi fedezete káreseményenként <b>dologi kárra 1 300 000 euró</b>, <b>személyi sérüléses kárra 6 450 000 euró</b> értékhatárig terjed. A limiteket a jogszabály euróban rögzíti. Ha a kötvényeden ennél alacsonyabb szám szerepel, az elavult adat: a törvényi limitre akkor is jogosult vagy.
      </div>

      <div class="box quote">
        <b>Fedezetlenség:</b> ha lejár a szerződésed és nem kötsz újat, fedezetlenségi díjat kell fizetni minden napra. Ez szándékosan magasabb a normál biztosítási díjnál, egy átlagos személyautónál naponta több mint ezer forint. Néhány hét alatt többe kerül, mint egy egész éves biztosítás.
      </div>
    </div>
  </div>
</section>

<!-- ═══ LAKÁS ═══ -->
<section id="lakas" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">02</div>
      <h2 class="section-title">Lakásbiztosítás: a leggyakoribb elavult szerződés</h2>
      <p class="section-sub">Sok háztartásnál évtizedes szerződés fut olyan biztosítási összeggel, ami ma már a fürdőszoba felújítására sem elég.</p>
    </div>
    <div class="art">
      <h3>A két érték, amit nem szabad összekeverni</h3>
      <p>Az <b>épület biztosítási összegének</b> az újjáépítési költséget kell fednie, nem a forgalmi értéket. Kár esetén ugyanis nem eladni fogod az ingatlant, hanem helyreállítani, és az építőipari árak az elmúlt években jelentősen emelkedtek. Egy panellakásnál ez ritkábban probléma, egy családi háznál annál gyakrabban.</p>
      <p>Az <b>ingóság biztosítási összege</b> a berendezés, a műszaki cikkek, a ruhák és az értéktárgyak pótlási értéke. Itt az a jellemző hiba, hogy évek óta ugyanaz a szám szerepel, közben a háztartás felszereltsége megváltozott.</p>

      <div class="box stop">
        <span class="box-t">Alulbiztosítás: arányos térítés</span>
        Ha a biztosítási összeg kisebb a vagyon tényleges értékénél, a biztosító a kárt <b>arányosan</b> téríti. 40 millió forintos újjáépítési értékű ház 20 millióra biztosítva: egy 4 milliós vízkárból a biztosító 2 milliót fizet, pedig a kár bőven belefért volna a biztosítási összegbe. Ez nem trükk, hanem a Ptk. szabálya, és ez a leggyakoribb csalódás forrása.
      </div>

      <h3>Mire figyelj a fedezeteknél</h3>
      <ul class="clean">
        <li><b>Felelősségbiztosítás:</b> ha a te csőtöröséd önti el a szomszédot, ez fizet. Olcsó, és sokszor hiányzik.</li>
        <li><b>Vízkár:</b> a leggyakoribb kártípus. Nézd meg, mire terjed ki, és mire nem.</li>
        <li><b>Üvegtörés, vandalizmus, betörés:</b> a betöréshez jellemzően védettségi előírás is tartozik.</li>
        <li><b>Napelem, klíma, kerti építmény:</b> ezek gyakran <b>külön nevesítést</b> igényelnek, egyébként nincsenek fedezve.</li>
        <li><b>Albérletbe adott ingatlan:</b> más szerződés kell rá, mint a saját használatúra.</li>
      </ul>
      <div class="box info">
        <span class="box-t">Egy gyors önellenőrzés</span>
        Nézd meg a kötvényeden az épület biztosítási összegét, és oszd el a ház alapterületével. Ha az eredmény jóval a mai építési négyzetméterár alatt van, akkor alulbiztosított vagy. Ez az a fajta dolog, ami öt percbe telik, és egy kárnál milliókat jelent.
      </div>
    </div>
  </div>
</section>

<!-- ═══ SZEMÉLYI ═══ -->
<section id="szemelyi" class="section dark-sec">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">03</div>
      <h2 class="section-title">Élet, baleset, egészség</h2>
      <p class="section-sub">Itt nem a vagyont védjük, hanem a jövedelemtermelő képességet. Ez a legtöbb családnál a legnagyobb, mégis a legritkábban biztosított érték.</p>
    </div>
    <div class="art wide">
      <div class="tiles">
        <div class="tile" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">
          <div class="tile-i">❤️</div><div class="tile-t" style="color:#fff;">Kockázati életbiztosítás</div>
          <div class="tile-d" style="color:rgba(255,255,255,.66);">Tiszta védelem, megtakarítási rész nélkül, ezért olcsó. Akkor fizet, ha a legrosszabb bekövetkezik. <b style="color:#fff">Lakáshitel mellé</b> gyakorlatilag kötelező józan ésszel.</div>
        </div>
        <div class="tile" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">
          <div class="tile-i">🩹</div><div class="tile-t" style="color:#fff;">Balesetbiztosítás</div>
          <div class="tile-d" style="color:rgba(255,255,255,.66);">Maradandó egészségkárosodásra, csonttörésre, kórházi napokra. Alacsony díj, és a gyerekeknél is érdemes gondolkodni rajta.</div>
        </div>
        <div class="tile" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">
          <div class="tile-i">🩺</div><div class="tile-t" style="color:#fff;">Egészségbiztosítás</div>
          <div class="tile-d" style="color:rgba(255,255,255,.66);">Magánellátás, szakorvosi vizsgálat, diagnosztika várólista nélkül. Sokan ezt cafeteria-elemként is megkapják, csak nem használják.</div>
        </div>
      </div>

      <h3 style="color:#fff;">Mekkora összegre szóljon?</h3>
      <p>Az életbiztosításnál van egy egyszerű kiindulópont: legyen elég ahhoz, hogy a család <b>kifizesse a fennálló hitelt</b>, és utána még legalább 2-3 évig ki tudja gazdálkodni a kieső jövedelmet. Ez idő alatt lehet átállni, munkát váltani, dönteni az ingatlanról.</p>
      <p>A gyakorlatban ez jóval nagyobb összeg, mint amivel a legtöbben szerződnek. Ugyanakkor a kockázati életbiztosítás fiatal korban <b>meglepően olcsó</b>, tehát a magasabb összeg általában nem havi tízezrekben jelentkezik.</p>

      <div class="box info" style="background:rgba(140,197,189,.1);border-color:rgba(140,197,189,.3);color:rgba(255,255,255,.8);">
        <span class="box-t" style="color:var(--teal-lite);">Hitelfedezeti életbiztosítás: bank vagy piac?</span>
        Lakáshitelnél a bank gyakran ajánl saját hitelfedezeti biztosítást, és ez néha kamatkedvezménnyel is jár. Érdemes viszont összevetni egy piaci kockázati életbiztosítással: sokszor <b style="color:#fff">ugyanaz a védelem olcsóbban</b> megvan, és a kedvezményezett is te maradsz, nem a bank. Mi mindkét változatot kiszámoljuk.
      </div>
    </div>
  </div>
</section>

<!-- ═══ HIBÁK ═══ -->
<section id="hibak" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">Amire figyelj</div>
      <h2 class="section-title">Hét dolog, amitől egy kárnál nem fizet a biztosító</h2>
      <p class="section-sub">Nem azért, mert át akar verni, hanem mert a szerződés így szól. Mindegyik elkerülhető.</p>
    </div>
    <div class="art wide">
      <div class="tiles c2">
        <div class="tile"><div class="tile-i">1️⃣</div><div class="tile-t">Alulbiztosítás</div><div class="tile-d">A leggyakoribb. Arányos térítés lesz belőle, és pont akkor derül ki, amikor a legrosszabbkor jön.</div></div>
        <div class="tile"><div class="tile-i">2️⃣</div><div class="tile-t">Be nem jelentett változás</div><div class="tile-d">Tetőtér-beépítés, napelem, új melléképület, megváltozott használat. Ha nincs bejelentve, <b>nincs fedezve</b>.</div></div>
        <div class="tile"><div class="tile-i">3️⃣</div><div class="tile-t">Nem teljesített védelmi előírás</div><div class="tile-d">Betörésnél a kötvény meghatározott zárat, rácsot vagy riasztót ír elő. Ha nincs meg, csökkenthetik a térítést.</div></div>
        <div class="tile"><div class="tile-i">4️⃣</div><div class="tile-t">Kizárások átugrása</div><div class="tile-d">Minden szerződésnek van kizárási listája. Ez a legunalmasabb rész, és ez dönt egy vitás kárnál.</div></div>
        <div class="tile"><div class="tile-i">5️⃣</div><div class="tile-t">Késedelmes kárbejelentés</div><div class="tile-d">A szerződés bejelentési határidőt ír elő, jellemzően pár nap. Utána a biztosító hivatkozhat arra, hogy a kár már nem vizsgálható.</div></div>
        <div class="tile"><div class="tile-i">6️⃣</div><div class="tile-t">Hiányos egészségi nyilatkozat</div><div class="tile-d">Élet- és egészségbiztosításnál az elhallgatott előzmény a szolgáltatás megtagadásához vezethet. Jobb mindent leírni.</div></div>
        <div class="tile"><div class="tile-i">7️⃣</div><div class="tile-t">Díjhátralék</div><div class="tile-d">A nem fizetett díj miatt megszűnt szerződés nem fizet. Banális, mégis gyakori, főleg csoportos beszedés visszautasításánál.</div></div>
      </div>
      <div class="box info">
        <span class="box-t">Amit ilyenkor csinálunk</span>
        Kár esetén nem neked kell telefonálgatnod és levelezned. Az ügyfeleinknek a kárrendezésben is <b>mi képviseljük az érdekeit</b> a biztosító felé, és a háttérben álló asszisztenciát is igénybe veheted, amíg nálunk vagy szerződésben. Sok esetben pont ezen a ponton derül ki, hogy megérte tanácsadón keresztül kötni.
      </div>
    </div>
  </div>
</section>

<!-- ═══ ONLINE ═══ -->
<section id="online" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">Azonnal</div>
      <h2 class="section-title">Amit most, azonnal elintézhetsz</h2>
      <p class="section-sub">Ezek a felületek az OVB hivatalos rendszerében futnak. Nem kell hozzájuk időpont, és nem kell hozzájuk mi sem, de ha elakadsz, szólj.</p>
    </div>
    <div class="rel">
      <a class="rel-c" href="https://ovbportal.hu/ovbphp/public/onlineKotesKGFB.php?hash=gentischer.richard" target="_blank" rel="noopener"><div class="rel-i">🚗</div><div><div class="rel-t">Gépjármű-biztosítás</div><div class="rel-d">KGFB és casco, online kötés</div></div></a>
      <a class="rel-c" href="https://online.ovb.hu/lakasbiztositas-informaciok/" target="_blank" rel="noopener"><div class="rel-i">🏠</div><div><div class="rel-t">Lakásbiztosítás</div><div class="rel-d">Információs microsite</div></div></a>
      <a class="rel-c" href="https://ovbportal.hu/ovbphp/public/onlineKotesUtasbiztositas.php?hash=gentischer.richard" target="_blank" rel="noopener"><div class="rel-i">✈️</div><div><div class="rel-t">Utasbiztosítás</div><div class="rel-d">Utazás előtt, percek alatt</div></div></a>
      <a class="rel-c" href="https://ovbportal.hu/ovbphp/public/onlineKotesAsszisztencia.php?hash=gentischer.richard" target="_blank" rel="noopener"><div class="rel-i">☂️</div><div><div class="rel-t">Gépjármű-asszisztencia</div><div class="rel-d">Defekt, indítás, vontatás</div></div></a>
      <a class="rel-c" href="https://online.ovb.hu/csob/" target="_blank" rel="noopener"><div class="rel-i">💳</div><div><div class="rel-t">Csoportos beszedés</div><div class="rel-d">Online átvezetés</div></div></a>
      <a class="rel-c" href="index.html#advisors"><div class="rel-i">📅</div><div><div class="rel-t">Inkább megbeszélném</div><div class="rel-d">Válassz tanácsadót</div></div></a>
    </div>
  </div>
</section>

<section id="gyik" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">GYIK</div>
      <h2 class="section-title">Gyakori kérdések</h2>
    </div>
    <div class="faq-list" style="max-width:820px;margin:0 auto;display:flex;flex-direction:column;gap:.7rem;">
      __FAQ__
    </div>
  </div>
</section>

<section class="section graph-light" style="padding-top:3rem;padding-bottom:3rem;">
  <div class="container">
    <div class="sec-head" style="margin-bottom:1.6rem;">
      <h2 class="section-title" style="font-size:1.35rem;">Kapcsolódó oldalak</h2>
    </div>
    <div class="rel">
      <a class="rel-c" href="vallalati.html"><div class="rel-i">🏢</div><div><div class="rel-t">Céges biztosítások</div><div class="rel-d">Vagyon, felelősség, flotta</div></div></a>
      <a class="rel-c" href="kalkulator.html"><div class="rel-i">🧮</div><div><div class="rel-t">Kalkulátorok</div><div class="rel-d">Hitel, JTM, bankszámla</div></div></a>
      <a class="rel-c" href="nyugdij.html"><div class="rel-i">🌅</div><div><div class="rel-t">Nyugdíj-megtakarítás</div><div class="rel-d">20% adó-visszatérítéssel</div></div></a>
    </div>
  </div>
</section>
'''

FAQ = [
("Mikor mondhatom fel a kötelezőmet?",
 ["Évente egyszer, a szerződés évfordulóján. A felmondásnak írásban <b>be kell érkeznie</b> a biztosítóhoz az évforduló előtti 30. napig, és nem a postára adás dátuma számít. Ajánlott tértivevényes küldés vagy visszaigazolható elektronikus út.",
  "A felmondásnak tartalmaznia kell a szerződő nevét és címét, a kötvényszámot, a rendszámot és a felmondás dátumát, ami az évforduló napja."]),

("Lemaradtam a határidőről. Mit tehetek?",
 ["Az évfordulós váltás lehetősége egy évre elment: a szerződés automatikusan folytatódik. Évközben csak érdekmúlással (eladás, forgalomból kivonás) vagy díjnemfizetéssel szűnhet meg, de a díjnemfizetés nem megoldás, mert utána az évfordulóig <b>csak ugyanannál a biztosítónál</b> köthetsz.",
  "Amit érdemes: jegyezd fel az évfordulót, és a biztosító 50 nappal korábban érkező díjértesítőjét kezeld emlékeztetőként. Mi az ügyfeleinknél ezt magunktól is jelezzük."]),

("Mennyit lehet nyerni a váltással?",
 ["Ez nagyon eltérő, mert a díjak biztosítónként, a gépjármű típusa, az életkorod, a lakcímed és a bonus-fokozatod szerint is szóródnak. Egy kármentes, jó besorolású ügyfélnél is jelentős különbségek vannak.",
  "Amit biztosan állíthatunk: a fedezet ugyanaz, mert a KGFB tartalmát törvény írja elő. Tehát ha ugyanazért kevesebbet lehet fizetni, azon nincs mit mérlegelni. Kárrendezési gyakorlatban és ügyfélkiszolgálásban viszont már van különbség, és ezt is figyelembe vesszük."]),

("Kell casco a hitelre vett autóhoz?",
 ["Ha a finanszírozó előírja, akkor igen, ez a szerződés feltétele. Ezen kívül általánosságban: casco akkor indokolt, ha az autó pótlása jelentős anyagi terhet jelentene. Egy régi, alacsony értékű autónál gyakran nem éri meg, egy új vagy hiteles autónál szinte mindig.",
  "Az önrészt itt érdemes tudatosan beállítani: a magasabb önrész jelentősen csökkenti a díjat, és a kis karcolásokat úgyis inkább magad rendezed, hogy ne rontsd a besorolást."]),

("Régi a lakásbiztosításom. Cseréljem vagy módosítsam?",
 ["Először nézzük meg, mi a baj. Ha csak a biztosítási összeg avult el, sok esetben <b>ugyanannál a biztosítónál</b> is lehet értékkövetéssel rendezni, és nem kell új szerződés.",
  "Ha viszont hiányoznak fedezetek, amik ma már alapnak számítanak, vagy a díj-érték arány rossz, akkor érdemes a piacot is megnézni. A döntés mindig a tiéd, mi a két változatot tesszük egymás mellé."]),

("Miért éri meg tanácsadón keresztül kötni, ha online is tudok?",
 ["Egyszerű termékeknél, például utasbiztosításnál vagy kötelezőnél, gyakran tényleg nem kell hozzánk jönnöd. Ezért is teszünk ki közvetlen online felületeket erre az oldalra.",
  "Ahol számítunk: az összetettebb szerződéseknél, ahol könnyű alulbiztosítani vagy fedezetet kihagyni, és <b>kárrendezéskor</b>. Akkor nem neked kell levelezned a biztosítóval, hanem mi képviselünk. És ugyanannyiba kerül a szerződés, mert a mi munkánkat a biztosító fizeti."]),

("Mi a helyzet az egészségbiztosítással? Megéri?",
 ["Attól függ, mit vársz tőle. Ha azt, hogy szakorvosi vizsgálathoz és diagnosztikához gyorsan hozzájuss, akkor jellemzően igen, és nem is drága. Ha azt, hogy minden egészségügyi kiadásodat fedezze, akkor nem: arra nincs ilyen termék.",
  "Sokan egyébként a munkáltatójukon keresztül már rendelkeznek valamilyen csoportos egészségbiztosítással, csak nem tudnak róla. Érdemes ezzel kezdeni, mielőtt újat kötnél."]),

("Hány biztosító ajánlatát nézitek meg?",
 ["A hazai piac meghatározó szereplőit, 30-nál több partnerrel dolgozunk. Nem mindegyik kínál minden terméket, ezért terméktípusonként más a releváns kör.",
  "Amit garantálunk: nem egy biztosító terméklistájából válogatunk, és ha a meglévő szerződésed a legjobb, azt is megmondjuk."]),
]

BODY = BODY.replace('__FAQ__', faq_html(FAQ))

LEGAL = (u'<b>*</b> Az oldalon szereplő adatok tájékoztató jellegűek, a <b>2026. szeptemberi</b> állapotot tükrözik, és nem minősülnek ajánlattételnek, '
         u'ajánlattételi felhívásnak vagy biztosítási tanácsadásnak. A biztosítási díj minden esetben egyedi kockázatelbírálás alapján dől el, és a '
         u'gépjármű, az ingatlan, az életkor, a lakóhely, a kárelőzmény és a választott fedezetek függvényében jelentősen eltérhet; az oldalon ezért '
         u'egyetlen biztosító konkrét díja vagy ajánlata sem szerepel. A kötelező gépjármű-felelősségbiztosítás tartalmát és kártérítési limiteit '
         u'(dologi kárra 1 300 000 euró, személyi sérüléses kárra 6 450 000 euró káreseményenként) jogszabály rögzíti; a limiteket a jogszabály euróban '
         u'határozza meg, a forintra átszámítás évente változik. A felmondási és évfordulós szabályok, valamint a bonus-malus rendszer leírása a hatályos '
         u'jogszabályi rendelkezéseken alapul. Az alulbiztosítás jogkövetkezményére vonatkozó leírás a Ptk. 6:460. §-án alapul. Egy adott kár térítése '
         u'minden esetben a megkötött szerződés feltételei, kizárásai és a biztosító kárrendezési döntése szerint alakul. A megjelenített biztosítói '
         u'logók az adott vállalatok tulajdonát képezik, feltüntetésük a hazai piac szemléltetését szolgálja. Adatok érvényessége: <b data-upd></b>.')

build('biztositasok.html',
      u'Biztosítások 2026: KGFB, lakás, élet, egészség | EAGLZ Finance',
      u'Mikor válthatsz KGFB-t, miért fizet kevesebbet a biztosító alulbiztosításnál, és mekkora életbiztosítás elég? 30+ biztosító, díjmentes összehasonlítás.',
      BODY, LEGAL,
      u'Nézzük át, mi van és mi hiányzik.',
      u'Egy díjmentes átvilágításon végigvesszük a meglévő szerződéseidet, megkeressük a lefedetlen kockázatokat, és megmondjuk azt is, ha valami már rendben van.')
