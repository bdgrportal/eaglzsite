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
mkdir -p $R/_forras && cp portal.css portal.js sub.css theme.css theme_inject.py landing.py audit_text.py build_sub.py build_all.sh step1_assets.py step2_portal.py step3_subpages.py page_*.py port_back.py index_layout.py $R/_forras/
echo "EAGLZ kesz -> $R"
