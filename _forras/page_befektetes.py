# -*- coding: utf-8 -*-
from build_sub import build, LEGAL_WRAP

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
    <h1 class="sub-h1">Befektetés: <em>a hozamod fele adón és költségen múlik</em></h1>
    <p class="sub-lead">A legtöbb ember a hozamot próbálja maximalizálni, pedig ugyanazon az eszközön két ember végeredménye 20-30 százalékkal is eltérhet attól függően, hogy milyen számlán tartja és mennyi költséget fizet rá. Ez az oldal erről a két dologról szól, mert ezt a kettőt tudod valóban befolyásolni.</p>
    <div class="sub-chips">
      <div class="sub-chip">📊 TBSZ 5 év után: <b>0% adó</b></div>
      <div class="sub-chip">⚠️ TBSZ nélkül: <b>15% + 13%</b></div>
      <div class="sub-chip">📅 Adatok: <b data-upd></b></div>
    </div>
    <div class="quicknav">
      <a href="#tbsz" class="qn on">📊 TBSZ</a>
      <a href="#kalk" class="qn">🧮 Kalkulátor</a>
      <a href="#alapok" class="qn">📈 Alapok</a>
      <a href="index.html#advisors" class="qn">📅 Időpontot foglalok</a>
    </div>
  </div>
</section>

<section class="section" style="background:#fff;padding-bottom:2.4rem;">
  <div class="container">
    <div class="toc">
      <div class="toc-t">Ezen az oldalon</div>
      <ol>
        <li><a href="#cel">Négy kérdés a termék előtt</a></li>
        <li><a href="#terkep">Befektetési térkép</a></li>
        <li><a href="#tbsz">TBSZ: a legolcsóbb adóoptimalizálás</a></li>
        <li><a href="#kalk">Kalkulátor: mennyit visz el az adó?</a></li>
        <li><a href="#alapok">Befektetési alapok és költségeik</a></li>
        <li><a href="#kockazat">Kockázat, időtáv, diverzifikáció</a></li>
        <li><a href="#hibak">Öt hiba, ami sokba kerül</a></li>
        <li><a href="#gyik">Gyakori kérdések</a></li>
      </ol>
    </div>
    <div class="art">
      <h2>Nem a termék az első döntés</h2>
      <p class="lead">A befektetési beszélgetések nagy része rossz helyen kezdődik: <b>„mibe tegyem?”</b> Ez a kérdés sorrendben a negyedik. Előtte három másik dönti el, hogy egyáltalán melyik termékcsalád jöhet szóba, és ha ezeket átugrod, jó eséllyel olyasmibe kerül a pénzed, amiből pont akkor nem tudsz kiszállni, amikor kellene.</p>
      <p>Az alábbi négy kérdést szoktuk végigvenni. A válaszokból többnyire magától adódik a megoldás, és jellemzően kiderül az is, hogy nem egy termék kell, hanem kettő-három, különböző időtávra.</p>
    </div>
  </div>
</section>

<!-- ═══ CÉL ═══ -->
<section id="cel" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">Alapozás</div>
      <h2 class="section-title">Négy kérdés, ami eldönti a termékkört</h2>
      <p class="section-sub">Ezek nélkül minden termékajánlás vaktában lövés. Érdemes végiggondolnod őket, mielőtt bárkivel leülsz, minket is beleértve.</p>
    </div>
    <div class="art">
      <div class="nsteps">
        <div class="nstep"><div class="nstep-n">1</div><div><div class="nstep-t">Mire gyűjtesz, és mikor kell a pénz?</div><div class="nstep-d">Egy három év múlva esedékes önerő és egy huszonöt év múlva esedékes nyugdíj két teljesen különböző eszköz. A rövid táv nem tűri az árfolyamkockázatot, mert nem tudod kivárni a visszaesést. A hosszú táv viszont nem tűri a túlzott óvatosságot, mert ott az infláció a valódi ellenfél. <b>Ökölszabály:</b> öt éven belüli célra nem megy részvénytúlsúlyos portfólió, tíz éven túli célra pedig nem megy tisztán pénzpiaci.</div></div></div>
        <div class="nstep"><div class="nstep-n">2</div><div><div class="nstep-t">Van már vésztartalékod?</div><div class="nstep-d">Három-hat havi kiadásnyi, azonnal hozzáférhető pénz. Amíg ez nincs meg, minden hosszú távú megtakarítás veszélyben van, mert az első komolyabb váratlan kiadásnál azt kell feltörnöd, méghozzá a lehető legrosszabb pillanatban. <b>A vésztartalék nem befektetés:</b> nem az a dolga, hogy hozzon, hanem az, hogy holnap ott legyen.</div></div></div>
        <div class="nstep"><div class="nstep-n">3</div><div><div class="nstep-t">Mekkora esést viselsz el anélkül, hogy pánikban eladnád?</div><div class="nstep-d">Nem elméletben, hanem a saját pénzeden. Aki azt mondja, elviseli a 30 százalékos esést, de az első mínusz 8 százaléknál felhív, hogy szálljunk ki, az a valóságban óvatos befektető. Ez nem baj, csak <b>tudni kell róla előre</b>, mert a rossz pillanatban való kiszállás többe kerül, mint bármelyik díj. A kockázattűrésedet a szolgáltatók kötelező alkalmassági tesztje is felméri: érdemes komolyan kitölteni, nem átkattintani rajta.</div></div></div>
        <div class="nstep"><div class="nstep-n">4</div><div><div class="nstep-t">Mennyire kell hozzáférned menet közben?</div><div class="nstep-d">Ez dönti el, jöhet-e egyáltalán olyan konstrukció, ami lekötéshez vagy minimális tartási időhöz köti az adókedvezményt. A TBSZ, a nyugdíjcélú termékek és a hosszú távú életbiztosítások mind adnak valamit, de mind kérnek is cserébe: <b>időt</b>. Ha jó eséllyel hozzá kell nyúlnod, ne az adókedvezményes formát válaszd, mert a feltörés büntetése többnyire elviszi az egész nyereséget.</div></div></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ TÉRKÉP ═══ -->
<section id="terkep" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">Áttekintés</div>
      <h2 class="section-title">Befektetési térkép: mi hova való</h2>
      <p class="section-sub">Nem rangsor, hanem szereposztás. A legtöbb jól működő portfólióban ezekből több is szerepel, különböző célra és időtávra.</p>
    </div>
    <div class="art">
      <div class="tiles">
        <div class="tile"><div class="tile-i">🏦</div><div class="tile-t">Bankbetét, pénzpiac</div><div class="tile-d">Vésztartalékra és nagyon rövid célra. Kiszámítható, azonnal elérhető, viszont a hozama jellemzően az infláció közelében mozog, és 2023 júliusa óta a kamatát szociális hozzájárulási adó is terheli. <b>Időtáv: 0-2 év.</b></div></div>
        <div class="tile"><div class="tile-i">📈</div><div class="tile-t">Befektetési alapok</div><div class="tile-d">A leggyakoribb belépő. Egy jegyen keresztül szórod szét a pénzt sok értékpapír között, professzionális kezeléssel. A választék óriási, a különbséget a kockázat és a költség adja. <b>Időtáv: 2-15+ év.</b></div></div>
        <div class="tile"><div class="tile-i">📊</div><div class="tile-t">Tőzsdei eszközök, ETF</div><div class="tile-d">Részvény, ETF, kötvény közvetlenül, értékpapírszámlán. A legátláthatóbb költségszerkezet, cserébe neked kell portfóliót építeni és fegyelmezetten tartani. <b>Időtáv: 5-20+ év.</b></div></div>
        <div class="tile"><div class="tile-i">🛡️</div><div class="tile-t">Unit-linked életbiztosítás</div><div class="tile-d">Befektetés biztosítási köntösben, eszközalapokkal. Rendszeres megtakarításra épült, kockázati fedezettel kombinálható. A költségszerkezete a legösszetettebb, ezért itt a legfontosabb a <b>TKM</b> megnézése. <b>Időtáv: 10-20 év.</b></div></div>
        <div class="tile"><div class="tile-i">👴</div><div class="tile-t">Nyugdíjcélú megtakarítás</div><div class="tile-d">Nyugdíjbiztosítás, önkéntes pénztár, NYESZ. A 20 százalékos adó-visszatérítés miatt hosszú távon nehéz felülmúlni, cserébe a pénz a nyugdíjkorhatárig be van zárva. <b><a href="nyugdij.html">Nyugdíj oldal →</a></b></div></div>
        <div class="tile"><div class="tile-i">👶</div><div class="tile-t">Gyermek megtakarítás</div><div class="tile-d">Babakötvény, gyermek-életbiztosítás, gyűjtőszámla. Itt az időtáv adott, és többnyire állami támogatás is kapcsolódik hozzá, ezért a korai indulásnak aránytalanul nagy hatása van. <b><a href="gyermekjovo.html">Gyermek oldal →</a></b></div></div>
      </div>

      <div class="box info">
        <span class="box-t">Amit nem közvetítünk</span>
        Állampapírt nem közvetítünk, ezért erről nem is adunk terméktanácsot. Ha ez érdekel, a Magyar Államkincstárnál vagy a saját bankodnál tudod megvásárolni, közvetítő nélkül. Attól még beszélgetünk róla, ha a portfóliód összképéhez hozzátartozik, csak nem mi adjuk el.
      </div>
    </div>
  </div>
</section>

<!-- ═══ TBSZ ═══ -->
<section id="tbsz" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">Adózás</div>
      <h2 class="section-title">TBSZ: a legolcsóbb dolog, amit a hozamodért tehetsz</h2>
      <p class="section-sub">A tartós befektetési számla nem termék, hanem egy számlatípus, amire a befektetéseidet ráteheted. Nem kerül külön pénzbe, és öt év után nullára viszi a hozamadót.</p>
    </div>

    <div class="art">
      <h2>Hogyan működik</h2>
      <p class="lead">A TBSZ-t egy banknál vagy befektetési szolgáltatónál nyitod. A megnyitás naptári éve a <b>gyűjtőév</b>: ebben az évben tehetsz rá pénzt, akárhányszor. A gyűjtőév végén a számla lezárul a befizetések elől, és elindul az óra. A minimálisan elhelyezendő összeg jellemzően 25 000 forint.</p>
      <p>Utána már csak várni kell. A számlán belül szabadon kereskedhetsz, átrendezheted a portfóliót, eladhatsz és vehetsz, ezek egyike sem adóztatható esemény. Az adót akkor nézik meg, amikor a pénzt kiveszed, és ekkor az számít, hány év telt el a gyűjtőév vége óta.</p>

      <h2>Mennyi adót fizetsz, ha kiveszed</h2>
      <p>Itt van a lényeg, és itt van egy fontos változás is: a <b>2025. január 1-jétől nyitott</b> számlák idő előtti feltörése drágább, mint a korábbiaké, mert a szociális hozzájárulási adó is rárakódik.</p>

      <div class="tbl-wrap">
        <table class="tbl">
          <thead>
            <tr><th>Mikor veszed ki</th><th>2025-től nyitott TBSZ</th><th>2025 előtt nyitott TBSZ</th></tr>
          </thead>
          <tbody>
            <tr><td>A gyűjtőévet követő <b>3 éven belül</b></td><td><b>15% szja + 13% szocho</b> (összesen 28%)</td><td><b>15% szja</b>, szocho nélkül</td></tr>
            <tr><td><b>3 és 5 év között</b></td><td><b>10% szja + 8% szocho</b> (összesen 18%)</td><td><b>10% szja</b>, szocho nélkül</td></tr>
            <tr class="hl"><td><b>5 év után, a lekötés végén</b></td><td><b>0%</b>: se szja, se szocho</td><td><b>0%</b></td></tr>
          </tbody>
        </table>
        <div class="tbl-note">A táblázat a hozamra vonatkozó adókulcsokat mutatja. A befizetett tőkéd után nincs adó, azt már egyszer leadóztad.</div>
      </div>

      <div class="box info">
        <span class="box-t">Mihez képest 0 százalék</span>
        TBSZ nélkül ugyanez a hozam jellemzően <b>15 százalék szja plusz 13 százalék szocho</b>, vagyis összesen 28 százalék, ha kamatjövedelemnek minősül. Ha ellenőrzött tőkepiaci ügyletként adózik, akkor 15 százalék, szocho nélkül. Az öt évet kivárt TBSZ mindkettőnél olcsóbb: nulla.
      </div>

      <h2>Amit érdemes tudni még róla</h2>
      <ul class="clean">
        <li><b>Évente nyithatsz újat.</b> Nem kell egyetlen számlára gyűjteni. Sokan minden januárban nyitnak egy újat, így minden évben lejár egy, és mindig van szabadon felhasználható, adómentes pénz.</li>
        <li><b>Az ötödik év után meghosszabbítható.</b> Ha nem kell a pénz, a lekötés folytatható, és az adómentesség megmarad.</li>
        <li><b>Nem termékfüggő.</b> Részvény, ETF, befektetési jegy, kötvény: sokféle eszköz tartható rajta, attól függően, mit kínál az adott szolgáltató.</li>
        <li><b>Átvihető másik szolgáltatóhoz.</b> Ha a jogszabály szerinti számlaátvezetéssel történik, az nem minősül feltörésnek, tehát nem veszíted el az eltelt időt. Ezt előre egyeztetni kell mindkét szolgáltatóval.</li>
      </ul>

      <div class="box warn">
        <span class="box-t">A leggyakoribb tévhit</span>
        Hogy a TBSZ önmagában hoz valamit. Nem hoz. A TBSZ egy adóburok: a hozamot továbbra is az adja, amit beleteszel. Rossz eszközzel a TBSZ-en is lehet veszíteni, csak akkor nincs mitől adót fizetni.
      </div>
    </div>
  </div>
</section>

<!-- ═══ KALKULÁTOR ═══ -->
<section id="kalk" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">Kalkulátor</div>
      <h2 class="section-title">Mennyit visz el az adó és a költség?</h2>
      <p class="section-sub">Állítsd be a havi összeget, az időtávot, a várt hozamot és a termék éves költséghányadát. A kalkulátor megmutatja, mennyi marad nálad TBSZ-en és anélkül.</p>
    </div>

    <div class="sc" id="bf">
      <div class="sc-in">
        <div class="sc-seg" role="group" aria-label="Számlatípus">
          <button type="button" class="on" data-mode="tbsz">TBSZ-en tartom</button>
          <button type="button" data-mode="ado">Sima számlán</button>
        </div>
        <div class="scf">
          <label class="scf-top" for="b_havi">Havi megtakarítás<b id="b_havi_v"></b></label>
          <input type="range" id="b_havi" min="5000" max="300000" step="5000" value="50000">
          <span class="scf-note">A TBSZ-re a gyűjtőévben bármikor tehetsz pénzt. A kalkulátor az egyszerűség kedvéért egyenletes havi befizetéssel számol.</span>
        </div>
        <div class="scf">
          <label class="scf-top" for="b_ev">Meddig tartod<b id="b_ev_v"></b></label>
          <input type="range" id="b_ev" min="1" max="25" step="1" value="10">
          <span class="scf-note">A TBSZ adómentességéhez a gyűjtőév után öt teljes évnek kell eltelnie. Állítsd öt alá, hogy lásd, mennyibe kerül a korai feltörés.</span>
        </div>
        <div class="scf">
          <label class="scf-top" for="b_hozam">Tájékoztató éves hozam<b id="b_hozam_v"></b></label>
          <input type="range" id="b_hozam" min="0" max="12" step="0.5" value="6">
          <span class="scf-note">A hozam nem garantált, évről évre eltér, és negatív is lehet. Óvatosabb forgatókönyvre is állítsd be.</span>
        </div>
        <div class="scf">
          <label class="scf-top" for="b_ktg">Éves költséghányad<b id="b_ktg_v"></b></label>
          <input type="range" id="b_ktg" min="0" max="4" step="0.1" value="1.2">
          <span class="scf-note">A kezelt vagyonra vetített teljes éves költség. Alapoknál ez az alapkezelési és letétkezelési díj, biztosításnál a TKM adja meg a nagyságrendjét.</span>
        </div>
      </div>
      <div class="sc-out">
        <div class="sc-hero">
          <div class="sc-hero-l">Ennyi marad nálad adózás után</div>
          <div class="sc-hero-n" id="b_big"></div>
          <div class="sc-hero-s" id="b_sub"></div>
        </div>
        <div class="sc-rows">
          <div><span>Amit befizetsz összesen</span><b id="b_bef"></b></div>
          <div><span>Hozam a költségek levonása után</span><b id="b_hoz"></b></div>
          <div><span>Hozamadó</span><b id="b_ado"></b></div>
          <div><span>Költségek összesen</span><b id="b_kts"></b></div>
          <div class="hl"><span id="b_dl">Különbség a másik változathoz</span><b id="b_diff"></b></div>
        </div>
        <div class="sc-warn" id="b_warn"></div>
      </div>
    </div>
    <div class="sc-actions">
      <a href="index.html#advisors" class="apt-btn-inner" style="padding:.85rem 1.8rem;">📅 Nézzük meg az én esetemre</a>
    </div>

    <div class="art" style="margin-top:2.4rem;">
      <div class="box warn">
        <span class="box-t">Amit a kalkulátor nem tud</span>
        Nem ismeri a konkrét eszközöd adójogi besorolását. A kamatjövedelem és az ellenőrzött tőkepiaci ügylet másképp adózik, és van néhány kivétel is, ahol nincs szocho. A modell azt mutatja meg, mekkora nagyságrendű a különbség a TBSZ javára, nem azt, hogy a te konkrét portfóliódon forintra mennyi adó keletkezik. Ez utóbbit adótanácsadóval vagy a számlavezetőddel érdemes tisztázni.
      </div>
    </div>
  </div>
</section>

<!-- ═══ ALAPOK ═══ -->
<section id="alapok" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">Termékek</div>
      <h2 class="section-title">Befektetési alapok: mit veszel valójában</h2>
      <p class="section-sub">Egy befektetési jegy egy közös kosárból vásárolt részesedés. Az alapkezelő megveszi az értékpapírokat, te pedig a kosár értékének egy darabját birtoklod.</p>
    </div>

    <div class="art">
      <h2>Az alaptípusok kockázat szerint</h2>
      <p>A nevek szolgáltatónként eltérnek, a logika viszont ugyanaz: minél több benne a részvény, annál nagyobb a hosszú távú várható hozam és annál nagyobb a menet közbeni ingadozás.</p>

      <div class="tbl-wrap">
        <table class="tbl">
          <thead>
            <tr><th>Típus</th><th>Mi van benne</th><th>Ajánlott időtáv</th><th>Jellemző ingadozás</th></tr>
          </thead>
          <tbody>
            <tr><td>Pénzpiaci</td><td>Rövid lejáratú betétek, diszkontpapírok</td><td>0-1 év</td><td>Minimális</td></tr>
            <tr><td>Kötvényalap</td><td>Állami és vállalati kötvények</td><td>2-4 év</td><td>Alacsony, de nem nulla</td></tr>
            <tr><td>Vegyes alap</td><td>Kötvény és részvény keverve</td><td>4-7 év</td><td>Közepes</td></tr>
            <tr><td>Részvényalap</td><td>Tőzsdei részvények</td><td>8-15+ év</td><td>Magas, két számjegyű esések is</td></tr>
            <tr><td>Ingatlanalap</td><td>Bérbe adott ingatlanok</td><td>5-10 év</td><td>Alacsonynak látszik, de illikvid</td></tr>
            <tr><td>Abszolút hozamú</td><td>Az alapkezelő szabadon dönt</td><td>3-5 év</td><td>Változó, kezelőfüggő</td></tr>
          </tbody>
        </table>
        <div class="tbl-note">Az ajánlott időtáv a termék kockázati profiljából adódó tájékoztató érték, nem kötelező tartási idő.</div>
      </div>

      <div class="box warn">
        <span class="box-t">Az ingatlanalapok csapdája</span>
        Az ingatlanalapok árfolyama simának látszik, mert az ingatlanokat nem naponta árazzák. Ettől még nem kockázatmentesek: a valódi kockázatuk a <b>likviditás</b>. Nagy visszaváltási hullám esetén a kifizetésre hosszabb, akár többhónapos várakozási idő is beépíthető, mert az alap nem tud egy hét alatt irodaházat eladni. Ha gyors hozzáférhetőség kell, ez nem az a termék.
      </div>

      <h2>A költség, ami elviszi a hozam egy részét</h2>
      <p>Alapoknál három költségtípussal találkozol. Ezek kis számoknak látszanak, de évtizedes távon összeadódnak, és a különbség jelentős.</p>
      <ul class="clean">
        <li><b>Alapkezelési díj</b>: évente, a kezelt vagyon százalékában. Ezt az árfolyamból automatikusan levonják, nem külön terheléssel, ezért sokan észre sem veszik.</li>
        <li><b>Vételi vagy visszaváltási jutalék</b>: egyszeri, a tranzakcióra. Sok alapnál nincs, de van, ahol rövid tartás esetén büntetőjelleggel megjelenik.</li>
        <li><b>Számlavezetési és letétkezelési díj</b>: a szolgáltatónál, az egész portfóliódra. Kis összegeknél ez arányaiban sokat nyom.</li>
      </ul>

      <div class="kpis">
        <div class="kpi"><b>~0,4%</b><span>passzív, indexkövető megoldások jellemző éves költsége</span></div>
        <div class="kpi"><b>1-2%</b><span>aktívan kezelt részvényalapok jellemző éves költsége</span></div>
        <div class="kpi"><b>1,5 pont</b><span>ekkora éves költségkülönbség 20 év alatt a végérték negyedét is elviheti</span></div>
        <div class="kpi"><b>0 Ft</b><span>ennyibe kerül megnézni a költséghányadot szerződés előtt</span></div>
      </div>

      <div class="box quote">
        Az alapok múltbeli hozamát mindenhol kiteszik, mert azt könnyű eladni. A költséghányadot már kevésbé. Pedig a jövőbeli hozamot nem ismeri senki, a költséget viszont pontosan tudod előre.
      </div>
    </div>
  </div>
</section>

<!-- ═══ KOCKÁZAT ═══ -->
<section id="kockazat" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">Kockázat</div>
      <h2 class="section-title">Az időtáv többet ér, mint a jó belépési pont</h2>
      <p class="section-sub">A befektetés két valódi ellenfele nem a piac, hanem a türelmetlenség és a koncentráció.</p>
    </div>
    <div class="art">
      <div class="tiles">
        <div class="tile"><div class="tile-i">⏳</div><div class="tile-t">Időtáv</div><div class="tile-d">A részvénypiacok rövid távon kiszámíthatatlanok, hosszú távon viszont a széles, jó minőségű portfóliók történelmileg felfelé mozogtak. Aki öt évre vesz részvénykockázatot, szerencsejátékot játszik. Aki tizenötre, az befektet.</div></div>
        <div class="tile"><div class="tile-i">🧩</div><div class="tile-t">Diverzifikáció</div><div class="tile-d">Ne egy országon, egy szektoron és egy devizán múljon a vagyonod. A szórás az egyetlen olyan eszköz, ami <b>ingyen</b> csökkenti a kockázatot anélkül, hogy a várható hozamot arányosan levágná.</div></div>
        <div class="tile"><div class="tile-i">📅</div><div class="tile-t">Rendszeresség</div><div class="tile-d">A havi, azonos összegű befizetés automatikusan többet vesz olcsón és kevesebbet drágán. Nem varázslat, csak annyi, hogy nem kell eltalálnod a mélypontot, ami amúgy sem szokott sikerülni senkinek.</div></div>
        <div class="tile"><div class="tile-i">💱</div><div class="tile-t">Devizakockázat</div><div class="tile-d">A külföldi eszközök hozamát a forint mozgása felül- vagy alulírja. Ez nem hiba, hanem tulajdonság: ha forintban költesz, a devizakitettség kockázat; ha a célod devizában van, akkor viszont védelem.</div></div>
        <div class="tile"><div class="tile-i">📉</div><div class="tile-t">Ingadozás és veszteség</div><div class="tile-d">A kettő nem ugyanaz. Az ingadozás az út, a veszteség a döntés. Az árfolyamesés akkor válik valódi veszteséggé, amikor eladsz. Ezért a kockázati szintet előre kell beállítani, nem esés közben.</div></div>
        <div class="tile"><div class="tile-i">🧾</div><div class="tile-t">Infláció</div><div class="tile-d">A leglassabb, ezért a legveszélyesebb kockázat. Nem látszik az egyenlegen, mégis évről évre csökkenti, hogy mit tudsz megvenni a pénzedből. A hozamot mindig az inflációhoz képest érdemes nézni.</div></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ HIBÁK ═══ -->
<section id="hibak" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">Tanulságok</div>
      <h2 class="section-title">Öt hiba, ami a legtöbb pénzbe kerül</h2>
      <p class="section-sub">Ezekkel találkozunk a leggyakrabban, amikor valaki meglévő portfólióval ül le hozzánk.</p>
    </div>
    <div class="art">
      <div class="nsteps">
        <div class="nstep"><div class="nstep-n">1</div><div><div class="nstep-t">Esésben eladni</div><div class="nstep-d">A legdrágább mozdulat a piacon. Az árfolyamveszteség a kiszállásig csak papíron létezik, az eladás pillanatában viszont valódivá válik, és a visszakapaszkodásból is kimaradsz, ami jellemzően a mélypont utáni néhány hónapban történik. <b>Ellenszer:</b> olyan kockázati szintet válassz előre, amit egy 20-30 százalékos esésben is bírsz.</div></div></div>
        <div class="nstep"><div class="nstep-n">2</div><div><div class="nstep-t">Hosszú távú pénzt sima számlán tartani</div><div class="nstep-d">Ugyanaz az eszköz, ugyanaz a hozam, csak a végén akár 28 százalékkal kevesebb marad. A TBSZ megnyitása néhány perc. A hosszú távra szánt pénzre nincs racionális indok sima számlán maradni. <b>Ellenszer:</b> a gyűjtőév kihasználása. Ha még idén nyitod, idén rá is teheted a pénzt, és hamarabb indul az óra.</div></div></div>
        <div class="nstep"><div class="nstep-n">3</div><div><div class="nstep-t">Múltbeli hozam alapján választani</div><div class="nstep-d">A tavalyi legjobb alap idén gyakran az átlag alatt teljesít, mert a kiugró teljesítmény mögött többnyire egy koncentrált, jól sikerült fogadás áll, ami nem ismételhető meg tetszőlegesen. A költség viszont minden évben ugyanúgy jelen van. <b>Ellenszer:</b> kockázati szint, költség és időtáv alapján válassz, ne rangsorból.</div></div></div>
        <div class="nstep"><div class="nstep-n">4</div><div><div class="nstep-t">Mindent egy termékbe tenni</div><div class="nstep-d">Se egyetlen részvénybe, se egyetlen biztosításba. A koncentráció akkor is kockázat, ha a termék önmagában jó. Egy hosszú távú megtakarítás mellé kell rövid távú, hozzáférhető pénz is, különben az első váratlan kiadás felborítja a rendszert. <b>Ellenszer:</b> legalább három réteg: vésztartalék, középtávú cél, hosszú távú vagyonépítés.</div></div></div>
        <div class="nstep"><div class="nstep-n">5</div><div><div class="nstep-t">Nem nézni rá évekig</div><div class="nstep-d">Az ellenkezője is hiba, mint a napi árfolyamfigyelés, de a teljes elengedés drágább. A célod változik, a kockázattűrésed változik, és a nyugdíjhoz közeledve a portfóliót fokozatosan óvatosabbá kell tenni, különben rosszkor ér a visszaesés. <b>Ellenszer:</b> évi egy átnézés. Nem több, de az meglegyen.</div></div></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ GYIK ═══ -->
<section id="gyik" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">GYIK</div>
      <h2 class="section-title">Gyakori kérdések a befektetésekről</h2>
    </div>
    <div class="faq-list">
      __FAQ__
    </div>
  </div>
</section>
'''

FAQ = [
("Mennyi pénzzel érdemes egyáltalán elkezdeni?",
 [u"Havi szinten már 10-20 ezer forinttal is van értelme, ha hosszú az időtáv, mert a rendszeresség és az idő többet számít, mint az induló összeg. Egyösszegű befektetésnél a legtöbb szolgáltatónál néhány tízezer forint a belépő, TBSZ-nél jellemzően 25 000 forint.",
  u"A fontosabb kérdés nem az összeg, hanem a sorrend: előbb legyen vésztartalék, és ne legyen drága, magas kamatozású adósságod. Ha ez a kettő megvan, onnantól minden befektetett forint dolgozik."]),

("Most szálljak be, vagy várjam meg, hogy essen a piac?",
 [u"A belépési pont eltalálása hosszú távon statisztikailag nem szokott sikerülni, még a szakembereknek sem. Aki a tökéletes pillanatra vár, jellemzően kimarad a hozam egy részéből, miközben a pénze addig inflálódik.",
  u"A gyakorlati megoldás nem az időzítés, hanem a szakaszolás: nagyobb összeget több részletben, több hónapra elosztva tenni be. Ezzel nem kell eltalálnod semmit, és az esetleges rossz belépés hatása is szétterül."]),

("Mi a különbség a TBSZ és a nyugdíjcélú megtakarítás között?",
 [u"A TBSZ szabad felhasználású: öt év után adómentesen kiveheted, és arra költöd, amire akarod. A nyugdíjcélú formák többet adnak, mert 20 százalékos adó-visszatérítés jár rájuk, cserébe viszont a pénz a nyugdíjkorhatárig gyakorlatilag be van zárva, és a korai felvétel büntetéssel jár.",
  u'A kettő nem versenyzik, hanem kiegészíti egymást. A nyugdíjra a nyugdíjcélú forma jobb, mindenre másra a TBSZ. A legtöbb jól működő portfólióban mindkettő szerepel. A nyugdíjcélú termékek részleteit a <a href="nyugdij.html">nyugdíj oldalunkon</a> szedtük össze.']),

("Ha TBSZ-en tartom a pénzt, menet közben hozzá tudok nyúlni?",
 [u"A számlán belül igen: szabadon eladhatsz, vehetsz, átrendezheted a portfóliót, ezek nem adóztatható események. Ami korlátozott, az a pénz kivétele a számláról.",
  u"Ha a lekötési idő letelte előtt kiveszed, a feltörés szabályai szerint adózik a hozam, a táblázatban látható kulcsokkal. Ezért szoktuk azt javasolni, hogy ne egyetlen nagy TBSZ legyen, hanem évente nyitott, több kisebb: így mindig lejár valamelyik, és nem kell feltörni egyet sem."]),

("Mi történik, ha a szolgáltató, ahol a pénzem van, csődbe megy?",
 [u"A befektetési jegyeid és értékpapírjaid a te tulajdonodban vannak, nem a szolgáltató vagyonának részei, ezért elvileg átvihetők egy másik szolgáltatóhoz. Erre az esetre működik a Befektetővédelmi Alap, ami a szolgáltató mulasztásából eredő károkra ad kártalanítást, jogszabályban rögzített felső határig.",
  u"Ez nem azonos a banki betétbiztosítással, és fontos tudni, hogy egyik sem véd az árfolyamveszteségtől. Ha az alapod esik, azt semmilyen alap nem téríti meg, mert az nem kár, hanem befektetési kockázat."]),

("Mennyire lehet megbízni a múltbeli hozamokban?",
 [u"Tájékozódásra jók, előrejelzésre nem. A múltbeli hozam megmutatja, hogyan viselkedett az adott alap különböző piaci helyzetekben, mekkorák voltak a visszaesései és mennyi idő alatt jött vissza belőlük. Ez hasznos információ a kockázatról.",
  u"Amit viszont nem mutat meg, az a jövőbeli hozam. Erre egyetlen szabályozott szolgáltató sem vállalhat garanciát, és ha valaki mégis konkrét jövőbeli hozamot ígér, az önmagában figyelmeztető jel."]),

("Devizában vagy forintban érdemes befektetni?",
 [u"Attól függ, milyen devizában lesz a kiadásod. Ha forintban élsz és forintban költesz, a devizakitettség önmagában kockázat, mert az árfolyam mindkét irányba mozoghat. Ha viszont devizában lesz célod, például külföldi tanulmány vagy ingatlan, akkor a devizás megtakarítás éppen hogy csökkenti a kockázatot.",
  u"A gyakorlatban a legtöbb hosszú távú portfólióban van valamennyi nemzetközi kitettség, mert a diverzifikáció előnye általában felülmúlja a devizamozgás okozta ingadozást. Az arányt viszont tudatosan kell beállítani, nem véletlenszerűen."]),

("Közvetítetek állampapírt?",
 [u"Nem. Az állampapír nem tartozik a közvetített termékeink közé, ezért erről nem is adunk terméktanácsot és nem is hasonlítjuk össze ajánlatként. Ha ez érdekel, a Magyar Államkincstárnál vagy a bankodnál tudod megvásárolni.",
  u"Attól még a beszélgetésen szóba kerülhet, mert a portfóliód összképéhez hozzátartozik, és annak is van jelentősége, mennyi pénzed van már ilyen formában. A döntést viszont ebben magadnak kell meghoznod, vagy a számlavezetőddel."]),

("Mennyibe kerül nálatok a tanácsadás?",
 [u"Az ügyfélnek nem kerül semmibe. A tanácsadói hálózat a megkötött szerződések után a szolgáltatótól kap jutalékot, ezért a beszélgetés, az összehasonlítás és a portfólió átnézése díjmentes, akkor is, ha a végén nem kötsz semmit.",
  u"Ez a modell felvet egy jogos kérdést, ezért nyíltan kezeljük: a javadalmazás terméktípusonként eltér. Ha kéred, elmondjuk, melyik konstrukcióhoz milyen jellegű javadalmazás kapcsolódik, hogy tudd, hol lehet érdekütközés."]),

("Van olyan eset, amikor azt mondjátok, ne fektess be?",
 [u"Rendszeresen. Ha van magas kamatozású, drága hitelkártya- vagy személyi kölcsön tartozásod, annak a törlesztése gyakorlatilag kockázatmentes, garantált megtérülés, amit egyetlen befektetés sem ver meg. Ilyenkor először azt rendezzük.",
  u"Ugyanez igaz a vésztartalékra: amíg nincs három-hat havi kiadásnyi elérhető pénzed, addig a hosszú távú megtakarítás inkább kockázat, mint érték, mert az első váratlan kiadásnál fel kell törni."]),
]

BODY = BODY.replace('__FAQ__', faq_html(FAQ))

EXTRA_JS = u'''
(function(){
var el = function(id){ return document.getElementById(id); };
if(!el('b_havi')) return;

var huf = function(x){ return Math.round(x).toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g,'\\u00a0') + '\\u00a0Ft'; };
var pc  = function(x){ return x.toString().replace('.',',') + '%'; };
var mode = 'tbsz';

function paint(r){
  var p = (r.value - r.min) / (r.max - r.min) * 100;
  r.style.background = 'linear-gradient(90deg,var(--teal) 0%,var(--teal) ' + p + '%,#d9e2ea ' + p + '%,#d9e2ea 100%)';
}

/* hozamado kulcs: TBSZ-en az eltelt ev szerint, sima szamlan kamatjovedelem */
function kulcs(m, ev){
  if(m === 'ado') return 0.28;
  if(ev < 3)  return 0.28;
  if(ev < 5)  return 0.18;
  return 0;
}

function veg(m, ev, r, k){
  var mr = (r - k)/12, n = ev*12;
  return mr === 0 ? m*n : m*((Math.pow(1+mr,n)-1)/mr)*(1+mr);
}

function calc(){
  var m  = +el('b_havi').value, ev = +el('b_ev').value,
      r  = +el('b_hozam').value/100, k = +el('b_ktg').value/100;

  var bef    = m*12*ev;
  var brutto = veg(m, ev, r, k);
  var nokt   = veg(m, ev, r, 0);
  var hozam  = Math.max(0, brutto - bef);
  var kts    = Math.max(0, nokt - brutto);

  var ado    = hozam * kulcs(mode, ev);
  var netto  = brutto - ado;
  var masik  = brutto - hozam * kulcs(mode === 'tbsz' ? 'ado' : 'tbsz', ev);

  el('b_big').textContent  = huf(netto);
  el('b_sub').textContent  = huf(m) + ' / hó · ' + ev + ' év · ' +
                             (mode === 'tbsz' ? 'TBSZ' : 'sima számla');
  el('b_bef').textContent  = huf(bef);
  el('b_hoz').textContent  = '+' + huf(hozam);
  el('b_ado').textContent  = (ado > 0 ? '−' + huf(ado) : '0\\u00a0Ft');
  el('b_kts').textContent  = '−' + huf(kts);

  var d = netto - masik;
  el('b_dl').textContent   = (Math.round(d) === 0 ? 'Ugyanannyi, mint sima számlán'
                              : mode === 'tbsz' ? 'Ennyivel több, mint sima számlán'
                              : 'Ennyivel kevesebb, mint TBSZ-en');
  el('b_diff').textContent = (Math.round(d) === 0 ? '0\\u00a0Ft' : (d > 0 ? '+' : '−') + huf(Math.abs(d)));

  var w = el('b_warn');
  if(mode === 'ado'){
    w.className = 'sc-warn';
    w.innerHTML = 'Sima számlán a hozamot <b>15 százalék szja és 13 százalék szocho</b>, összesen 28 százalék terheli, ha kamatjövedelemnek minősül. ' +
      'Ugyanez a pénz TBSZ-en, az öt évet kivárva <b>adómentes</b> lenne. A különbség ebben a beállításban <b>' + huf(Math.abs(d)) + '</b>.';
  } else if(ev < 3){
    w.className = 'sc-warn';
    w.innerHTML = 'Három éven belül feltörve a TBSZ nem ad kedvezményt: a 2025-től nyitott számláknál ilyenkor <b>15% szja + 13% szocho</b> jár, ' +
      'ugyanannyi, mint sima számlán. Ez a konstrukció <b>legalább három, igazán öt évre</b> szól.';
  } else if(ev < 5){
    w.className = 'sc-warn';
    w.innerHTML = 'Három és öt év között a kulcs <b>10% szja + 8% szocho</b>, összesen 18 százalék. ' +
      'Ha még <b>' + (5 - ev) + ' évig</b> bent hagyod, a hozamadó nullára csökken, és ' +
      'ebben a beállításban további <b>' + huf(hozam * 0.18) + '</b> maradna nálad.';
  } else {
    w.className = 'sc-warn ok';
    w.innerHTML = 'Az ötödik év letelte után a TBSZ hozama <b>se szja-t, se szochót nem fizet</b>. ' +
      'Ebben a beállításban ez <b>' + huf(Math.abs(d)) + '</b> megtakarított adó a sima számlához képest.';
  }
}

['b_havi','b_ev','b_hozam','b_ktg'].forEach(function(id){
  var r = el(id), v = el(id+'_v');
  var fmt = { b_havi:function(x){return huf(x)+' / hó';}, b_ev:function(x){return x+' év';},
              b_hozam:pc, b_ktg:pc }[id];
  function show(){ paint(r); v.textContent = fmt(+r.value); calc(); }
  r.addEventListener('input', show); show();
});

document.querySelectorAll('#bf .sc-seg button').forEach(function(b){
  b.addEventListener('click', function(){
    document.querySelectorAll('#bf .sc-seg button').forEach(function(x){ x.classList.remove('on'); });
    b.classList.add('on'); mode = b.dataset.mode; calc();
  });
});
})();
'''

LEGAL = (u'<b>*</b> Az oldalon szereplő adatok tájékoztató jellegűek, a <b>2026. szeptemberi</b> állapotot tükrözik, és nem minősülnek befektetési tanácsadásnak, '
         u'befektetési elemzésnek, ajánlattételnek, ajánlattételi felhívásnak vagy adótanácsadásnak. A bemutatott termékek kockázatot hordoznak: a befektetés '
         u'értéke csökkenhet, a múltbeli hozam nem jelent garanciát a jövőbeli hozamra, és a befektetett tőke egy része vagy egésze elveszhet. '
         u'A kalkulátor egyszerűsített modellel dolgozik: egyenletes havi befizetéssel, egyenletes éves hozammal és a kezelt vagyonra vetített egyenletes éves '
         u'költséghányaddal számol, az adót pedig a futamidő végén, a teljes halmozott hozamra vetítve, egy összegben veszi figyelembe. A valóságban az adókötelezettség '
         u'keletkezésének időpontja, alapja és jogcíme eszközönként eltér. A tartós befektetési számlára vonatkozó adózási szabályokat az Szja tv. 67/B. §-a, '
         u'a kamatjövedelemre vonatkozókat az Szja tv. 65. §-a, az ellenőrzött tőkepiaci ügyletre vonatkozókat az Szja tv. 67/A. §-a, a kamatjövedelmet '
         u'terhelő szociális hozzájárulási adót pedig a szociális hozzájárulási adóról szóló törvény rendelkezései tartalmazzák; a 2025. január 1-jétől nyitott '
         u'TBSZ-ek idő előtti megszüntetésére eltérő, szigorúbb szabályok vonatkoznak, mint a korábban nyitottakra. A befektetési egységhez kötött életbiztosítások '
         u'teljes költségmutatójára (TKM) vonatkozó számítási és közzétételi szabályokat, valamint a TKM-limitrendszert jegybanki rendelet és ajánlás, illetve az '
         u'ezeken alapuló szakmai szabályzat rögzíti; szerződés előtt a konkrét termék hatályos TKM-értékének és feltételeinek megismerése szükséges. '
         u'A Befektetővédelmi Alap és az Országos Betétbiztosítási Alap kártalanítási szabályai és összeghatárai jogszabályban rögzítettek, és egyik sem nyújt '
         u'fedezetet árfolyamveszteségre. Állampapírt nem közvetítünk. Az adószabályok év közben is módosulhatnak, ezért a konkrét adóhatást minden esetben érdemes '
         u'adótanácsadóval vagy a számlavezető szolgáltatóval egyeztetni. Adatok érvényessége: <b data-upd></b>.')

build('befektetesek.html',
      u'Befektetés 2026: TBSZ, befektetési alapok, unit-linked | EAGLZ Finance',
      u'TBSZ adózás 2026-os szabályokkal, befektetési alapok költségei, unit-linked életbiztosítás és TKM. Kalkulátor: mennyit visz el a hozamodból az adó és a költség.',
      BODY, LEGAL,
      u'Nézzük meg, mennyit hagysz az asztalon.',
      u'Egy díjmentes átnézésen megmutatjuk, mennyi adót és költséget fizetsz feleslegesen a jelenlegi megtakarításaidon, és mit lehetne ebből visszanyerni.',
      EXTRA_JS)
