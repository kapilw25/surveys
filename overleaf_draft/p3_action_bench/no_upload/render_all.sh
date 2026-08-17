#!/usr/bin/env bash
# Render every P3 figure + table replica to a cropped PDF (+PNG) in deliverables/, named to match
# the p1 original for side-by-side eyeball comparison. Pure-local (pdflatex/gs/pdfcrop; no network).
# Citations render as [?] in these quick single-item builds (no bibtex) but resolve in the full paper.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
DEST="$HERE/../deliverables"; mkdir -p "$DEST"
cd "$HERE"

# name|texpath (relative to no_upload/, without .tex). table6 == table4 (folded); table10 = 3 provenance parts.
ITEMS="
fig1|figures/fig_corpus_collage
fig2|figures/fig_taxonomy_main
fig3|figures/fig_survey_timeline
fig4|figures/fig_prisma
fig5|figures/fig_corpus_overview
fig6|figures/fig_corpus_dist
fig7|figures/fig_lane_trend
fig8|figures/fig_subject_gallery
fig9|figures/fig_results_gallery
fig10|figures/fig_eval_loop
fig11|figures/fig_future_protocol
table1|tables/tab_survey_compare
table2|tables/tab_compare_main
table3|tables/tab_definitions
table4|tables/tab_compare_capability
table5|tables/tab_wm_senses
table7|tables/tab_capability_matrix
table8|tables/tab_branch_limits
table9|tables/tab_future_metrics
table10a|tables/tab_panel_provenance
table10b|tables/tab_results_provenance
table10c|tables/tab_collage_provenance
table11|tables/tab_landscape
"

ok=0; fail=0
for pair in $ITEMS; do
  [ -z "$pair" ] && continue
  name="${pair%%|*}"; tex="${pair#*|}"
  w="_w_${name}"
  cp render_head.tex "$w.tex"
  printf '\\input{../%s.tex}\n\\end{document}\n' "$tex" >> "$w.tex"
  pdflatex -interaction=nonstopmode -halt-on-error "$w.tex" >/dev/null 2>&1
  pdflatex -interaction=nonstopmode -halt-on-error "$w.tex" >/dev/null 2>&1
  if [ ! -f "$w.pdf" ]; then echo "!! $name FAILED to compile"; fail=$((fail+1)); rm -f ${w}.*; continue; fi
  np=$(pdfinfo "$w.pdf" 2>/dev/null | awk '/Pages/{print $2}')
  content=""
  for p in $(seq 1 "${np:-1}"); do
    if pdftotext -f "$p" -l "$p" "$w.pdf" - 2>/dev/null | grep -q "Temporary page"; then continue; fi
    content="$content,$p"
  done
  content="${content#,}"; [ -z "$content" ] && content="1"
  gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sPageList="$content" -o "_x_${name}.pdf" "$w.pdf" 2>/dev/null
  pdfcrop --margins "10 10 10 10" "_x_${name}.pdf" "$DEST/${name}_p3.pdf" >/dev/null 2>&1
  pdftoppm -png -r 130 "$DEST/${name}_p3.pdf" "$DEST/${name}_p3" >/dev/null 2>&1
  echo "   $name -> ${name}_p3.pdf  (pages $content of $np)"
  ok=$((ok+1))
  rm -f ${w}.* "_x_${name}.pdf"
done
echo "DONE: $ok rendered, $fail failed. In: $DEST"
ls "$DEST"/*_p3.pdf 2>/dev/null | wc -l | xargs echo "total *_p3.pdf files:"
