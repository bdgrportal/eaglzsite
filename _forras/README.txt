
── 2026-09-14 ─────────────────────────────────────────────
Uj fajlok ebben a mappaban:
  sub.css          az aloldalak komponenskonyvtara
  build_sub.py     aloldal-osszeszerelo (fejlec + mega-menu kivetel index.html-bol)
  page_*.py        a hat uj aloldal tartalma, egyenkent
  index_assets.html  a step1 kimenete, ebbol dolgozik a step2
  eredeti/         a feltoltott, erintetlen forras-HTML-ek

Sorrend ujraepiteshez:
  step1_assets.py -> step2_portal.py -> step3_subpages.py -> page_*.py
A page_*.py-k az mar atalakitott index.html-bol veszik a fejlecet,
ezert ezeket a step2 UTAN kell futtatni, es a kimenetet az index.html
melle kell masolni.
