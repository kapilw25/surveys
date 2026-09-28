# Reviewer audit R1: P05 core tables, round 2

Audit date: 2026-09-27. Stance: default FIX. Scope: the current Tables 1-8 in `deliverables/` (table3: 5 pp., table5: 3 pp., table8: 6 pp.). Every page was viewed, and each table was checked against its source `.tex`, its generator (`gen_phaseA.py`, `gen_corpus.py`, `gen_handtables.py`, `gallery.py`, `p05_common.py`, `build_all.py`) and the primary data (`corpus.tsv`, `s4_families.tsv`, `field_overrides.tsv`, `prior_surveys.md`, the g1 audit notes). Appendix Tables A1 and A2 are out of scope.

Mapping from round 1: old 4 and 6 are now Table 4; old 7 is now 6; old 8a and 8b are now 7; old 9 is now 8.

## Re-derived at audit time (passes)

| Item | Result |
|------|--------|
| Table 1: 39 rows; full-mark counts 24/2/3/8/0/6/5 | All 39 rows match the `prior_surveys.md` matrix cell by cell (0 differences). The counts were recomputed |
| Table 3: 79 core + 5 theory rows; family sizes T1 22, T2 6, T3 31, T4 16, T5 4 | All 84 rows match `corpus.tsv` (Yr, Contract, Action, Metric) and `s4_families.tsv` (family), with 0 differences. Corpus stages: S4 79, TH 5 |
| Table 5: 50 = 23 typed-decision + 27 X constrained; "3 of the 23 report a calibration metric" | The row set equals the stated rule applied to the corpus. The 3 are Jung 2024 (multiple), Yaldiz 2026 (ECE) and Badhe 2026 (multiple) |
| Table 8: 408 = 35+34+63+126+79 (pointer)+5+66 | 329 listed rows match `corpus.tsv` in all 9 columns (0 differences); the S4 pointer covers 79 |
| Table 7: 44 rows | Every arXiv id equals the corpus id and the bib eprint, and every row's stage equals its group heading. arXiv abstract pages fetched: 2601.13284 Yaldiz, 2604.22779 Gao, 2607.04332 Tan, 2505.04016 SLOT, 2210.12265 Ahuja, 2305.13281 Cohen. Titles match and all six are CC BY 4.0. Figure numbers checked in arXiv HTML: Yaldiz Fig. 1 is a reliability diagram, Tan Fig. 4 is calibration plots, Gao Fig. 4 is the framework overview |
| Citation labels across renders | `all.bbl` and `longs.bbl` give identical labels (checked for baniharouni2025rewarding, wang2026process, li2026jev, liu2024can) |
| Table 5, Li 2026b row | The arXiv abstract of 2609.26550 confirms "sixteen ... judges" and "retains 99%" |

## Status of the 32 round-1 findings

| # | Round-1 finding (short) | Status | Evidence now |
|---|-------------------------|--------|--------------|
| 1 | Table 5 caption "None of them measures ... calibrated", contradicted by Badhe | FIXED | The caption now counts "3 of the 23 typed-decision works report a calibration metric"; Yaldiz and Badhe are listed |
| 2 | T1-T5 assigned by keyword regex | FIXED | Families are read from `literature/s4_families.tsv`, which gives a per-paper reason; 84 of 84 rows match it |
| 3 | 8 non-S4 works counted in the core | FIXED | Theory and analysis works are now stage TH (5), listed separately and "not counted in the core". Kang 2024 is now T2 with a method reason |
| 4 | Table 9 render ran into the References | FIXED | `\clearpage` before the bibliography; table8 p. 6 ends at the bottom rule |
| 5 | "¡uncertain¿" glyph | FIXED | `esc()` escapes `<>`; Table 3 p. 2 shows "<uncertain>" |
| 6 | Table 1 product-derived columns plus all-✓ self row | FIXED | PAR and S12 dropped; the self row uses a distinct ● defined as "within this survey's scope" (a residual on HAL is N9) |
| 7 | Old Table 4 exemplars not typed; product-claim clause | FIXED | The merged Table 4 S4 row cites Yaldiz 2026 (typed-decision); the clause is gone |
| 8 | Lin 2022 used as the S2 exemplar | FIXED | The Table 2 S2 exemplar is now Tian 2023 (corpus S2) |
| 9 | S1/S4 "no guarantee" contradicted by the corpus | FIXED | Table 4: S1 reads "binning: distribution-free [Gupta and Ramdas]"; S4 notes Pan 2026a |
| 10 | Old Table 3 repeated in Table 9 | FIXED | The Table 8 S4 block is a pointer to Table 3 |
| 11 | Old Tables 4 and 6 overlapped | FIXED | Merged into Table 4 |
| 12 | Table 5 repeated in Table 9 | NO LONGER APPLICABLE | The user declined further removals. Recorded overlap: 41 of 50 Table 5 rows also appear in Table 8, and 9 of 50 in Table 3; Yr and Metric are shared |
| 13 | Table 5 selected by keyword regex | FIXED | A stated contract rule; the row set equals the rule applied to the corpus |
| 14 | Undefined values in Contract, Metric, Trained, Yr | NOT FIXED (partial) | The shared legend now defines Contract, Access, Metric, Trained, Yr and "?". Two values remain undefined in Table 8: Metric "coverage" (33 works) and "selective" (10), which the legend folds into "other" but prints as distinct values; and every Action value (none, answer, abstain, set, route, defer, escalate). See N1 for the contract-definition conflict |
| 15 | X routers had Trained = yes; Chuang in X | FIXED | Routers and SLOT are now "partial" (X: 13 partial, 0 yes); Chuang 2024 is S4, T1 |
| 16 | Table 2 caption over-claimed "recorded for every work" | FIXED | The parallel row is removed; row 1 is declared "a term, not an inclusion rule" |
| 17 | Table 7 caption "four of them" and product framing | FIXED | Table 6 now says "measured decision ECE (panels a and d) and the target shapes ... (panels b and c)", which matches Fig. 11; "on common ground" replaces "the terms they claim" |
| 18 | Yr and citation year differed with no definition | FIXED | "Yr: year of the first public version" appears in the Tables 3, 5 and 8 captions |
| 19 | Citation letters differed across renders | FIXED | One shared bibliography; labels are identical in `all.bbl` and `longs.bbl` |
| 20 | T0 undefined; family names inconsistent | FIXED | The theory block has a heading, not T0; "?" is defined; names come from `p05_common.TNAME` and match `fig_taxonomy_main.tex` |
| 21 | Table 1: full-text rows unmarked, colour undefined, no selection rule, venue style | FIXED | † added, the red 0 defined, the rule stated, venues normalised (a residual on the † set is N8) |
| 22 | Process and assurance wording in captions | FIXED | The Table 7 and Table 8 captions are plain; "never guessed" and "verified primary works" are gone |
| 23 | Gallery panels picked with no stated rule | FIXED for the table | Table 7 lists 8 S4 panels, 6 of them 2025-26 core works; the rule is in the Fig. 8/9 captions (a residual is N10) |
| 24 | Tables 8a and 8b duplicated each other | FIXED | Merged into Table 7 with a "Used in Fig." column |
| 25 | Render: orphan heading, wrapped cite labels, "typed-/decision", `\scriptsize` | NOT FIXED (partial) | The orphan and cite-label wrapping are fixed (`\\*`, hanging indent). "typed-/decision" still breaks over two lines in Tables 3, 5 and 8. Table 4 hyphenates "probabili-ties", "elicita-tion" and "confor-mal". Table 8 is still `\scriptsize` |
| 26 | American spelling in authored cells | NOT FIXED (partial) | Still rendered: "penalized" (Che 2026, Tables 3 and 5), "Characterizes" (Jitkrittum), "tokenization" (Beurer-Kellner 2024), "detokenizing" (Koo), "Blackbox" (Geng 2024a), all in Table 5; "self-judgment" (Liu 2026a, Table 3). `brit()` has no rules for these forms |
| 27 | Uncited self-consistency; unverified 5-10 samples; over-claim | FIXED | Table 4 cites Wang 2022, reads "several sampled answers", and the claim is removed |
| 28 | "Xiaohu et al." author inversion | NOT FIXED | Tables 3 and 8 still render "Xiaohu et al. [2026]". The bib now reads "Xie Xiaohu, Liu Xiaohu" in first-last order, so BibTeX still takes "Xiaohu" as the surname. arXiv lists "Xie Xiaohu, Liu Xiaohu, Yao Benjamin" |
| 29 | Families labelled "other" | FIXED | Families are named in Table 8 |
| 30 | Raw lowercase Table 5 headers; SLOT labelled constrained | FIXED | Headers are title case; SLOT is free-text via `field_overrides.tsv` |
| 31 | 13 S2 rows with Samples = yes against the S3 criterion | FIXED | The Table 2 S2 row now keeps prompt methods that aggregate prompted answers in S2 |
| 32 | Table 6 S2 cost; S1 black-box wording | NOT FIXED (partial) | The S2 cost is now explained. The Black-box column still mixes forms: S0 "no: needs token probabilities" and S1 "needs the model's scores, not its weights", with no yes/no for S1, though S1 needs the same token probabilities as S0 |

## New findings on the current Tables 1-8 (most severe first)

| # | Artefact | Check | What the reader sees | Evidence | Severity | Fix |
|---|----------|-------|----------------------|----------|----------|-----|
| N1 | table2, table5, table8 | R5, R7 | Two definitions of a typed decision disagree. Table 2: "the output space is declared before inference and the model cannot emit a value outside it". The legend in Tables 3, 5 and 8: "typed-decision (a probability per declared option)" and "constrained (grammar or schema)" | By Table 2's wording, all 27 grammar- or schema-constrained works in Table 5 are typed decisions. Labels also disagree within Table 5: Singh 2026a (a JSON-schema validity benchmark) is typed-decision, while Shorten 2024 (a JSON-formatting benchmark) was overridden to constrained with the reason "Table 2 defines typed-decision as a declared option set scored per option", which is not what Table 2 now says | major | Make Table 2's row match the legend (a probability per declared option), and apply the Shorten override reasoning to Singh 2026a |
| N2 | table5 | R4 | "3 of the 23 typed-decision works report a calibration metric (ECE, Brier or several)" | Two of the three (Jung 2024, Badhe 2026) are "multiple", which the legend defines as "more than one" metric, not "more than one calibration metric". Jung 2024 reports human-agreement guarantees | minor | Say "report ECE or several metrics", or check that Jung's metrics include a calibration metric |
| N3 | table5 | R5 | The caption defines Contract, Access and Trained values | Table 5 shows only Work, Yr, Contribution and Metric | minor | Trim the legend to the columns shown |
| N4 | table5 | R2 | The Li 2026b cell reads "decision-only (System-One) judge" | The arXiv 2609.26550 abstract has no "System-One" or "System 1"; the term is product vocabulary | minor | Drop "(System-One)" from the corpus contribution text |
| N5 | table2 | R5, R7 | The caption defines "the stages (S0 to S4)" | Tables 3 and 8 also group by TH (5 works) and X (66 works); neither is defined in Table 2. TH appears only as the S4 "does not count" note | minor | Add rows for X (consumers and contract) and TH, or a sentence in the caption |
| N6 | table8 | R7 | The TH block shows Bereket and Leskovec 2025 under the subgroup "RL calibration reward" with Trained = yes | `s4_families.tsv` gives the reason "analysis ... no new objective", and the legend says Trained = yes means calibration is a training objective of the model itself | minor | Set Trained to no (or partial) and relabel the subgroup "Analysis" |
| N7 | table3 | R7 | Wang 2026a (CAPO) is in S4 T3 with Metric AUROC; its contribution is "logistic AUC surrogate loss" | Table 2 row 1: AUROC "measures discrimination, not calibration"; S4 requires a calibration term in the loss or reward | minor | Justify the calibration term in the contribution text, or move the work out of the core |
| N8 | table1 | R5, R3 | † is defined as "corrected from a full-text reading", but Li 2025b, Lin 2026 and Boudiaf 2026 have no † | `g1_reaudit.md` R3 and lines 36-37 set A8 and A9 `TYP` from full text; round 4 set F5 `TYP` from the round-2 full-text read. `FULLTEXT` in `gen_phaseA.py` omits A8, A9 and F5 | minor | Add A8, A9 and F5 to `FULLTEXT` |
| N9 | table1 | R12 | The ● scope row includes `HAL` | No Table 2 construct, corpus column or stage records hallucination | minor | Drop `HAL` from the scope row (keep it as context), or state how the survey covers it |
| N10 | table7 (and the Fig. 8/9 captions) | R6 | The rule reads "one per training family T1 to T5 at S4" | Table 7's Fig. 9 S4 panels are Steyvers and Zhang 2025c (both T1) and Tan and Yaldiz (both T3); Fig. 8 has no T2 panel. `gallery.py` picks round-robin across families and then filters by visual verdicts (`gallery_verdicts.tsv`), which the caption does not state | minor | Restate the rule as "round-robin across families, then tiles kept after visual inspection", or enforce one per family |
| N11 | table6 | R12, R5 | Decision ECE names two testbeds (MMLU, and the Decision Index in appendix Table A2); none of the six metrics separates the T1-T5 families, which are the paper's axis | Table 6 row 1; `novelty_gap.md` | minor | Name one testbed per metric; consider adding a family-level comparison (e.g. decision ECE by family under matched compute) |

## Count

8 artefacts, 1 CLEAN (table7), 7 FIX (table1, table2, table3, table4, table5, table6, table8). Remaining open items: 1 major (N1) and 15 minor (residuals of #14, #25, #26, #28 and #32, plus N2-N11).

REVIEWER VERDICT: FIX

# Round 3

Audit date: 2026-09-27. Every page of the rebuilt Tables 1-8 renders (01:40 build) was viewed, and each was checked against its current `.tex`, the generators (`p05_common.py` `legend()`/`brit()`/`contract_label()`, `gen_phaseA.py` `FULLTEXT`, `gallery.py` RULE) and `corpus.tsv`, `s4_families.tsv` and `field_overrides.tsv`.

## Re-derived at audit time (passes)

| Item | Result |
|------|--------|
| Corpus stages | S0 35, S1 34, S2 63, S3 126, S4 79, TH 5, X 66 (408) |
| Table 3: 84 rows | All match the corpus (Yr, Contract, Action, Metric) with 0 differences. Family sizes T1 22, T2 6, T3 31, T4 16, T5 4 |
| Table 5: 50 rows = 22 typed + 28 X constrained | The row set equals the stated rule applied to the corpus (Singh 2026a moved to constrained by override) |
| Table 8: 324 rows | All match the corpus in all 9 columns (0 differences). 324 = 408 - 79 - 5; the caption's "324" is correct |
| Table 7: 32 rows | Every arXiv id equals the corpus id and the bib eprint, and every row's stage equals its heading. The S4 panels (Gao T4, Guo T1, Yang 2026b T3 in Fig. 8; Steyvers T1, Tan T3 in Fig. 9) follow the stated rule "one per training family, largest families first, at most 3 per stage" |
| Xie et al. 2026 | The arXiv HTML byline reads "Xiaohu Xie, Xiaohu Liu, Benjamin Yao"; the bib is now `Xie, Xiaohu and ...` and the table renders "Xie et al. [2026]" |
| Badhe 2026 (arXiv 2605.09739) | The abstract reports "Expected Calibration Error (ECE) and Brier Score" as well as AUROC and Macro-F1 |

## Status of the 16 items open after round 2

| # | Item | Status | Evidence now |
|---|------|--------|--------------|
| 14 | Metric "coverage"/"selective" and all Action values undefined | FIXED | Per-table legends (Tables 3, 5, 8) define selective, coverage and every Action value; each legend covers only the columns printed |
| 25 | "typed-/decision" wrap; Table 4 hyphenation; Table 8 `\scriptsize` | NOT FIXED (partial) | "typed" now fits on one line. Table 4 still renders "probabili-ties" (S0 Black-box), "elicita-tion" and "confor-mal" (Stage column): `\hyphenpenalty=2000` is not enough in 0.08/0.09`\textwidth` columns. Table 8 is still `\scriptsize` |
| 26 | American spellings in authored cells | FIXED | The renders show penalised, Characterises, tokenisation, detokenising, Black-box and self-judgement; a grep of the table sources finds only cite keys and LaTeX `\color` |
| 28 | "Xiaohu et al." | FIXED | See the table above |
| 32 | Table 4 S1 Black-box cell | FIXED | Now reads "partly: needs the model's scores, not its weights" |
| N1 | Two conflicting definitions of typed decision | FIXED | Table 2 now reads "the options are declared ... the model assigns a probability to each option", and grammar or schema output is "constrained", matching the legend. Singh 2026a and Shorten 2024 are both constrained |
| N2 | Table 5 calibration-metric count | NOT FIXED | The caption now says "1 of the 22 typed-decision works report ECE or Brier score as their calibration metric". This is false: Badhe 2026 (in Table 5) reports ECE and Brier per its arXiv abstract but is coded "multiple", so an exact-match count on ECE/Brier misses it. The true count is at least 2 (Yaldiz, Badhe); Jung 2024 is also "multiple" and unchecked. Grammar: "1 ... report" |
| N3 | Table 5 legend defined columns not shown | FIXED | The legend now covers only Yr and Metric |
| N4 | "(System-One)" product vocabulary | FIXED | Reworded via `field_overrides.tsv`. The same cell now has a render defect, see N12 |
| N5 | X and TH undefined in Table 2 | FIXED | New "X consumers" and "Theory and analysis" rows |
| N6 | Bereket 2025 Trained = yes under an RL label | FIXED | All 5 TH works are Trained = no in the group "theory and analysis"; the Table 8 TH block is a pointer to Table 3 |
| N7 | CAPO (AUC) in S4 T3 | FIXED | The T3 definition now includes ranking-based (AUC) rewards and states that they "target discrimination as well as calibration" |
| N8 | † missing on A8, A9, F5 | FIXED | `FULLTEXT` includes them; the render shows † on Li 2025b, Lin 2026 and Boudiaf 2026 |
| N9 | HAL in the scope row | FIXED | A separate ❍ symbol, defined as "in scope only through abstention training and the theory works" |
| N10 | Gallery rule did not match the panels | FIXED | The rule now says "largest families first, newest figure that passed a visual check, at most 3 per stage", which matches Table 7 |
| N11 | Table 6 had no family-level metric | FIXED | New "Family comparison" row (T1-T5 on the same base model and data, MMLU); "Seven quantities" matches the 7 rows |

## New findings (round 3)

| # | Artefact | Check | What the reader sees | Evidence | Severity | Fix |
|---|----------|-------|----------------------|----------|----------|-----|
| N12 | table5 | R10 | The Li 2026b cell prints "retains 99\% of the comparator accuracy", with a visible backslash | `field_overrides.tsv` stores the value already escaped (`99\%`), and `esc()` escapes the backslash again (`99\textbackslash{}\%`) | minor | Store plain `99%` in the override and let `esc()` escape it |
| N13 | table3 | R5 | The T2 definition says "its works are marked Trained = partial when the policy is not retrained", but Table 3 has no Trained column. In the corpus, Lou 2024 (URM, a reward model with no policy step in its contribution) is Trained = yes | Table 3 columns: Work, Yr, Contribution, Contract, Action, Metric; corpus `trained` values for T2: kang yes, leng yes, lou yes, park partial, ma partial, pan yes | minor | Drop the Trained clause from the Table 3 caption (Trained is shown only in Table 8), or check Lou 2024's value |

## Count

By artefact:

| Artefact | Status | Open items |
|----------|--------|------------|
| table1 | CLEAN | none |
| table2 | CLEAN | none |
| table3 | FIX | N13 (minor) |
| table4 | FIX | #25 hyphenated stage and cell words (minor) |
| table5 | FIX | N2 (major), N12 (minor) |
| table6 | CLEAN | none |
| table7 | CLEAN | none |
| table8 | FIX | #25 `\scriptsize` body (minor) |

8 artefacts, 4 CLEAN, 4 FIX. Open: 1 major (N2), 4 minor (#25 in Tables 4 and 8, N12, N13).

REVIEWER VERDICT: FIX

# Round 4

Audit date: 2026-09-27. The rebuilt renders (01:58 build) of Tables 2, 3, 4 and 5 were viewed page by page. Tables 1, 3, 5, 7 and 8 were re-derived from the data again.

## Re-derived at audit time (passes)

| Item | Result |
|------|--------|
| Table 5 claim "3 of the 22 typed works report ECE or Brier score, alone or with other metrics" | 22 typed works in the corpus. Yaldiz 2026 has ECE. Badhe 2026 and Jung 2024 are "multiple" with a recorded check in `literature/metric_checks.tsv`. Independently confirmed on arXiv: the 2605.09739 abstract names ECE and Brier; the 2407.18370 HTML has "ECE ↓" in Table 1 and "reducing ECE by 50%". Zong 2026 (selective) is correctly excluded. The count is 3 |
| Row checks | Table 3: 84 rows, 0 differences. Table 5: 50 rows (rule-exact). Table 8: 324 rows, 0 differences in all 9 columns. Table 7: 32 links. Table 1: 39 rows |

## Status of the open items

| # | Item | Status | Evidence now |
|---|------|--------|--------------|
| N2 | Table 5 ECE/Brier count | FIXED | See above. Label "typed" and verb agreement ("3 ... report") are correct |
| N12 | "99\%" backslash in the Li 2026b cell | FIXED | The override stores plain `99%`; the Table 5 render reads "retains 99% of the comparator accuracy" |
| N13 | T2 definition referred to the absent Trained column | FIXED | The Table 3 caption for T2 now ends "is calibrated or made uncertainty-aware"; "Trained" no longer appears in the Table 3 source |
| #25 (Table 4) | Hyphen breaks in narrow columns | FIXED | Table 4 now renders "S0 read-off", "S2 prompt elicitation", "S3 conformal" and "token probabilities" with no hyphen breaks; no cell in the render is hyphenated |
| #25 (Table 8) | `\scriptsize` body | NO LONGER APPLICABLE | Kept by an owner decision as the full-corpus landscape (324 rows by 10 columns). Legibility was re-checked on all 6 pages at render resolution, with no clipping or overlap. Small type is standard for a table of this size. If the paper later moves Table 8 out of the appendix-style position into the main text flow, this should be revisited |

## New findings (round 4)

| # | Artefact | Check | What the reader sees | Evidence | Severity | Fix |
|---|----------|-------|----------------------|----------|----------|-----|
| N14 | table2 | R10 | The new "Theory" chip in the row label "Theory and analysis" is pale pink on white and noticeably fainter than the S0-S4 and X chips | `stTH` = #D4B0C8; contrast against white is 1.94:1, below the 3:1 minimum for large or bold text. The other chips range from 2.55 (S2 orange, borderline) to 4.61 | minor | Darken `SCOLOR["TH"]` in `p05_common.py` (e.g. #9C6B8E, above 3:1), or render the chip text in black with a pale background |

No other new defects were found. Tables 1, 6, 7 and 8 are unchanged in content since round 3 (rows re-derived), and the Table 2 row relabelling uses the shared stage names consistently with Tables 3, 4 and 8.

## Count

| Artefact | Status | Open items |
|----------|--------|------------|
| table1 | CLEAN | none |
| table2 | FIX | N14 (minor) |
| table3 | CLEAN | none |
| table4 | CLEAN | none |
| table5 | CLEAN | none |
| table6 | CLEAN | none |
| table7 | CLEAN | none |
| table8 | CLEAN | none (#25 waived by owner decision, legibility checked) |

8 artefacts, 7 CLEAN, 1 FIX. Open: 0 major, 1 minor (N14).

REVIEWER VERDICT: FIX

# Round 5

Audit date: 2026-09-27. The rebuilt renders of Tables 2 and 7 (02:12 build) were viewed, and their sources were read. The Table 7 caption claims were re-derived from `corpus.tsv`, `s4_families.tsv`, `literature/gallery_licences.tsv`, `build/gallery_candidates.tsv` and `build/gallery_verdicts.tsv`.

## Status of N14

| # | Item | Status | Evidence now |
|---|------|--------|--------------|
| N14 | Pale "Theory" chip in Table 2 | FIXED | `SCOLOR["TH"]` = #9C6B8E; contrast against white is 4.28:1 (above 3:1). The render shows a legible mauve "Theory" |

## Table 7 caption claims, re-derived

| Claim | Result |
|-------|--------|
| Fig. 8, S4: panels from T3, T1 and T4 (largest families first); "T5 had a figure but was cut by the cap of 3" | True. T3 (31) > T1 (22) > T4 (16) fill the cap of 3; Wang 2026d (T5) has a kept CC BY method figure |
| Fig. 8: "T2 has no reusable figure" | True. All 3 T2 works with a method figure (Leng, Lou, Pan) are marked reusable = no in the licence file |
| Fig. 9: "At S4, T2, T4, T5 have no reusable figure that passed the check" | True. No T2, T4 or T5 work has a recorded results figure; T1 (Steyvers) and T3 (Tan) are shown |
| "newest figure of each" | True for Fig. 9 (T1 Steyvers 2510 is newer than Zhang 2509 and Jang 2506; T3 Tan 2607 is newer than Yaldiz 2601), Fig. 8 T1 (Guo 2026) and Fig. 8 T4 (Gao 2026). Not literally true for Fig. 8 T3: Xu 2026 DualStake (2609, CC BY, method figure) is newer than the chosen Yang 2026b (2607) but was rejected at the visual check (`gallery_verdicts.tsv`: purge). See N16 |

## New findings (round 5)

| # | Artefact | Check | What the reader sees | Evidence | Severity | Fix |
|---|----------|-------|----------------------|----------|----------|-----|
| N16 | table7 | R6 | The rule says "the newest figure of each [family]". The visual check is mentioned only at family level ("families with no reusable figure that legibly shows the method or a result are skipped") | For Fig. 8 T3 the newest CC BY figure is Xu 2026 DualStake (2609.00935, Fig. 1), which was purged at the visual check; Yang 2026b (2607) is shown. A reader re-applying the stated rule would pick a different panel. The round-3 wording "the newest figure of each that passed a visual check" was dropped in the move from the figure captions | minor | Restore the per-figure clause: "taking the largest families first and, in each, the newest figure that legibly shows the method or a result" |
| N15 | table2 | R5 | The caption says the last three rows define properties "recorded for every work: the Contract and Action columns of Tables 3 and 8, and the Guar. column of Table 8" | Table 8 lists only the 324 works outside the core. Table 3 has no Guar. column, so the guarantee property of the 84 core and theory works is recorded in the data but shown nowhere (corpus: 1 of them, Pan 2026a, has Guar. = yes, which only Table 4 mentions) | minor | Add "(for the core, only Pan 2026a states a guarantee; Table 4)" to the caption, or add a Guar. column to Table 3 |

No other new defects in Tables 2 and 7. The Table 7 rows are unchanged from round 4 (32 links, ids and stages verified), and "CC BY 4.0" in every row agrees with the rule. The Table 2 theory-row wording and caption agree with Tables 3 and 8.

## Count

| Artefact | Status | Open items |
|----------|--------|------------|
| table1 | CLEAN | none (unchanged since round 4) |
| table2 | FIX | N15 (minor) |
| table3 | CLEAN | none |
| table4 | CLEAN | none |
| table5 | CLEAN | none |
| table6 | CLEAN | none |
| table7 | FIX | N16 (minor) |
| table8 | CLEAN | none |

8 artefacts, 6 CLEAN, 2 FIX. Open: 0 major, 2 minor (N15, N16).

REVIEWER VERDICT: FIX

# Round 6

Audit date: 2026-09-27. The rebuilt renders (02:25 build) of Tables 1, 2, 3 (all 6 pages viewed where changed: pp. 1, 3, 6) and 7 were viewed, and their sources were read. Tables 3, 5, 7 and 8 were re-derived from the data again.

## Re-derived at audit time (passes)

| Item | Result |
|------|--------|
| Table 3 Guar. column, all 84 rows (79 core + 5 theory) | Every Guar. cell equals the corpus `guarantee` field (0 differences). The only "yes" is Pan 2026a, the one corpus S4 work with guarantee = yes. Yr, Contract, Action and Metric also match on all 84 rows. The legend now defines "Guar.: a stated distribution-free guarantee" |
| Table 5 | 50 rows = rule-exact (22 typed + 28 X constrained); the caption's "3 of the 22 typed works report ECE or Brier score" is unchanged and still verified (round 4) |
| Table 7 | 32 rows, 0 arXiv-id mismatches against the corpus |
| Table 8 | 324 rows, 0 differences in all 9 columns |
| Table 1 | The only source change is the scope symbols (`stS4` to `stS4txt`); the marks and counts are unchanged from round 4 |

## Status of the open items

| # | Item | Status | Evidence now |
|---|------|--------|--------------|
| N15 | Guarantee not shown for the core works | FIXED | Table 3 has a Guar. column for all 84 works. The Table 2 caption now reads "the Contract, Action and Guar. columns of Tables 3 and 8", which is true for both tables |
| N16 | Table 7 rule omitted the per-figure visual check | FIXED | The caption now says "taking the largest families first and, in each, the newest figure that legibly shows the method or a result". This matches the Fig. 8 T3 choice (Yang 2026b over the purged Xu 2026 DualStake) and every other S4 panel checked in round 5 |

## New-defect scan (skill applied to Tables 1-8)

| Check | Result |
|-------|--------|
| R10 colour legibility | Table 2 stage labels use 70% darkened variants (`st<S>!70!black`); every label, including the S2 orange and the new olive "Theory" (#8C6D1F darkened), reads clearly on white. Table 1 scope dots use `stS4txt` and remain distinct from the ✓ marks. The TH colour change (mauve to olive) comes from the shared `SCOLOR`, so the figures that use `stTH` (fig5 bar, fig2 taxonomy box) take the same colour on rebuild. No cross-deliverable mismatch |
| R10 layout | Table 3 with the added Guar. column: no clipping or overlap on pp. 1, 3 and 6; the Contribution column is narrower but wraps cleanly; headers repeat on continuation pages. Table 3 now runs to 6 pages (was 5) |
| R5 semantics | Guar. is defined in the Table 3 legend. The Table 7 caption's "passed the check" refers back to "legibly shows the method or a result" in the same caption, so it is readable as defined |
| R1, R2, R4, R7, R11 | No new process wording, chat framing, unsupported quantifier, cross-table inconsistency or spelling issue in the changed captions and cells |

No new defects found.

## Count

| Artefact | Status |
|----------|--------|
| table1 | CLEAN |
| table2 | CLEAN |
| table3 | CLEAN |
| table4 | CLEAN |
| table5 | CLEAN |
| table6 | CLEAN |
| table7 | CLEAN |
| table8 | CLEAN (#25 small type waived by owner decision, legibility checked in round 4) |

8 artefacts, 8 CLEAN, 0 FIX. Open: 0 major, 0 minor.

REVIEWER VERDICT: CLEAN
