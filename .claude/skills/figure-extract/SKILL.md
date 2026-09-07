---
name: figure-extract
description: Extract every figure (or table) from a LaTeX paper as a standalone tight-cropped PNG and PDF, correctly named. Use for "compile the figures", "figure as png", "standalone figure", "export figures from the paper", or whenever a figure image is needed for slides, a website, a social post, or a hand-drawn redraw.
---

# Figure extract (LaTeX float -> standalone PNG + PDF)

Renders each float of a compiled paper on its own tight-cropped page, then maps page -> figure name
and exports `figures/out/<name>.png` (300 DPI) and `figures/out/<name>.pdf`.

## The two traps (both cost real time; do not skip)

| Trap | Symptom | Fix |
|---|---|---|
| Missing `floats` option | every page blank, PNGs ~98 bytes | `\usepackage[active,tightpage,**floats**]{preview}` -- figures ARE floats, so `\PreviewEnvironment{figure}` alone renders nothing |
| Unseeded `.aux` | captions show `\S??` and `[?]` | copy the REAL `main.aux` to `<job>.aux` before the run, or just run pdflatex TWICE |
| Page order != figure order | `fig_taxonomy.png` holds a table | tables interleave with figures; NEVER assume page N = figure N. Build a contact sheet and map by eye |
| zsh unmatched glob | cleanup deletes nothing | see the `zsh-glob-nomatch` audit rule; delete explicit names, globs separately |

## Recipe

```bash
python3 .claude/skills/figure-extract/tools/extract_figures.py <paper_dir> [--tables] [--dpi 300]
```

It (1) copies `main.tex` to `fr.tex` injecting the preview package, (2) runs pdflatex twice,
(3) emits a labelled contact sheet at `figures/out/_contact.png`, (4) prints a page->name mapping
template for you to confirm, (5) on `--map` renders the named PNG+PDF pair for every entry.

## MANDATORY verification (a render is not a result)
1. Check no output is blank: every PNG must be well over 5 KB and its dimensions sane.
2. **VIEW the pixels** of at least the hero figure and any figure you will reuse downstream.
3. Confirm the NAME matches the CONTENT (this is the page-order trap). If `fig_eval_loop.png`
   shows a table, the map is wrong, not the renderer.

## Cleanup
Delete `fr.tex fr.pdf fr.aux fr.log fr.out fr.bbl` by EXPLICIT NAME (never mixed with a glob).
`figures/out/` is a derived artifact: gitignore it, or delete it after use. It reached 159 MB in
this repo and had to be purged.
