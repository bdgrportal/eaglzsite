#!/bin/bash
# EAGLZ teljes ujraepites, helyes sorrendben
set -e
cd "$(dirname "$0")"
python3 step1_assets.py   >/dev/null
python3 step2_portal.py   >/dev/null
python3 step3_subpages.py >/dev/null
for f in nyugdij gyermek tamogatas vallalati biztositas befektetes bankszamla lakastakarek; do python3 page_$f.py; done
R=/home/claude/eaglz-repo
cp index_portal.html $R/index.html
cp kalkulator_portal.html $R/kalkulator.html
cp kviz_portal.html $R/kviz.html
cp lakashitel-folyamat_portal.html $R/lakashitel-folyamat.html
cp nyugdij.html gyermekjovo.html tamogatasok.html vallalati.html biztositasok.html befektetesek.html bankszamla.html lakastakarek.html $R/
mkdir -p $R/_forras && cp portal.css portal.js sub.css theme.css harmonia.css mozgas.js ui.js theme_inject.py landing.py audit_text.py build_sub.py build_all.sh step1_assets.py step2_portal.py step3_subpages.py page_*.py port_back.py index_layout.py $R/_forras/
# vedoháló: a régi felső segédsor egyetlen oldalon sem térhet vissza
if grep -l 'class="uhead' $R/*.html; then echo "HIBA: dupla fejléc maradt a fenti oldalakon"; exit 1; fi
# kitoltetlen helyorzok jelzese (nem hiba, de a tulajdonosnak porgetni kell)
python3 - <<'PY'
import glob,io,re
bad={}
for f in glob.glob("/home/claude/eaglz-repo/*.html"):
    s=re.sub(r"<!--.*?-->","",io.open(f,encoding="utf-8").read(),flags=re.S)
    s=re.sub(r"<script.*?</script>","",s,flags=re.S)
    for m in re.finditer(r"[A-Z_]{3,}_IDE", s): bad.setdefault(m.group(0),set()).add(f.split("/")[-1])
if bad:
    print("HIANYZO ADAT (elo tartalomban maradt helyorzo):")
    for k,v in sorted(bad.items()): print("   %-26s %s" % (k, ", ".join(sorted(v))[:70]))
PY
echo "EAGLZ kesz -> $R ($(ls $R/*.html | wc -l) oldal, egyetlen fejléc-sor)"
