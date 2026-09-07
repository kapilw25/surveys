#!/usr/bin/env bash
# Build a verified arXiv submission zip from a canonical paper dir.
#   usage: build_arxiv_zip.sh <canonical_paper_dir> <out.zip> [main_basename]
# Stages -> purges artifacts -> zips -> FRESH-EXTRACTS -> compiles twice -> reports readiness.
set -uo pipefail

SRC="${1:?usage: build_arxiv_zip.sh <paper_dir> <out.zip> [main]}"
OUT="${2:?usage: build_arxiv_zip.sh <paper_dir> <out.zip> [main]}"
MAIN="${3:-main}"

SRC="$(cd "$SRC" && pwd)"
NAME="$(basename "$SRC")"
STAGE="$(mktemp -d)"; VERIFY="$(mktemp -d)"
trap 'rm -rf "$STAGE" "$VERIFY"' EXIT

# ---- stage a clean copy (exclude derived/local-only trees) -------------------
mkdir -p "$STAGE/$NAME"
( cd "$SRC" && tar cf - \
    --exclude='figures/out' --exclude='no_upload' --exclude='.git' \
    --exclude='*.aux' --exclude='*.log' --exclude='*.out' --exclude='*.synctex.gz' \
    --exclude='*.blg' --exclude='*.fls' --exclude='*.fdb_latexmk' --exclude='.DS_Store' \
    . ) | ( cd "$STAGE/$NAME" && tar xf - )

# ---- purge build artifacts by EXPLICIT NAME ---------------------------------
# NEVER mix explicit names with a may-not-match glob: in zsh an unmatched glob
# aborts the WHOLE command, so nothing gets deleted and artifacts ship silently.
for f in "$MAIN.pdf" "$MAIN.aux" "$MAIN.log" "$MAIN.out" "$MAIN.synctex.gz" "$MAIN.blg"; do
  rm -f "$STAGE/$NAME/$f"
done
find "$STAGE/$NAME" -type f \( -name '*.aux' -o -name '*.log' -o -name '*.out' \
     -o -name '*.synctex.gz' -o -name '.DS_Store' -o -name '*.fls' \) -delete
# main.bbl MUST survive (arXiv runs no bibtex)
[ -f "$SRC/$MAIN.bbl" ] && cp "$SRC/$MAIN.bbl" "$STAGE/$NAME/$MAIN.bbl"

# ---- zip --------------------------------------------------------------------
[ -f "$OUT" ] && cp "$OUT" "$OUT.bak" && echo "backed up previous zip -> $OUT.bak"
rm -f "$OUT"
( cd "$STAGE" && zip -q -r -X "$OUT" "$NAME" )

# ---- FRESH EXTRACT + compile twice (the only proof that matters) ------------
( cd "$VERIFY" && unzip -q "$OUT" )
PD="$VERIFY/$NAME"
( cd "$PD" && pdflatex -interaction=nonstopmode -halt-on-error "$MAIN.tex" >p1.log 2>&1 ); R1=$?
( cd "$PD" && pdflatex -interaction=nonstopmode -halt-on-error "$MAIN.tex" >p2.log 2>&1 ); R2=$?

PDF="$PD/$MAIN.pdf"; LOG="$PD/p2.log"
# NOTE: `grep -c` prints a count AND exits 1 when the count is 0, so never append
# `|| echo 0` here -- that emits a second line and breaks every comparison below.
num() { tr -dc '0-9' <<<"${1:-0}"; }
PAGES=$( [ -f "$PDF" ] && pdfinfo "$PDF" 2>/dev/null | awk '/Pages/{print $2}' || echo 0 )
UNDEF=$(num "$(grep -c 'undefined' "$LOG" 2>/dev/null)")
# `set -o pipefail` makes a no-match grep fail the whole pipeline, so an `|| echo 0`
# fallback would print a SECOND zero. Route every count through num() instead.
QQ=$(num "$(pdftotext "$PDF" - 2>/dev/null | grep -c '??' 2>/dev/null)")
ERRS=$(num "$(grep -c '^! ' "$LOG" 2>/dev/null)")
OVER=$(num "$(grep -c 'Overfull .hbox' "$LOG" 2>/dev/null)")
ABS=$(num "$(grep -rIl -e '/Users/' -e '/private/tmp' "$PD/figures" 2>/dev/null | wc -l)")
# count artifacts INSIDE THE ZIP, not in the verify dir (the verification compile
# legitimately creates its own .aux/.log there and would always false-FAIL).
ART=$(unzip -l "$OUT" | awk '$4 ~ /\.(aux|log|out|synctex\.gz|blg|fls|fdb_latexmk)$/' | wc -l | tr -d ' ')
PDFOUT=$(num "$(grep -c 'pdfoutput=1' "$PD/$MAIN.tex" 2>/dev/null)")
BBL=$( [ -f "$PD/$MAIN.bbl" ] && echo yes || echo NO )
SIZE=$(du -h "$OUT" | awk '{print $1}')
FILES=$(unzip -l "$OUT" | tail -1 | awk '{print $2}')

pass() { [ "$1" = "$2" ] && echo "PASS" || echo "FAIL <--"; }
echo
echo "================ arXiv readiness: $(basename "$OUT") ================"
printf "  %-34s %s\n" "zip size / files"            "$SIZE / $FILES"
printf "  %-34s %s\n" "compile pass1 / pass2"       "$R1 / $R2  $(pass "$R1$R2" "00")"
printf "  %-34s %s\n" "pages"                       "$PAGES"
printf "  %-34s %s %s\n" "undefined refs/citations" "$UNDEF" "$(pass "$UNDEF" 0)"
printf "  %-34s %s %s\n" "'??' in rendered text"    "$QQ"    "$(pass "$QQ" 0)"
printf "  %-34s %s %s\n" "LaTeX errors"             "$ERRS"  "$(pass "$ERRS" 0)"
printf "  %-34s %s %s\n" "overfull hbox >5pt"       "$OVER"  "$(pass "$OVER" 0)"
printf "  %-34s %s %s\n" "absolute paths in figures" "$ABS"  "$(pass "$ABS" 0)"
printf "  %-34s %s %s\n" "build artifacts in zip"   "$ART"   "$(pass "$ART" 0)"
printf "  %-34s %s %s\n" "\\pdfoutput=1 present"     "$PDFOUT" "$([ "$PDFOUT" -ge 1 ] && echo PASS || echo 'FAIL <--')"
printf "  %-34s %s %s\n" "main.bbl bundled"         "$BBL"   "$([ "$BBL" = yes ] && echo PASS || echo 'FAIL <--')"
echo "======================================================================"
echo "Any FAIL above = NOT ready. Fix, then rebuild (the zip does not self-update)."
