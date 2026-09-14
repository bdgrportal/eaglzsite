# -*- coding: utf-8 -*-
import io
from build_sub import build

BODY = u'''
<section class="sub-hero">
  <div class="container">
    <a href="index.html" class="sub-back">← Vissza a főoldalra</a>
    <h1 class="sub-h1">Nyugdíj-megtakarítás: <em>20% adó-visszatérítéssel</em></h1>
    <p class="sub-lead">Az állami nyugdíj a nettó átlagkeresetnek nagyjából a felét pótolja. Ezen az oldalon végigvesszük, mit jelent ez a te esetedben, milyen három megtakarítási forma kap állami támogatást, mennyit ad vissza az állam, és mi történik, ha idő előtt hozzányúlsz a pénzhez.</p>
    <div class="sub-chips">
      <div class="sub-chip">💰 <b>20%</b> adó-visszatérítés</div>
      <div class="sub-chip">📈 Évente max. <b>280 000 Ft</b></div>
      <div class="sub-chip">📅 Adatok: <b data-upd></b></div>
    </div>
    <div class="quicknav">
      <a href="#kalkulator" class="qn on">📊 Kalkulátor</a>
      <a href="#termekek" class="qn">🔍 A három termék</a>
      <a href="#gyik" class="qn">❓ GYIK</a>
      <a href="index.html#advisors" class="qn">📅 Időpontot foglalok</a>
    </div>
  </div>
</section>

<!-- ═══ 1. A PROBLÉMA ═══ -->
<section class="section" style="background:#fff;padding-bottom:2.4rem;">
  <div class="container">
    <div class="toc">
      <div class="toc-t">Ezen az oldalon</div>
      <ol>
        <li><a href="#miert">Miért nem elég az állami nyugdíj</a></li>
        <li><a href="#kalkulator">Mennyit ad vissza az állam? Kalkulátor</a></li>
        <li><a href="#termekek">A három támogatott termék</a></li>
        <li><a href="#melyiket">Melyiket válaszd?</a></li>
        <li><a href="#igenyles">Hogyan jut hozzád a visszatérítés</a></li>
        <li><a href="#feltores">Mi történik idő előtti feltöréskor</a></li>
        <li><a href="#hibak">Öt gyakori hiba</a></li>
        <li><a href="#gyik">Gyakori kérdések</a></li>
      </ol>
    </div>

    <div class="art" id="miert">
      <h2>Miért nem elég önmagában az állami nyugdíj?</h2>
      <p class="lead">Nem azért, mert az állam rosszul számol, hanem mert a rendszer felosztó-kirovó: a mai aktívak járuléka a mai nyugdíjakat fizeti. Ha kevesebb aktív jut egy nyugdíjasra, a rendszer előbb-utóbb szűkül. Ez nem vélemény, hanem demográfia.</p>

      <div class="kpis">
        <div class="kpi"><b>263 990 Ft</b><span>öregségi átlagnyugdíj, 2026. július</span></div>
        <div class="kpi"><b>232 440 Ft</b><span>medián nyugdíj, ennél a fele kevesebbet kap</span></div>
        <div class="kpi"><b>~50%</b><span>helyettesítési ráta a nettó átlagkeresethez</span></div>
        <div class="kpi"><b>15 év</b><span>minimum szolgálati idő a résznyugdíjhoz</span></div>
      </div>
      <p style="font-size:.78rem;">Forrás: KSH-adatok alapján, 2026. Az átlag és a medián közti különbség azért fontos, mert az átlagot néhány magas nyugdíj húzza felfelé: a nyugdíjasok fele a mediánnál is kevesebbet kap.</p>

      <h3>Mit jelent a „helyettesítési ráta"?</h3>
      <p>Azt, hogy a nyugdíjad az utolsó kereseted hány százaléka lesz. Magyarországon ez aggregált szinten <b>nagyjából 50 százalék</b>. A gyakorlatban viszont annál rosszabb az arány, minél többet keresel: a nyugdíj kiszámításánál a magasabb keresetek egyre kisebb súllyal számítanak. Egy átlagkereset körüli munkavállalónál az 50 százalék reális, egy jóval afölött keresőnél ez 35-40 százalék is lehet.</p>
      <p>A különbözet az, amit neked kell pótolnod. Nem azért, hogy gazdag legyél nyugdíjasként, hanem azért, hogy ne kelljen életszínvonalat váltanod 65 évesen.</p>

      <div class="box info">
        <span class="box-t">A jó hír: az állam fizet azért, hogy félretegyél</span>
        Három megtakarítási formára ad <b>20 százalékos adó-visszatérítést</b>, évente összesen legfeljebb 280 000 forint értékben. Ez nem hozam, hanem azonnali, garantált plusz a befizetésedre. Egyetlen más megtakarítási formánál sem kapsz ilyet.
      </div>
    </div>
  </div>
</section>

<!-- ═══ 2. KALKULÁTOR ═══ -->
<section id="kalkulator" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">Kalkulátor</div>
      <h2 class="section-title">Mennyit ad vissza az állam, és mennyi gyűlik össze?</h2>
      <p class="section-sub">Állítsd be, mennyit tudsz havonta félretenni és hány éved van a nyugdíjig. A kalkulátor kiszámolja az éves adó-visszatérítést, és azt, hogy ez mennyivel növeli a végösszeget.</p>
    </div>

    <div class="sc" id="ny">
      <div class="sc-in">
        <div class="sc-seg" role="group" aria-label="Termék">
          <button type="button" class="on" data-prod="nyb">Nyugdíjbiztosítás</button>
          <button type="button" data-prod="onyp">Önk. pénztár</button>
          <button type="button" data-prod="nyesz">NYESZ</button>
        </div>
        <div class="scf">
          <label class="scf-top" for="n_havi">Havi megtakarítás<b id="n_havi_v"></b></label>
          <input type="range" id="n_havi" min="5000" max="80000" step="1000" value="25000">
          <span class="scf-note">Az adó-visszatérítés plafonjához nyugdíjbiztosításnál havi 54 167 Ft, önkéntes pénztárnál 62 500 Ft, NYESZ-nél 41 667 Ft befizetés kell.</span>
        </div>
        <div class="scf">
          <label class="scf-top" for="n_ev">Hátralévő évek a nyugdíjig<b id="n_ev_v"></b></label>
          <input type="range" id="n_ev" min="3" max="45" step="1" value="25">
          <span class="scf-note">A jelenlegi öregségi nyugdíjkorhatár 65 év.</span>
        </div>
        <div class="scf">
          <label class="scf-top" for="n_hozam">Tájékoztató éves hozam<b id="n_hozam_v"></b></label>
          <input type="range" id="n_hozam" min="0" max="12" step="0.5" value="6">
          <span class="scf-note">A hozam nem garantált, és az általad választott eszközalaptól vagy portfóliótól függ. Óvatosabb forgatókönyvre is állítsd be.</span>
        </div>
        <div class="scf">
          <label class="scf-top" for="n_ktg">Éves költséghányad<b id="n_ktg_v"></b></label>
          <input type="range" id="n_ktg" min="0" max="4" step="0.1" value="1.5">
          <span class="scf-note">A termék teljes költsége a kezelt vagyonra vetítve. A biztosítói és pénztári konstrukciók között itt van a legnagyobb különbség, ezért érdemes összehasonlítani.</span>
        </div>
      </div>
      <div class="sc-out">
        <div class="sc-hero">
          <div class="sc-hero-l">Becsült érték a futamidő végén</div>
          <div class="sc-hero-n" id="n_big"></div>
          <div class="sc-hero-s" id="n_sub"></div>
        </div>
        <div class="sc-rows">
          <div><span>Amit te fizetsz be összesen</span><b id="n_bef"></b></div>
          <div class="hl"><span>Amit az állam hozzátesz</span><b id="n_ado"></b></div>
          <div><span>Éves adó-visszatérítés</span><b id="n_evi"></b></div>
          <div><span>Ebből a hozam</span><b id="n_hoz"></b></div>
          <div><span>Költségek összesen</span><b id="n_kts"></b></div>
        </div>
        <div class="sc-warn" id="n_warn"></div>
      </div>
    </div>
    <div class="sc-actions">
      <a href="index.html#advisors" class="apt-btn-inner" style="padding:.85rem 1.8rem;">📅 Nézzük meg az én esetemre</a>
    </div>

    <div class="art" style="margin-top:2.4rem;">
      <div class="box warn">
        <span class="box-t">Amit a kalkulátor nem tud</span>
        Nem ismeri a te adóalapodat. Az adó-visszatérítést csak a ténylegesen befizetett személyi jövedelemadód terhére kaphatod meg: ha nincs elég szja-d (mert például családi kedvezményt is érvényesítesz, vagy 25 év alatti adómentes a jövedelmed), akkor a visszatérítés is kevesebb lesz. Ezt a beszélgetésen konkrétan átnézzük.
      </div>
    </div>
  </div>
</section>

<!-- ═══ 3. A HÁROM TERMÉK ═══ -->
<section id="termekek" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">A piac</div>
      <h2 class="section-title">Három termék kap állami támogatást</h2>
      <p class="section-sub">Mindháromra ugyanaz a 20 százalék jár, de más a plafon, más a rugalmasság, és más a kockázat. Ez a legfontosabb különbségük egymás mellett.</p>
    </div>

    <div class="art wide">
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>&nbsp;</th><th>Nyugdíjbiztosítás</th><th>Önkéntes nyugdíjpénztár</th><th>NYESZ</th></tr></thead>
          <tbody>
            <tr><td>Adó-visszatérítés</td><td>20%, max. <b>130 000 Ft</b>/év</td><td>20%, max. <b>150 000 Ft</b>/év</td><td>20%, max. <b>100 000 Ft</b>/év</td></tr>
            <tr><td>Ehhez éves befizetés</td><td>650 000 Ft</td><td>750 000 Ft</td><td>500 000 Ft</td></tr>
            <tr><td>Ki kezeli a pénzt</td><td>a biztosító, választott eszközalapokban</td><td>a pénztár, választott portfólióban</td><td><b>te magad</b>, értékpapírszámlán</td></tr>
            <tr><td>Mikor jár le</td><td>a <b>szerződéskötéskori</b> nyugdíjkorhatárnál</td><td>10 év várakozás + nyugdíjba vonulás</td><td>nyugdíjkorhatár <b>és</b> 10 év</td></tr>
            <tr><td>Ha emelik a korhatárt</td><td><b>nem érinti</b> a szerződésedet</td><td>érinti</td><td>érinti</td></tr>
            <tr class="hl"><td>Kinek való</td><td>aki fix célt és haláleseti védelmet is szeretne</td><td>aki a legnagyobb visszatérítést akarja, olcsón</td><td>aki maga akar befektetni és ért hozzá</td></tr>
          </tbody>
        </table>
      </div>
      <p class="tbl-note">Az önkéntes pénztári 150 000 Ft-os plafon a nyugdíj-, egészség- és önsegélyező pénztárra <b>együttesen</b> vonatkozik, nem pénztáranként külön. A három forma együttes éves maximuma 280 000 Ft.</p>

      <h3>Nyugdíjbiztosítás</h3>
      <p>Biztosítási szerződés, aminek megtakarítási része van. A pénzed eszközalapokba kerül, a kockázatot te választod meg. Két dolog különbözteti meg a másik kettőtől: <b>a lejárat a szerződéskötéskor érvényes nyugdíjkorhatárhoz kötődik</b>, tehát ha a korhatárt később emelik, a te szerződésedet az nem tolja ki; és tartalmaz haláleseti szolgáltatást is, ami a családod védelme szempontjából számít.</p>
      <p>Cserébe jellemzően ez a legköltségesebb a három közül, főleg az első években. Ezért nyugdíjbiztosítást csak hosszú, 15 évnél is hosszabb távra érdemes kötni, és a költségmutatót (TKM) mindenképp nézd meg szerződés előtt.</p>

      <h3>Önkéntes nyugdíjpénztár</h3>
      <p>A legrégebbi és jellemzően a legolcsóbb forma, és itt a legmagasabb a visszatérítési plafon. Rugalmas: a befizetés mértéke szabadon változtatható, a minimum tagdíjat a pénztár alapszabálya rögzíti. Sok munkáltató is fizet bele, ami tovább javítja a képet.</p>
      <p>Amit tudni kell róla: <b>10 éves várakozási idő</b> van a belépéstől. A tizedik év után a hozam háromévente egyszer adómentesen felvehető, a tőke viszont bent marad a nyugdíjig.</p>

      <div class="box stop">
        <span class="box-t">Fontos aktualitás: a lakáscélú felhasználás megszűnt</span>
        2025-ben egy évig lehetett az önkéntes nyugdíjpénztári megtakarítást lakáscélra, adómentesen felvenni. Ez <b>egyszeri, átmeneti ablak volt: 2025. december 31-én lezárult</b>, és a kormány nem hosszabbította meg. 2026. január 1-től új kérelem nem nyújtható be. Több pénzügyi oldalon még mindig élő lehetőségként szerepel, ezért érdemes odafigyelni rá.
      </div>

      <h3>NYESZ</h3>
      <p>Nyugdíj-előtakarékossági számla: lényegében egy értékpapírszámla nyugdíjcélra, kedvező adózással. Itt <b>te döntöd el, mit veszel</b>: állampapírt, részvényt, befektetési alapot. Ez a legolcsóbb és legrugalmasabb megoldás annak, aki ért a befektetéshez, és a legkockázatosabb annak, aki nem.</p>
      <p>Alacsonyabb a visszatérítési plafon (100 000 Ft), és a hozzáféréshez két feltétel kell együtt: betöltött nyugdíjkorhatár <b>és</b> a számlanyitástól eltelt 10 év.</p>
    </div>
  </div>
</section>

<!-- ═══ 4. MELYIKET ═══ -->
<section id="melyiket" class="section dark-sec">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">Döntés</div>
      <h2 class="section-title">Melyiket válaszd?</h2>
      <p class="section-sub">Nincs objektíven legjobb termék, csak a helyzetedhez illő. Ez a négy kérdés dönti el.</p>
    </div>
    <div class="art wide">
      <div class="nsteps">
        <div class="nstep" style="background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.1);">
          <div class="nstep-n">1</div>
          <div><div class="nstep-t" style="color:#fff;">Hány éved van a nyugdíjig?</div>
          <div class="nstep-d" style="color:rgba(255,255,255,.66);">15 évnél rövidebb távon a magas kezdeti költségű konstrukciók nem tudják behozni magukat. Ilyenkor az önkéntes pénztár vagy a NYESZ jellemzően jobb.</div></div>
        </div>
        <div class="nstep" style="background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.1);">
          <div class="nstep-n">2</div>
          <div><div class="nstep-t" style="color:#fff;">Mennyi szja-d van évente?</div>
          <div class="nstep-d" style="color:rgba(255,255,255,.66);">A visszatérítés a befizetett adód terhére jár. Ha kevés az adód, nincs értelme a legmagasabb plafonú termékre hajtani, mert úgysem tudod kihasználni.</div></div>
        </div>
        <div class="nstep" style="background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.1);">
          <div class="nstep-n">3</div>
          <div><div class="nstep-t" style="color:#fff;">Akarsz-e magad befektetni?</div>
          <div class="nstep-d" style="color:rgba(255,255,255,.66);">Ha igen, és van hozzá idő és tudás, a NYESZ a legolcsóbb út. Ha nem, ne válaszd: az önkezelt számla rosszul kezelve többet veszít, mint amennyit a költségkülönbség hoz.</div></div>
        </div>
        <div class="nstep" style="background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.1);">
          <div class="nstep-n">4</div>
          <div><div class="nstep-t" style="color:#fff;">Számít-e a korhatár-kockázat?</div>
          <div class="nstep-d" style="color:rgba(255,255,255,.66);">Ha fontos, hogy a lejárat ne csússzon el egy jövőbeli jogszabály-változással, a nyugdíjbiztosítás az egyetlen, ahol a szerződéskötéskori korhatár rögzül.</div></div>
        </div>
      </div>

      <div class="yn">
        <div class="yn-col ok">
          <div class="yn-h">✓ Amit mi csinálunk</div>
          <ul>
            <li>Mindhárom formát kiszámoljuk a te adóalapodra</li>
            <li>Összevetjük a szolgáltatók tényleges költségmutatóit</li>
            <li>Megnézzük, van-e már meglévő, elfelejtett pénztári tagságod</li>
            <li>Beállítjuk a hozzád illő kockázati szintet</li>
            <li>Évente újranézzük, jól halad-e</li>
          </ul>
        </div>
        <div class="yn-col no">
          <div class="yn-h">✕ Amit nem csinálunk</div>
          <ul>
            <li>Nem mondjuk, hogy egy termék mindenkinek jó</li>
            <li>Nem ígérünk hozamot, mert nem lehet</li>
            <li>Nem beszélünk rá arra, amit nem tudsz végigfizetni</li>
            <li>Nem szüntetünk meg működő szerződést csak azért, hogy újat kössünk</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ 5. IGÉNYLÉS + FELTÖRÉS ═══ -->
<section id="igenyles" class="section" style="background:#fff;">
  <div class="container">
    <div class="art">
      <h2>Hogyan jut hozzád a 20 százalék?</h2>
      <p>Egyszerűbben, mint gondolnád: <b>nem kell külön igényelned</b>. A biztosító, a pénztár vagy a számlavezető minden évben adatot szolgáltat a NAV-nak a befizetéseidről, és a visszatérítés megjelenik az szja-bevallási tervezetedben.</p>
      <div class="nsteps">
        <div class="nstep"><div class="nstep-n">1</div><div><div class="nstep-t">Befizetsz az év során</div><div class="nstep-d">Rendszeresen vagy eseti jelleggel. Az adott adóévben ténylegesen beérkezett összeg számít.</div></div></div>
        <div class="nstep"><div class="nstep-n">2</div><div><div class="nstep-t">A szolgáltató adatot szolgáltat</div><div class="nstep-d">Automatikusan, a következő év elején. Neked ezzel nincs teendőd.</div></div></div>
        <div class="nstep"><div class="nstep-n">3</div><div><div class="nstep-t">Ellenőrzöd a bevallási tervezetet</div><div class="nstep-d">A NAV tervezetében már szerepel az összeg. Ha nem, ott lehet pótolni. Ezért érdemes átnézni, nem csak jóváhagyni.</div></div></div>
        <div class="nstep"><div class="nstep-n">4</div><div><div class="nstep-t">A NAV a megtakarításodra utal</div><div class="nstep-d">Nem a bankszámládra, hanem a nyugdíjcélú szerződésedre vagy számládra. Így a visszatérítés is tovább kamatozik.</div></div></div>
      </div>
      <div class="box info">
        <span class="box-t">Ez évente visszatérő döntés</span>
        Ha decemberben eseti befizetéssel feltöltöd az éves keretet, ugyanabban az évben már a magasabb visszatérítést kapod. Sokan itt hagynak pénzt az asztalon: januárban már késő az előző évre.
      </div>

      <h2 id="feltores" style="margin-top:2.6rem;">Mi történik, ha idő előtt kiveszed?</h2>
      <p>Az állam a támogatásért cserébe azt várja, hogy nyugdíjig bent hagyd a pénzt. Ha előbb nyúlsz hozzá, a visszatérítést vissza kell fizetni, és további adóteher is keletkezhet. Ez termékenként eltér.</p>
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Termék</th><th>Mi történik feltöréskor</th></tr></thead>
          <tbody>
            <tr><td>Nyugdíjbiztosítás</td><td>A kapott adó-visszatérítést <b>20 százalékkal növelten</b> kell visszafizetni, plusz a biztosító visszavásárlási költsége terhel. Kivétel: legalább 40%-os egészségkárosodás vagy haláleset.</td></tr>
            <tr><td>Önkéntes pénztár</td><td>10 év után a hozam adómentesen felvehető. A <b>tőke</b> viszont nyugdíj előtt egyéb jövedelemnek minősül: 15% szja + 13% szocho. A 11. évtől ez évente 10 százalékponttal csökken, a 21. évre nullára.</td></tr>
            <tr><td>NYESZ</td><td>A felvett adójóváírásokat vissza kell fizetni <b>20% büntetőkamattal</b>, a hozamon pedig 15% szja + 13% szocho.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="box warn">
        <span class="box-t">Ebből egy dolog következik</span>
        A nyugdíj-megtakarítás <b>nem vésztartalék</b>. Előbb legyen 3-6 havi kiadásnyi, azonnal hozzáférhető tartalékod, és csak azon felül indulj nyugdíjcélú megtakarítást. Aki fordítva csinálja, az az első váratlan kiadásnál bünteti meg magát.
      </div>
    </div>
  </div>
</section>

<!-- ═══ 6. HIBÁK ═══ -->
<section id="hibak" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">Amire figyelj</div>
      <h2 class="section-title">Öt hiba, ami sok pénzbe kerül</h2>
    </div>
    <div class="art wide">
      <div class="tiles c2">
        <div class="tile"><div class="tile-i">⏳</div><div class="tile-t">A halogatás</div><div class="tile-d">A kamatos kamat matematikája kegyetlen: <b>tíz év csúszás nagyjából kétszer akkora havi befizetést</b> igényel ugyanahhoz a végösszeghez. A legdrágább döntés az, ha „majd jövőre".</div></div>
        <div class="tile"><div class="tile-i">🧾</div><div class="tile-t">A ki nem használt keret</div><div class="tile-d">Sokan kevesebbet fizetnek be, mint amennyi után még járna a visszatérítés. Egy decemberi eseti befizetés <b>azonnal 20 százalékot hoz</b> arra az összegre.</div></div>
        <div class="tile"><div class="tile-i">💸</div><div class="tile-t">A költségek figyelmen kívül hagyása</div><div class="tile-d">Évi 1 és 3 százalék költség között 25 év alatt <b>több millió forint</b> a különbség. A TKM-mutatót szerződés előtt kell megnézni, nem utána.</div></div>
        <div class="tile"><div class="tile-i">😴</div><div class="tile-t">A be nem állított kockázat</div><div class="tile-d">Sokan alapértelmezett, óvatos portfólióban ülnek 30 évre. Hosszú távon ez <b>inflációs veszteség</b>. A kockázatot az időtávhoz kell igazítani, nem a hangulathoz.</div></div>
        <div class="tile"><div class="tile-i">🗂️</div><div class="tile-t">Az elfelejtett pénztári tagság</div><div class="tile-d">Nagyon sok embernek van régi, munkáltatón keresztül nyitott pénztári számlája, amiről elfeledkezett. <b>Érdemes megkeresni</b>: néha meglepően nagy összeg alszik rajta.</div></div>
        <div class="tile"><div class="tile-i">🔥</div><div class="tile-t">A korai feltörés</div><div class="tile-d">Ez a legdrágább hiba: elveszted a visszatérítést, kifizeted a büntetést, és elveszted az addig felhalmozott kamatos kamat előnyét is.</div></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ 7. GYIK ═══ -->
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

<!-- ═══ 8. KAPCSOLÓDÓ ═══ -->
<section class="section graph-light" style="padding-top:3rem;padding-bottom:3rem;">
  <div class="container">
    <div class="sec-head" style="margin-bottom:1.6rem;">
      <h2 class="section-title" style="font-size:1.35rem;">Kapcsolódó oldalak</h2>
    </div>
    <div class="rel">
      <a class="rel-c" href="befektetesek.html"><div class="rel-i">📈</div><div><div class="rel-t">Befektetések</div><div class="rel-d">TBSZ, alapok, adóhatékonyan</div></div></a>
      <a class="rel-c" href="gyermekjovo.html"><div class="rel-i">👶</div><div><div class="rel-t">Gyermek-megtakarítás</div><div class="rel-d">Babakötvény, 18 évre előre</div></div></a>
      <a class="rel-c" href="kalkulator.html"><div class="rel-i">🧮</div><div><div class="rel-t">Kalkulátorok</div><div class="rel-d">Hitel, JTM, bankszámla</div></div></a>
    </div>
  </div>
</section>
'''

FAQ = [
("Mennyit érdemes félretenni nyugdíjra?",
 ["Nincs egy jó szám, de van egy jó módszer: a célösszegből visszafelé számolunk. Megnézzük, mekkora kiegészítésre lenne szükséged a várható állami nyugdíjad mellé, hány éved van hátra, és ebből jön ki a havi összeg.",
  "Hüvelykujjszabályként a nettó jövedelem 10 százaléka körüli összeg hosszú távon érdemi kiegészítést ad, de a lényeg nem az arány, hanem az, hogy <b>végig tudd fizetni</b>. Inkább kevesebbel indulj és emeld, mint hogy két év után abbahagyd."]),

("A 20 százalékos visszatérítés ugyanaz, mint a 20 százalékos hozam?",
 ["Nem. A visszatérítés <b>egyszeri, garantált jóváírás</b> az adott évi befizetésedre, a hozam pedig a befektetett pénz évről évre változó eredménye. A kettő egymásra épül: a visszatérítés is bekerül a megtakarításba, és onnantól az is kamatozik.",
  "Épp ezért a visszatérítés az első években aránylag nagyot dob a számládon, a futamidő második felében viszont már a hozam viszi a hátán az egészet."]),

("Van-e felső korhatár, ameddig érdemes elkezdeni?",
 ["Jogi korlát nincs, gazdasági viszont van. Nyugdíjbiztosításnál a szerződés jellemzően minimum 10 éves futamidőt igényel, és a magas kezdeti költségek miatt 15 évnél rövidebb távon ritkán éri meg.",
  "Ha 10 évnél kevesebb van hátra a nyugdíjkorhatárig, jellemzően az önkéntes pénztár vagy a NYESZ marad értelmes opció. Ötven felett is van értelme elkezdeni, csak más eszközzel, mint harmincévesen."]),

("Felvehetem a nyugdíjpénztári pénzemet lakásra?",
 ["2026-ban nem. Ez egy <b>2025-re szóló, egyéves átmeneti lehetőség</b> volt, ami 2025. december 31-én lezárult, és a kormány nem hosszabbította meg. 2026. január 1-től új kérelmet nem lehet benyújtani.",
  "Ez azért fontos, mert sok online cikk és összehasonlító oldal még mindig aktuálisként mutatja. Ha valaki ma erre alapozva tervez lakásvásárlást, rossz feltételezésből indul ki."]),

("Mi van, ha megszűnik a munkaviszonyom, és nem tudok fizetni?",
 ["Mindhárom forma tud szünetelni, csak másképp. Az önkéntes pénztárnál a befizetés felfüggeszthető, a számla megmarad és tovább kamatozik, csak a minimális költséglevonás megy tovább. A NYESZ-nél sincs kötelező befizetés.",
  "A nyugdíjbiztosításnál van a legszigorúbb keret: itt díjmentesítés vagy szüneteltetés kérhető, de ennek feltételei szerződésenként eltérnek. Pont ezért nem mindegy, mekkora díjat vállalsz be induláskor."]),

("Mit jelent az, hogy a nyugdíjbiztosítást nem érinti a korhatár emelése?",
 ["Azt, hogy a szerződésben rögzített lejárat a <b>szerződéskötéskor hatályos</b> nyugdíjkorhatárhoz igazodik. Ha a jogalkotó később emeli a korhatárt, az a te szerződésed lejáratát nem tolja ki.",
  "A másik két formánál ez nem így van: ott a hozzáférés a mindenkori nyugdíjkorhatárhoz kötődik. Aki ma harmincéves, annak ez a különbség több évet is jelenthet."]),

("Jár a visszatérítés akkor is, ha 25 év alatti vagyok?",
 ["Csak annyiban, amennyi szja-t ténylegesen fizetsz. A 25 év alattiak kedvezménye miatt sok fiatalnak nincs vagy alig van összevont adóalap utáni szja-ja, és a visszatérítés ehhez van kötve.",
  "Ez nem érv a halogatás mellett: a korán elkezdett megtakarítás előnye a kamatos kamatból jön, nem a visszatérítésből. A visszatérítés később, magasabb jövedelemnél automatikusan beindul."]),

("Mi történik a pénzzel, ha meghalok a nyugdíj előtt?",
 ["Nem vész el. Az önkéntes pénztárnál és a NYESZ-nél a megtakarítás a kedvezményezettet vagy az örökösöket illeti. A nyugdíjbiztosításnál ezen felül haláleseti szolgáltatás is jár, és a kedvezményezett a hagyatéki eljárás megkerülésével, közvetlenül jut hozzá.",
  "Ez az egyik olyan pont, ahol a három termék érdemben különbözik, és amit szerződés előtt érdemes tudatosan beállítani."]),
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
/* ══ NYUGDÍJ KALKULÁTOR, karbantartás: csak a PLAFON blokk ══ */
var PLAFON = { nyb:130000, onyp:150000, nyesz:100000 };   /* éves adó-visszatérítés maximuma, Ft */
var RATE   = 0.20;                                         /* a visszatérítés mértéke */
var NEV    = { nyb:'Nyugdíjbiztosítás', onyp:'Önkéntes nyugdíjpénztár', nyesz:'NYESZ' };

function el(id){ return document.getElementById(id); }
function huf(v){ return Math.round(v).toLocaleString('hu-HU') + ' Ft'; }
function pc(v){ return (+v).toFixed(1).replace('.',',') + '%'; }
function paint(e){ e.style.setProperty('--p', (e.value-e.min)/(e.max-e.min)*100 + '%'); }

var prod = 'nyb';

function calc(){
  var m = +el('n_havi').value, ev = +el('n_ev').value,
      r = +el('n_hozam').value/100, k = +el('n_ktg').value/100;
  var net = r - k;                       /* költséggel csökkentett éves hozam */
  var mr  = net/12, n = ev*12;
  var evi = Math.min(m*12*RATE, PLAFON[prod]);   /* éves adó-visszatérítés */

  /* havi befizetések jövőértéke (év eleji befizetés) */
  function fvHavi(x){ return mr === 0 ? x*n : x*((Math.pow(1+mr,n)-1)/mr)*(1+mr); }
  /* az évente egyszer érkező visszatérítés jövőértéke */
  var yr = Math.pow(1+mr,12)-1;
  var fvAdo = yr === 0 ? evi*ev : evi*((Math.pow(1+yr,ev)-1)/yr);

  var bef = m*12*ev, ado = evi*ev;
  var veg = fvHavi(m) + fvAdo;
  var brutto = (function(){                       /* költség nélkül, a különbség a költség */
    var br = r/12, ny = Math.pow(1+r/12,12)-1;
    var a = br === 0 ? m*n : m*((Math.pow(1+br,n)-1)/br)*(1+br);
    var b = ny === 0 ? evi*ev : evi*((Math.pow(1+ny,ev)-1)/ny);
    return a + b;
  })();

  el('n_big').textContent = huf(veg);
  el('n_sub').textContent = huf(m) + ' / hó · ' + ev + ' év · ' + NEV[prod];
  el('n_bef').textContent = huf(bef);
  el('n_ado').textContent = '+' + huf(ado);
  el('n_evi').textContent = huf(evi) + ' / év';
  el('n_hoz').textContent = '+' + huf(Math.max(0, veg - bef - ado));
  el('n_kts').textContent = '−' + huf(Math.max(0, brutto - veg));

  var w = el('n_warn'), kihasznalt = m*12*RATE;
  if(kihasznalt > PLAFON[prod] + 1){
    w.className = 'sc-warn';
    w.innerHTML = 'Ennél a terméknél az éves visszatérítés <b>' + huf(PLAFON[prod]) +
      '</b>-nál megáll. A havi ' + huf(m) + ' befizetésből ' + huf(PLAFON[prod]/RATE/12) +
      ' az, amire még jár a 20 százalék. A fölötte lévő rész is gyűlik és kamatozik, csak visszatérítést már nem hoz.';
  } else if(kihasznalt < PLAFON[prod] - 1){
    w.className = 'sc-warn';
    w.innerHTML = 'Van még kihasználatlan kereted: havi <b>' + huf(PLAFON[prod]/RATE/12 - m) +
      '</b> további befizetésig jár a 20 százalék. Ez évente <b>' + huf(PLAFON[prod] - kihasznalt) +
      '</b> plusz visszatérítést jelentene.';
  } else {
    w.className = 'sc-warn ok';
    w.innerHTML = 'Pontosan kihasználod az éves keretet: <b>' + huf(PLAFON[prod]) +
      '</b> visszatérítés jár évente. Ez a maximum ennél a terméknél.';
  }
}

['n_havi','n_ev','n_hozam','n_ktg'].forEach(function(id){
  var r = el(id), v = el(id+'_v');
  var fmt = { n_havi:function(x){return huf(x)+' / hó';}, n_ev:function(x){return x+' év';},
              n_hozam:pc, n_ktg:pc }[id];
  function show(){ paint(r); v.textContent = fmt(+r.value); calc(); }
  r.addEventListener('input', show); show();
});

document.querySelectorAll('#ny .sc-seg button').forEach(function(b){
  b.addEventListener('click', function(){
    document.querySelectorAll('#ny .sc-seg button').forEach(function(x){ x.classList.remove('on'); });
    b.classList.add('on'); prod = b.dataset.prod; calc();
  });
});
})();
'''

LEGAL = (u'<b>*</b> Az oldalon szereplő adatok tájékoztató jellegűek, nem minősülnek befektetési tanácsadásnak, ajánlattételnek vagy adótanácsadásnak. '
         u'A kalkulátor egyszerűsített modellel dolgozik: a havi befizetéseket az időszak elején, az adó-visszatérítést évente egy összegben veszi figyelembe, '
         u'és egyenletes hozammal, valamint a kezelt vagyonra vetített egyenletes költséghányaddal számol. A tényleges hozam nem garantált, évről évre eltér, '
         u'és negatív is lehet; a tényleges költségszerkezet szolgáltatónként és terméktípusonként jelentősen különbözik, ezért szerződés előtt a teljes '
         u'költségmutató (TKM), illetve a pénztári költségek megismerése szükséges. Az adó-visszatérítés kizárólag a magánszemély által ténylegesen megfizetett, '
         u'összevont adóalapot terhelő személyi jövedelemadó terhére érvényesíthető, ezért a kalkulátor által mutatott összeg egyéni adóhelyzettől függően kevesebb lehet. '
         u'Az adó-visszatérítés mértékére (20%) és éves felső határaira (nyugdíjbiztosítás 130 000 Ft, NYESZ 100 000 Ft, önkéntes pénztárak együttesen 150 000 Ft, '
         u'összesen legfeljebb 280 000 Ft) vonatkozó adatok a 2026. szeptemberi jogszabályi állapotot tükrözik; a mindenkori hatályos szabályozás az irányadó. '
         u'Az önkéntes nyugdíjpénztári megtakarítás lakáscélú felhasználásának lehetősége 2025. december 31-én lezárult. Adatok érvényessége: <b data-upd></b>.')

build('nyugdij.html',
      u'Nyugdíj-megtakarítás 2026: 20% adó-visszatérítés | EAGLZ Finance',
      u'Nyugdíjbiztosítás, önkéntes pénztár és NYESZ összehasonlítva: mennyi adó-visszatérítés jár, mi a plafon, mi történik idő előtti feltöréskor. Kalkulátorral, 2026-os adatokkal.',
      BODY, LEGAL,
      u'Nézzük meg, mennyi kiegészítésre lesz szükséged.',
      u'Egy díjmentes átvilágításon kiszámoljuk a várható állami nyugdíjadat, a hiányzó részt, és hogy a három támogatott termék közül melyik illik a helyzetedhez.',
      JS)
