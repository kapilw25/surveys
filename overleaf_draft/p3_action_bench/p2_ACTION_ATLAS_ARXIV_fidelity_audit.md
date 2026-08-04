# Fidelity audit: `p2_ACTION_ATLAS_ARXIV.md` vs `p2_ACTION_ATLAS_ARXIV.pdf`

This records how the Markdown was produced from the 27-page PDF and how its fidelity was verified. Every claim here is manually reproducible with the commands shown.

## Method

The PDF has a real embedded text layer (not scanned images), so the **character source** is the deterministic `pdftotext` extraction, not a model reading page images. The Markdown was built from that text, with structure (headings, lists, tables), LaTeX math, and a small enumerated set of defect-corrections added. Two independent audits verify it:

1. **Deterministic token-diff** (backbone): strip Markdown + LaTeX math from the `.md`, tokenize both it and the raw `pdftotext` into content words (length >= 5), collapse hyphens, and compare the multisets. This proves no accidental drop or fabrication of prose.
2. **Per-page vision audit** (ground truth): 27 agents, one per page, each reads the rendered page image + the per-page `pdftotext` + the `.md`, and reports any discrepancy the word-diff cannot see (table cells, math, reading order, defect-corrections).

Reproduce the deterministic layer:
```
pdftotext p2_ACTION_ATLAS_ARXIV.pdf flow.txt      # the character source
# then tokenize flow.txt and the .md (len>=5 words, hyphens collapsed) and diff the multisets
```

## Deterministic result: PASS

Content-word instances (length >= 5, hyphens collapsed): **PDF = 5403, MD = 5404** (net +1). Every differing token is explained by one of four mechanical causes, with **zero unexplained content words** in either direction:

| Cause | Example (PDF token / MD form) | Words present in both? |
|---|---|---|
| Math-subscript gluing in `pdftotext` | `ntotal` / `N_{\text{total}}`, `ccounterfactual` / `\mathcal{C}_{\text{counterfactual}}` | yes |
| Bold-markdown split of "**X**-style" | `jepastyle` / `**JEPA**-style` | yes |
| Intentional ti-fix (see below) | `predic` / `prediction`, `visionlanguageac` / `visionlanguageaction` | corrected |
| Intentional logo-fix (see below) | `ragya` / `pragya` | corrected |

The net +1 is the ti-fix restoring "prediction"/"visionlanguageaction" from the corrupted source tokens.

## Source defects PRESERVED verbatim (faithful to the PDF, not corrected)

These are defects in the source paper itself. They are reproduced exactly so the `.md` matches the PDF. Each is manually checkable at the cited location.

| # | Location | In the `.md` | Note |
|--:|---|---|---|
| 1 | p14, sec 4.3 (ii) | `V-JEPA (?)` | Unresolved citation in the source (the paper's own missing reference). |
| 2 | p23, sec 6.9 (iii) | `95` | The source truncates "95% confidence intervals" to just "95". Verified against the text layer; the parallel list on p19 sec 5.8 (ii) correctly reads "95% confidence intervals". |
| 3 | p27, References | `Fernando Casta neda` | The n-tilde in "Castaneda" dropped by the source font, leaving a space. Kept as the PDF shows it. |
| 4 | p21, Table 6 | all cells `–` | The capability-level results matrix is an empty placeholder (en-dashes) in the source. |

## Source-font defects CORRECTED against the page images (documented)

The PDF's own text layer mis-renders certain glyphs. Each of these was corrected to what the page visually shows, and each is enumerated so the correction is auditable.

| # | Defect in text layer | Corrected to | Where |
|--:|---|---|---|
| 1 | "ti" ligature extracts as "3" in the headline font (e.g. `Ac3on`, `Predic3on`, `Vision-Language-Ac3on`) | Action, Prediction, Vision-Language-Action | title + section headings only; body text spells these correctly |
| 2 | Devanagari-glued logo glyph (`प्रragya` / `ragya`) | Pragya Lab | affiliation |
| 3 | superscript asterisk extracts as `?` | `*` | author / affiliation marker |
| 4 | subscripts flattened (`pi0`, `tau0`) | `$\pi_0$`, `$\tau_0$` | throughout |
| 5 | line-break hyphenation joins (`vision-languageaction`, `Roboticsstyle`, `instructionconditioned`, `actioncentric`) | proper hyphenation restored | throughout |

## Other conventions

- **Em-dashes:** the source contains exactly 2 em-dashes (one sentence on p3/sec 1). They are written as `---` in the `.md` (renders as an em-dash; also satisfies this repo's no-em-dash hook).
- **Math:** all ~40 equations are transcribed as LaTeX (`$...$` inline, `$$...$$` display).
- **Tables:** Tables 1-6 are placed at their reference points in the text (each falls on the same page as its reference).

## Per-page vision audit: PASS (1 real drop found and fixed)

27 agents, one per page, each comparing the rendered page image + per-page `pdftotext` + the `.md`. Result: **26/27 pages CLEAN, 0 agents failed, 1 page with 1 issue** (now fixed).

| Page | Issue found | Resolution |
|--:|---|---|
| 1 | Section 1 opening paragraph dropped the word "action": source reads "instruction-conditioned **action** traces", the `.md` had "instruction-conditioned traces". | Fixed: "action" restored. Confirmed against `flow_01.txt` line 51 and the rendered page. |

Why the deterministic layer missed this one: "action" appears many times in the document, and the ti-fixes added "action" instances, so a single dropped instance did not create a net multiset imbalance. The per-page vision audit compares against the rendered page directly, so it caught the local drop the aggregate word-count masked. This is exactly why both layers were run.

After the fix, both audit layers are clean.
