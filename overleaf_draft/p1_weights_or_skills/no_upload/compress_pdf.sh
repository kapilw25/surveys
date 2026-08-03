#!/bin/sh
# Post-build hook (invoked by latexmk $success_cmd in ../.latexmkrc, run from the paper dir).
# Shrinks the NAMED preprint PDF to ~18-20 MB with a high-quality JPEG re-encode (QFactor 0.03 @ 2000dpi).
# Only touches main_preprint.pdf; leaves the anonymized main.pdf (and anything else) untouched.
# Skips a file already under 20 MB, so no-op rebuilds do not re-compress (which would progressively
# degrade quality). A real recompile produces a fresh full-res PDF that is compressed exactly once here.

pdf="$1"
case "$pdf" in
  *main_preprint.pdf) : ;;   # the named preprint: proceed
  *) exit 0 ;;               # main.pdf / anything else: skip
esac
[ -f "$pdf" ] || exit 0

sz=$(stat -f%z "$pdf" 2>/dev/null || stat -c%s "$pdf" 2>/dev/null || echo 0)
[ "$sz" -lt 20971520 ] && exit 0   # already < 20 MB: nothing to do

tmp="${pdf%.pdf}.__c.pdf"
gs -sDEVICE=pdfwrite -sOutputFile="$tmp" -dCompatibilityLevel=1.5 -dNOPAUSE -dQUIET -dBATCH \
   -dDownsampleColorImages=true -dColorImageResolution=2000 -dColorImageDownsampleThreshold=1.0 \
   -dDownsampleGrayImages=true  -dGrayImageResolution=2000  -dGrayImageDownsampleThreshold=1.0 \
   -dAutoFilterColorImages=false -dColorImageFilter=/DCTEncode \
   -dAutoFilterGrayImages=false  -dGrayImageFilter=/DCTEncode \
   -c "<< /ColorImageDict << /QFactor 0.03 /Blend 1 /HSamples [1 1 1 1] /VSamples [1 1 1 1] >> /GrayImageDict << /QFactor 0.03 /Blend 1 /HSamples [1 1 1 1] /VSamples [1 1 1 1] >> >> setdistillerparams" \
   -f "$pdf" 2>/dev/null || { rm -f "$tmp"; exit 0; }

if [ -f "$tmp" ]; then
  mv "$tmp" "$pdf"
  newsz=$(stat -f%z "$pdf" 2>/dev/null || stat -c%s "$pdf" 2>/dev/null || echo 0)
  echo "[compress_pdf] $pdf -> $((newsz / 1024 / 1024)) MB (QFactor 0.03 @ 2000dpi)"
fi
