# eaglz.hu: portál verzió

Statikus HTML, nincs build lépés. Feltölthető úgy, ahogy van.

```
index.html                  főoldal (portál-fejléc, hero-kalkulátor, partnersáv, 12 kártyás hub)
kalkulator.html             kalkulátorok            ← portál-fejléc
kviz.html                   Otthon Start kvíz       ← portál-fejléc
lakashitel-folyamat.html    folyamatleírás          ← portál-fejléc

nyugdij.html                Nyugdíj-megtakarítás    ← ÚJ, kalkulátorral
gyermekjovo.html            Gyermek-megtakarítás    ← ÚJ, kalkulátorral
befektetesek.html           Befektetés, TBSZ        ← ÚJ, kalkulátorral
tamogatasok.html            Állami támogatások 2026 ← ÚJ
biztositasok.html           Biztosítások            ← ÚJ
vallalati.html              Vállalati megoldások    ← ÚJ

assets/                     képek, logók, tanácsadói fotók
CNAME, favicon.ico, apple-touch-icon.png
_forras/                    a portál-réteg forrása és a generátor scriptek
```

---

## 0. Design réteg (2026. szeptember, második kör)

Minden oldal utolsó stíluslapja a `_forras/theme.css`. Ez egyetlen fájl, és ez adja:

| Mit | Hogyan |
|---|---|
| **Betűtípus** | Az OVB a fizetős Stag Sans betűt használja, azt nem lehet feltenni. A hozzá legközelebb álló szabad betű az **Archivo**, ez megy mindenhol. |
| **Visszaállás a régire** | A `theme.css` elején két csillagos sor: `--fb` és `--fd`. Írd át `var(--font-old-h)` és `var(--font-old-b)` értékre, futtasd a `build_all.sh`-t, és minden oldal visszaáll Space Grotesk + Poppinsra. Más nem változik. |
| **Szélesvásznú konténer** | 1440 px (1700 felett 1560), folyékony oldalmargóval. A fejléc, a mega-menü és a tartalom ugyanazon a bal élen kezdődik. |
| **Igazítás** | 1024 px felett minden szekciófejléc és bevezető **balra zárt**, teal→lila akcentcsíkkal a cím előtt. Alatta (tablet, mobil) minden **középre zárt**. |
| **Térköz-skála** | Négy változó: `--sp-sec` (szekció), `--sp-sec-s` (kis szekció), `--sp-head` (fejléc → tartalom), `--sp-mod` (modulköz). Mobiltól desktopig folyékonyan nőnek. A tableten nagyobb-mint-desktopon padding-hiba megszűnt. |
| **Tipográfia** | Törzs 16 px, sorköz 1,7. Címsorok feszesebbek, negatív betűközzel. |
| **Paletta** | Kártyák felső fejsávja teal→lila→arany, táblázatfej navy, dobozok bal éle színkódolt, sötét szekciók teal fénnyel. |
| **Javított hibák** | Forgó zöld keret a gombok körül (statikus lett), pulzáló/remegő kártyák (kikapcsolva), a 8 terület-kártya desktopon nyitva kártyaként (nem üres harmonika-sáv), tanácsadói kártyák egy sorban széles kijelzőn, lead-űrlap kétoszlopos, mobilon a felső szolgáltatási sáv rejtve (a hamburger-menüben ott van minden). |
| **Landing-váz** | Minden aloldalon: hero → bizalmi sáv → tartalom → halk közbenső CTA a fő szekció után → GYIK → záró CTA → jogi lábjegyzet. Ezt a `_forras/landing.py` teszi be generáláskor. |
| **Szöveg** | Nincs hosszú kötőjel sehol, a `_forras/audit_text.py` szűri. Végig tegező. |
| **Fejléc** | Egy sáv: logó, 6 mega-menü kategória, egy halkabb „Rólunk" lenyíló (Kinek, Hogyan, Miért mi, Vélemények, Rólunk, GYIK, Karrier) és egyetlen CTA. A korábbi dupla sáv és a dupla gomb megszűnt. |
| **Főoldal-váz** | Hero → számok → partnerek → kalkulátor-hub → Kinek → Ennyit spórolhatsz → Tanácsadók → Folyamat → Online → Miért mi → Ügyfélvélemények (görgethető, nagyobb videók) → Rólunk (két oszlop) → GYIK (két oszlop) → egy záró blokk: időpont bal oldalt, üzenet-űrlap jobb oldalt → zárókép + lábléc. A „8 terület" szekció kikerült, a helyére az „Ennyi pénzt spórolhatsz" jött. |
| **Saját aloldalak** | A lakástakarék és a bankszámla oldal az eaglz.hu-n fut (`_forras/port_back.py` emeli át Zoé oldaláról), egyetlen link sem mutat a tanácsadói oldalakra. |

Újraépítés egy paranccsal: `bash _forras/build_all.sh` (a fájlok az én munkakörnyezetemre vannak beállítva, neked nem kell futtatnod; a kész HTML-ek a repóban vannak).

---

## 1. Mi változott

| | Előtte | Most |
|---|---|---|
| Fejléc | egy sáv, 9 horgony a főoldalra | **három sáv**: szolgáltatási sáv, logó + 6 kategória mega-menüvel, foglalás gomb |
| Menüpontok | csak a főoldal szekciói | **36 menüpont** 6 kategóriában, ikonnal, alcímmel, leíró panellel és banki logókkal |
| Hero | cím + 4 gomb + logó-pálya | cím + **4 előnykártya** + **gyorskalkulátor** (3 fül), a logó-pálya külön partnersávba került |
| Kalkulátorok | csak a `kalkulator.html`-ben | **kalkulátor-hub** a főoldalon, **12 kártya**, mind él |
| Szakmai aloldalak | nem volt, a menü fele `#services`-re mutatott | **6 hosszú, SEO-s aloldal**, 3 saját kalkulátorral, 60+ GYIK-kérdéssel |
| Aloldalak fejléce | saját, egyszerű fejléc | **ugyanaz a portál-fejléc** mindenhol |
| Fájlméret | 985 KB (minden kép a HTML-be ágyazva) | **~210 KB** főoldal + külön képfájlok, gyorsabb és cache-elhető |

**Ami nem változott:** a 8 terület kártyái és termékmodáljai, a tanácsadói rács a popuppal, a megtakarítási példák a jogi kitétellel, a folyamat, az online ügyintézés linkjei, a „Miért mi" és az összehasonlító tábla, a videós vélemények, a Rólunk és a mérföldkövek, a GYIK, a lead űrlap és a teljes impresszum.

---

## 2. A hat új aloldal

Mindegyik azonos felépítésű: hero + tartalomjegyzék + hosszú szakmai szöveg + dobozok (info / figyelmeztetés / stop / idézet) + táblázatok + GYIK + oldalspecifikus jogi lábjegyzet.

| Oldal | Kalkulátor | Fő tartalom |
|---|---|---|
| `nyugdij.html` | ✅ 3 termék, adó-visszatérítéssel | Miért nem elég az állami nyugdíj, a három támogatott forma, melyiket válaszd, idő előtti feltörés |
| `gyermekjovo.html` | ✅ Babakötvény + gyűjtés | Babakötvény és az állami támogatás, gyermek-életbiztosítás, mikor mit érdemes indítani |
| `befektetesek.html` | ✅ TBSZ vs. sima számla | TBSZ adótábla, befektetési alapok és költségeik, unit-linked és TKM őszintén, öt hiba |
| `tamogatasok.html` | - | Otthon Start, CSOK Plusz, Falusi CSOK, Babaváró; külön szekció arról, **mi futott ki** |
| `biztositasok.html` | - | KGFB-váltás az évfordulón, bonus-malus, alulbiztosítás, hét hiba amitől nem fizet a biztosító |
| `vallalati.html` | - | Széchenyi Kártya Program 2026, cafeteria-keretek, céges biztosítás, kötelező felelősségbiztosítások |

**Állampapír-aloldal szándékosan nincs**, mert nem közvetítünk állampapírt. A `befektetesek.html` ezt ki is mondja egy dobozban és egy GYIK-pontban, és a menüből is kikerült.

---

## 3. A gyorskalkulátor a hero-ban

| Fül | Mit csinál |
|---|---|
| **Lakásfinanszírozás** | hitelösszeg + futamidő → törlesztő hirdetett kamattal és egyedi bírálattal, plusz a különbség a teljes futamidőn |
| **Megtakarítás** | havi összeg + időtáv → mennyi lesz belőle, mennyit tesz hozzá a hozam |
| **Jár nekem?** | Otthon Start felvezetés → a kvízre visz |

---

## 4. Karbantartás: negyedévente kb. 10 perc

### a) Kamatok és hozamok

Minden oldal alján, a portál-script elején ugyanez a blokk:

```js
var RATES = {
  advertised:  7.49,   // jellemző hirdetett lakáshitel-kamat, %
  best:        5.59,   // egyedi bírálattal elérhető kamat, %
  otthonStart: 3.00,   // Otthon Start fix kamata, jogszabályból
  savingYield: 6.00,   // megtakarítás tájékoztató éves hozama, %
  updated: '2026. szeptember'
};
```

Az `updated` minden oldalon több helyen automatikusan megjelenik (`<b data-upd>`). **A blokkot minden HTML-ben át kell írni**, mert mindegyik saját példányt kap. (Ha a sablonos generálás felkerül, ez egy helyre költözik.)

### b) Az aloldalak saját adatai

Minden kalkulátoros aloldal tetején van egy hasonló blokk. Ezt évente egyszer, a költségvetési törvény után érdemes átnézni:

| Oldal | Blokk | Mit tartalmaz |
|---|---|---|
| `nyugdij.html` | `PLAFON`, `RATE` | adó-visszatérítés kulcsa és a három termék éves plafonja |
| `gyermekjovo.html` | `BK` | babakötvény támogatási %, plafon, induló összeg, kamat |
| `befektetesek.html` | `kulcs()` | TBSZ 3 / 5 éves adókulcsai és a kamatjövedelem adója |

### c) Menüpont felvétele

A `NAV` tömbben, a portál-scriptben. Egy sor egy menüpont:

```js
{i:'🌅', t:'Nyugdíj-megtakarítás', m:'20% adó-visszatérítéssel', h:'nyugdij.html', tag:'ÚJ', tagc:'new'}
```

A `tag:'ÚJ'` jelölést töröld róla néhány hónap után. Ha `#valami` horgonyt írsz be, az aloldalakon automatikusan `index.html#valami` lesz belőle (a `HREF()` függvény intézi), tehát nem törik el.

---

## 5. Szövegek: szándékosan nincs átvétel

Minden szakmai szöveg saját megfogalmazás. Amit a forrásokból vittünk át, az a **tényanyag** (jogszabályi számok, összeghatárok, eljárásrend), nem a megfogalmazás.

- A menü hat kategóriája a **saját 8 területetek** nevei, nem egy összehasonlító portál kategóriái
- „Mennyit nyerhetsz rajta?", ez a **saját szövegetek** volt a megtakarítási szekcióban
- Az aloldalak szerkezete (tartalomjegyzék → szakaszok → GYIK) általános szakmai cikkfelépítés, nem egy konkrét oldalé
- Minden oldalon lefutott egy 29 kifejezéses szűrő konkurens szlogenekre és kockázatos ígéretekre („garantált hozam", „a piac legjobb", stb.), **nulla találat**

### A kockázati elv végig tartva

- **Egyetlen pénzintézet neve mellett sem szerepel kamat, ajánlat vagy THM.**
- A logók a piacot szemléltetik, a csúszkák alapértéke tájékoztató nagyságrend.
- Minden kalkulátor alatt ott van, hogy mit **nem** tud a modell.
- Minden aloldal alján saját jogi lábjegyzet, a konkrét jogszabályhelyekkel.
- Az MNB Termékkereső hivatkozásként szerepel, mint hiteles forrás.

**Amit szándékosan nem vettünk át:** termékadatbázis és „Összesen X termék" típusú számlálók. Az heti több óra karbantartás lenne, és OVB-s közvetítőként más felelősségi kategória, ha banknevek mellé kamat és THM kerül.

### 2026-os aktualizálás

A jogszabályi adatok 2026. szeptemberi állapotúak, és külön ellenőrizve lettek. Ami időközben kifutott, azt nem élő lehetőségként, hanem a **„mi futott ki"** szekcióban mutatjuk. A 2026-os költségvetési vita folyamatban van, ezért a lábjegyzetek mindenhol jelzik, hogy a szabályok év közben is módosulhatnak. Politikai állásfoglalás, párt- vagy személynév sehol nem szerepel.

---

## 6. Amit érdemes még kitölteni

Ezek a saját `_IDE` jelöléseid, a portál-rétegtől függetlenül:

| Hol | Mi hiányzik |
|---|---|
| `ADVISORS` tömb, `index.html` alja | 5 tanácsadónál a `bio`, `email`, `phone`, `book` (naptárlink) még `_IDE`. A hiányzó foglalólink a közös EAGLZ naptárra esik vissza, tehát nem törik el, de mindenki a saját naptárával konvertál jobban. |
| `INFO_EMAIL_IDE` | footer „Kapcsolat" link |
| `EAGLZ_MNB_ADAT_IDE` | „Miért mi?" szekció, ellenőrzött kártya |
| Footer közösségi ikonok | mind `href="#"` |

A **Supabase** oldalon pedig (ez a lead-mentést érinti):

```sql
alter table web_leads add column if not exists advisor text;
alter table web_leads add column if not exists source  text;

alter table web_leads enable row level security;
create policy "anon insert only" on web_leads
  for insert to anon with check (true);
-- SELECT policy anon szerepre NE legyen
```

Az anon kulcs nyilvános a forráskódban, ezért olvasás nem lehet engedélyezve.

---

## 7. Hogyan készült, ha újra kell futtatni

A `_forras/` mappában van a portál-réteg és az összes generátor. Ezek az **eredeti** fájlokból csinálják a mostaniakat, tehát ha az eredeti oldalhoz nyúlsz, a réteg újra ráhúzható:

```bash
python3 step1_assets.py        # data: URI-k kiemelése fájlokba
python3 step2_portal.py        # portál-réteg a főoldalra   -> index_portal.html
python3 step3_subpages.py      # ugyanaz a fejléc a 3 régi aloldalra

python3 page_nyugdij.py        # a hat új aloldal
python3 page_gyermek.py
python3 page_befektetes.py
python3 page_tamogatas.py
python3 page_biztositas.py
python3 page_vallalati.py
```

- `portal.css` / `portal.js`, a portál-réteg (fejléc, mega-menü, hero-kalkulátor, hub)
- `sub.css`, az aloldalak komponenskönyvtára (`.art`, `.box`, `.tbl`, `.nsteps`, `.tiles`, `.kpis`, `.yn`, `.sc`, `.toc`)
- `build_sub.py`, az aloldal-összeszerelő: kiveszi a fejlécet és a mega-menü scriptet az `index.html`-ből, és köré építi az oldalt

Ez a réteg lesz a következő lépésben a közös sablon alapja, amiből a tanácsadói oldalak generálódnak.

---

## 8. Ellenőrzés

Minden kiadás előtt lefut egy Playwright-os végigjárás mind a 10 oldalon, 1440 és 390 px szélességen:

- nincs vízszintes túlcsordulás (`document.scrollWidth === 390`)
- a mega-menü mind a 6 kategóriában felépül
- nincs JS hiba és nincs 404-es kép
- nincs kitöltetlen `{{TOKEN}}`
- minden belső link létező fájlra és létező horgonyra mutat
