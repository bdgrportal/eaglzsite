# -*- coding: utf-8 -*-
from build_sub import build

BODY = u'''
<section class="sub-hero">
  <div class="container">
    <a href="index.html" class="sub-back">← Vissza a főoldalra</a>
    <h1 class="sub-h1">Gyermek-megtakarítás: <em>18 évre előre</em></h1>
    <p class="sub-lead">A legnagyobb ajándék egy gyereknek az, ha felnőttként nem nulláról kell kezdenie. Ezen az oldalon végigvesszük, mit ad hozzá az állam a babakötvényhez, mennyit hoz a havi pár ezer forint 18 év alatt, és mikor melyik megtakarítási forma a jobb.</p>
    <div class="sub-chips">
      <div class="sub-chip">🏛️ <b>10%</b> állami támogatás</div>
      <div class="sub-chip">📈 Infláció <b>+3%</b> kamat</div>
      <div class="sub-chip">📅 Adatok: <b data-upd></b></div>
    </div>
    <div class="quicknav">
      <a href="#kalkulator" class="qn on">📊 Kalkulátor</a>
      <a href="#babakotveny" class="qn">🏛️ Babakötvény</a>
      <a href="#melyiket" class="qn">🔍 Melyiket válaszd</a>
      <a href="index.html#advisors" class="qn">📅 Időpontot foglalok</a>
    </div>
  </div>
</section>

<section class="section" style="background:#fff;padding-bottom:2.4rem;">
  <div class="container">
    <div class="toc">
      <div class="toc-t">Ezen az oldalon</div>
      <ol>
        <li><a href="#miert">Miért az idő a legfontosabb</a></li>
        <li><a href="#kalkulator">Kalkulátor: mennyi gyűlik össze</a></li>
        <li><a href="#babakotveny">A babakötvény pontosan</a></li>
        <li><a href="#melyiket">Babakötvény, TBSZ vagy más?</a></li>
        <li><a href="#indulas">Hogyan kezdj hozzá</a></li>
        <li><a href="#hibak">Hat gyakori hiba</a></li>
        <li><a href="#gyik">Gyakori kérdések</a></li>
      </ol>
    </div>

    <div class="art" id="miert">
      <h2>A gyerekednél az idő többet ér, mint az összeg</h2>
      <p class="lead">Egy 18 éves időtáv ritka luxus a pénzügyekben. Ennyi idő alatt a kamatos kamat annyit dolgozik, hogy a havi befizetés nagysága másodlagossá válik ahhoz képest, hogy <b>mikor kezdted el</b>.</p>
      <p>Egy egyszerű összehasonlítás ugyanarra a célösszegre: aki születéskor kezdi, jóval kisebb havi összeggel ér célba, mint aki tíz évvel később. Nem azért, mert okosabban fektet be, hanem mert több éven át kamatozik a pénze.</p>

      <div class="kpis">
        <div class="kpi"><b>42 500 Ft</b><span>induló életkezdési támogatás, automatikusan</span></div>
        <div class="kpi"><b>12 000 Ft</b><span>maximális éves állami támogatás</span></div>
        <div class="kpi"><b>7,4%</b><span>a babakötvény kamata 2026-ban</span></div>
        <div class="kpi"><b>0%</b><span>adó a babakötvény kamatán</span></div>
      </div>

      <div class="box info">
        <span class="box-t">Amiről sokan nem tudnak</span>
        Minden 2005. december 31. után született gyermeknek jár egy <b>42 500 forintos induló életkezdési támogatás</b>, amit az állam automatikusan elkülönít. Amíg nem nyitsz Start-számlát, ez az összeg <b>kamat nélkül</b> áll a Kincstárnál. Start-számlára átvezetve viszont azonnal elkezd inflációkövető kamatot fizetni. Sok családnál ez a pénz évekig parlagon hever.
      </div>
    </div>
  </div>
</section>

<!-- ═══ KALKULÁTOR ═══ -->
<section id="kalkulator" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">Kalkulátor</div>
      <h2 class="section-title">Mennyi gyűlik össze 18 éves korára?</h2>
      <p class="section-sub">Állítsd be a gyermeked mostani életkorát és a havi összeget. A kalkulátor kiszámolja, mennyi lesz a 18. születésnapján, és hogy ebből mennyit tett hozzá az állam.</p>
    </div>

    <div class="sc" id="gy">
      <div class="sc-in">
        <div class="sc-seg" role="group" aria-label="Forma">
          <button type="button" class="on" data-f="bk">Babakötvény</button>
          <button type="button" data-f="egyeb">Egyéb megtakarítás</button>
        </div>
        <div class="scf">
          <label class="scf-top" for="g_havi">Havi megtakarítás<b id="g_havi_v"></b></label>
          <input type="range" id="g_havi" min="2000" max="100000" step="1000" value="10000">
          <span class="scf-note">Babakötvénynél a maximális állami támogatáshoz havi 10 000 Ft (évi 120 000 Ft) befizetés kell.</span>
        </div>
        <div class="scf">
          <label class="scf-top" for="g_kor">A gyermek mostani életkora<b id="g_kor_v"></b></label>
          <input type="range" id="g_kor" min="0" max="17" step="1" value="0">
          <span class="scf-note">A számítás a 18. születésnapig tart. Újszülöttnél az induló 42 500 Ft-tal is számolunk.</span>
        </div>
        <div class="scf">
          <label class="scf-top" for="g_kamat">Éves kamat vagy hozam<b id="g_kamat_v"></b></label>
          <input type="range" id="g_kamat" min="0" max="14" step="0.1" value="7.4">
          <span class="scf-note" id="g_kamat_note"></span>
        </div>
      </div>
      <div class="sc-out">
        <div class="sc-hero">
          <div class="sc-hero-l">A 18. születésnapján</div>
          <div class="sc-hero-n" id="g_big"></div>
          <div class="sc-hero-s" id="g_sub"></div>
        </div>
        <div class="sc-rows">
          <div><span>Amit ti fizettek be</span><b id="g_bef"></b></div>
          <div class="hl"><span>Amit az állam hozzátesz</span><b id="g_allam"></b></div>
          <div><span>Ebből kamat vagy hozam</span><b id="g_kam"></b></div>
          <div><span>Évi állami támogatás</span><b id="g_evi"></b></div>
          <div><span>Hátralévő évek</span><b id="g_ev"></b></div>
        </div>
        <div class="sc-warn" id="g_warn"></div>
      </div>
    </div>
    <div class="sc-actions">
      <a href="index.html#advisors" class="apt-btn-inner" style="padding:.85rem 1.8rem;">📅 Nézzük meg a mi esetünkre</a>
    </div>

    <div class="art" style="margin-top:2.4rem;">
      <div class="box warn">
        <span class="box-t">A kamatról őszintén</span>
        A babakötvény kamata <b>nem fix</b>: az előző évi átlagos infláció plusz 3 százalékpont, és minden február 1-jén fordul. 2026-ban ez 7,4 százalék. Magas inflációs években ez sokkal több (2024-ben például 20 százalék felett volt), alacsony inflációnál kevesebb. A kalkulátor egyetlen, állandó kamattal számol, tehát a valóság ettől mindkét irányban eltérhet. Amit viszont biztosan tud: <b>az inflációnál mindig 3 százalékponttal többet fizet</b>.
      </div>
    </div>
  </div>
</section>

<!-- ═══ BABAKÖTVÉNY ═══ -->
<section id="babakotveny" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">Részletek</div>
      <h2 class="section-title">A babakötvény pontosan</h2>
      <p class="section-sub">Hivatalos nevén Start-értékpapírszámla. Ez az egyetlen gyermek-megtakarítás, amihez az állam közvetlen támogatást ad.</p>
    </div>
    <div class="art">
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Paraméter</th><th>Érték</th></tr></thead>
          <tbody>
            <tr><td>Állami támogatás</td><td>a befizetések <b>10 százaléka</b>, évente legfeljebb <b>12 000 Ft</b></td></tr>
            <tr><td>Emelt támogatás</td><td><b>20 százalék</b>, max. 24 000 Ft/év — rendszeres gyermekvédelmi kedvezményben részesülő, illetve nevelésbe vett gyermeknél</td></tr>
            <tr><td>Ehhez éves befizetés</td><td>120 000 Ft, vagyis havi 10 000 Ft</td></tr>
            <tr><td>A támogatás jóváírása</td><td>évente egyszer, <b>április 15-én</b>, automatikusan</td></tr>
            <tr class="hl"><td>Kamat</td><td>előző évi átlagos infláció <b>+ 3 százalékpont</b>, február 1-jén fordul. 2026-ban: <b>7,4%</b></td></tr>
            <tr><td>Adózás</td><td>a kamat <b>teljesen adómentes</b>, nincs kamatadó és nincs szocho</td></tr>
            <tr><td>Éves befizetési plafon</td><td><b>1 200 000 Ft</b> gyermekenként, minden befizetőre együttesen</td></tr>
            <tr><td>Ki fér hozzá</td><td><b>kizárólag a gyermek</b>, a 18. életéve betöltése után, és a számlanyitástól legalább 3 évnek el kell telnie</td></tr>
            <tr><td>Halasztás</td><td>a lekötés 19 éves korig meghosszabbítható, a kamatozás közben folytatódik</td></tr>
            <tr><td>Felhasználás</td><td><b>szabadon</b>, nincs célhoz kötés: tanulmány, önerő, autó, bármi</td></tr>
          </tbody>
        </table>
      </div>

      <h3>Miért ez a kiindulópont?</h3>
      <p>Három dolog miatt, és mindhárom ritka egy megtakarításnál. Először is <b>az infláció fölött garantáltan 3 százalékponttal</b> kamatozik, tehát a pénz reálértéke nem tud csökkenni. Másodszor a kamat <b>adómentes</b>. Harmadszor az állam <b>hozzátesz</b> a befizetésedhez, ami sehol máshol nincs így.</p>
      <p>Amit cserébe vállalsz: a pénz 18 éves koráig le van kötve, és nem te fogsz róla dönteni, hanem a gyereked. Ez sokaknak nem előny, hanem hátrány, és ezt érdemes előre végiggondolni.</p>

      <div class="box quote">
        <b>Egy tipikus félreértés:</b> a 10 százalékos állami támogatás nem évi 10 százalék hozam. Egyszeri jóváírás az adott évi befizetésre, és <b>évi 12 000 forintnál megáll</b>. Ha havi 30 000 forintot fizetsz be, a támogatás akkor is 12 000 forint marad. A 12 000 forint feletti rész is gyűlik és kamatozik, csak támogatást már nem hoz rá.
      </div>
    </div>
  </div>
</section>

<!-- ═══ MELYIKET ═══ -->
<section id="melyiket" class="section dark-sec">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">Összehasonlítás</div>
      <h2 class="section-title">Babakötvény, TBSZ vagy valami más?</h2>
      <p class="section-sub">A babakötvény jó alap, de nem mindenre jó. Ez a négy szempont dönt.</p>
    </div>
    <div class="art wide">
      <div class="tiles c2">
        <div class="tile" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">
          <div class="tile-i">🎯</div>
          <div class="tile-t" style="color:#fff;">Mikor kell a pénz?</div>
          <div class="tile-d" style="color:rgba(255,255,255,.66);">Ha <b style="color:#fff">18 éves korára</b>, a babakötvény illeszkedik. Ha korábban, például 14 évesen egy külföldi nyelvtanuláshoz, akkor nem: onnan addig nem lehet kivenni.</div>
        </div>
        <div class="tile" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">
          <div class="tile-i">👤</div>
          <div class="tile-t" style="color:#fff;">Ki döntsön a pénzről?</div>
          <div class="tile-d" style="color:rgba(255,255,255,.66);">A babakötvényen a gyerek dönt 18 évesen, szabadon. Ha ezt <b style="color:#fff">te akarod kontrollálni</b>, akkor a saját nevedre szóló megtakarítás a jobb, amit majd te adsz oda, amikor jónak látod.</div>
        </div>
        <div class="tile" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">
          <div class="tile-i">📊</div>
          <div class="tile-t" style="color:#fff;">Mekkora hozamot vársz?</div>
          <div class="tile-d" style="color:rgba(255,255,255,.66);">A babakötvény infláció fölött 3 százalékpontot ad, kockázat nélkül. Hosszú távon egy <b style="color:#fff">részvényalapú portfólió</b> ennél többet hozhat, de ingadozik, és veszíthet is.</div>
        </div>
        <div class="tile" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">
          <div class="tile-i">💰</div>
          <div class="tile-t" style="color:#fff;">Mennyit tudsz félretenni?</div>
          <div class="tile-d" style="color:rgba(255,255,255,.66);">Havi 10 000 forintig a babakötvény hozza a maximális állami támogatást. <b style="color:#fff">Efölött</b> már érdemes a többletet más formában elhelyezni, mert ott támogatás úgysem jár rá.</div>
        </div>
      </div>

      <div class="box info" style="background:rgba(140,197,189,.1);border-color:rgba(140,197,189,.3);color:rgba(255,255,255,.8);">
        <span class="box-t" style="color:var(--teal-lite);">A legtöbb családnál a jó válasz: mindkettő</span>
        Havi 10 000 forint a babakötvénybe, mert ott van az állami támogatás és az inflációvédelem. Az ezen felüli összeg pedig olyan formába, ahol nagyobb hozam is elérhető, és ahol rugalmasabban hozzá lehet férni, ha közben közbejön valami. Ez a felosztás a legtöbb esetben jobb, mint bármelyik forma önmagában.
      </div>

      <h3 style="margin-top:2rem;">A TBSZ mint kiegészítés</h3>
      <p>A tartós befektetési számla akkor jön szóba, ha a babakötvény plafonja fölött is tudtok félretenni. A logikája egyszerű: a nyitás évében fizetsz be, utána a pénz dolgozik, és az <b>ötödik teljes év után a hozam adómentes</b>.</p>
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Mikor szünteted meg</th><th>Adóteher a hozamon</th></tr></thead>
          <tbody>
            <tr><td>3 éven belül</td><td>15% szja + 13% szocho = <b>28%</b></td></tr>
            <tr><td>3 és 5 év között</td><td>10% szja + 8% szocho = <b>18%</b></td></tr>
            <tr class="hl"><td>5 teljes év után</td><td><b>0%</b>, teljesen adómentes</td></tr>
          </tbody>
        </table>
      </div>
      <p class="tbl-note">A táblázat a 2025. január 1. után nyitott számlákra vonatkozik. A korábban nyitottaknál nincs szocho, csak a 15, illetve 10 százalékos szja. Fontos: <b>a TBSZ-t a legtöbb szolgáltatónál nem lehet közvetlenül kiskorú nevére nyitni</b>, ezért a gyermekcélú TBSZ jellemzően a szülő nevén fut, és 18 éves korban kerül át a gyerekhez. Ez szolgáltatónként eltér, ezért mindig egyedileg kell ellenőrizni.</p>
    </div>
  </div>
</section>

<!-- ═══ INDULÁS ═══ -->
<section id="indulas" class="section" style="background:#fff;">
  <div class="container">
    <div class="art">
      <h2>Hogyan kezdj hozzá?</h2>
      <div class="nsteps">
        <div class="nstep"><div class="nstep-n">1</div><div><div class="nstep-t">Nézd meg, van-e már elkülönített összeg</div><div class="nstep-d">Ha a gyermeked 2005. december 31. után született, jár neki a 42 500 forintos induló támogatás. Ez a Kincstárnál van, és amíg nem nyitsz számlát, nem kamatozik.</div></div></div>
        <div class="nstep"><div class="nstep-n">2</div><div><div class="nstep-t">Döntsd el a célt és az időtávot</div><div class="nstep-d">Egyetemre? Első lakás önerejére? Autóra? Nem mindegy, mert a 18 éves kötöttség az egyiknél előny, a másiknál akadály.</div></div></div>
        <div class="nstep"><div class="nstep-n">3</div><div><div class="nstep-t">Nyiss Start-számlát és vezettesd át az induló összeget</div><div class="nstep-d">A Kincstárnál vagy szerződött szolgáltatónál intézhető. Az átvezetéssel a 42 500 forint is elkezd inflációkövető kamatot fizetni.</div></div></div>
        <div class="nstep"><div class="nstep-n">4</div><div><div class="nstep-t">Állíts be állandó átutalást</div><div class="nstep-d">Havi rendszerességgel, hogy az éves 120 000 forint összejöjjön. Az állami támogatás a ténylegesen befizetett összeg alapján jár, tehát a decemberi pótlás is számít.</div></div></div>
        <div class="nstep"><div class="nstep-n">5</div><div><div class="nstep-t">A plafon fölötti részt tedd máshová</div><div class="nstep-d">Ha havi 10 000 forintnál többet tudtok félretenni, a többletre már nem jár támogatás. Ott érdemes megnézni, mi hozhat többet.</div></div></div>
      </div>
      <div class="box info">
        <span class="box-t">Nagyszülők, keresztszülők</span>
        A babakötvényre <b>bárki befizethet</b>, nem csak a szülő. Az éves 1,2 millió forintos plafon minden befizetőre együttesen vonatkozik. Sok családnál ez jobb ajándék, mint a sokadik játék: születésnapra és karácsonyra is működik, és 18 év alatt komoly összeggé áll össze.
      </div>
    </div>
  </div>
</section>

<!-- ═══ HIBÁK ═══ -->
<section id="hibak" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">Amire figyelj</div>
      <h2 class="section-title">Hat hiba, amit érdemes elkerülni</h2>
    </div>
    <div class="art wide">
      <div class="tiles c2">
        <div class="tile"><div class="tile-i">😶</div><div class="tile-t">Az induló összeg ottfelejtése</div><div class="tile-d">A 42 500 forint <b>kamat nélkül áll</b>, amíg nem nyitsz Start-számlát. 18 év alatt ez önmagában komoly veszteség.</div></div>
        <div class="tile"><div class="tile-i">📉</div><div class="tile-t">A támogatási keret kihagyása</div><div class="tile-d">Aki havi 5 000 forintot fizet be, évi 6 000 forint támogatást kap 12 000 helyett. <b>18 év alatt ez több mint 100 000 forint</b> elmaradt támogatás.</div></div>
        <div class="tile"><div class="tile-i">🏦</div><div class="tile-t">Minden egy helyre</div><div class="tile-d">A támogatási plafon fölött a babakötvény már nem különleges. A többletet <b>érdemes máshová</b> tenni, ahol nagyobb hozam is elérhető.</div></div>
        <div class="tile"><div class="tile-i">🎁</div><div class="tile-t">A folyószámlán gyűjtés</div><div class="tile-d">Sok családnál a gyereknek szánt pénz a szülő folyószámláján ül. Ott <b>az infláció évről évre eszi</b>, és könnyen el is költik.</div></div>
        <div class="tile"><div class="tile-i">⏰</div><div class="tile-t">A várakozás a „jobb pillanatra"</div><div class="tile-d">Nincs jobb pillanat. Egy 18 éves időtávon a <b>kezdés dátuma</b> többet számít, mint a havi összeg nagysága.</div></div>
        <div class="tile"><div class="tile-i">🤐</div><div class="tile-t">A gyerek kihagyása</div><div class="tile-d">18 évesen ő fog dönteni a pénzről. Ha addigra <b>nem beszéltetek róla</b>, nagyobb az esély, hogy egy hét alatt elmegy.</div></div>
      </div>
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
      <a class="rel-c" href="tamogatasok.html"><div class="rel-i">💰</div><div><div class="rel-t">Állami támogatások</div><div class="rel-d">CSOK Plusz, Babaváró, Otthon Start</div></div></a>
      <a class="rel-c" href="befektetesek.html"><div class="rel-i">📈</div><div><div class="rel-t">Befektetések</div><div class="rel-d">TBSZ és alapok, adóhatékonyan</div></div></a>
      <a class="rel-c" href="nyugdij.html"><div class="rel-i">🌅</div><div><div class="rel-t">Nyugdíj-megtakarítás</div><div class="rel-d">20% adó-visszatérítéssel</div></div></a>
    </div>
  </div>
</section>
'''

FAQ = [
("Mikor érdemes elkezdeni?",
 ["Amint megvan az adóazonosító jel, tehát gyakorlatilag a születés után pár héttel. Nem azért, mert sürget valami, hanem mert a 18 éves időtávból minden elvesztett év sokat számít.",
  "Ha a gyereked már nagyobb, attól még van értelme: nyolc- vagy tízéves időtávon is érdemben gyűlik a pénz, csak nagyobb havi összeggel jön ki ugyanaz a végeredmény."]),

("Tényleg csak a gyerek férhet hozzá?",
 ["Igen, és ez a babakötvény legfontosabb tulajdonsága. A pénzhez <b>kizárólag a gyermek juthat hozzá, a 18. életéve betöltése után</b>, és a számlanyitástól is el kell telnie legalább három évnek.",
  "Szülőként te nem tudod feltörni, még vészhelyzetben sem. Ezért fontos, hogy csak olyan összeget tegyél bele, amire biztosan nem lesz szükségetek közben."]),

("Mi történik, ha a gyerek 18 évesen rosszul költi el?",
 ["Jogilag semmi: a pénz az övé, szabadon felhasználható. Ez a konstrukció valódi kockázata, és nem lehet szerződéssel kivédeni.",
  "Amit tehetsz: időben beszélni róla. A 16-17 éves korban elkezdett beszélgetés arról, hogy mire lehetne használni, többet ér, mint bármilyen jogi korlát. És ha ez a kockázat számodra vállalhatatlan, akkor a saját nevedre szóló megtakarítás a jobb megoldás, még ha állami támogatás nem is jár rá."]),

("Befizethetnek a nagyszülők is?",
 ["Igen, bárki befizethet a gyermek Start-számlájára. Az állami támogatás a <b>befizetések összegére</b> jár, nem személyenként, és az éves 1,2 millió forintos plafon is minden befizetőre együttesen vonatkozik.",
  "A gyakorlatban ez azt jelenti, hogy egy nagyszülői születésnapi befizetés ugyanúgy hozza a 10 százalékot, mint a szülői állandó átutalás."]),

("Mi a különbség a babakötvény és a Start-számla között?",
 ["Gyakorlatilag ugyanazt jelenti a két szó. A Start-értékpapírszámla a hivatalos elnevezés, a babakötvény pedig az a speciális állampapír, amit ezen a számlán tartanak. A köznyelv a kettőt felváltva használja.",
  "A lényeg, hogy a számla nyitása nélkül az induló 42 500 forint nem kamatozik, tehát a számlanyitás az első érdemi lépés."]),

("Elveszik a támogatás, ha egy évben nem fizetünk be?",
 ["Nem, csak arra az évre nem jár. A számla megmarad, a már benne lévő pénz tovább kamatozik, és a következő évben ott folytathatjátok, ahol abbahagytátok.",
  "Nincs szankció és nincs minimális befizetési kötelezettség. Ez az egyik oka annak, hogy a babakötvény jól viseli a hullámzó jövedelmet."]),

("Nyithatok TBSZ-t a gyerekem nevére?",
 ["A legtöbb szolgáltatónál nem közvetlenül. A gyakorlatban a gyermekcélú TBSZ <b>a szülő nevén fut</b>, a szülő kezeli, és 18 éves korban kerül át a gyerekhez ajándékozással vagy átutalással.",
  "Ez szolgáltatónként eltér, és kiskorú vagyonával való rendelkezéshez gyámhatósági jóváhagyás is kellhet. Konkrét banknál vagy brókernél mindig egyedileg kell ellenőrizni."]),

("Mennyivel jobb ez, mint a bankbetét?",
 ["Két dologban. Egyrészt a babakötvény <b>kamata az inflációt követi plusz 3 százalékpont</b>, tehát reálértéken nem tud veszíteni, míg egy lekötött betét magas infláció idején simán veszít. Másrészt a betét kamata adóköteles, a babakötvényé nem.",
  "Harmadikként pedig a betétre nincs állami támogatás. A három együtt 18 éves távon nagyon nagy különbséget ad."]),
]

def faq_html(items):
    out = []
    for q, ps in items:
        body = ''.join('<p>%s</p>' % p for p in ps)
        out.append('<details class="faq-item"><summary class="faq-q">%s'
                   '<svg class="faq-chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                   'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>'
                   '</summary><div class="faq-a">%s</div></details>' % (q, body))
    return '\n      '.join(out)

BODY = BODY.replace('__FAQ__', faq_html(FAQ))

JS = u'''
(function(){
/* ══ GYERMEK-MEGTAKARÍTÁS — karbantartás: csak a BK blokk ══ */
var BK = {
  tamogatasPct: 10,        /* állami támogatás a befizetésre, %      */
  tamogatasMax: 12000,     /* éves maximum, Ft                        */
  indulo:       42500,     /* induló életkezdési támogatás, Ft        */
  kamat2026:    7.4        /* a babakötvény kamata 2026-ban, %        */
};

function el(id){ return document.getElementById(id); }
function huf(v){ return Math.round(v).toLocaleString('hu-HU') + ' Ft'; }
function pc(v){ return (+v).toFixed(1).replace('.',',') + '%'; }
function paint(e){ e.style.setProperty('--p', (e.value-e.min)/(e.max-e.min)*100 + '%'); }

var forma = 'bk';

function calc(){
  var m = +el('g_havi').value, kor = +el('g_kor').value, r = +el('g_kamat').value/100;
  var ev = 18 - kor;
  var mr = r/12, n = ev*12;

  /* havi befizetések jövőértéke, hó eleji befizetéssel */
  var fvBef = mr === 0 ? m*n : m*((Math.pow(1+mr,n)-1)/mr)*(1+mr);

  var evi = 0, fvTam = 0, induloFv = 0;
  if(forma === 'bk'){
    evi = Math.min(m*12*BK.tamogatasPct/100, BK.tamogatasMax);
    var yr = Math.pow(1+mr,12)-1;
    fvTam = yr === 0 ? evi*ev : evi*((Math.pow(1+yr,ev)-1)/yr);
    if(kor === 0) induloFv = BK.indulo*Math.pow(1+r,ev);
  }

  var bef = m*12*ev, allam = evi*ev + (kor === 0 && forma === 'bk' ? BK.indulo : 0);
  var veg = fvBef + fvTam + induloFv;

  el('g_big').textContent  = huf(veg);
  el('g_sub').textContent  = huf(m) + ' / hó · ' + ev + ' éven át · ' +
                             (forma === 'bk' ? 'babakötvény' : 'egyéb megtakarítás');
  el('g_bef').textContent  = huf(bef);
  el('g_allam').textContent = allam > 0 ? '+' + huf(allam) : '—';
  el('g_kam').textContent  = '+' + huf(Math.max(0, veg - bef - allam));
  el('g_evi').textContent  = forma === 'bk' ? huf(evi) : 'nem jár';
  el('g_ev').textContent   = ev + ' év';

  var w = el('g_warn');
  if(forma !== 'bk'){
    w.className = 'sc-warn';
    w.innerHTML = 'Ezen a formán <b>nincs állami támogatás</b>, és a hozam sem garantált. Cserébe rugalmasabb: nincs 18 éves kötöttség, és te döntesz a felhasználásról. A babakötvény melletti kiegészítésnek jellemzően ez a jó helye.';
  } else if(m*12*BK.tamogatasPct/100 > BK.tamogatasMax + 1){
    w.className = 'sc-warn';
    w.innerHTML = 'Az állami támogatás <b>évi ' + huf(BK.tamogatasMax) + '</b>-nál megáll. Havi ' +
      huf(BK.tamogatasMax/(BK.tamogatasPct/100)/12) + ' fölött a többletre már nem jár. Az e fölötti részt érdemes olyan formába tenni, ahol nagyobb hozam is elérhető.';
  } else if(m*12*BK.tamogatasPct/100 < BK.tamogatasMax - 1){
    var kell = BK.tamogatasMax/(BK.tamogatasPct/100)/12 - m;
    w.className = 'sc-warn';
    w.innerHTML = 'Havi <b>' + huf(kell) + '</b> további befizetésig még nő az állami támogatás. Ez ' + ev +
      ' év alatt összesen <b>' + huf((BK.tamogatasMax - m*12*BK.tamogatasPct/100)*ev) + '</b> elmaradó támogatás.';
  } else {
    w.className = 'sc-warn ok';
    w.innerHTML = 'Pontosan kihasználjátok a keretet: <b>' + huf(BK.tamogatasMax) + '</b> állami támogatás jár évente. Ez a maximum.';
  }

  el('g_kamat_note').innerHTML = forma === 'bk'
    ? 'A babakötvény kamata az előző évi átlagos infláció + 3 százalékpont, 2026-ban <b>' + pc(BK.kamat2026) + '</b>. A csúszkával óvatosabb és derűlátóbb forgatókönyvet is megnézhetsz.'
    : 'Egyéb megtakarításnál a hozam <b>nem garantált</b>, és a választott eszköztől függ. Óvatosabb forgatókönyvre is állítsd be.';
}

['g_havi','g_kor','g_kamat'].forEach(function(id){
  var r = el(id), v = el(id+'_v');
  var fmt = { g_havi:function(x){return huf(x)+' / hó';},
              g_kor:function(x){return x === 0 ? 'újszülött' : x+' éves';},
              g_kamat:pc }[id];
  function show(){ paint(r); v.textContent = fmt(+r.value); calc(); }
  r.addEventListener('input', show); show();
});

document.querySelectorAll('#gy .sc-seg button').forEach(function(b){
  b.addEventListener('click', function(){
    document.querySelectorAll('#gy .sc-seg button').forEach(function(x){ x.classList.remove('on'); });
    b.classList.add('on'); forma = b.dataset.f;
    if(forma === 'bk'){ el('g_kamat').value = BK.kamat2026; paint(el('g_kamat'));
                        el('g_kamat_v').textContent = pc(BK.kamat2026); }
    calc();
  });
});
})();
'''

LEGAL = (u'<b>*</b> Az oldalon szereplő adatok tájékoztató jellegűek, nem minősülnek befektetési tanácsadásnak, ajánlattételnek vagy adótanácsadásnak. '
         u'A kalkulátor egyszerűsített modellel dolgozik: a havi befizetéseket a hónap elején, az állami támogatást évente egy összegben veszi figyelembe, '
         u'és a teljes futamidőre egyetlen, állandó kamattal számol. A babakötvény kamata ezzel szemben <b>évente változik</b>: az előző évi átlagos '
         u'fogyasztóiár-index és 3 százalékpont kamatprémium összege, amely minden év február 1-jén fordul; a 2026-os 7,4 százalékos érték a 2025-ös '
         u'átlagos infláción alapul. A tényleges végösszeg ezért a kalkulátor eredményétől mindkét irányban eltérhet. Az „egyéb megtakarítás" módban '
         u'megadott hozam nem garantált, és negatív is lehet. Az állami támogatás mértéke (a befizetések 10 százaléka, évente legfeljebb 12 000 Ft, '
         u'emelt esetben 20 százalék és 24 000 Ft), az induló életkezdési támogatás (42 500 Ft), az éves befizetési plafon (1 200 000 Ft gyermekenként) '
         u'és a hozzáférés feltételei (a 18. életév betöltése és a számlanyitástól számított legalább 3 év) a 2026. szeptemberi jogszabályi állapotot '
         u'tükrözik; a mindenkori hatályos szabályozás az irányadó. A tartós befektetési számla adókulcsai a 2025. január 1. után nyitott számlákra '
         u'vonatkoznak. Adatok érvényessége: <b data-upd></b>.')

build('gyermekjovo.html',
      u'Gyermek-megtakarítás 2026: babakötvény, Start-számla, TBSZ | EAGLZ Finance',
      u'Mennyit ad az állam a babakötvényhez, mennyi gyűlik össze 18 éves korára, és mikor jobb a TBSZ? Kalkulátorral és 2026-os adatokkal.',
      BODY, LEGAL,
      u'Nézzük meg, mi illik a ti helyzetetekhez.',
      u'Egy díjmentes beszélgetésen végigvesszük a célt, az időtávot és a havi keretet, és kiszámoljuk, hogyan érdemes felosztani a babakötvény és más formák között.',
      JS)
