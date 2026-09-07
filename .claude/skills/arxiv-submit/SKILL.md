---
name: arxiv-submit
description: Package a LaTeX paper into a verified arXiv submission zip and fill the arXiv metadata form. Use for "ready for arxiv", "build the arxiv zip", "submit to arxiv", "arxiv metadata", "is the zip ready", or any preprint packaging and submission-readiness check.
---

# arXiv submit (package + verify + metadata)

A zip is "ready" ONLY after a FRESH EXTRACT of the delivered zip compiles clean. Never certify the
working directory and assume the zip matches; they drift.

## Build

```bash
bash .claude/skills/arxiv-submit/tools/build_arxiv_zip.sh <canonical_paper_dir> <out.zip>
```

Stages the canonical dir, purges build artifacts, zips, then fresh-extracts and compiles twice.

## Readiness checklist (every line must pass on the FRESH EXTRACT)

| Check | Pass condition |
|---|---|
| Compile | `pdflatex` x2, exit 0 both passes |
| Pages | matches the expected count |
| Undefined refs / citations | **0** |
| `??` in rendered text | **0** |
| LaTeX errors (`^! `) | **0** |
| Overfull hbox > 5pt | 0 (or justified) |
| `\pdfoutput=1` | present in `main.tex` (forces pdfLaTeX) |
| `main.bbl` bundled | yes (arXiv runs no bibtex) |
| Absolute paths (`/Users/`, `/tmp/`) in includes | **0** |
| Build artifacts in zip (`.pdf/.aux/.log/.out/.synctex.gz`) | **0** |
| Size | < 50 MB |

## The traps

| Trap | What happened |
|---|---|
| **zsh unmatched glob** | `rm -f main.pdf main.aux *.bcf` deleted NOTHING because `*.bcf` had no match; 15 MB of artifacts shipped inside the zip. Delete EXPLICIT names only; keep globs in a separate command. Verify with a file count afterwards. |
| **Stale zip** | The zip does NOT auto-update when the source changes. Rebuild after every content edit, and check its mtime against the source. |
| **Duplicate source trees** | If the repo has more than one copy of the paper, the zip may build from the stale one. Confirm the canonical dir first (see the `duplicate-source-copies` audit rule). |
| **Certifying the wrong artifact** | Compiling the working dir proves nothing about the zip. Always fresh-extract to a temp dir. |

## Metadata form (fill from the paper, never invent)
Pull each value from the source, not from memory:

| Field | Source |
|---|---|
| Title | `\title{}` + subtitle, joined with `. ` |
| Author(s) | `\author{}` block, first names first, comma separated, no "et al." |
| Abstract | `sections/0_abstract.tex`, LaTeX stripped (`\emph{}`, `\%` -> `%`), blank line between paragraphs |
| Comments | `N pages, N figures, N tables` (count them; add venue only if true) |
| Report number / Journal ref / DOI | blank unless actually published |
| ACM class | map `\ccsdesc` to ACM CCS codes (e.g. Robotic planning -> I.2.9, Machine learning -> I.2.6, Computer vision -> I.2.10, general AI -> I.2.0) |
| MSC class | blank for CS papers |
| Categories | primary + cross-list, set on the earlier Add Files step, NOT the metadata page |

Never paste an em-dash or a smart quote into the arXiv form; use plain ASCII.

## After acceptance
Record the arXiv id in project memory and update the site/README links.
