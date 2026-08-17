#!/usr/bin/env bash
# Build the fig9 RESULTS-gallery tiles (480x384) into figures/img/results_tiles/.
# Sources: rasterised results plots hand-picked from fig9_results/ per-paper contact sheets, plus
# two bridge results figures already fetched in fig8_gaps/. Plots are CONTAIN-fitted (padded on
# white), NOT cropped-to-fill, so no bars / axes / radar spokes are cut off.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
R="$HERE/fig9_results"; G="$HERE/fig8_gaps"
OUT="$HERE/../figures/img/results_tiles"; mkdir -p "$OUT"

# contain-fit at HIGH resolution + boost text legibility: sigmoidal contrast deepens dark text
# (and brightens light text on dark-bg radars -- polarity-agnostic), unsharp thickens/crisps strokes.
fit() { convert "$1" -resize 1000x800 -background white -gravity center -extent 1024x820 \
        -sigmoidal-contrast 3.5x50% -unsharp 0x0.9+1.4+0 "$2" 2>/dev/null; }

# Band A: leaderboard & model-comparison
fit "$G/worldinworld_cand_16.png"      "$OUT/worldinworld.png"      # task-success / gen-quality leaderboard
fit "$R/evalcrafter_cand_008.png"      "$OUT/evalcrafter_bars.png"  # overall model-ranking bar chart
fit "$R/videoscore_cand_000.png"       "$OUT/videoscore.png"        # annotation score-ratio grouped bars
fit "$R/worldmodelbench_cand_000.png"  "$OUT/worldmodelbench.png"   # VBench-vs-Ours win-rate comparison
# Band B: per-dimension radar / multi-metric
fit "$R/vbench_cand_007.png"           "$OUT/vbench_radar.png"      # 16-dimension VBench radar
fit "$R/ewmbench_cand_038.png"         "$OUT/ewmbench.png"          # EWMScore 5-dimension radar
convert "$G/worldarena_cand_38.png" -crop 452x190+425+52 +repage "$G/_warena_fig.png" 2>/dev/null
fit "$G/_warena_fig.png"               "$OUT/worldarena.png"        # EWMScore evaluation radars (panel b)
fit "$R/physicsiq_cand_035.png"        "$OUT/physicsiq_bars.png"    # per-model physical-realism ranking bars
fit "$R/evalcrafter_cand_010.png"      "$OUT/evalcrafter_userradar.png" # user-study radar (5 dims)
fit "$R/vbench_cand_025.png"           "$OUT/vbench_permodel.png"   # per-model VBench radar (LaVie)
# Band C: distributions & composition
fit "$R/evalcrafter_cand_024.png"      "$OUT/evalcrafter_hist.png"  # prompt-length histogram
fit "$R/evalcrafter_cand_028.png"      "$OUT/evalcrafter_pie.png"   # meta-type composition pie
fit "$R/vbench_cand_008.png"           "$OUT/vbench_wordcloud.png"  # prompt word cloud
fit "$R/videophy_cand_009.png"         "$OUT/videophy_sunburst.png" # action-object category sunburst
fit "$R/ewmbench_cand_022.png"         "$OUT/ewmbench_wordcloud.png" # task word cloud

echo "Built $(ls "$OUT"/*.png | wc -l | tr -d ' ') results tiles in $OUT"