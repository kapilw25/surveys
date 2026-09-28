#!/usr/bin/env bash
# Build ONE deliverable in isolation and export it to deliverables/ as .pdf + .png (all pages).
#   usage: bash build/build_one.sh fig10_p05 figures/fig_decision_loop [nopreview]
set -uo pipefail
P="$(cd "$(dirname "$0")/.." && pwd)"; OUT="$1"; SRC="$2"; MODE="${3:-preview}"
cd "$P/build"; J="h_${OUT}"
{ cat preamble.tex
  [ "$MODE" = "preview" ] && echo '\usepackage[active,tightpage,floats]{preview}'
  echo '\begin{document}'; echo "\\input{../${SRC}}"
  echo '\bibliographystyle{plainnat}'; echo '\bibliography{../refs}'; echo '\end{document}'; } > "$J.tex"
rm -f "$J.aux" "$J.bbl"
pdflatex -interaction=nonstopmode "$J.tex" >"$J.log1" 2>&1
bibtex "$J" >"$J.blg1" 2>&1
pdflatex -interaction=nonstopmode "$J.tex" >"$J.log1" 2>&1
pdflatex -interaction=nonstopmode "$J.tex" >"$J.log1" 2>&1
E=$(grep -c '^! ' "$J.log"); U=$(grep -c 'undefined' "$J.log"); O=$(grep -c 'Overfull .hbox' "$J.log")
N=$(pdfinfo "$J.pdf" 2>/dev/null | awk '/Pages/{print $2}')
if [ "$MODE" != "preview" ]; then N=$((N)); fi
cp "$J.pdf" "$P/deliverables/${OUT}.pdf"
rm -f "$P/deliverables/${OUT}"-*.png
if [ "${N:-0}" -le 1 ]; then pdftoppm -png -r 200 -singlefile "$J.pdf" "$P/deliverables/${OUT}-1"
else pdftoppm -png -r 170 "$J.pdf" "$P/deliverables/${OUT}"; fi
printf '%-14s pages=%-3s errors=%-2s undefined=%-2s overfull=%s\n' "$OUT" "$N" "$E" "$U" "$O"
