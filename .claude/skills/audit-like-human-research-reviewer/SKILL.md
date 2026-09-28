---
name: audit-like-human-research-reviewer
description: Audit every figure and table of a paper the way a skeptical human reviewer reads it, not the way its builder does. Catches process artefacts (columns or sentences about HOW we built it), chat framing leaked into the paper, numbers carried over from chat instead of re-derived, unsupported caption claims, cherry-picked rows, undefined symbols, cross-deliverable inconsistency, redundancy and render defects. Use for "audit the figures/tables", "review like a reviewer", "is this table publishable", before any hand-over of deliverables, and after any renumbering or regeneration.
---

# Audit like a human research reviewer

A builder audits what they meant to build. A reviewer audits what is on the page, asking of every
column, row, symbol and caption sentence: **"What does this tell me about the subject, and how do I
know it is true?"** This skill makes the audit take the reviewer's side.

It complements, not replaces: `.claude/audit/rubric.md` (render parity), `.claude/agents/parity-auditor.md`
(type/structure parity) and the survey-pipeline audit fleet. Log every confirmed miss to
`.claude/audit/misses.jsonl`.

## Who runs it
A **fresh agent with no build context** (spawn `general-purpose`, hand it this file plus the deliverable
paths, never your own summary of them). The builder's memory of intent is exactly what hides a defect:
the regression case below was built, rendered, viewed and reported as done by the same session.
Default stance: **every artefact is FIX until each check below is shown to pass.**

## Inputs to read (all three, per artefact)
1. The **render** (PNG at full resolution, every page of a longtable). Judge what a reader sees.
2. The **source** (.tex) and its **generator** (the script that wrote it).
3. The **primary data** the numbers come from (TSV/JSON snapshot, API, paper, leaderboard file).
   Never accept a number because it appears in a chat message, a hand-off report, or another table.

## The checklist (every artefact, every item)

| # | Check | Fails when | Typical fix |
|---|-------|-----------|-------------|
| R1 | **Reader relevance** | A column, row, symbol or caption sentence describes our PROCESS or TOOLING (our search query, our harvester, our script, "found by", "in our snapshot", "we verified with a token", file names, TSV paths) instead of a property of the works or systems. Methods artefacts (PRISMA flow, search strings) are the only place process belongs. | Delete it, or replace it with the subject property it was standing in for (e.g. base model, weights released, method kind). |
| R2 | **Chat-to-paper leak** | Framing, labels or vocabulary invented in a chat reply reach the paper unexamined: emojis, "who is competing", "name clash", "honest", "beats", rhetorical questions, casual shorthand, a column that answered a question only the user asked in chat. | Rewrite in neutral scholarly terms, or drop if it only served the chat. |
| R3 | **Re-derived numbers** | Any count, score, date or percentage is not recomputed from the primary data at audit time. Chat-era numbers are presumed wrong (see regressions: 7 vs 6 mirrors, "about 33" vs 31, "~140" vs 136). | Recompute from the snapshot; generator must compute, never type, every number. |
| R4 | **Caption claims supported** | A caption or in-figure sentence asserts something the artefact does not show, or uses an unchecked quantifier ("most", "only", "several", "all", "can still rise", "better calibrated"). | Verify against the data; soften, quantify, or delete. |
| R5 | **Column and symbol semantics** | A column header is ambiguous, a unit is missing, or a symbol (--, ?, check mark, colour, shading, bold) is not defined in the caption or legend; or a cell value follows a different rule from its neighbours. | Define every symbol in the caption; make every column's rule explicit. |
| R6 | **Selection and bias** | Rows are a subset without a stated, reproducible rule; ranks have unexplained gaps; the selection flatters one side; a comparison mixes incomparable settings (hosted vs on-card latency, different benchmark versions). | State the rule in the caption, or show contiguous rows; separate incomparable settings. |
| R7 | **Cross-deliverable consistency** | The same entity has different numbers or names in two artefacts (works, surveys, stages, family names T1-T5), or a cross-reference points to the wrong table after renumbering. | Single source of truth in the generator; rebuild all. |
| R8 | **Redundancy** | Two artefacts carry the same rows and columns (a subset table), or a figure repeats a table without adding a view. | Offer removal with overlap counts (ask the user). |
| R9 | **Provenance** | A named paper, model or system has no citation or link; a link does not resolve; a URL, id or figure number is guessed. | Cite or hyperlink every name; check each link; drop what cannot be verified. |
| R10 | **Render and legibility** | Text below body size, overlaps, clipping, overfull > 5 pt, washed-out or single-colour categorical fills, unreadable tiles, links invisible. | Fix on the source, re-render, re-view the pixels. |
| R11 | **Publication tone** | Em-dashes, non-British spelling, promotional or adversarial wording about a product or group, personal notes, TODOs, venue self-reference, file paths in captions. | Rewrite. |
| R12 | **Scope fit** | The artefact answers a question outside the paper's stated scope or axis, or its category labels are ad hoc rather than defined in the paper. | Tie it to the paper's axis in the caption, or move it out of the paper. |

**The reviewer's question, asked of every column and caption sentence:** write one line saying what
it tells a reader about the subject. If the honest answer is "how we collected or built it", it fails R1.

## Procedure
1. Enumerate the deliverables from the build manifest (not from memory); count them.
2. For each artefact, fill one row per failing check: artefact | check id | what the reader sees |
   evidence (data, line, pixel region) | severity (block / major / minor) | fix.
3. Re-derive at least every number in captions and every table cell that a reader would quote.
4. Default-FIX: an artefact is CLEAN only when every check has a stated pass reason.
5. Apply fixes in the GENERATOR, rebuild, and send the SAME agent the new renders to re-verify its own
   findings. Loop until every artefact is CLEAN.
6. Append each confirmed miss to `.claude/audit/misses.jsonl` (date, ref, class, miss, why_missed, rule).

## Output
One table, most severe first, then a count line: `N artefacts, K CLEAN, M FIX`, ending with exactly
`REVIEWER VERDICT: CLEAN` or `REVIEWER VERDICT: FIX`.

## Regressions this skill exists to stop (dated)
- **2026-09-27, P05 Table 11 (Decision Index):** a column "Found by search 'jev'" (yes/no/--) plus a
  caption sentence about what a Hugging Face name search finds. It described the authors' search
  procedure, not the ranked systems, and came from a chat framing ("the jev search misses the strongest
  competitors"). Built, rendered and reported done by the same session; caught by the user. Class R1+R2.
- **2026-09-27, same session, chat numbers carried into artefacts:** "7 exact mirrors" (weight hashes: 6),
  "about 33 checkpoints" (31), "~140 with trained weights" (136), "open-model scores can still rise"
  (false: all systems share the scored panel), an AutoJev "jev in repo name: no" (its id contains
  "jev"). Each came from a chat summary, not a re-derivation. Class R3+R4.
- **2026-09-27, same session, a definition changed but only the named rows were retagged:** Table 2's
  Action and X definitions were tightened over six audit rounds (explicit rule or trained behaviour;
  evaluation-only selective curves are none; X admits judge calibration and reliance studies), but each
  round retagged only the rows the auditor had named, so twins of those rows kept the old value
  (steyvers2024what vs kim2024im; cole2023selectively vs kamath2020selective; "adapt compute" first defined
  backwards). Rule: when a definition or controlled value changes, re-apply it to EVERY row and encode it
  as a build-time check that fails on any row violating it (merge_corpus.py: X-row clause check,
  Metric-records-the-curve check). Check the direction of every new value against 2+ tagged papers. Class R5.
- **2026-09-27, P05 paper build, floats taller than the page were invisible:** the deliverables were
  rendered with the `preview` package, which crops each float with no page limit, so Tables 1 and 2
  (110 pt and 129 pt taller than an acmsmall page) looked fine as PNGs and only failed when the full
  paper was compiled (LaTeX deferred every later table to the end). Rule: check page fit in the TARGET
  document, not in a cropped render; `build/build_paper.py` now reports `floats_too_large`. Class R12.
- **2026-09-28, P05, per-row fields fixed by name, never swept:** the Contract, Metric and Trained
  columns were corrected row by row as each audit round named rows (15+ rounds), while twins of every
  named row kept the wrong value. What converged was a FULL column sweep: one reading agent per stage
  slice labels every row from the paper's main text into a per-paper file with a quote
  (literature/contract_labels.tsv, literature/metric_labels.tsv), applied by the build. Rule: the second
  time an audit names rows of one column, stop fixing names and sweep the whole column. Class R3+R5.
