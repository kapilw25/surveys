#!/usr/bin/env bash
# Build the 24 fig8 SUBJECT-gallery tiles (480x384) into figures/img/subject_tiles/:
#   - 15 already-clean subject tiles reused from collage_tiles/ (classified subject-present)
#   - 9 gap tiles cropped from the hand-picked candidate in fig8_gaps/ (indices chosen by eye
#     from the per-paper contact sheets; NOT largest-raster)
# Reproducible: the picked candidate index per key is baked in below.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
COLL="$HERE/../figures/img/collage_tiles"
GAPS="$HERE/fig8_gaps"
OUT="$HERE/../figures/img/subject_tiles"; mkdir -p "$OUT"

fit() { convert "$1" -resize 480x384^ -gravity center -extent 480x384 "$2" 2>/dev/null; }

# 15 reused clean subject tiles
for k in alfred behavior1k calvin gembench maniskill2 metaworld robocasa \
         evabench ewmbench physicsiq physion physionpp videophy worldmodelbench worldscore; do
  cp "$COLL/$k.png" "$OUT/$k.png"
done

# 9 gap tiles: key -> picked candidate (verified clean by eye)
fit "$GAPS/libero_cand_23.png"          "$OUT/libero.png"
fit "$GAPS/vlabench_cand_16.png"        "$OUT/vlabench.png"
fit "$GAPS/habitat30_cand_09.png"       "$OUT/habitat30.png"
fit "$GAPS/vbench20_cand_00.png"        "$OUT/vbench20.png"
fit "$GAPS/worldprediction_cand_13.png" "$OUT/worldprediction.png"
fit "$GAPS/worldinworld_cand_26.png"    "$OUT/worldinworld.png"
fit "$GAPS/robowmbench_cand_18.png"     "$OUT/robowmbench.png"
fit "$GAPS/worldarena_cand_22.png"      "$OUT/worldarena.png"
# worldsimbench: crop the "Video Prediction" robot-manipulation filmstrip out of the framework figure
convert "$GAPS/worldsimbench_cand_04.png" -crop 380x175+1135+325 +repage "$GAPS/_wsb_crop.png" 2>/dev/null
fit "$GAPS/_wsb_crop.png"                "$OUT/worldsimbench.png"

echo "Built $(ls "$OUT"/*.png | wc -l | tr -d ' ') subject tiles in $OUT"