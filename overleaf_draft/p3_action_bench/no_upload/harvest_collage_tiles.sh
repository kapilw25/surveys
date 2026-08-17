#!/usr/bin/env bash
# Populate figures/img/collage_tiles/<key>.png with one representative figure per benchmark paper,
# so gen_collage_p3.py can emit the PHOTO version of fig_corpus_collage (the p1_fig1 replica).
# REPRODUCIBLE: the 18 tiles match LEFT/RIGHT in gen_collage_p3.py exactly, and the 3 whose teaser
# is not the largest raster carry a baked-in page + crop box, so re-running reproduces the same set.
#
# You (the paper's author) run this and own the fair-use / scholarly-review reproduction, exactly as
# p1_fig1 did ("Images (c) their respective authors, reproduced for scholarly review").
# Requires: curl, pdfimages, pdftoppm, identify, convert (poppler + ImageMagick).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../../.." && pwd)"
CAT="$ROOT/docs/assets/catalog_p3.js"
OUTDIR="$HERE/../figures/img/collage_tiles"; mkdir -p "$OUTDIR"
TMP="$(mktemp -d)"; PROV="$OUTDIR/provenance.tsv"
echo -e "benchmark\tkey\tarxiv_id\tsource\tsize" > "$PROV"

# "Name|key|method"  method = raster  OR  cropP:WxH+X+Y  (render page P at 150dpi, crop that box)
TILES="LIBERO|libero|crop2:1100x560+88+80 CALVIN|calvin|raster Meta-World|metaworld|raster \
ManiSkill2|maniskill2|raster RoboCasa|robocasa|raster Habitat-3.0|habitat30|raster \
ALFRED|alfred|raster GemBench|gembench|raster VLABench|vlabench|crop1:1090x548+95+598 \
WorldModelBench|worldmodelbench|raster Physics-IQ|physicsiq|raster WorldScore|worldscore|raster \
EWMBench|ewmbench|raster EVA-Bench|evabench|raster VideoPhy|videophy|raster \
Physion++|physionpp|raster Physion|physion|crop3:910x540+80+110 EvalCrafter|evalcrafter|raster"

id_for() { python3 - "$CAT" "$1" <<'PY'
import re,sys
blk=open(sys.argv[1],encoding="utf-8").read().split("var DATA = [",1)[1].split("].map",1)[0]
def mk(n): return re.sub(r'[^a-z0-9]','',n.split("(")[0].split("/")[0].strip().lower().replace("+","p"))
for r in re.findall(r'\["([^"]+)",\s*"[^"]+",\s*"[^"]*",\s*"[^"]*",\s*"[^"]*",\s*\d+,\s*(null|"[^"]*")\]',blk):
    if mk(r[0])==sys.argv[2] and r[1]!="null": print(r[1].strip('"')); break
PY
}

for entry in $TILES; do
  name="${entry%%|*}"; rest="${entry#*|}"; key="${rest%%|*}"; method="${rest##*|}"
  id="$(id_for "$key")"
  [ -z "${id:-}" ] && { echo "$name ($key): no arXiv id, skipped"; continue; }
  pdf="$TMP/$key.pdf"
  curl -sL --max-time 150 -A "Mozilla/5.0 (scholarly)" "https://arxiv.org/pdf/$id" -o "$pdf"
  head -c5 "$pdf" 2>/dev/null | grep -q "%PDF" || { echo "$name: download failed"; continue; }
  best=""; src=""
  if [ "${method#crop}" != "$method" ]; then
     pg="${method#crop}"; pg="${pg%%:*}"; box="${method#*:}"
     pdftoppm -png -r 150 -f "$pg" -l "$pg" "$pdf" "$TMP/${key}_pg" 2>/dev/null
     page=$(ls "$TMP/${key}_pg"*.png 2>/dev/null | head -1)
     [ -n "$page" ] && convert "$page" -crop "$box" +repage "$TMP/${key}_c.png" 2>/dev/null && best="$TMP/${key}_c.png"
     src="teaser figure (p.$pg, cropped)"
  else
     pdfimages -f 1 -l 3 -png "$pdf" "$TMP/${key}_r" 2>/dev/null
     area=0
     for f in "$TMP/${key}_r"*.png; do [ -f "$f" ] || continue
        d=$(identify -format '%w %h' "$f" 2>/dev/null); w=${d% *}; h=${d#* }
        [ -z "${w:-}" ] && continue; [ "$w" -lt 130 ] && continue; [ "$h" -lt 130 ] && continue
        a=$((w*h)); [ "$a" -gt "$area" ] && { area=$a; best="$f"; }
     done
     src="representative figure (pp.1--3)"
  fi
  [ -z "${best:-}" ] && { echo "$name: no image extracted"; continue; }
  convert "$best" -resize 480x384^ -gravity center -extent 480x384 "$OUTDIR/$key.png" 2>/dev/null
  echo -e "$name\t$key\t$id\t$src\t$(identify -format '%wx%h' "$OUTDIR/$key.png")" >> "$PROV"
  echo "$name -> $key.png ($src)"
  rm -f "$pdf" "$TMP/${key}_r"* "$TMP/${key}_pg"* "$TMP/${key}_c.png"
  sleep 2
done
rm -rf "$TMP"
echo "Done ($(($(wc -l < "$PROV")-1))/18 tiles). Provenance: $PROV"
echo "Next: python3 no_upload/gen_collage_p3.py  (then compile no_upload/test_collage.tex)"
