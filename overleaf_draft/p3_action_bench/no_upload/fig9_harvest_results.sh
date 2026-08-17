#!/usr/bin/env bash
# Harvest RESULTS-figure candidates for the fig9 results gallery (P1 analog: p1_fig9,
# "Results reported across the surveyed systems"). For a benchmark survey the "results" are the
# leaderboards / metric-comparison / correlation plots each benchmark publishes.
#
# Results plots are usually VECTOR (rendered on the page, mid-paper), so pdfimages alone misses them;
# we render pages 1-14 at 150dpi AND pull embedded rasters, then contact-sheet per paper so the real
# results figure can be chosen by eye and its plot region cropped. Key-prefixed (no clobber).
#
# You (the author) run this; it fetches public arXiv PDFs of already-cited benchmarks. Requires:
# curl, pdfimages, pdftoppm, identify, montage (poppler + ImageMagick).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
OUTDIR="$HERE/fig9_results"; mkdir -p "$OUTDIR"
TMP="$(mktemp -d)"
MANIFEST="$OUTDIR/candidates.tsv"; echo -e "key\tarxiv_id\tcandidate\tsource\tsize" > "$MANIFEST"

# key|arxiv_id  (curated for strong results figures across evidence types)
SET="evalcrafter|2310.11440 vbench|2311.17982 videophy|2406.03520 worldmodelbench|2502.20694 \
physicsiq|2501.09038 worldscore|2504.00983 videoscore|2406.15252 ewmbench|2505.09694 \
libero|2306.03310 maniskill2|2302.04659 roboarena|2506.18123 physbench|2501.16411"

for entry in $SET; do
  key="${entry%%|*}"; id="${entry#*|}"
  pdf="$TMP/$key.pdf"
  curl -sL --max-time 180 -A "Mozilla/5.0 (scholarly)" "https://arxiv.org/pdf/$id" -o "$pdf"
  if ! head -c5 "$pdf" 2>/dev/null | grep -q "%PDF"; then
    echo "!! $key ($id): download FAILED -- skipped"; continue
  fi
  cdir="$TMP/${key}_cand"; mkdir -p "$cdir"; n=0
  pdfimages -f 1 -l 14 -png "$pdf" "$cdir/r" 2>/dev/null
  for f in "$cdir"/r*.png; do [ -f "$f" ] || continue
    d=$(identify -format '%w %h' "$f" 2>/dev/null); w=${d% *}; h=${d#* }
    [ -z "${w:-}" ] && continue; [ "$w" -lt 200 ] && continue; [ "$h" -lt 130 ] && continue
    cp "$f" "$cdir/cand_$(printf '%03d' $n).png"; n=$((n+1))
  done
  pdftoppm -png -r 130 -f 1 -l 14 "$pdf" "$cdir/pg" 2>/dev/null
  for f in "$cdir"/pg*.png; do [ -f "$f" ] || continue
    cp "$f" "$cdir/cand_$(printf '%03d' $n).png"; n=$((n+1))
  done
  rm -f "$OUTDIR/${key}_cand_"*.png
  i=0; rm -f "$cdir"/lab_*.png
  for f in "$cdir"/cand_*.png; do [ -f "$f" ] || continue
    cp "$f" "$OUTDIR/${key}_$(basename "$f")"
    identify -format "$key\t$id\t$i\t${key}_cand_$(printf '%03d' $i).png\t%wx%h\n" "$f" >> "$MANIFEST"
    convert "$f" -resize 320x260 -background white -gravity North -splice 0x20 \
      -gravity NorthWest -pointsize 15 -fill red -annotate +3+1 "$key [$i]" \
      "$cdir/lab_$(printf '%03d' $i).png" 2>/dev/null; i=$((i+1))
  done
  if ls "$cdir"/lab_*.png >/dev/null 2>&1; then
    montage "$cdir"/lab_*.png -tile 6x -geometry +2+2 -background white "$OUTDIR/${key}_sheet.png" 2>/dev/null
    echo "$key ($id): $i candidates -> ${key}_sheet.png"
  else
    echo "$key ($id): no candidates"
  fi
  rm -f "$pdf"; sleep 2
done
rm -rf "$TMP"
echo "Done. Per-paper results contact sheets in: $OUTDIR"
