#!/usr/bin/env bash
# Supplementary harvest for the fig8 SUBJECT gallery gaps: the papers whose collage tile was a
# schematic / text page / broken raster (LIBERO, VLABench, Habitat-3.0, VBench-2.0, WorldPrediction)
# plus the 4 bridge benchmarks never fetched (WorldSimBench, World-in-World, RoboWM-Bench, WorldArena).
#
# Unlike harvest_collage_tiles.sh this does NOT auto-pick the largest raster (that is exactly what
# poisoned 6 of 21 tiles). It dumps EVERY figure candidate per paper into a per-paper contact sheet,
# so the true task/scene figure can be chosen by eye, then cropped in a second pass.
#
# You (the paper's author) run this and own the fair-use / scholarly-review reproduction, exactly as
# the collage did. Requires: curl, pdfimages, pdftoppm, identify, montage (poppler + ImageMagick).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
OUTDIR="$HERE/fig8_gaps"; mkdir -p "$OUTDIR"
TMP="$(mktemp -d)"
MANIFEST="$OUTDIR/candidates.tsv"; echo -e "key\tarxiv_id\tcandidate\tsource\tsize" > "$MANIFEST"

# key|arxiv_id  (ids from catalog_p3.js; the two 2026 bridge ids are VERIFY-on-download)
GAPS="libero|2306.03310 vlabench|2412.18194 habitat30|2310.13724 vbench20|2503.21755 \
worldprediction|2506.04363 worldsimbench|2410.18072 worldinworld|2510.18135 \
robowmbench|2604.19092 worldarena|2602.08971"

for entry in $GAPS; do
  key="${entry%%|*}"; id="${entry#*|}"
  pdf="$TMP/$key.pdf"
  curl -sL --max-time 180 -A "Mozilla/5.0 (scholarly)" "https://arxiv.org/pdf/$id" -o "$pdf"
  if ! head -c5 "$pdf" 2>/dev/null | grep -q "%PDF"; then
    echo "!! $key ($id): download FAILED (id may not exist) -- skipped"; continue
  fi
  cdir="$TMP/${key}_cand"; mkdir -p "$cdir"; n=0
  # (a) embedded rasters, first 8 pages
  pdfimages -f 1 -l 8 -png "$pdf" "$cdir/r" 2>/dev/null
  for f in "$cdir"/r*.png; do [ -f "$f" ] || continue
    d=$(identify -format '%w %h' "$f" 2>/dev/null); w=${d% *}; h=${d#* }
    [ -z "${w:-}" ] && continue; [ "$w" -lt 150 ] && continue; [ "$h" -lt 120 ] && continue
    cp "$f" "$cdir/cand_$(printf '%02d' $n).png"; n=$((n+1))
  done
  # (b) full-page renders, pages 1-6 (catches vector/composite teaser figures rasters miss)
  pdftoppm -png -r 110 -f 1 -l 6 "$pdf" "$cdir/pg" 2>/dev/null
  for f in "$cdir"/pg*.png; do [ -f "$f" ] || continue
    cp "$f" "$cdir/cand_$(printf '%02d' $n).png"; n=$((n+1))
  done
  # per-paper contact sheet, each candidate stamped [key idx]
  i=0; rm -f "$cdir"/lab_*.png; rm -f "$OUTDIR/${key}_cand_"*.png
  for f in "$cdir"/cand_*.png; do [ -f "$f" ] || continue
    # KEY-PREFIXED so papers never clobber each other's full-res candidates
    cp "$f" "$OUTDIR/${key}_$(basename "$f")"
    identify -format "$key\t$id\t$i\t${key}_cand_$(printf '%02d' $i).png\t%wx%h\n" "$f" >> "$MANIFEST"
    convert "$f" -resize 320x260 -background white -gravity North -splice 0x20 \
      -gravity NorthWest -pointsize 15 -fill red -annotate +3+1 "$key [$i]" \
      "$cdir/lab_$(printf '%03d' $i).png" 2>/dev/null; i=$((i+1))
  done
  if ls "$cdir"/lab_*.png >/dev/null 2>&1; then
    montage "$cdir"/lab_*.png -tile 6x -geometry +2+2 -background white "$OUTDIR/${key}_sheet.png" 2>/dev/null
    echo "$key ($id): $i candidates -> ${key}_sheet.png"
  else
    echo "$key ($id): no candidates extracted"
  fi
  rm -f "$pdf"; sleep 2
done
rm -rf "$TMP"
echo "Done. Per-paper contact sheets + candidates in: $OUTDIR"
echo "Next: view each *_sheet.png, note the subject-figure index per key, then run the crop pass."
