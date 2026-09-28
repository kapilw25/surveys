# Reviewer audit, round 2: Tables A1 and A2, cross-artefact consistency, parity of Table 2 and Fig 10 (2026-09-27)

## Sources re-checked at audit time

| Source | Check | Result |
|---|---|---|
| Live board `index.json` (generated 2026-09-27T03:42:13Z) | Diffed field by field against `literature/notes/jev_decision_index_2026-09-27.json`: name, skill, ECE, reliability bins, base, kind, weights and code URLs | ✅ 68 of 68 systems identical; the extract is sorted by skill, so its list position equals the rank |
| Live HF API `search=jev&full=true` (no token) | Recounted A1 counts and downloads from the `downloads` field | ✅ 188 repositories, 41,653 downloads; now 270 results, 2 of them created after the snapshot |
| All 51 hyperlinks in A1 and A2 | HTTP status | ✅ all return 200, including the 9 new links |
| arXiv licences of 7 gallery sources | CC BY check | ✅ all CC BY 4.0 |
| `literature/corpus.tsv` | Stage counts and the Fig 6 panels | ✅ S0 35, S1 34, S2 63, S3 126, S4 79, TH 5, X 66 (408); Fig 6(b)-(d) match |
| Board-derived figures | Fig 11(a) reliability bins, Fig 11(d) points, A2 caption | ✅ Fig 11(a) bins match the JSON; Fig 11(d) plots 67 points plus the Jev star; 17 of 67 open systems have ECE below 0.074 |
| Deliverables and cross-references | Manifest count; every "Table N" / "Figure N" | ✅ 21 artefacts; every reference resolves to the right artefact under the new numbering |

Numbers recomputed and correct:
- **Table 1:** 39 rows; column totals 24/2/3/8/0/6/5.
- **Table 3:** families 22/6/31/16/4 = 79.
- **Table 5:** 23 typed + 27 constrained; 3 of the 23 typed works report a calibration metric.
- **Fig 7:** 75 of 79 S4 works in 2024-26, and 38 of 258 S0-S3 works by 2022.
- **Fig 3:** 33 of 39 surveys from 2024 onward.
- **Fig 2:** 108 leaves, 34 of them S4.
- **Fig 4 boxes:** 79 + 329 = 408; 32 + 17 - 10 = 39; 268 - 76 - 4 = 188.

## Part 1: status of the round-1 findings

| # | Round-1 finding | Status | Evidence |
|---|---|---|---|
| 1 | Table 11: "four widely discussed" rows | 🟢 FIXED | A2 is ranks 1-15, contiguous, from the JSON order (sorted by skill) |
| 2 | Table 10: population overclaimed ("built around Jev") | 🟢 FIXED | Title now names the search; caption states "of the 51 open systems with released weights ... it returns 4" (recomputed: 4) |
| 3 | Table 3 / Table 9 / Fig 2: two S4 typologies | 🟢 FIXED | Table 8 no longer lists the S4 works (header points to Table 3); Fig 2 families 8/6/8/8/4 are subsets of Table 3's 22/6/31/16/4 |
| 4 | "T0" undefined sixth family | 🟢 FIXED | "Theory and analysis (5), not counted in the core" appears in Table 2 (S4 "does not count"), Table 3, Table 8, Figs 2, 4, 5 and 7 |
| 5 | 92% download share | 🟢 FIXED | Now 87%, computed per copy's source. Attributing the 4 base-model re-uploads (138 downloads) elsewhere still gives 86.7% |
| 6 | "No model weights" row; 136 trained | 🔴 NOT FIXED (partly) | Row renamed "No newly trained model" and the WIlfLin and ohtaman repos moved, which is correct. But `ajh-code/Jev-Bonsai-Compass` moved to "Copy, port or package (no new training)" although its NOTICE says the adapter was "further trained in local decision-preservation and fast-route experiments. The selected artifact is `adapters/broad-lr0.0001.adapter`". It is newly trained, so 136 should be 137 and "the 39 copies ... add none" is false for 1 of the 39 |
| 7 | Inclusion rule vs card-less or gated repos | 🔴 NOT FIXED (partly) | 4 unverifiable repos are now excluded. But `atmaneayoub/jev-ar` is gated (API `gated: auto`; README returns 401; TSV "card gated, read from public metadata") and is classified and shown as an A1 example. Gated `canbingol/jev-mmlu-classifier` is excluded as unverifiable although it also has a public file list |
| 8 | Fig 11(d) "none public yet" contradicted Table 11 | 🟢 FIXED | Fig 11 (a) and (d) are now measured from the board; Table 6 cites the Decision Index as a decision-ECE testbed |
| 9 | R12: Jev tables off-axis and unreferenced | 🟢 FIXED | Moved to the appendix; A1 ties to Table 2 (typed decision); referenced from Figs 4, 10 and 11 and Table 6 |
| 10 | Overlapping categories, no precedence rule | 🟢 FIXED | Caption states that application takes precedence over language; jev-ar and the Thai model sit in Agents; ohtaman is in Copy |
| 11 | "4 of the 9 open systems have lower ECE" (selection-dependent) | 🟢 FIXED | Board-wide 17 of 67, recomputed |
| 12 | No uncertainty note; ECE panel not stated | 🟢 FIXED | "point estimates without uncertainty intervals"; "32 benchmarks with a per-field right answer" |
| 13 | Method column alignment; owner parentheticals | 🟢 FIXED | `rlllrr`; board names used as is |
| 14 | Scored variants dropped | 🟢 FIXED | [bf16], [Q8_0], [NVFP4], [FP8 · wide choice] kept |
| 15 | Mirrors "identical" | 🟢 FIXED | "contain their source's weight files byte for byte" (4 exact, 2 superset: true) |
| 16 | "Models" counted repositories | 🟢 FIXED | Header "Repositories" |
| 17 | "open Jev alternative" framing | 🟢 FIXED | "General-purpose typed-decision model" |
| 18 | Jev and typed decision undefined | 🟢 FIXED | A1 caption defines both, citing Table 2 |
| 19 | Mixed US and British spelling | 🔴 NOT FIXED (residual) | Authored text still has "penalized" (Table 3), and "Characterizes", "penalized", "tokenization", "detokenizing" (Table 5 Contribution column) |
| 20 | Build-tooling sentences in captions | 🟢 FIXED | Zoom, cropping and "never guessed" sentences gone; A2's link sentence now tells the reader which systems release weights |
| 21 | Fig 6 "harvester" vs "?" | 🟢 FIXED | "not reported" in Fig 6; "? = not reported in the paper" in the tables |
| 22 | "Landscape" = 325 in Fig 4 vs 408 in Table 9 | 🔴 NOT FIXED | Fig 4 box: "Landscape: 329 works (S0 to S3, X, theory and analysis)". Table 8 caption: "The landscape: all 408 works of the corpus", but Table 8 has 329 rows. Figs 2, 6 and 7 cite Table 8 as the source of all 408 or of S4 data that sit only in Table 3 or corpus.tsv |
| 23 | Fig 1 "Inside training" banner over X panels; rhetorical title | 🟢 FIXED | Title is declarative; the S4 band holds only S4 panels (T1, T3, T4, T5 per corpus.tsv `tfam`) |
| 24 | Citation year vs Yr column | 🟢 FIXED | Tables 3, 5 and 8 define "Yr: year of the first public version"; Fig 2 dropped the year prefix |
| 25 | Old Table 7: "four of them" | 🟢 FIXED | Table 6 now says panels a and d are measured, b and c are target shapes |
| 26 | Fig 3 "none covers TYP" | 🟢 FIXED | "None fully covers ... (1 partial: Lin 2026)" |
| 27 | Fig 4 "adversarial audits" | 🟢 FIXED | "by citation searching" |
| 28 | R8 redundancy | 🟠 NOT FIXED (partly) | Table 3 ⊂ Table 9 is resolved. Still present: Table 5 = 50 of 50 rows also in Table 3 or Table 8 (Yr and Metric repeated); Fig 6(a) = column sums of Fig 7 plus the 5 theory works; the 5 theory works are listed in both Table 3 and Table 8. Needs a user decision |
| 29 | Generator typed caption numbers | 🟢 FIXED | A2 panel size, sample rate, release and date now read from the JSON; A1 counts computed. Only "2026-09-15" (the Jev release date) is typed |

## Part 2: new defects (A1, A2, and consistency across all 21 artefacts), most severe first

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| fig9 | R4, R6 | The caption states a fixed rule, "one per training family T1 to T5 at S4", but the S4 row breaks it | Fig 9 S4 panels per corpus.tsv `tfam`: Steyvers 2025 = T1, Tan 2026 = T3, Zhang 2025 = T1, Yaldiz 2026 = T3. Two families are shown twice and three not at all | major | Apply the stated rule in the gallery selector, or state the rule actually used |
| fig1, fig8, fig9, table7 | R7, R9 | Panel labels use a different a/b suffix scheme from the bibliography, so a reader looking a label up in Table 7 lands on a different paper | Fig 1 and Fig 8 "Wang 2026b" = arXiv:2604.23333, but Table 7 "Wang et al. [2026b]" = arXiv:2602.03814 (a Fig 9 panel). Fig 8 "Wang 2025b" = 2505.04016, but Table 7 "[2025b]" = 2511.14275. Also "Yang 2026" / [2026b], "Aggarwal 2023" / [2023b], and in Fig 9 six more (Li 2025 / 2025f, Liu 2023 / 2023a, Wang 2025a / 2025b, Wang 2026a / 2026b, Yang 2024 / 2024b, Zhang 2025 / 2025c) | major | Generate panel labels from the same citation labels natbib prints (or put the arXiv id under each label) |
| tableA1 | R4 | `ajh-code/Jev-Bonsai-Compass` is counted as a copy with "no new training" | Repo NOTICE: adapter "further trained in local decision-preservation and fast-route experiments", file `adapters/broad-lr0.0001.adapter`; the card reports 611/720 with the adapter vs 584/720 untuned | major | Move it to General-purpose; the trained count becomes 137 and copies 38 (recompute in the generator) |
| table8, fig2, fig4, fig6, fig7 | R7 | "Landscape" and "Table 8" mean different sets in different captions | Table 8: "The landscape: all 408 works", 329 rows. Fig 4: Landscape = 329. Fig 2: "108 of the 408 works in Table 8" (34 of the 108 are in Table 3 only). Fig 6 cites "(Table 8)", but core works' Access and Task appear in no table. Fig 7 cites Table 8 for S4 years that are in Table 3 | minor | Caption Table 8 as "the landscape: the 329 works outside the core (S4 works are in Table 3)", and cite "Tables 3 and 8" where both are used |
| fig10 | R10 | The right edge of the "escalate" box is cut off | Overfull hbox 1.59 pt at `fig_decision_loop.tex` lines 43-54 (`build/all.log` line 3472); the 600 dpi render shows no right border or rounded corners on the escalate box; x=1098 is blank at every row inside the box | minor | Shift `a1..a3` left or narrow the picture by 2 pt; re-render and view the right edge |
| tableA1 | R4, R6 | The gated-repo rule is applied two ways | `atmaneayoub/jev-ar` (gated, card 401) is classified and used as an example; `canbingol/jev-mmlu-classifier` (gated) is excluded as unverifiable | minor | Exclude jev-ar, or state "gated repos classified from public tags and file lists" and apply that to both |
| tableA1 | R7, R1 | The `\Description` still says "one row per application category of open models built around Jev"; the title defines the population by the authors' search query | The title was changed to search results; two rows (copies, no newly trained model) are not application categories | minor | Align the Description with the title; keep the search definition (it is the sampling frame) but name it once, e.g. "Hugging Face repositories returned for 'jev' (snapshot 2026-09-27)" |
| tableA2 | R5 | The caption defines "LoRA with a trained decision head", which no shown row uses, but not "head or adapter" (rank 14) | Board kinds in ranks 1-15: full fine-tune, inference technique, LoRA, head / adapter | minor | Define the methods that appear, computed from the shown rows |
| tableA2 | R3 | ECE 0.2155 is printed as 0.215 | Board `calibration.ece` = 0.2155 for rank 10; Python `%.3f` rounds the binary float down; half-up gives 0.216 | minor | Round with `Decimal(str(x)).quantize(..., ROUND_HALF_UP)` |
| tableA2 | R5 | The evaluated Jev version is not shown | Extract `jev_version: jev-1.13.0`; row reads "Jev (TypeSafe, hosted)" | minor | Add "1.13" from the JSON |
| fig8, fig9 | R4 | Rule "one per training family T1 to T5 at S4, at most 4 per stage" cannot hold (5 families, cap 4) | Fig 8 S4 = T1, T3, T4, T5 (T2 dropped silently) | minor | State which family is dropped and why, or allow 5 panels at S4 |
| fig1 | R4 | "Panels are drawn from Figures 8 and 9" | All 8 Fig 1 rows in Table 7 read "1, 8"; none come from Fig 9 | minor | "drawn from Figure 8" |
| fig4 | R4 | "7 web searches, one per stage (two for S3) plus one for Jev" does not match the box's own list | The list has one search for S0 and S1 together, plus X. The count 7 holds only as S0+S1, S2, S3 sampling, S3 conformal, S4, X, Jev | minor | "7 web searches: S0 and S1 together, S2, two for S3, S4, X, and one for Jev" |
| table3, table5 | R5 | The shared caption legend defines columns the table does not have | Table 3 columns: Work, Yr, Contribution, Contract, Action, Metric; its caption also defines Access and Trained. Table 5 columns: Work, Yr, Contribution, Metric; its caption also defines Contract, Access and Trained | minor | Emit only the legend entries for columns present |
| fig3 | R10 | Labels in the calibration lane collide | "Shorinwa" has a leader line through it; "S. Li", "Beigi", "Huang" and "M. Li" overlap near 2024.8-2025.0 | minor | Stagger or offset the labels |
| fig9 | R10 | Several panels are unreadable thumbnails | e.g. Sanz-Guerrero, Marashian, Li 2025 and Yaldiz tiles at column width | minor | Crop to the key subplot, or accept as a gallery with the zoom provided by the PDF |
| table3, table5 | R11 | Residual US spellings in authored text | See round-1 #19 | minor | British spelling in authored text |
| table5, fig6, table3/table8 | R8 | Remaining duplicates | See round-1 #28 | minor | User decision |
| novelty_gap.md (not a deliverable) | R7 | The paper's novelty claim still says "Across 49 verified surveys"; the deliverables now say 39 | novelty_gap.md "The gap" section vs Table 1, Fig 3, Fig 4, Fig 5 | minor | Update the claim to 39, or state that 10 off-axis surveys were checked but not compared |

Status: 21 artefacts, 7 CLEAN, 14 FIX.
- **CLEAN:** fig5, fig11, table1, table2, table4, table6, table7.
- **FIX:** fig1, fig2, fig3, fig4, fig6, fig7, fig8, fig9, fig10, table3, table5, table8, tableA1, tableA2.
- **Round-1 findings (29):** 22 FIXED, 7 NOT FIXED (including 2 partly fixed).
- **New findings:** 3 major, 16 minor.

## Part 3: parity audit (`.claude/agents/parity-auditor.md`)

| Reference | Claimed representative | type(R) to type(P) | Verdict | Missing / note |
|---|---|---|---|---|
| `figures/fig_decision_loop.tex` (previous render + its caption) | `deliverables/fig10_p05` | schematic-diagram to schematic-diagram | PARTIAL | Render defect: the "escalate" box's right border and rounded corners are clipped at the float edge (overfull 1.59 pt, confirmed at 600 dpi). All other elements are present: state, declared options (choice, score, yes/no), model, probability per option, action policy with thresholds, act / abstain or ask / escalate with inequalities, S0-S4 tags in the Table 2 colours, S3 arc, S4 return bus, and the free-text callout. The S4 label matches Table 2's S4 rule. Note, not a defect: the `p(option \| state)` sub-label and the callout clause about confidence were removed in the edit; the caption no longer needs them |
| `tables/tab_definitions.tex` (previous render + Table 2 references) | `deliverables/table2_p05` | definition-table to definition-table | MATCH | Every element is present and legible: header, calibrated-confidence row, S0-S4 rows with stage colours matching Fig 10, and the typed-output, action-policy and coverage-guarantee rows. The removed "Parallel decision" row is consistent with the PAR column leaving Table 1. No overflow in the log or pixels. All 6 citations resolve to real entries (Guo 2017 1706.04599, Tian 2023 2305.14975, Campos 2024 2405.01976, Farquhar 2024 Nature, Bani-Harouni 2503.02623, Leng 2410.09724). Its claim that the last three rows are the Contract, Action and Guar. columns of Table 8 holds |

Ledger:
- A CLEAN record was appended for `tables/tab_definitions.tex`.
- No record was written for `figures/fig_decision_loop.tex`, because it is PARTIAL.
- `pending_audit.txt` was left unchanged; the coordinator's rules allowed editing only the ledger.

PARITY VERDICT (tables/tab_definitions.tex): CLEAN
PARITY VERDICT (figures/fig_decision_loop.tex): FLAGGED (1 discrepancy)

REVIEWER VERDICT: FIX

# Round 3 (2026-09-27): re-verification against the rebuilt renders, sources and primary data

Correction to the round-2 tally. Part 1 of round 2 marked 5 rows NOT FIXED (#6, #7, #19, #22, #28), not 7, so the correct round-2 count was 24 FIXED and 5 NOT FIXED.

## Primary data re-checked

| Check | Result |
|---|---|
| **A1:** recounted from the TSV and the live HF API | ✅ 188 repositories, 41,653 downloads; 137 with newly trained weights; General-purpose 55 / 19,655, Copy 38 / 18,640 |
| **Gated rule:** read `cardData` of both gated repos | ✅ `atmaneayoub/jev-ar` has full card metadata (tags, base model, model-index); `canbingol/jev-mmlu-classifier` has only `library_name`. The stated rule is applied consistently |
| **A2:** vs the board extract (already verified against live `index.json` in round 2) | ✅ Rank 10 ECE is now 0.216; Jev row reads "Jev 1.13"; only the methods shown are defined |
| **Corpus counts:** recomputed from `literature/corpus.tsv` | ✅ S4 = 79, TH = 5, Table 8 = 324 rows (408 - 79 - 5); Table 3 rows 84 = 79 + 5; Fig 6 (typed 22, constrained 79), Fig 7 (75 of 79; 38 of 258), Table 5 (22 + 28 = 50) |
| **Gallery panels:** Table 7 panels vs `corpus.tsv` stage, method group and T-family; labels matched against Table 7 | ✅ all 32 entries sit in the stated stage; every label now matches its Table 7 entry |
| **Fig 10 clipping:** 600 dpi render of the right edge; build log | ✅ escalate box border intact; no overfull box for `fig_decision_loop` (the only overfull left is Table 6 at 2.29 pt, under the 5 pt limit) |
| **Table 5 metric claim:** checked two typed-decision papers in full text | ❌ arXiv:2407.18370 reports ECE; arXiv:2605.09739 reports ECE and Brier (see new finding 2) |

## Status of the open items

| Item | Status | Evidence |
|---|---|---|
| #6 ajh-code/Jev-Bonsai-Compass counted as a copy | 🟢 FIXED | Now General-purpose; trained count 137, copies 38 |
| #7 gated-repo rule | 🟢 FIXED | Caption: "gated with no public card metadata" excluded, else classified from public card metadata; both gated repos follow it |
| #19 residual US spelling | 🟢 FIXED | The remaining -ize forms are only inside quoted paper titles in Fig 2 |
| #22 "landscape" count | 🔴 NOT FIXED | Table 8 now reads "the 324 works outside the training core ... the 79 core works and the 5 theory and analysis works are listed in Table 3". Fig 4 still shows "Landscape: 329 works (S0 to S3, X, theory and analysis)", and its caption says "theory and analyses of such training are placed in the landscape" |
| #28 duplication | ⚪ NO LONGER APPLICABLE | Kept by the user's choice. Theory works are now listed only in Table 3 |
| R2-1 Fig 9 S4 panels break the one-per-family rule | 🟢 FIXED in Fig 9 | Fig 9 S4 = Steyvers (T1) and Tan (T3). The same rule is now broken in Fig 1 (new finding 1) |
| R2-2 gallery labels vs bibliography suffixes | 🟢 FIXED | Every Fig 1, 8 and 9 label matches its Table 7 entry (e.g. "Yang et al. 2026b", "Wang et al. 2026b" = arXiv:2602.03814 in Fig 9) |
| R2-3 A1 Bonsai-Compass | 🟢 FIXED | As #6 |
| R2-4 Table 8 / Figs 2, 6, 7 cite the wrong table | 🟢 FIXED (Fig 4 part open) | Figs 2, 6 and 7 cite "Tables 3 and 8"; Table 8 counts 324. Fig 4 is still open under #22 |
| R2-5 Fig 10 clipping | 🟢 FIXED | Border visible at 600 dpi; no overfull; `p(option \| state)` restored |
| R2-6 gated-repo rule | 🟢 FIXED | As #7 |
| R2-7 A1 `\Description` | 🟢 FIXED | Now says "repositories returned by the Hugging Face search for jev" |
| R2-8 A2 methods defined but not shown | 🟢 FIXED | Methods listed are exactly those shown, including head or adapter and hosted API |
| R2-9 A2 ECE rounding | 🟢 FIXED | 0.216 |
| R2-10 A2 Jev version | 🟢 FIXED | "Jev 1.13 (TypeSafe AI, hosted)" |
| R2-11 Fig 8/9 rule not satisfiable | 🟢 FIXED | Rule is now "largest families first, at most 3 per stage". Fig 8 S4 = T3, T1, T4, the three largest families (31, 22, 16) |
| R2-12 Fig 1 says "from Figures 8 and 9" | 🟢 FIXED | Tan 2026 is used in Figs 1 and 9 (Table 7 "1, 9"); the others in Figs 1 and 8 |
| R2-13 Fig 4 search wording | 🟢 FIXED | "7 web searches run on 2026-09-26 (queries not recorded)" with a matching 7-item list |
| R2-14 Table 3 and 5 legends define absent columns | 🟢 FIXED | Legends list only printed columns. A leftover pointer remains (new finding 3) |
| R2-15 Fig 3 label collisions | 🟢 FIXED | Labels staggered with years; no overlaps in the render |
| R2-16 Fig 9 unreadable thumbnails | 🔴 NOT FIXED | Tan 2026, Luo et al. 2026 and Sanz-Guerrero panels are still illegible at print size, as are Soiffer's axes |
| R2-17 residual spelling | 🟢 FIXED | As #19 |
| R2-18 duplication | ⚪ NO LONGER APPLICABLE | User's choice |
| R2-19 novelty_gap.md said 49 surveys | 🟢 FIXED | Line 17: "the paper's Table 1 compares the 39 in the six on-axis topic groups (C ... and E ... were dropped as off-axis on 2026-09-27)" |

## New defects (round 3), most severe first

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| fig1 | R4, R6 | Caption: "one per training family for S4 (T1, T3, T4; T2, T5 not shown)", but the S4 band has 4 panels, two of them T3 | S4 panels: Yang et al. 2026b (arXiv:2607.01612, `tfam` T3), Guo et al. 2026 (T1), Gao et al. 2026 (T4), Tan et al. 2026 (arXiv:2607.04332, `tfam` T3). Table 7 marks both T3 entries "1, 8" and "1, 9" | major | Drop one T3 panel (3 S4 panels), or change the caption to the rule actually applied |
| table5 | R3, R4 | "1 of the 22 typed-decision works report ECE or Brier score as their calibration metric" | Corpus metric for the 22 typed works: ECE 1 (Yaldiz), multiple 2, selective 1, other 18. Both "multiple" works report ECE: Jung et al. 2024 (arXiv:2407.18370, "ECE ↓" in its tables) and Badhe et al. 2026 (arXiv:2605.09739, "Expected Calibration Error (ECE) and Brier"). The true count is 3 of 22; the round-2 caption had it right. Also "report" should be "reports" | major | Count the multiple-metric rows that include ECE or Brier (store the metric list, not just "multiple"), or revert to "3 of the 22 report a calibration metric (ECE, Brier or several)" |
| fig4 | R7 | "Landscape: 329 works (S0 to S3, X, theory and analysis)"; caption says theory works "are placed in the landscape" | Table 8: "The landscape: the 324 works outside the training core ... the 5 theory and analysis works are listed in Table 3" | minor | Fig 4: "Landscape (Table 8): 324 works (S0 to S3, X)", plus "Theory and analysis: 5 (Table 3)"; change the caption sentence to match |
| table3 | R5 | T2 definition: "its works are marked Trained = partial when the policy is not retrained" | Table 3 has no Trained column (Work, Yr, Contribution, Contract, Action, Metric), and the S4 works are not in Table 8, so the mark appears nowhere | minor | Drop the parenthesis or mark it in the Contribution text |
| fig8, fig9 | R1, R6 | Rule "largest families first and the newest figure of each that passed a visual check": the check is not recorded, so the rule cannot be reproduced | e.g. Fig 8 S0 skips the largest S0 group (empirical studies, 14 works) for groups of 9 and 7; Fig 9 S2 shows families of 3 and 3 but not linguistic hedges (20); Fig 9 S3 skips semantic entropy (19) and sampling consistency (16) | minor | State the skip rule in reader terms, e.g. "families with no CC BY figure showing the method are skipped", and keep the per-candidate verdicts with the data |
| fig6, table5 | R7 | Contract label "typed-decision" in Fig 6(b) and the Table 5 caption, "typed" in the Contract cells and legends of Tables 3 and 8 | `& typed &` in `tab_compare_s4.tex` (9) and `tab_landscape.tex` (13) | minor | Use one label everywhere |

## Tally

- **Artefacts:** 21 artefacts, 14 CLEAN, 7 FIX.
  - **CLEAN:** fig2, fig3, fig5, fig7, fig10, fig11, table1, table2, table4, table6, table7, table8, tableA1, tableA2.
  - **FIX:** fig1, fig4, fig6, fig8, fig9, table3, table5.
- **Open items from rounds 1 and 2:** of the 24 re-checked, 20 FIXED, 2 NOT FIXED (#22, whose Fig 4 half is also R2-4's open part, and R2-16), 2 NO LONGER APPLICABLE.
- **New in round 3:** 2 major, 4 minor.

REVIEWER VERDICT: FIX

# Round 4 (2026-09-27): re-verification against the rebuilt renders and data

## Checks run this round

| Check | Result |
|---|---|
| **Text diff:** all 21 rebuilt PDFs vs round 3 | 13 artefacts changed text (fig1, fig2, fig4, fig6, fig8, fig9, fig10, fig11, table2, table3, table4, table5, table7). The other 8 (fig3, fig5, fig7, table1, table6, table8, tableA1, tableA2) are unchanged |
| **Gallery panels:** all 32 Table 7 entries re-checked against `corpus.tsv` (stage, method group, T-family) | ✅ Panel families and labels match (details in the status table) |
| **`metric_checks.tsv`** vs my round-3 full-text checks | ✅ Consistent: jung2024trust (ECE) and badhe2026silent (ECE and Brier) |
| **`harvest/search_log.tsv`** | ✅ 7 streams dated 2026-09-26, matching the Fig 4 box |
| **Build log** | ✅ The only overfull box left is Table 6 at 2.29 pt (under 5 pt) |
| **Renders viewed** | fig1, fig4, fig6, fig9, fig10, fig11, table2 |

## Status of the round-3 open items and new findings

| Item | Status | Evidence |
|---|---|---|
| #22 "landscape" count | 🔴 NOT FIXED (wording only; numbers now reconcile) | The Fig 4 box reads "Landscape: 329 works: 324 at S0 to S3 and X (Table 8), 5 theory and analysis (Table 3)", and the caption still says theory works "are placed in the landscape". Table 8's caption reads "The landscape: the 324 works outside the training core ... the 5 theory and analysis works are listed in Table 3". The same word still names 329 works in Fig 4 and 324 works in Table 8 |
| R2-16 Fig 9 illegible tiles | 🔴 NOT FIXED (declared a trade-off by the builder, not by the user) | At print size the Tan et al. 2026 (S4), Luo et al. 2026 and Luo et al. 2025 (S1) and Soiffer et al. 2025 (X) tiles have unreadable axes and legends. Fig 9's own caption says families are skipped unless a figure "legibly shows the method or a result", so the Tan tile contradicts the stated rule at print size |
| R3-1 Fig 1 S4 had two T3 panels | 🟢 FIXED | S4 band = Yang et al. 2026b (T3), Guo et al. 2026 (T1), Gao et al. 2026 (T4), one per family. All 7 Fig 1 panels are marked "1, 8" in Table 7, matching "drawn from Figure 8" |
| R3-2 Table 5 "1 of the 22" | 🟢 FIXED | "3 of the 22 typed works report ECE or Brier score, alone or with other metrics" |
| R3-3 Fig 4 landscape 329 vs Table 8 324 | 🟠 PARTLY FIXED | The numbers are now decomposed and consistent (324 + 5 = 329); the term clash remains (see #22) |
| R3-4 Table 3 "marked Trained = partial" | 🟢 FIXED | The T2 definition no longer mentions Trained |
| R3-5 Fig 8/9 unrecorded "visual check" | 🟢 FIXED | Both captions now state the skip rule in reader terms and name the S4 families cut or without a figure. This matches the panels: Fig 8 S4 = T3, T1, T4 (T2 no figure, T5 cut by the cap); Fig 9 S4 = T1, T3 (T2, T4, T5 none) |
| R3-6 "typed" vs "typed-decision" | 🟢 FIXED | Fig 6(b) bar, the Table 5 caption and every Contract cell and legend say "typed". "Typed-decision" survives only in prose compounds (A1 row names, Fig 4 caption), not as the contract label |

## New defects (round 4)

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| table2 | R7, R4 | "The last three rows define the properties recorded for every work as the Contract, Action and Guar. columns of Table 8" | Table 8 now holds only the 324 works outside the core. The 79 core and 5 theory works are in Table 3, which has Contract and Action but no Guar. column, so Guar. is shown for no core work | minor | "... recorded for every work, shown as the Contract and Action columns of Tables 3 and 8 and the Guar. column of Table 8" |
| table2 | R10 | The new "Theory" row label is printed in a very pale pink | Row "Theory and analysis": the word "Theory" is near-white on white in the render, well below the contrast of the S0-S4 and X labels | minor | Darken the theory colour (e.g. the same hue at `!60!black`), matching Figs 2 and 5 |

## Tally

- **Artefacts:** 21 artefacts, 18 CLEAN, 3 FIX.
  - **FIX:** fig4 (landscape term; Table 8's caption is the other side of the same clash), fig9 (illegible tiles), table2 (two minor findings).
  - **CLEAN:** fig1, fig2, fig3, fig5, fig6, fig7, fig8, fig10, fig11, table1, table3, table4, table5, table6, table7, table8, tableA1, tableA2.
- **Open items from round 3 (8):** 5 FIXED, 1 PARTLY FIXED (R3-3), 2 NOT FIXED (#22, R2-16).
- **New in round 4:** 0 major, 2 minor.

REVIEWER VERDICT: FIX

# Round 5 (2026-09-27): re-verification against the rebuilt renders

## Checks run this round

| Check | Result |
|---|---|
| **Text diff:** all 21 rebuilt PDFs vs round 4 | 7 artefacts changed: fig4, fig6, fig8, fig9, fig10, table2, table7. The other 14 are unchanged, so their round-4 CLEAN status carries over |
| **Build log** | ✅ The only overfull box is Table 6 at 2.29 pt (under 5 pt) |
| **Renders viewed** | fig4, fig8, fig9, fig10, table2, table7. The fig9 label region was re-rendered at 400 dpi |

## Status of the round-4 open items

| Item | Status | Evidence |
|---|---|---|
| #22 / R3-3 "landscape" | 🟢 FIXED | "Landscape" now appears in only two places and both mean the same 324 works. Table 8: "The landscape: the 324 works outside the training core". Fig 4 box: "Outside the core: 329 works: the landscape of 324 at S0 to S3 and X (Table 8), and 5 theory and analysis works (Table 3)". Fig 4 caption: theory works "are listed with the core in Table 3 but not counted in it" |
| R4-1 Table 2 caption pointed to Table 8 only | 🟢 FIXED | "... the Contract and Action columns of Tables 3 and 8, and the Guar. column of Table 8". The caption also now covers the theory row |
| R4-2 Table 2 "Theory" label barely visible | 🟢 FIXED | The label renders in a readable mauve (#9C6B8E), close in weight to the other stage labels |
| R2-16 Fig 9 illegible tiles | ⚪ NO LONGER APPLICABLE | You chose "Shrink to fit one page"; tile legibility is your accepted trade-off. The selection rule and family notes moved to the Table 7 caption, which matches the panels: Fig 8 S4 = T3/T1/T4, T5 cut by the cap of 3, T2 no figure; Fig 9 S4 = T1/T3 |

Other round-5 edits checked:
- **Fig 10:** "choice, ordinal scale, yes/no" and the matching caption no longer collide with the Contract value "score" (one stated number), which Fig 6(b) now defines.
- **Fig 8 and 9:** the short captions point to Table 7 correctly.

## New defect (round 5)

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| fig9 | R10 | In the S0 row the first two panel labels print on top of each other: "Stengel-Eskin and Van Durme 2022" runs into "Liu et al. 2023a" and both are unreadable ("...Van DurmLi2022al. 2023a") | 400 dpi crop of the S0 label line. Caused by the new 5-column grid: the longest label is wider than its tile. pdftotext also returns the two labels interleaved | minor | Let long labels wrap within the tile width (e.g. `\parbox{\tilewidth}`) or shorten to "Stengel-Eskin and Van Durme 2022" on two lines; re-render and view every label row of Figs 8 and 9 |

## Tally

- **Artefacts:** 21 artefacts, 20 CLEAN, 1 FIX (fig9).
- **Open items from round 4 (4):** 3 FIXED, 1 NO LONGER APPLICABLE.
- **New in round 5:** 0 major, 1 minor.

REVIEWER VERDICT: FIX

# Round 6 (2026-09-27): re-verification and final consistency pass

## Checks run this round

| Check | Result |
|---|---|
| **Text diff:** all 21 rebuilt PDFs vs round 5 | Text changed in fig9 (labels), fig10, table2, table3 (new Guar. column) and table7 |
| **Colour changes** | Colour-only edits do not show in a text diff, so I checked pixels: fig2, fig5, fig8, fig9, fig10, table2 |
| **Build log** | ✅ No undefined references; the only overfull box is Table 6 at 2.29 pt (under 5 pt) |

## Status of the round-5 item

| Item | Status | Evidence |
|---|---|---|
| R5-1 Fig 9 S0 label overprint | 🟢 FIXED | At 400 dpi, "Stengel-Eskin and Van Durme 2022" is shrunk to its tile width and ends before "Liu et al. 2023a". No other label row in Figs 8 or 9 touches its neighbour; pdftotext returns each label intact |

## Round-6 changes verified

| Change | Result | Evidence |
|---|---|---|
| **Table 3 Guar. column** | ✅ | All 84 rows (79 core + 5 theory) match `corpus.tsv` on Contract, Action, Guar. and Metric: 0 mismatches. Guar. = yes for exactly one work (pan2026uncertaintyaware), which agrees with Table 4's S4 row ("none in general; one reward-model method adds conformal bounds [Pan et al. 2026a]"). The Guar. legend was added to the Table 3 caption |
| **Table 2 caption** | ✅ | "the Contract, Action and Guar. columns of Tables 3 and 8"; both tables now carry all three columns |
| **Theory colour #8C6D1F** | ✅ | Same olive in the Table 2 label, the Fig 5 bar and the Fig 2 "Theory and analysis" node; readable against white |
| **Darkened stage colours** | ✅ | Band colours are pixel-identical in Figs 8 and 9 (S0 98/98/98, S1 53/84/117, S2 171/93/16, S3 58/113/52, S4 124/84/113, X 159/60/60). The Table 2 and Fig 10 stage tags use the same hues; all text on them stays legible |
| **Fig 10 actions** | ✅ | Boxes read answer / abstain or defer / escalate, and the caption reads "answers, abstains or defers, or escalates". These match Table 2's action-policy row (answer, abstain, defer, route or escalate). The render has no clipping |
| **Table 7 rule wording** | ✅ | "... taking the largest families first and, in each, the newest figure that legibly shows the method or a result, at most 3 per stage". The notes on Figs 8 and 9 still match the panels (Fig 8 S4 T3/T1/T4; Fig 9 S4 T1/T3) |

## New defect (round 6; present since round 4, missed in rounds 4 and 5)

| artefact | check | what the reader sees | evidence | severity | fix |
|---|---|---|---|---|---|
| fig5 | R3, R4 | "408 primary works (450 references in the bibliography)" | `gen_corpus.py` computes 450 as 460 bib entries (refs.bib 63 + corpus.bib 397) minus the 10 off-axis surveys. That matches neither of the two sets a reader could check. (1) The built bibliography: `build_all.py` emits `\nocite{*}`, so `all.bbl` and `longs.bbl` each hold 460 entries, including the 10 off-axis surveys. (2) The works cited across all figure and table sources: 449 distinct keys; the 11 uncited are the 10 off-axis surveys plus `joshi2017triviaqa` | minor | Count the keys actually cited by the paper (drop `\nocite{*}` and any uncited entry, or cite TriviaQA where it is used), and compute the number from that set |

## Tally

- **Artefacts:** 21 artefacts, 20 CLEAN, 1 FIX (fig5).
- **Round-5 item:** FIXED.
- **New in round 6:** 0 major, 1 minor.

REVIEWER VERDICT: FIX
