#!/usr/bin/env bash
# Re-render every table deliverable WITH bibtex so \cite keys resolve to real numbers (no [?]).
# Extracts only the table pages (references pages excluded). Pure render; no source edits.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; cd "$HERE"
DEST="$HERE/../deliverables"

ITEMS="
table1|tables/tab_survey_compare
table2|tables/tab_compare_main
table3|tables/tab_definitions
table4|tables/tab_compare_capability
table5|tables/tab_wm_senses
table6|tables/tab_compare_wmeval
table7|tables/tab_capability_matrix
table8|tables/tab_branch_limits
table9|tables/tab_future_metrics
table10a|tables/tab_panel_provenance
table10b|tables/tab_results_provenance
table10c|tables/tab_collage_provenance
table11|tables/tab_landscape
"

for pair in $ITEMS; do
  [ -z "$pair" ] && continue
  name="${pair%%|*}"; tex="${pair#*|}"; w="_wt_${name}"
  cp render_head.tex "$w.tex"
  printf '\\input{../%s.tex}\n\\clearpage\n\\bibliographystyle{ACM-Reference-Format}\n\\bibliography{../refs}\n\\end{document}\n' "$tex" >> "$w.tex"
  pdflatex -interaction=nonstopmode "$w.tex" >/tmp/rt_$name.log 2>&1
  bibtex "$w" >/dev/null 2>&1
  pdflatex -interaction=nonstopmode "$w.tex" >/tmp/rt_$name.log 2>&1
  pdflatex -interaction=nonstopmode "$w.tex" >/tmp/rt_$name.log 2>&1
  if [ ! -f "$w.pdf" ]; then echo "!! $name FAILED"; rm -f ${w}.*; continue; fi
  und=$(grep -c "Citation.*undefined" /tmp/rt_$name.log)
  np=$(pdfinfo "$w.pdf" | awk '/Pages/{print $2}')
  refstart=$((np+1))
  for p in $(seq 1 $np); do pdftotext -f $p -l $p "$w.pdf" - 2>/dev/null | grep -qiE "^ *references\b|arxiv preprint|in proc|proceedings of|in advances" && { refstart=$p; break; }; done
  content=""; for p in $(seq 1 $((refstart-1))); do pdftotext -f $p -l $p "$w.pdf" - 2>/dev/null | grep -q "Temporary page" && continue; content="$content,$p"; done
  content=${content#,}; [ -z "$content" ] && content=1
  gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sPageList="$content" -o _xt.pdf "$w.pdf" 2>/dev/null
  pdfcrop --margins "10 10 10 10" _xt.pdf "$DEST/${name}_p3.pdf" >/dev/null 2>&1
  echo "$name: undefined-cites=$und  table-pages=[$content]  -> ${name}_p3.pdf"
  rm -f ${w}.* _xt.pdf
done
echo "DONE."
