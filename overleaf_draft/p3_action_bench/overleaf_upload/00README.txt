Do World Models Make Better Robots?
A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence
================================================================

Self-contained LaTeX source, ready for arXiv submission (and Overleaf).

ARXIV SUBMISSION
----------------
Upload this whole zip. arXiv auto-detects main.tex (the only file with
\documentclass) and builds with pdfLaTeX (forced via \pdfoutput=1).
A pre-built main.bbl is bundled, so arXiv needs no .bib run; refs.bib is
included as well.

  Primary category : cs.RO
  Cross-list       : cs.AI, cs.CV

Expected output: 34 pages, 0 undefined references, 0 undefined citations,
no line numbers, no ACM branding, identical margins on every page, every
figure and table spanning the full text width.

LOCAL / OVERLEAF BUILD
----------------------
  pdflatex main            (one pass is enough thanks to the bundled .bbl)
Full rebuild from scratch:
  pdflatex main && bibtex main && pdflatex main && pdflatex main
Overleaf: upload zip, main document = main.tex, compiler = pdfLaTeX.

DOCUMENT CLASS + LAYOUT
-----------------------
\documentclass[manuscript,nonacm,oneside]{acmart}
\geometry{hmarginratio=1:1}
  manuscript = single-column preprint layout
  nonacm     = no ACM conference/journal branding, no copyright strip
  oneside + hmarginratio=1:1 = same left/right margins on every page
  (no odd/even "slip"); the review/line-number option is removed.
All figures and tables (body + appendix) are set to the full text width.

FILE MAP
--------
main.tex                  preamble (\pdfoutput, \geometry, mark macros
                          \yy \nn \pp \dm \dopen \dclosed \dbridge + colours),
                          title, author block, \input order, bib, appendix
main.bbl                  pre-built bibliography (164 references)
refs.bib                  all 164 references
styles/taxonomy_style.tex forest style + colour palette
sections/                 abstract, intro, methodology, taxonomy, gap,
                          future, limitations, conclusion, appendix
figures/                  11 figures (TikZ/forest) + figures/img/ (61 assets)
tables/                   13 tables (longtable / booktabs)

CONTENT
-------
160 web-verified benchmarks, 2017-2026, across four evaluation lanes
(policy suites, embodied agents, world-model evaluation, prediction-to-action
bridges). Core taxonomy = 86 representatives; full catalogue in Appendix A.
