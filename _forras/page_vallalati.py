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
    <h1 class="sub-h1">Vállalati megoldások: <em>finanszírozás, juttatás, védelem</em></h1>
    <p class="sub-lead">Kedvezményes vállalkozói hitel, adóhatékony béren kívüli juttatás és céges biztosítás, egy kézben. Ezen az oldalon a 2026-os feltételek szerepelnek, beleértve azt is, ami az idén megváltozott a Széchenyi Kártya Programban.</p>
    <div class="sub-chips">
      <div class="sub-chip">🏦 <b>750 M Ft</b>-ig beruházási hitel</div>
      <div class="sub-chip">🎁 <b>570 000 Ft</b> SZÉP-keret</div>
      <div class="sub-chip">📅 Adatok: <b data-upd></b></div>
    </div>
    <div class="quicknav">
      <a href="#szechenyi" class="qn on">🏦 Széchenyi Kártya</a>
      <a href="#cafeteria" class="qn">🎁 Cafeteria</a>
      <a href="#biztositas" class="qn">🛡️ Céges biztosítás</a>
      <a href="index.html#advisors" class="qn">📅 Időpontot foglalok</a>
    </div>
  </div>
</section>

<section class="section" style="background:#fff;padding-bottom:2.4rem;">
  <div class="container">
    <div class="toc">
      <div class="toc-t">Ezen az oldalon</div>
      <ol>
        <li><a href="#szechenyi">Széchenyi Kártya Program</a></li>
        <li><a href="#valtozas">Ami 2026-ban megváltozott</a></li>
        <li><a href="#cafeteria">Cafeteria és juttatások</a></li>
        <li><a href="#lakhatas">Lakhatási támogatás 35 alatt</a></li>
        <li><a href="#biztositas">Céges biztosítások</a></li>
        <li><a href="#alulbiztositas">Az alulbiztosítás csapdája</a></li>
        <li><a href="#kotelezo">Kinek kötelező biztosítás</a></li>
        <li><a href="#gyik">Gyakori kérdések</a></li>
      </ol>
    </div>
    <div class="art">
      <h2>Három terület, egy logika</h2>
      <p class="lead">Egy kkv-nál a pénzügyek három irányba mennek: <b>honnan jön a forrás</b>, <b>hogyan juttatsz értéket a munkavállalóidnak</b>, és <b>mi történik, ha baj van</b>. A három összefügg, mégis a legtöbb cég három külön helyen intézi, három különböző emberrel, akik nem tudnak egymásról.</p>
      <p>Mi a hármat együtt nézzük, és a céges oldalt összehangoljuk a magánpénzügyeiddel. Egy ügyvezetőnél ez a kettő gyakorlatilag ugyanaz a zseb.</p>
    </div>
  </div>
</section>

<!-- ═══ SZÉCHENYI ═══ -->
<section id="szechenyi" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">01</div>
      <h2 class="section-title">Széchenyi Kártya Program: kedvezményes kkv-hitel</h2>
      <p class="section-sub">Az ország legnagyobb támogatott vállalkozói hitelprogramja. 2015 óta mintegy 4 500 milliárd forintot helyezett ki, évente nagyjából 30 ezer vállalkozásnak.</p>
    </div>
    <div class="art wide">
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Konstrukció</th><th>Max. összeg</th><th>Futamidő</th><th>Kamat</th></tr></thead>
          <tbody>
            <tr class="hl"><td>Beruházási Hitel MAX+</td><td><b>750 M Ft</b></td><td>13-120 hónap</td><td><b>3% fix</b>; zöld célra 1,5% fix</td></tr>
            <tr><td>Folyószámlahitel MAX+</td><td>250 M Ft</td><td>1-3 év</td><td>3 havi BUBOR</td></tr>
            <tr><td>Likviditási Hitel MAX+</td><td>250 M Ft</td><td>max. 3 év</td><td>3 havi BUBOR</td></tr>
            <tr><td>Turisztikai Kártya MAX+</td><td>250-300 M Ft</td><td>max. 3 év</td><td>3 havi BUBOR</td></tr>
            <tr><td>Agrár Beruházási Hitel MAX+</td><td>750 M Ft</td><td>max. 10 év</td><td>támogatott</td></tr>
          </tbody>
        </table>
      </div>
      <p class="tbl-note">A konstrukciók hatályos kondícióit a KAVOSZ üzletszabályzata rögzíti, és ez időről időre módosul. A fenti adatok tájékoztató jellegűek, a pontos feltételeket minden esetben az igényléskor hatályos üzletszabályzat alapján ellenőrizzük.</p>

      <h3>Ki jogosult?</h3>
      <ul class="clean">
        <li>Kkv-minősítés: mikro-, kis- vagy középvállalkozás. A Mikrohitel MAX+ középvállalkozásnak nem elérhető.</li>
        <li>Nincs lejárt köztartozás és lejárt hiteltartozás.</li>
        <li>Legalább <b>1 lezárt teljes üzleti év</b>; 150 millió forint feletti igénylésnél 2 lezárt év.</li>
        <li>Beruházási hitelnél legalább <b>10 százalék önerő</b>.</li>
        <li>A hitelhez <b>80 százalékos állami készfizető kezesség</b> kapcsolódik, ami sok esetben fedezethiány mellett is lehetővé teszi a hitelfelvételt.</li>
      </ul>

      <h3>Hol igényelhető?</h3>
      <p>Kizárólag a <b>KAVOSZ országos irodahálózatán</b> keresztül, valamint VOSZ-irodákban és a kereskedelmi és iparkamaráknál. A regisztráló irodai közreműködés díjmentes: az iroda állítja össze és továbbítja a dokumentációt a választott banknak. Bankfiókban közvetlenül nem igényelhető.</p>
    </div>
  </div>
</section>

<!-- ═══ VÁLTOZÁS ═══ -->
<section id="valtozas" class="section dark-sec">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">Fontos</div>
      <h2 class="section-title">Ami 2026-ban megváltozott</h2>
      <p class="section-sub">Ez a rész sok helyen elavult, pedig a különbség a havi törlesztőben azonnal látszik.</p>
    </div>
    <div class="art wide">
      <div class="box stop" style="background:rgba(232,69,122,.09);border-color:rgba(232,69,122,.3);color:rgba(255,255,255,.82);">
        <span class="box-t" style="color:#F2799F;">A likviditási termékek kamata már nem fix 3 százalék</span>
        2026. július 15-től a <b style="color:#fff">Folyószámlahitel MAX+</b>, a <b style="color:#fff">Likviditási Hitel MAX+</b> és a <b style="color:#fff">Turisztikai Kártya MAX+</b> kamata a korábbi fix 3 százalék helyett <b style="color:#fff">3 havi BUBOR</b>. Ez a gyakorlatban érdemben magasabb kamatot jelent, és mivel változó, a törlesztő is mozogni fog. A 2026. június 18-ig beadott kérelmek még július 14-ig szerződhettek a régi, fix 3 százalékos kamattal.
      </div>
      <div class="box info" style="background:rgba(140,197,189,.1);border-color:rgba(140,197,189,.3);color:rgba(255,255,255,.8);">
        <span class="box-t" style="color:var(--teal-lite);">A beruházási hitel maradt fix</span>
        A <b style="color:#fff">Beruházási Hitel MAX+</b> kamata nem változott: továbbra is fix 3 százalék, zöld és fenntarthatósági célra 1,5 százalék. Ez ma az egyik legkedvezőbb vállalkozói forrás a piacon, és pont ezért érdemes megnézni, hogy egy tervezett fejlesztés belefér-e.
      </div>
      <div class="box info" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);color:rgba(255,255,255,.75);">
        <span class="box-t" style="color:#fff;">Agrár oldalon bővülés</span>
        2026. április 1-től az Agrár Széchenyi Beruházási Hitel MAX+ négy új támogatási jogcímmel bővült. A lényeg gyakorlati: <b style="color:#fff">a kimerült de minimis keret sem jelent automatikusan akadályt</b>, mert csoportmentességi támogatási formában is elérhetővé vált. Sok gazdálkodó emiatt esett ki korábban.
      </div>

      <div class="yn">
        <div class="yn-col ok">
          <div class="yn-h">✓ Mikor éri meg most</div>
          <ul>
            <li>Konkrét beruházás van, ami a 3 százalékos fix hitelbe belefér</li>
            <li>Zöld vagy energetikai fejlesztés, mert ott 1,5 százalék</li>
            <li>Van legalább egy lezárt üzleti év és tiszta köztartozás</li>
            <li>Fedezet hiányzik, de a 80 százalékos kezesség megoldja</li>
          </ul>
        </div>
        <div class="yn-col no">
          <div class="yn-h">✕ Mikor gondold át</div>
          <ul>
            <li>Csak forgóeszköz-finanszírozás kell, mert ott már BUBOR-os a kamat</li>
            <li>Bizonytalan az árbevétel, és a változó kamat kockázatot jelent</li>
            <li>Kizárólag azért vennél fel hitelt, mert olcsó</li>
            <li>Nincs lezárt üzleti év, mert akkor még nem vagy jogosult</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ CAFETERIA ═══ -->
<section id="cafeteria" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">02</div>
      <h2 class="section-title">Cafeteria: ugyanabból a pénzből 30 százalékkal több</h2>
      <p class="section-sub">A béren kívüli juttatás adóterhe lényegesen alacsonyabb a béré­nél. A különbség nem marketing, hanem számtan.</p>
    </div>
    <div class="art">
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>100 Ft nettó a dolgozó kezébe</th><th>Munkáltatói költség</th></tr></thead>
          <tbody>
            <tr><td>Bruttó bérként</td><td>kb. <b>170 Ft</b></td></tr>
            <tr class="hl"><td>SZÉP-kártyán vagy lakhatási támogatásként</td><td><b>128 Ft</b></td></tr>
          </tbody>
        </table>
      </div>
      <p class="tbl-note">Saját számítás a hatályos kulcsokkal: 13% szocho munkáltatói oldalon, 15% szja és 18,5% tb munkavállalói oldalon, béren kívüli juttatásnál 15% szja + 13% szocho. Kiva-alany munkáltatónál a juttatás terhe 25 százalék. A tényleges adóteher egyedi helyzettől függ.</p>
      <p>Másképp fogalmazva: <b>ugyanabból a munkáltatói ráfordításból nagyjából 30 százalékkal több érték jut a dolgozóhoz</b>, ha a kereten belüli juttatási formát választod. Cserébe a pénz célhoz kötött, nem szabadon elkölthető.</p>

      <h3>SZÉP kártya 2026</h3>
      <div class="kpis">
        <div class="kpi"><b>450 000 Ft</b><span>éves rekreációs keret</span></div>
        <div class="kpi"><b>120 000 Ft</b><span>Aktív Magyarok alszámla</span></div>
        <div class="kpi"><b>570 000 Ft</b><span>összesen egy évben</span></div>
        <div class="kpi"><b>28%</b><span>adóteher a kereten belül</span></div>
      </div>
      <ul class="clean">
        <li>A régi három alszámla megszűnt: egységes rekreációs számla van, <b>plusz</b> a külön Aktív Magyarok alszámla.</li>
        <li>Az Aktív Magyarok keretről <b>nem lehet átvezetni</b> a fő számlára, és csak a kártyabirtokos használhatja, társkártyás nem.</li>
        <li>A rekreációs keret szálláshelyre, melegkonyhás vendéglátásra, wellnessre, szabadidős és kulturális szolgáltatásra költhető.</li>
        <li>Az Aktív Magyarok keret sportszolgáltatásra: konditerem, uszoda, sípálya, aktív szabadidős programok.</li>
        <li>A kereten felüli rész adóterhe magasabb, nagyjából 33 százalék.</li>
      </ul>

      <div class="box warn">
        <span class="box-t">Két lehetőség, ami 2026-ban kifutott</span>
        A <b>SZÉP-kártyás lakásfelújítás</b> lehetősége 2026. január 1-jén megszűnt: 2025-ben a keret fele volt fordítható építőanyagra, bútorra, világításra, ez már nem él. A <b>hideg élelmiszer</b> vásárlása a teljes egyenlegből szintén átmeneti lehetőség volt, 2026. április 30-án lejárt. Sok cafeteria-szabályzat még mindig ezekkel számol.
      </div>

      <h3>Adómentes elemek, amik mellette elférnek</h3>
      <p>Ezek nem terhelik a SZÉP-keretet, és sok cégnél kihasználatlanok: bölcsődei és óvodai térítési díj, kulturális és sportbelépő a minimálbérig, munkába járás költségtérítése, diákhitel-törlesztés támogatása, valamint a home office-átalány.</p>
    </div>
  </div>
</section>

<!-- ═══ LAKHATÁS ═══ -->
<section id="lakhatas" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">Kiemelt</div>
      <h2 class="section-title">Lakhatási támogatás 35 év alatt: évi 1,8 millió</h2>
      <p class="section-sub">Ez ma a legerősebb, mégis legkevésbé kihasznált juttatási forma. Ha fiatal munkavállalóid vannak, érdemes tudni róla.</p>
    </div>
    <div class="art">
      <div class="kpis">
        <div class="kpi"><b>150 000 Ft</b><span>havonta adható maximum</span></div>
        <div class="kpi"><b>1 800 000 Ft</b><span>éves keret</span></div>
        <div class="kpi"><b>28%</b><span>adóteher (kiva-nál 25%)</span></div>
        <div class="kpi"><b>35 év</b><span>felső korhatár</span></div>
      </div>
      <ul class="clean">
        <li>Albérleti díjra <b>vagy</b> lakáshitel-törlesztésre fordítható.</li>
        <li>A SZÉP-kerettől <b>függetlenül</b> adható, tehát nem esik bele az 570 ezer forintba.</li>
        <li>Az utolsó jogosult hónap az, amelyben a munkavállaló betölti a 35. életévét.</li>
        <li>Albérletnél <b>írásos bérleti szerződés</b> szükséges; családnál vagy ismerősnél lakás esetén nem adható.</li>
        <li>A munkáltatónak adatszolgáltatási kötelezettsége van, január 31-ig.</li>
      </ul>
      <div class="box info">
        <span class="box-t">Miért ez a legjobb ár-érték arányú juttatás ma</span>
        Egy pályakezdőnél az albérlet a legnagyobb havi kiadás. Évi 1,8 millió forint kedvezményes adózású támogatás nagyjából ugyanakkora, mint egy érdemi béremelés, csak a munkáltatónak <b>jóval olcsóbb</b>. Toborzásnál és megtartásnál ez ma erősebb érv, mint a szokásos juttatási csomag.
      </div>
      <div class="box quote">
        2026-ban indult emellett a <b>közszolgálati lakhatási támogatás</b> is: pedagógusoknak, rendőröknek, ápolóknak és orvosoknak évi legfeljebb 1 millió forint, a 35 év alattiaknak szóló támogatás mellett is igénybe vehető.
      </div>
    </div>
  </div>
</section>

<!-- ═══ BIZTOSÍTÁS ═══ -->
<section id="biztositas" class="section" style="background:#fff;">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-teal">03</div>
      <h2 class="section-title">Céges biztosítások: mi ellen érdemes védekezni</h2>
      <p class="section-sub">Egy kkv-nál nem az a kérdés, hogy lesz-e kár, hanem hogy melyik kár tudja megállítani a működést.</p>
    </div>
    <div class="art wide">
      <div class="tiles">
        <div class="tile"><div class="tile-i">🏢</div><div class="tile-t">Vagyonbiztosítás</div><div class="tile-d">Épület, gép, készlet, elektronika. Érdemes <b>üzemszünet-biztosítással</b> kiegészíteni: sokszor nem a kár összege fáj, hanem a leállás.</div></div>
        <div class="tile"><div class="tile-i">⚖️</div><div class="tile-t">Felelősségbiztosítás</div><div class="tile-d">Ha a tevékenységeddel harmadik személynek okozol kárt. Több szakmánál ennek <b>szakmai változata kötelező</b>.</div></div>
        <div class="tile"><div class="tile-i">👷</div><div class="tile-t">Munkáltatói felelősség</div><div class="tile-d">Üzemi baleset esetén a munkáltató kártérítési felelőssége szigorú. Ez a fedezet ezt veszi át.</div></div>
        <div class="tile"><div class="tile-i">🎩</div><div class="tile-t">Vezető tisztségviselői (D&amp;O)</div><div class="tile-d">Az ügyvezető a Ptk. szerint <b>saját vagyonával is felelhet</b> a döntéseiért. Ez a fedezet erre szól.</div></div>
        <div class="tile"><div class="tile-i">🚚</div><div class="tile-t">Flotta</div><div class="tile-d">KGFB és casco céges járművekre, egy szerződésben. Több jármű fölött jellemzően kedvezőbb, mint egyesével.</div></div>
        <div class="tile"><div class="tile-i">🔐</div><div class="tile-t">Kiberbiztosítás</div><div class="tile-d">Zsarolóvírus, adatvédelmi incidens, üzemszünet. A kkv-knál ez ma a leggyorsabban növekvő kockázat, és a legritkábban fedezett.</div></div>
        <div class="tile"><div class="tile-i">🤝</div><div class="tile-t">Kulcsember-biztosítás</div><div class="tile-d">Ha a cég bevétele egy-két emberen múlik, az ő kiesésük <b>a céget viszi magával</b>. Ez a fedezet időt vásárol.</div></div>
        <div class="tile"><div class="tile-i">❤️</div><div class="tile-t">Csoportos élet és baleset</div><div class="tile-d">Munkavállalói juttatásként is működik, és jellemzően olcsóbb, mint az egyéni szerződések összege.</div></div>
        <div class="tile"><div class="tile-i">📦</div><div class="tile-t">Szállítmány, jogvédelem, hitelbiztosítás</div><div class="tile-d">Kereskedelmi és logisztikai cégeknél ezek a leggyakoribb kiegészítők.</div></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ ALULBIZTOSÍTÁS ═══ -->
<section id="alulbiztositas" class="section dark-sec">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-gold">Amire figyelj</div>
      <h2 class="section-title">Az alulbiztosítás csapdája</h2>
      <p class="section-sub">A leggyakoribb és legdrágább hiba a céges vagyonbiztosításnál. Nem az, hogy nincs biztosítás, hanem hogy kevesebbre szól, mint kellene.</p>
    </div>
    <div class="art">
      <div class="box stop" style="background:rgba(232,69,122,.09);border-color:rgba(232,69,122,.3);color:rgba(255,255,255,.82);">
        <span class="box-t" style="color:#F2799F;">Így működik a pro rata kártérítés</span>
        A Ptk. szerint ha a biztosítási összeg kisebb a biztosított vagyon értékénél, a biztosító a kárt <b style="color:#fff">arányosan</b> téríti meg. Példa: 100 millió forint értékű vagyon 60 millióra biztosítva, a kár 10 millió. A biztosító nem 10 milliót fizet, hanem <b style="color:#fff">6 milliót</b>, pedig a kár jóval a biztosítási összeg alatt van. Ez az, amit a legtöbb cégvezető félreért.
      </div>
      <h3 style="color:#fff;">Öt tipikus hiba</h3>
      <ol style="color:rgba(255,255,255,.72);">
        <li><b style="color:#fff">Könyv szerinti értéken biztosítanak.</b> Az amortizált gépsor könyv szerint 2 millió, újra megvenni 20 millió. A biztosításnak a pótlási értéket kell fednie.</li>
        <li><b style="color:#fff">Épületnél forgalmi értéket adnak meg.</b> Kár esetén nem eladni kell az épületet, hanem újjáépíteni, és az más összeg.</li>
        <li><b style="color:#fff">Bővítés után nem emelik a biztosítási összeget.</b> Az új csarnok, az új gép beépül a vagyonba, a szerződés viszont marad a régi.</li>
        <li><b style="color:#fff">Elmarad az éves értékkövetés felülvizsgálata.</b> Néhány év magasabb infláció csendben jelentős alulbiztosítást halmoz.</li>
        <li><b style="color:#fff">A vagyonösszetétel változását nem jelentik be.</b> Új készlet, új telephely, új tevékenység. Ha nincs bejelentve, nincs fedezve.</li>
      </ol>
      <div class="box info" style="background:rgba(140,197,189,.1);border-color:rgba(140,197,189,.3);color:rgba(255,255,255,.8);">
        <span class="box-t" style="color:var(--teal-lite);">Amit ilyenkor csinálunk</span>
        Végigmegyünk a vagyonelemeken, és <b style="color:#fff">pótlási értéken</b> vesszük fel őket, nem könyv szerintin. Ez néha kellemetlen beszélgetés, mert magasabb díjat jelent, de a különbség egy kárnál derül ki, és akkor már nem lehet javítani.
      </div>
    </div>
  </div>
</section>

<!-- ═══ KÖTELEZŐ ═══ -->
<section id="kotelezo" class="section graph-light">
  <div class="container">
    <div class="sec-head">
      <div class="label-chip chip-purple">Jogszabály</div>
      <h2 class="section-title">Kinek kötelező a szakmai felelősségbiztosítás?</h2>
      <p class="section-sub">Általános, minden cégre kiterjedő kötelező céges biztosítás nincs. Bizonyos tevékenységeknél viszont a működés feltétele.</p>
    </div>
    <div class="art">
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Tevékenység</th><th>Megjegyzés</th></tr></thead>
          <tbody>
            <tr><td>Ügyvéd</td><td>e nélkül nem praktizálhat, a kamara nyilvántartja</td></tr>
            <tr><td>Utazásszervező, -közvetítő</td><td><b>vagyoni biztosíték</b>: az árbevétel meghatározott százaléka, minimumösszeggel</td></tr>
            <tr><td>Könyvvizsgáló, könyvelő, adótanácsadó</td><td>kamarai és ágazati szabályozás szerint</td></tr>
            <tr><td>Társasházkezelő, ingatlankezelő</td><td>üzletszerű tevékenységnél kötelező</td></tr>
            <tr><td>Vagyonvédelmi vállalkozás, vagyonőr</td><td>személy- és vagyonvédelmi törvény</td></tr>
            <tr><td>Hitel- és biztosításközvetítő</td><td>a biztosítási tevékenységről szóló törvény</td></tr>
            <tr><td>Építész, műszaki tervező</td><td>kamarai szabályozás</td></tr>
            <tr><td>Orvos, állatorvos</td><td>egészségügyi, illetve állategészségügyi szabályozás</td></tr>
            <tr><td>Bírósági végrehajtó, szabadalmi ügyvivő, szakfordító</td><td>ágazati szabályozás</td></tr>
          </tbody>
        </table>
      </div>
      <p class="tbl-note">A minimális biztosítási összegek szakmánként eltérnek, és az adott kamarai szabályzat vagy jogszabály rögzíti őket. Konkrét esetben mindig a hatályos szöveget nézzük meg.</p>

      <h3>És a társasházak?</h3>
      <p>A társasház <b>épületbiztosítása nem kötelező</b>: nincs olyan jogszabály, amely előírná. A <b>társasházkezelő, illetve a közös képviselő felelősségbiztosítása</b> viszont üzletszerű tevékenységnél igen, és ez fontos különbség: a közös képviselő a hibás ügyvitelért saját vagyonával is felelhet.</p>
      <p>A gyakorlatban a társasházak túlnyomó többsége mégis köt közösségi épületbiztosítást, mert enélkül egy nagyobb kár, például egy tűz vagy egy vezetéktörés, közvetlen tulajdonosi befizetést jelent.</p>
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
      <a class="rel-c" href="biztositasok.html"><div class="rel-i">🛡️</div><div><div class="rel-t">Biztosítások</div><div class="rel-d">KGFB, lakás, élet, egészség</div></div></a>
      <a class="rel-c" href="nyugdij.html"><div class="rel-i">🌅</div><div><div class="rel-t">Nyugdíj-megtakarítás</div><div class="rel-d">Ügyvezetőként is fontos</div></div></a>
      <a class="rel-c" href="befektetesek.html"><div class="rel-i">📈</div><div><div class="rel-t">Befektetések</div><div class="rel-d">A céges pénz mellé</div></div></a>
    </div>
  </div>
</section>
'''

FAQ = [
("Miért nem a bankfiókban igényeljem a Széchenyi hitelt?",
 ["Mert ott nem lehet. A Széchenyi Kártya Program konstrukciói <b>kizárólag a KAVOSZ regisztráló irodahálózatán</b> keresztül igényelhetők, VOSZ-irodákban és a kereskedelmi és iparkamaráknál. Az iroda állítja össze a dokumentációt, és továbbítja a választott banknak.",
  "A regisztráló irodai közreműködés díjmentes. A mi szerepünk az, hogy előtte átnézzük, melyik konstrukció illik a cégedhez, és hogy a beruházási vagy a likviditási ág a jobb út."]),

("Megéri még a Széchenyi hitel a kamatváltozás után?",
 ["A beruházási ágon egyértelműen: a Beruházási Hitel MAX+ kamata továbbra is <b>fix 3 százalék</b>, zöld célra 1,5. Ez ma a piac egyik legkedvezőbb vállalkozói forrása.",
  "A likviditási ágon már árnyaltabb a kép, mert ott 2026. július 15-től 3 havi BUBOR a kamat, ami magasabb és változó. Forgóeszköz-finanszírozásnál ezért érdemes összevetni a piaci ajánlatokkal is, nem automatikusan ezt választani."]),

("Mennyit spórolok a cafeteriával a béremeléshez képest?",
 ["Nagyjából 25 százalékot a munkáltatói költségen, vagy másképp nézve ugyanabból a ráfordításból kb. 30 százalékkal több érték jut a dolgozóhoz. A béren kívüli juttatás adóterhe 28 százalék, a bruttó béré a munkáltatói és munkavállalói oldalt együtt nézve lényegesen magasabb.",
  "A korlát az, hogy a juttatás <b>célhoz kötött</b> és keretes. A kereten felül az előny lecsökken, ezért a jó cafeteria-szabályzat pont a kereteket használja ki."]),

("Kötelező-e biztosítást kötnöm a cégemre?",
 ["Általános, minden cégre kiterjedő kötelező biztosítás nincs. Az egyetlen univerzális kötelezettség a KGFB, de az is a gépjárműhöz kötődik, nem a céghez.",
  "Bizonyos tevékenységeknél viszont a <b>szakmai felelősségbiztosítás a működés feltétele</b>, és hiánya a tevékenység megtiltásáig terjedő következménnyel járhat. Ügyvédnél, utazásszervezőnél, könyvvizsgálónál, társasházkezelőnél és több más szakmánál ez a helyzet."]),

("Mit jelent az, hogy alulbiztosított vagyok?",
 ["Azt, hogy a szerződésben szereplő biztosítási összeg kisebb, mint a biztosított vagyon tényleges értéke. Ilyenkor a biztosító a kárt <b>arányosan</b> téríti: ha a vagyon fele van biztosítva, a kár felét fizeti, akkor is, ha a kár összege bőven belefért volna a biztosítási összegbe.",
  "A leggyakoribb ok, hogy a vagyont könyv szerinti, amortizált értéken vették fel, nem pótlási értéken. Ezt egy vagyonfelmérésen lehet rendezni, és jellemzően nem is olyan drága, mint amire számítanak."]),

("Ügyvezetőként mit érdemes a magánpénzügyeimből is átgondolni?",
 ["Három dolgot. Egy: van-e olyan kulcsember-kockázat, ami téged érint, mert ha a bevétel rajtad múlik, a te kiesésed a cégre is hat. Kettő: a vezető tisztségviselői felelősség, mert a Ptk. szerint saját vagyonoddal is felelhetsz.",
  "Három: a nyugdíjcélú öngondoskodás. Vállalkozóként nincs mögötted munkáltatói pénztári befizetés, és a jövedelmed sem feltétlenül egyenletes. Az adó-visszatérítéses formákat itt is érdemes kihasználni."]),

("Nem szeretnék a meglévő biztosítómtól elmenni. Van értelme a beszélgetésnek?",
 ["Igen, mert nem az a cél, hogy váltsál. Sok esetben az derül ki, hogy a meglévő szerződés rendben van, csak a biztosítási összeg elavult, vagy hiányzik mellőle egy fedezet, amit ugyanannál a biztosítónál is fel lehet venni.",
  "Ha viszont jobb ajánlat van a piacon, azt megmutatjuk, és rád bízzuk a döntést."]),
]

BODY = BODY.replace('__FAQ__', faq_html(FAQ))

LEGAL = (u'<b>*</b> Az oldalon szereplő adatok tájékoztató jellegűek, a <b>2026. szeptemberi</b> állapotot tükrözik, és nem minősülnek ajánlattételnek, '
         u'ajánlattételi felhívásnak, THM-tájékoztatásnak, adó- vagy jogi tanácsadásnak. A Széchenyi Kártya Program konstrukcióinak hatályos kondícióit '
         u'(összeghatárok, futamidők, kamatok, jogosultsági feltételek) a mindenkori KAVOSZ üzletszabályzat rögzíti, amely év közben is módosulhat; '
         u'a 2026. július 15-től hatályos kamatmodell szerint a Folyószámlahitel MAX+, a Likviditási Hitel MAX+ és a Turisztikai Kártya MAX+ kamata '
         u'3 havi BUBOR, amely változó kamat. A béren kívüli juttatások kereteire és adóterhére vonatkozó adatok az szja-törvény és a szocho-törvény '
         u'hatályos rendelkezésein alapulnak; a bemutatott költség-összehasonlítás saját számítás, egyedi helyzettől függően eltérhet, és nem helyettesíti '
         u'a könyvelői vagy adótanácsadói véleményt. A kötelező szakmai felelősségbiztosítások köre és minimális biztosítási összege ágazati jogszabályok '
         u'és kamarai szabályzatok szerint alakul. Az alulbiztosítás jogkövetkezményére vonatkozó leírás a Ptk. 6:460. §-án alapul. '
         u'Adatok érvényessége: <b data-upd></b>.')

build('vallalati.html',
      u'Vállalati megoldások 2026: Széchenyi hitel, cafeteria, céges biztosítás | EAGLZ Finance',
      u'Széchenyi Kártya Program 2026-os feltételekkel, SZÉP-kártya és lakhatási támogatás adóterhe, céges biztosítások és az alulbiztosítás csapdája, egy helyen.',
      BODY, LEGAL,
      u'Nézzük meg a cégedet egyben.',
      u'Egy díjmentes céges átvilágításon átnézzük a finanszírozást, a juttatási csomagot és a biztosítási fedezeteket, és megmondjuk, hol van valódi tartalék.')
