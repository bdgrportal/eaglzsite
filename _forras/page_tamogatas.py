# -*- coding: utf-8 -*-
from build_sub import build

BODY = u'''
<section class="sub-hero">
  <div class="container">
    <a href="index.html" class="sub-back">← Vissza a főoldalra</a>
    <h1 class="sub-h1">Állami támogatások <em>2026-ban</em></h1>
    <p class="sub-lead">Otthon Start, CSOK Plusz, Falusi CSOK, Babaváró és az idén induló Otthontámogatás: melyik mire való, ki jogosult rá, és mi változott az idén. Azt is megírjuk, ami kifutott, mert ezzel sok oldal adós marad.</p>
    <div class="sub-chips">
      <div class="sub-chip">🔑 <b>3%</b> fix kamat Otthon Starttal</div>
      <div class="sub-chip">👨‍👩‍👧 <b>50 M Ft</b> CSOK Plusszal</div>
      <div class="sub-chip">📅 Állapot: <b data-upd></b></div>
    </div>
    <div class="quicknav">
      <a href="kviz.html" class="qn on">✅ Jár nekem? Kvíz</a>
      <a href="#programok" class="qn">📋 A programok</a>
      <a href="#kifutott" class="qn">⚠️ Ami kifutott</a>
      <a href="index.html#advisors" class="qn">📅 Időpontot foglalok</a>
    </div>
  </div>
</section>

<section class="section" style="background:#fff;padding-bottom:2.4rem;">
  <div class="container">
    <div class="toc">
      <div class="toc-t">Ezen az oldalon</div>
      <ol>
        <li><a href="#attekintes">Áttekintés egy táblázatban</a></li>
        <li><a href="#otthonstart">Otthon Start</a></li>
        <li><a href="#csokplusz">CSOK Plusz</a></li>
        <li><a href="#falusi">Falusi CSOK</a></li>
        <li><a href="#babavaro">Babaváró</a></li>
        <li><a href="#otthontamogatas">Otthontámogatás (új)</a></li>
        <li><a href="#kifutott">Ami 2026-ban kifutott</a></li>
        <li><a href="#gyik">Gyakori kérdések</a></li>
      </ol>
    </div>

    <div class="art" id="attekintes">
      <h2>Öt élő program, és egy, ami már nincs</h2>
      <p class="lead">Az otthonteremtési támogatások rendszere évről évre mozog: van, ami bővül, van, ami kifut, és van, ami közben csendben átalakul. Ezen az oldalon a <b>2026. szeptemberi állapot</b> szerepel, és külön jelöljük, ami az idén változott.</p>

      <div class="box warn">
        <span class="box-t">Egy dolog, amit előre érdemes tudni</span>
        Ezek a programok <b>kombinálhatók egymással</b>, de nem mindegyik mindegyikkel, és a sorrend sem mindegy. A leggyakoribb hiba nem az, hogy valaki rossz programot választ, hanem az, hogy egy elérhető támogatásról egyszerűen nem tud, vagy rossz sorrendben igényli, és ezzel elesik egy másiktól.
      </div>
    </div>

    <div class="art wide">
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Program</th><th>Mi ez</th><th>Összeg</th><th>Fő feltétel</th></tr></thead>
          <tbody>
            <tr class="hl"><td>Otthon Start</td><td>fix 3%-os lakáshitel</td><td>max. <b>50 M Ft</b></td><td>első lakás, 2 év TB, életben egyszer</td></tr>
            <tr><td>CSOK Plusz</td><td>kamattámogatott hitel</td><td>15 / 30 / <b>50 M Ft</b></td><td>házasság, gyermekvállalás</td></tr>
            <tr><td>Falusi CSOK</td><td>vissza nem térítendő</td><td>1 / 4 / <b>15 M Ft</b></td><td>kistelepülés, vásárlás + felújítás</td></tr>
            <tr><td>Babaváró</td><td>szabad felhasználású kölcsön</td><td>max. <b>11 M Ft</b></td><td>házasság, feleség 35 alatt</td></tr>
            <tr><td>Otthontámogatás</td><td>vissza nem térítendő</td><td><b>1 M Ft</b></td><td>közszférás munkaviszony</td></tr>
          </tbody>
        </table>
      </div>
      <p class="tbl-note">Az összegek a maximumot mutatják; a ténylegesen elérhető összeg a jövedelemtől, a meglévő hitelektől és a fedezettől függ. Egyik program sem jár automatikusan.</p>
    </div>
  </div>
</section>

<!-- ═══ OTTHON START ═══ -->
<section id="programok" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">01</div>
      <h2 class="section-title" id="otthonstart">Otthon Start: 3% fix kamat, 25 évre</h2>
      <p class="section-sub">A legnagyobb hatású program: 2026-ban a folyósított lakáshitelek túlnyomó részét ez adja. Első lakást szerzőknek szól, és életben egyszer vehető igénybe.</p>
    </div>
    <div class="art">
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Paraméter</th><th>Érték</th></tr></thead>
          <tbody>
            <tr class="hl"><td>Kamat</td><td><b>fix 3%</b> a teljes futamidőre</td></tr>
            <tr><td>Maximális összeg</td><td>50 000 000 Ft</td></tr>
            <tr><td>Futamidő</td><td>max. 25 év</td></tr>
            <tr><td>Minimum önerő</td><td>10%</td></tr>
            <tr><td>Ingatlan értékhatára</td><td>lakás <b>100 M Ft</b>, családi ház és tanya <b>150 M Ft</b></td></tr>
            <tr><td>Négyzetméterár-plafon</td><td>1 500 000 Ft/m²</td></tr>
            <tr><td>TB-jogviszony</td><td>legalább 2 év folyamatos</td></tr>
            <tr><td>Előző tulajdon</td><td>az elmúlt 10 évben nem lehetett lakóingatlanod (több kivétellel)</td></tr>
            <tr><td>Igénybevétel</td><td><b>életben egyszer</b>, adósként és adóstársként is</td></tr>
            <tr><td>Kötöttség</td><td>5 év elidegenítési tilalom, állami jelzálog a hitelösszeg 20%-ára</td></tr>
            <tr><td>Előtörlesztési díj</td><td>legfeljebb 1%</td></tr>
          </tbody>
        </table>
      </div>

      <h3>A kivételek, amikről kevesen tudnak</h3>
      <p>A tízéves tulajdonmentességi szabály szigorúnak hangzik, de több kivétel is van. Nem zár ki a programból, ha a korábbi ingatlanod:</p>
      <ul class="clean">
        <li>15 millió forintnál kisebb értékű volt</li>
        <li>legfeljebb 50 százalékos tulajdoni hányad volt</li>
        <li>bontásra ítélt, lakhatásra alkalmatlan ingatlan</li>
        <li>haszonélvezettel terhelt, és a haszonélvező ott lakik</li>
        <li>örökölt közös tulajdon, amelynek a többi részét kivásárolnád</li>
      </ul>
      <p>Ez a lista a leggyakoribb ok arra, hogy valaki tévesen kizárja magát a programból. Ha van a múltadban ingatlan, érdemes végignézni, beleesik-e valamelyik kivételbe.</p>

      <div class="box info">
        <span class="box-t">2026-os változás: külterületre is</span>
        2026. január 1-től az Otthon Start <b>külterületi és zártkerti lakóingatlanra</b> is felvehető, korábban csak belterületire volt. Ez sok vidéki vásárlónak nyitott utat, aki addig kiesett.
      </div>

      <div class="box info">
        <span class="box-t">2026-os változás: szakaszos folyósítás új építésnél</span>
        2026. március 6-tól új építésű lakásnál három folyósítási mód közül lehet választani: szakaszos folyósítás állami kamattámogatással már az építés alatt, szakaszos folyósítás támogatás nélkül, vagy egyösszegű folyósítás a használatbavétel után. Ugyanez a CSOK Pluszra is vonatkozik. Ez érdemben befolyásolja, mennyit fizetsz az építkezés ideje alatt.
      </div>

      <div class="box warn">
        <span class="box-t">Amit most tudni kell a program jövőjéről</span>
        A program <b>aktív</b>, és a már megkötött szerződések feltételei nem változnak. 2026 szeptemberében ugyanakkor a program szakmai és jogi felülvizsgálata folyamatban van, döntés még nincs. A sajtóban keringő szigorítási elemek egyelőre <b>várakozások, nem kihirdetett szabályok</b>. Ha most vagy döntés előtt, ez önmagában érv amellett, hogy ne halogasd az igénylést, de csak akkor, ha egyébként is a te helyzetedbe illik.
      </div>

      <div class="sc-actions" style="margin-top:1.8rem;">
        <a href="kviz.html" class="apt-btn-inner" style="padding:.85rem 1.8rem;">✅ Kitöltöm a jogosultsági kvízt</a>
      </div>
    </div>
  </div>
</section>

<!-- ═══ CSOK PLUSZ ═══ -->
<section class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">02</div>
      <h2 class="section-title" id="csokplusz">CSOK Plusz: gyermekvállalásra építve</h2>
      <p class="section-sub">Kamattámogatott lakáshitel házaspároknak, ahol az igényelhető összeg a meglévő és vállalt gyermekek számától függ.</p>
    </div>
    <div class="art">
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Gyermekszám</th><th>Max. hitelösszeg</th><th>Gyermekvállalási határidő</th></tr></thead>
          <tbody>
            <tr><td>1 gyermek</td><td>15 000 000 Ft</td><td>4 év</td></tr>
            <tr><td>2 gyermek</td><td>30 000 000 Ft</td><td>8 év</td></tr>
            <tr class="hl"><td>3 vagy több</td><td><b>50 000 000 Ft</b></td><td>10 év</td></tr>
          </tbody>
        </table>
      </div>
      <ul class="clean">
        <li><b>Kamat:</b> legfeljebb 3 százalék fix a támogatási időszak alatt</li>
        <li><b>Futamidő:</b> legfeljebb 25 év, az első 12 hónapban csak kamatot fizetsz</li>
        <li><b>Tőkeelengedés:</b> a szerződéskötés után született második és minden további gyermek után <b>10-10 millió forint</b></li>
        <li><b>Feltétel:</b> házasság, legalább az egyik félnél 2 év folyamatos TB-jogviszony, büntetlen előélet, köztartozás-mentesség</li>
        <li><b>Ingatlan:</b> gyermekszámtól függő minimum alapterület, 100 millió forintos (ház esetén 150 milliós) értékhatár</li>
      </ul>

      <div class="box info">
        <span class="box-t">2026-os változás: véglegessé vált a korhatár-mentesség</span>
        2026. január 1-től <b>határidő nélkülivé vált</b> az a könnyítés, amely szerint a 41. életévét betöltött feleség is igényelheti a CSOK Pluszt, ha igazoltan betöltött 12. hetes magzata van, illetve örökbefogadási kérelem esetén. Korábban ez a szabály csak 2025 végéig szólt.
      </div>

      <div class="box quote">
        <b>A leggyakoribb buktató:</b> a vállalt gyermek. Ha a határidőn belül nem születik meg, a támogatást <b>vissza kell fizetni</b>, késedelmi kamattal. Ez nem elméleti kockázat, és nem érdemes rá „majd valahogy lesz" alapon szerződni. Az igénylés előtt reálisan, kimondva kell végiggondolni.
      </div>
    </div>
  </div>
</section>

<!-- ═══ FALUSI CSOK ═══ -->
<section class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">03</div>
      <h2 class="section-title" id="falusi">Falusi CSOK: vissza nem térítendő, kistelepülésre</h2>
      <p class="section-sub">A legkevésbé ismert, pedig ez az egyik legnagyobb összegű vissza nem térítendő támogatás.</p>
    </div>
    <div class="art">
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Gyermekszám</th><th>Vásárlás + felújítás</th><th>Csak felújítás vagy bővítés</th></tr></thead>
          <tbody>
            <tr><td>1 gyermek</td><td>1 000 000 Ft</td><td>600 000 Ft</td></tr>
            <tr><td>2 gyermek</td><td>4 000 000 Ft</td><td>2 000 000 Ft</td></tr>
            <tr class="hl"><td>3 vagy több</td><td><b>15 000 000 Ft</b></td><td><b>7 500 000 Ft</b></td></tr>
          </tbody>
        </table>
      </div>
      <ul class="clean">
        <li>A támogatás <b>legfeljebb fele</b> fordítható vásárlásra, a másik felét felújításra vagy bővítésre kell fordítani. Csak vásárlásra nem igényelhető.</li>
        <li>Meglévő gyermekek után házastársak, élettársak és <b>egyedülálló szülők</b> is igényelhetik, életkortól függetlenül.</li>
        <li>Előre vállalt gyermek esetén házaspároknál legalább az egyik félnek 40 év alattinak kell lennie.</li>
        <li>A felújítást a folyósítástól számított <b>4 éven belül</b> be kell fejezni, és <b>10 év bentlakási kötelezettség</b> van.</li>
        <li>Kapcsolódó kamattámogatott hitel is igényelhető mellé: 2 gyermeknél 10, 3 vagy több gyermeknél 15 millió forint.</li>
      </ul>

      <div class="box warn">
        <span class="box-t">A településlista a kulcskérdés</span>
        A program 5 000 fő alatti, kedvezményezett kistelepülésekre, tanyákra és birtokközpontokra vonatkozik. A <b>hivatalos lista a 302/2023. Korm. rendelet 2. melléklete</b>, és időről időre módosul. Az interneten keringő településszámok (2 600, 2 900) forrásonként eltérnek, ezért igénylés előtt mindig a hatályos melléklet az irányadó. Ezt mi minden esetben ellenőrizzük.
      </div>
    </div>
  </div>
</section>

<!-- ═══ BABAVÁRÓ ═══ -->
<section class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">04</div>
      <h2 class="section-title" id="babavaro">Babaváró: kamatmentes, szabad felhasználású</h2>
      <p class="section-sub">Nem lakáscélhoz kötött, ezért önerőként is használható. Cserébe szigorú a korhatár.</p>
    </div>
    <div class="art">
      <ul class="clean">
        <li><b>Maximális összeg:</b> 11 millió forint, minimum 1 millió</li>
        <li><b>Futamidő:</b> 5-20 év, a törlesztési szüneteken felül</li>
        <li><b>Kamat:</b> a támogatási időszakban 0 százalék, mellette 0,5 százalék éves kezességvállalási díj a fennálló tőkére. A havi törlesztő legfeljebb <b>51 000 Ft</b></li>
        <li><b>Korhatár:</b> a feleség betöltötte a 18., de <b>még nem töltötte be a 35. életévét</b></li>
        <li><b>TB:</b> legalább az egyik félnél 3 év folyamatos jogviszony</li>
        <li><b>Feltétel:</b> házasság, büntetlen előélet, köztartozás-mentesség, negatív KHR-mentesség</li>
      </ul>

      <h3>Mit hoz a gyermekvállalás?</h3>
      <div class="nsteps">
        <div class="nstep"><div class="nstep-n">1</div><div><div class="nstep-t">Első gyermek</div><div class="nstep-d">A kamatmentesség <b>véglegessé válik</b> a teljes futamidőre, és 3 év törlesztési szünet jár (ikreknél 3 plusz 2 év).</div></div></div>
        <div class="nstep"><div class="nstep-n">2</div><div><div class="nstep-t">Második gyermek</div><div class="nstep-d">További 3 év törlesztési szünet, és a fennálló <b>tőketartozás 30 százalékának</b> elengedése.</div></div></div>
        <div class="nstep"><div class="nstep-n">3</div><div><div class="nstep-t">Harmadik gyermek</div><div class="nstep-d">A <b>teljes fennmaradó tőketartozás</b> elengedése. Innentől nincs mit visszafizetni.</div></div></div>
      </div>

      <div class="box quote">
        <b>A szankció, amit komolyan kell venni:</b> ha 5 éven belül nem születik gyermek, a felvett kamattámogatást 120 napon belül vissza kell fizetni, és a hitel piaci kamatozásúvá válik. Ez az a pont, ahol a legtöbb ember alábecsüli a kockázatot.
      </div>

      <div class="box info">
        <span class="box-t">2026-os változás: haladék a régi szerződéseknél</span>
        A 2019. július 1. és 2021. október 31. között felvett Babavárók esetében a gyermekvállalási határidőt <b>2026. július 1-ről 2026. november 1-re</b> tolták ki. Ez kb. 25 ezer házaspárt érint. Ha ez rád vonatkozik, most van egy szűk ablak, amiben érdemes végiggondolni a lehetőségeket.
      </div>
    </div>
  </div>
</section>

<!-- ═══ OTTHONTÁMOGATÁS ═══ -->
<section class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">05 · ÚJ</div>
      <h2 class="section-title" id="otthontamogatas">Otthontámogatás: 1 millió forint a közszférának</h2>
      <p class="section-sub">2026. január 1-től elérhető, vissza nem térítendő támogatás, kifejezetten közszférás dolgozóknak.</p>
    </div>
    <div class="art">
      <ul class="clean">
        <li><b>Kinek:</b> költségvetési szervek, önkormányzatok és egyes regisztrált munkáltatók alkalmazottai. A 2026. januári módosítás kiterjesztette önkormányzati tűzoltókra, egyházi hitoktatókra és képviselői munkatársakra is.</li>
        <li><b>Összeg:</b> nettó 1 000 000 forint, vissza nem térítendő</li>
        <li><b>Mire:</b> meglévő lakáshitel törlesztésére, új lakáshitel önerejére vagy törlesztésére, illetve munkáltatói kölcsönre</li>
        <li><b>Igénylés:</b> a munkáltatón keresztül, a Kincstár felé</li>
      </ul>
      <div class="box warn">
        <span class="box-t">Egy ponton ellentmondanak a hivatalos források</span>
        A Kincstár tájékoztatója <b>egyösszegű</b>, nettó 1 millió forintot ír, a kormányzati tájékoztató viszont <b>évi</b> nettó 1 millió forintként fogalmaz. A kettő között érdemi különbség van, ezért konkrét igénylésnél a 361/2025. Korm. rendelet hatályos szövegét kell megnézni. Ezt mi minden esetben ellenőrizzük, mielőtt bármit ígérnénk.
      </div>
      <div class="box info">
        <span class="box-t">Kapcsolódó: 35 év alattiak lakhatási támogatása</span>
        Ez nem otthonteremtési támogatás, hanem <b>béren kívüli juttatás</b>, de ugyanarra a problémára ad választ. A munkáltató havi legfeljebb 150 000 forinttal, évi 1,8 millió forintig támogathatja a 35 év alatti munkavállaló albérleti díját vagy lakáshitel-törlesztését, kedvezményes, 28 százalékos adóteher mellett. Ha fiatal vagy és albérletben laksz, ezt érdemes felvetni a munkáltatódnál: sokan nem is tudnak róla.
      </div>
    </div>
  </div>
</section>

<!-- ═══ KIFUTOTT ═══ -->
<section id="kifutott" class="section dark-sec">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">Fontos</div>
      <h2 class="section-title">Ami 2026-ban kifutott</h2>
      <p class="section-sub">Ezt a részt sok oldal kihagyja, pedig ez okozza a legtöbb csalódást: valaki olyan támogatásra tervez, ami már nem igényelhető.</p>
    </div>
    <div class="art wide">
      <div class="yn">
        <div class="yn-col no">
          <div class="yn-h">✕ Energetikai Otthonfelújítási Program</div>
          <ul>
            <li>Max. 5 millió Ft vissza nem térítendő + 5 millió Ft kamatmentes kölcsön volt</li>
            <li>2007 előtt épült családi házakra, min. 30% energiamegtakarítás mellett</li>
            <li><b style="color:#fff">Keretkimerülés miatt leállt: 2026. április 23-án országosan</b></li>
            <li>Újraindulásról nincs hivatalos bejelentés</li>
          </ul>
        </div>
        <div class="yn-col no">
          <div class="yn-h">✕ Vidéki Otthonfelújítási Program</div>
          <ul>
            <li>A felújítási költség 50 százaléka, max. 3 millió Ft volt</li>
            <li>5 000 fő alatti településeken, gyermekes családoknak és nyugdíjasoknak</li>
            <li><b style="color:#fff">Az igénylési időszak 2026. június 30-án lezárult</b></li>
            <li>Nincs bejelentett utódprogram</li>
          </ul>
        </div>
      </div>

      <div class="box info" style="background:rgba(140,197,189,.1);border-color:rgba(140,197,189,.3);color:rgba(255,255,255,.8);margin-top:1.8rem;">
        <span class="box-t" style="color:var(--teal-lite);">Akkor mi maradt felújításra?</span>
        Nem tűnt el minden lehetőség, csak a vissza nem térítendő, közvetlen felújítási támogatás. Ami 2026 őszén használható: a <b>Falusi CSOK korszerűsítési ága</b>, a kistelepülési áfa-visszatérítés, a <b>Babaváró</b> (mert szabad felhasználású), a lakástakarék, és a piaci felújítási hitelek. Melyik a jó, az a településtől, a gyermekszámtól és az összegtől függ.
      </div>

      <div class="box info" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);color:rgba(255,255,255,.75);">
        <span class="box-t" style="color:#fff;">Egy harmadik változás, ami a hitelképességet érinti</span>
        2026. január 1-től az MNB adósságfék-szabályában a magasabb, 60 százalékos törlesztési korlát jövedelemküszöbe <b>600 ezer forintról 800 ezer forintra emelkedett</b>. Akinek a nettó jövedelme e két összeg közé esik, annak romlott a hitelképessége: 20 éves futamidőn ez több millió forinttal kisebb felvehető hitelt jelenthet. A <a href="kalkulator.html#jtm" style="color:var(--teal-lite);">JTM-kalkulátorunk</a> már ezzel a küszöbbel számol.
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
      <a class="rel-c" href="kviz.html"><div class="rel-i">✅</div><div><div class="rel-t">Otthon Start kvíz</div><div class="rel-d">12 kérdés, 2 perc</div></div></a>
      <a class="rel-c" href="kalkulator.html"><div class="rel-i">🧮</div><div><div class="rel-t">Hitelkalkulátorok</div><div class="rel-d">Törlesztő, JTM, kiváltás</div></div></a>
      <a class="rel-c" href="lakashitel-folyamat.html"><div class="rel-i">🗺️</div><div><div class="rel-t">A lakáshitel folyamata</div><div class="rel-d">Mi történik és mikor</div></div></a>
    </div>
  </div>
</section>
'''

FAQ = [
("Kombinálhatom egymással a támogatásokat?",
 ["Több esetben igen. Az Otthon Start kombinálható CSOK Plusszal, Falusi CSOK-kal, az önerőként felhasznált Babaváróval és az áfa-visszatérítéssel is.",
  "A sorrend és az időzítés viszont nem mindegy: egy rosszul sorrendezett igénylés miatt el lehet esni egy másik támogatástól. Ez az egyik olyan pont, ahol a legtöbbet tudjuk segíteni, mert a kombinációk feltételrendszere összetett."]),

("Ha volt már ingatlanom, biztosan kiesek az Otthon Startból?",
 ["Nem feltétlenül. A tízéves tulajdonmentességi szabály alól <b>több kivétel</b> van: 15 millió forint alatti értékű korábbi ingatlan, legfeljebb 50 százalékos tulajdoni hányad, bontásra ítélt ingatlan, haszonélvezettel terhelt tulajdon, vagy örökölt közös tulajdon kivásárlása.",
  "A tapasztalat az, hogy sokan tévesen zárják ki magukat. Ha bizonytalan vagy, érdemes átnézetni, mielőtt lemondasz róla."]),

("Mi történik, ha a vállalt gyermek nem születik meg?",
 ["A CSOK Plusznál a támogatást vissza kell fizetni, késedelmi kamattal. A Babavárónál, ha 5 éven belül nem születik gyermek, a felvett kamattámogatást 120 napon belül vissza kell fizetni, és a hitel piaci kamatozásúvá válik.",
  "Ezért a gyermekvállaláshoz kötött konstrukciókat csak akkor érdemes választani, ha a gyermekvállalás egyébként is reális terv. Nem szabad a támogatás miatt vállalni."]),

("Meddig lesznek még elérhetők ezek a programok?",
 ["Az Otthon Start, a CSOK Plusz, a Falusi CSOK és a Babaváró jogszabálya jelenleg <b>nem tartalmaz végső igénylési határidőt</b>. Ez azonban nem jelent garanciát: a programok költségvetési és szabályozási döntéstől függenek, és 2026 folyamán több otthonteremtési program ki is futott.",
  "Az Otthon Start felülvizsgálata 2026 szeptemberében folyamatban van. Ha a te helyzetedbe illik a program, a halogatásnak most valós kockázata van."]),

("Egyedülállóként igényelhetek támogatást?",
 ["Az Otthon Startot igen, mert nem köti házassághoz. A Falusi CSOK-ot egyedülálló szülő is igényelheti meglévő gyermekek után, életkortól függetlenül.",
  "A CSOK Plusz és a Babaváró viszont <b>házassághoz kötött</b>, ezekhez házassági anyakönyvi kivonat kell. Ez sokakat meglep, ezért érdemes előre tisztázni."]),

("Van még bármilyen felújítási támogatás?",
 ["Közvetlen, vissza nem térítendő felújítási támogatás 2026 szeptemberében nincs: az energetikai program 2026 áprilisában keretkimerülés miatt leállt, a Vidéki Otthonfelújítási Program 2026. június 30-án lezárult, és egyiknek sincs bejelentett utódja.",
  "Ami maradt: a Falusi CSOK korszerűsítési ága, a kistelepülési áfa-visszatérítés, a szabad felhasználású Babaváró, a lakástakarék és a piaci felújítási hitelek. Ezek közül melyik jöhet szóba, az a településtől és a gyermekszámtól függ."]),

("Mennyi idő az ügyintézés?",
 ["A Babaváró kérelmét a hitelintézet a benyújtástól számított 10 munkanapon belül bírálja el. Lakáshitelnél a teljes folyamat az igényléstől a folyósításig átlagosan másfél hónap, jó előkészítéssel rövidíthető.",
  "Ami a leginkább lassít: a hiányosan benyújtott dokumentáció. Ezért kezdjük mindig azzal, hogy pontosan összeállítjuk, mire van szükség."]),

("Mennyibe kerül nekem, ha rajtatok keresztül igénylem?",
 ["Semmibe. A támogatás összegét és feltételeit jogszabály rögzíti, tehát nálunk pontosan ugyanazt kapod, mint bárhol máshol. A mi munkánkat a pénzintézet fizeti.",
  "Amit kapsz cserébe: átnézzük, mire vagy jogosult, milyen sorrendben érdemes igényelni, és a papírmunka nagy részét levesszük rólad."]),
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

LEGAL = (u'<b>*</b> Az oldalon szereplő adatok tájékoztató jellegűek, a <b>2026. szeptemberi</b> jogszabályi állapotot tükrözik, és nem minősülnek '
         u'ajánlattételnek, ajánlattételi felhívásnak, THM-tájékoztatásnak vagy jogi tanácsadásnak. Az otthonteremtési támogatások feltételrendszerét '
         u'kormányrendeletek szabályozzák, amelyek év közben is módosulhatnak; konkrét igénylésnél minden esetben a hatályos rendeleti szöveg az irányadó. '
         u'Az Otthon Start feltételeit a 227/2025. (VII. 31.) Korm. rendelet, a CSOK Pluszt az 518/2023. (XI. 30.) Korm. rendelet, a kistelepülési '
         u'támogatásokat a 302/2023. (VII. 11.) Korm. rendelet, az Otthontámogatást a 361/2025. (XI. 25.) Korm. rendelet tartalmazza; a Falusi CSOK '
         u'kedvezményezett településeinek hivatalos listája a 302/2023. Korm. rendelet 2. melléklete. A támogatásra való jogosultságot minden esetben '
         u'a hitelintézet, illetve az eljáró hatóság állapítja meg, egyedi vizsgálat alapján. Az Otthon Start program szakmai és jogi felülvizsgálata '
         u'2026 szeptemberében folyamatban van; a már megkötött szerződések feltételei nem változnak. Az Energetikai Otthonfelújítási Program 2026. '
         u'április 23-án, a Vidéki Otthonfelújítási Program 2026. június 30-án lezárult. Adatok érvényessége: <b data-upd></b>.')

build('tamogatasok.html',
      u'Állami támogatások 2026: Otthon Start, CSOK Plusz, Babaváró | EAGLZ Finance',
      u'Melyik otthonteremtési támogatás jár neked 2026-ban? Otthon Start, CSOK Plusz, Falusi CSOK, Babaváró és Otthontámogatás feltételei, összegei, és ami idén kifutott.',
      BODY, LEGAL,
      u'Nézzük meg, mire vagy jogosult valójában.',
      u'Egy díjmentes beszélgetésen átnézzük, melyik programba férsz bele, milyen sorrendben érdemes igényelni, és mekkora összeg jöhet ki a te helyzetedben.')
