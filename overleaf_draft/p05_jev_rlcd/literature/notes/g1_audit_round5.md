# G1 audit (round 5): P5 novelty claim version 5

Audit date: 2026-09-26. Stance: default REFUTED. Target: `novelty_gap.md` version 5. Round 4's 49-of-49 full-text citation check was not redone.

| Task | What was done |
|------|---------------|
| (a) round-4 fixes | Checked R4-1 to R4-9 against `novelty_gap.md` v5, `prior_surveys.md` (wording, credit rows, matrix marks, legend), `rlr_marks.tsv`, `refs.bib`. Re-tallied every matrix row in `prior_surveys.md` by script. Crossref works API for A21 and A22. Duplicate-key scan of `refs.bib` and `corpus.bib`; read `build/all.blg` |
| (b) sentence check | Downloaded arXiv:2609.07395 and arXiv:2608.23058 again (md5 identical to the round-3 and round-4 copies, so no new version). Read Lin Sec 8.3, 8.3.1, 8.3.2 (pp. 36-38) and Xu Table 3 (p. 15), Sec 4.2 (pp. 15-16) and the full Xu reference list. arXiv API for all 14 core ids |
| (c) competitor search | 19 arXiv API queries restricted to `submittedDate:[202608290000 TO 202609262359]`, 6 Semantic Scholar queries (5 returned HTTP 429), 5 web searches. Phrasings are listed in Sec 5; none repeat the round 1-4 logs. 5 candidates downloaded and scanned in full |

Legend: 🔴 fails, 🟠 medium, 🟡 low, 🟢 clears.

## 1. Findings (most severe first)

| # | Finding | Evidence (verified) | Severity | Fix | Refutes the claim? |
|---|---------|---------------------|----------|-----|--------------------|
| R5-1 | **Duplicate bib key `li2025survey` gives a wrong citation in the rendered survey table.** `refs.bib` line 137 is Li (S.) honesty survey (arXiv:2409.18786, A8); line 320 is Li (T.) diffusion-LM survey (arXiv:2508.10875, C2). BibTeX keeps the first and skips the second (`build/all.blg`: "Repeated entry---line 320 of file ../refs.bib"). In `tables/tab_survey_compare.tex` the C2 row under "Parallel and non-autoregressive output" therefore cites the honesty survey. The table captioned "Coverage of the 49 closest prior surveys" renders 48 distinct surveys, with A8 twice and C2 missing | `refs.bib` L137 and L320; `build/all.blg` L8-10; `tab_survey_compare.tex` rows 8 and 25 | 🟠 Medium (a misattribution in the paper's key table) | Rename the C2 key (for example `li2025diffusion`) in `refs.bib` and in `build/gen_phaseA.py` key mapping, then regenerate the table | No. The v5 text, ids and counts are unaffected |
| R5-2 | **17 coverage-matrix rows sit inside the Sec 1 survey tables, not in the Sec 2 matrix.** Rows A8-A14 (L35-41), A15-A18 (L49-52), A19-A22 (L57-60), F5 (L111) and G3 (L120) have 10 matrix cells but are placed in 7-column title tables. The Sec 2 matrix (L150-183) shows only 32 rows. The marks themselves are correct and `gen_phaseA.py` still picks them up, so the tex table is right | `prior_surveys.md` line numbers above; script tally of all 49 rows | 🟡 Low-Medium (the file v5 names as "the full table" does not display it) | Move the 17 rows into the Sec 2 matrix in A-H order | No |
| R5-3 | **Stale Phase-1 sentences in `prior_surveys.md` now contradict the matrix and v5.** "Totals: 32 verified surveys" (L136; v5 says 49). Sec 3.0 "The `RLC` column has **zero `Y`**" (L201; A8 and A19 are `Y`). Sec 3.1 "`TYP` ... no survey exists, not even a `~`" (L208; A9 is `~`). Sec 3.3 "none holds `RLC` or `TYP` at all" (L224). Sec 2a breadth ranking omits the 17 later surveys. Sec 5 "Coverage marks: Abstract/scope level only" (L260) repeats the out-of-date legend text that R4-8 fixed only in Sec 2 | `prior_surveys.md` L136, L185-195, L201, L208, L224, L260 | 🟡 Low-Medium | Mark Sec 2a and Sec 3 as "Phase 1 (superseded by rounds 1-5)" or update them; fix the total to 49; update the Sec 5 row to match the Sec 2 legend | No. None of these sentences is in v5, and v5 is consistent with the matrix |
| R5-4 | **`rlr_marks.tsv` was not updated in round 4.** G2 is still `?` (tsv note: OpenAlex list of 20 refs) and H2 is still `?`, while the matrix has G2 `~` and H2 `.`. The tsv has no rows for A19-A22 or G3. v5 cites the tsv as a source for "all 49" | `rlr_marks.tsv` rows G2, H2; row count 44 | 🟡 Low | Update G2 and H2 notes with the Crossref counts from R4-8; add A19-A22 and G3 rows citing `g1_audit_round3.md` and R4-8; add `g1_audit_round3.md` to the v5 source list | No. The v5 sentence is true (every mark has a full-text or full-reference-list source in rounds 2-4), only the pointer is incomplete |
| R5-5 | **New position paper cites 3 of the 14 core works.** Ravikumar, "The Missing 'I Don't Know': Why Three Reasoning-Reliability Findings Converge on Calibrated Abstention", arXiv:2609.17686 (15 Sep 2026, 12 pp.). Table 3 lists TruthRL, Abstain-R1, KeRLQA and Reinforced Hesitation as one row, "ternary reward at training time", and calls abstention rewards "surveyed broadly in Wen et al. (2025)". It argues for benchmark reform (triple-scoring, abstention-rate reporting). It is not a survey, covers one family (T4), has no typology by signal and no output contract | arXiv:2609.17686 full text | 🟡 Low | Cite it next to 2609.28940 as a non-survey precedent that groups T4 abstention rewards. The v5 sentence "no survey cites more than one" stays true because it is a position paper | No |
| R5-6 | **R4-7 (Sapunov ArXivIQ grey-literature review) is not recorded anywhere in v5 or the notes.** There is no related-work section yet (`sections/` does not exist), so the fix has nowhere to land, but nothing tracks it | `grep` of the tree: only `g1_audit_round4.md` mentions it | 🟡 Low | Add it to the v5 "Precedent to cite" line as grey literature, with the note to re-check for an arXiv version | No (R4-7 was a related-work to-do, not a claim fix) |
| R5-7 | **"after 2024 single-turn precursors in Sec 8.3" is slightly narrow.** Lin Sec 8.3 also cites Lin et al. 2022a and Mielke et al. 2022. The RL precursors it names (Band 2024, SaySelf / Xu 2024b) are 2024, so the sentence is true for calibration-shaped RL | arXiv:2609.07395 p. 37 | 🟡 Low (wording) | Optional: "2022-24 single-turn precursors" | No |
| R5-8 | **All round-4 claim fixes (R4-1 to R4-6, R4-8 marks and legend, R4-9) are applied and correct** | Sec 2 | 🟢 Clears | None | |
| R5-9 | **Every sentence of v5 "The gap" holds against the primary sources** | Sec 3 | 🟢 Clears | None | |
| R5-10 | **All 14 core ids and titles match arXiv** | Sec 4 | 🟢 Clears | None | |
| R5-11 | **No survey, tutorial, SoK or position paper posted 29 Aug to 26 Sep 2026 pre-empts the claim** | Sec 5 | 🟢 Clears | None | |

## 2. Task a: round-4 findings, fix status

| R4 | Required fix | Where checked | Status |
|----|--------------|---------------|--------|
| R4-1 | Replace "the one survey" with two single-domain subsections (Xu, Lin 8.3.1) | v5 "The gap", sentences 2-4 | 🟢 fixed, verbatim from the R4 replacement text |
| R4-2 | "its only general-domain entry is RLCR" | v5 "The gap", sentence 3 | 🟢 fixed, and true (Sec 3) |
| R4-3 | Credit Xu's forecast-form to proper-score mapping | v5 credit table, Xu row; v5 closing paragraph | 🟢 fixed (Xu Sec 2: CRPS, pinball, point error; Table 3 "Connected modalities") |
| R4-4 | Own credit row for Lin 2026 | v5 credit table | 🟢 fixed |
| R4-5 | List the 14 core ids in the gap section | v5 core-work table | 🟢 fixed (all 14 verified, Sec 4) |
| R4-6 | Cite arXiv:2609.28940 as single-domain precedent | v5 "Precedent to cite" | 🟢 fixed (not yet in `refs.bib`, which is fine until the related work is written) |
| R4-7 | Mention Sapunov ArXivIQ post as grey literature | not in v5 or any note | 🟡 not tracked (R5-6) |
| R4-8 | Resolve `RLR` `?` marks; F5 `TYP` to `.`; update legend | `prior_surveys.md` matrix and legend | 🟢 marks fixed: A21 `.`, A22 `.`, H2 `.`, G2 `~`, F5 `TYP` `.`; legend L147-148 updated. 🟡 residue: `rlr_marks.tsv` stale (R5-4); same legend text still in Sec 5 L260 (R5-3) |
| R4-9 | A21 and A22 as `@article` with full authors, volume, pages | `refs.bib` L254-273 vs Crossref | 🟢 fixed, exact match (below) |

Re-tally of all 49 matrix rows (script over `prior_surveys.md`):

| Column | Y | ~ | . | ? | v5 says | Match |
|--------|---|---|---|---|---------|-------|
| `RLR` | 3 (A8, A9, A19) | 12 | 34 | 0 | 3 / 12 / 34 / 0 | 🟢 |
| `TYP` | 0 | 1 (A9) | 48 | 0 | 0 / 1 / 48 / 0 | 🟢 |

Bib entries against Crossref:

| Key | Field | `refs.bib` | Crossref | Match |
|-----|-------|------------|----------|-------|
| `zhang2026uncertainty` | type, authors | `@article`; Zhang, Min-Ling and Wang, Deng-Bao | 2 authors: Min-Ling Zhang, Deng-Bao Wang | 🟢 |
| | journal, vol(issue), pages | JCST 41(1) 318--340, 2026 | JCST 41(1) 318-340, 2026-01 | 🟢 |
| `he2026survey` | type, authors | `@article`; 16 authors He ... Lu | same 16 authors in the same order | 🟢 |
| | journal, vol, article no. | Information Fusion 130, 104057, 2026 | Information Fusion 130, 104057, 2026-06 | 🟢 |

## 3. Task b: sentence-by-sentence check of v5 "The gap"

| # | v5 sentence (abridged) | Verdict | Evidence |
|---|------------------------|---------|----------|
| 1 | The 2025-26 calibration / proper-scoring RL wave has no cross-domain synthesis | 🟢 holds | 49 surveys (round 4) plus the Sec 5 search |
| 2 | Two surveys have a dedicated subsection on 2025-26 calibration-shaped RL, each scoped to one domain | 🟢 holds | Xu Sec 4.2 (forecasting); Lin Sec 8.3.1 (agents). Lin 8.3.1 opens with general RLHF context (Leng 2024 as a cause, pessimistic reward models, Pan 2026a), but every 2026 method it describes is an agent method. Li 2024 Sec 4.2 is 2024-only; A17 Liu is `~` (one RLMF mention) |
| 3 | Xu 2026 (Sec 4.2, Table 3) covers forecasting (Brier, outcome, market rewards); its only general-domain entry is RLCR | 🟢 holds | Table 3 RL rows: Time-R1, TimeMaster, TimeRFT, CastFlow, Outcome-RL [186 Turtel], Question synthesis [27 Chandak], FutureWorld [65], Market reward [93 Levy], RLCR [41 Damani], Calibrated VR [174 Singh, "Verifiable Rewards for Calibrated Probabilistic Forecasting"], Beta-Bernoulli [39, post-hoc]. Only [41] is general-domain. The whole Xu reference list has no other general-domain calibration-training work (Xiong 2024 and Devic 2025 are elicitation / position) |
| 4 | Lin 2026 (Sec 8.3.1) covers LLM agents (confident-error penalties on tool calls, abstention advantage reweighting), after 2024 single-turn precursors in Sec 8.3 | 🟢 holds | p. 37: Zhou 2026c "penalize confident errors when the objective is to align step confidence c_t with tool-call success"; Pan 2026b "train abstention through trajectory-informed advantage reweighting". Sec 8.3 precursors: Band 2024, Xu 2024b (SaySelf), also Lin 2022a and Mielke 2022 (R5-7, wording only) |
| 5 | Li 2024 covers 2024 methods only | 🟢 holds | `rlr_marks.tsv` A8; round 4 |
| 6 | Across 49 surveys, no survey cites more than one of the 14 core works | 🟢 holds | Round 4 Sec 2 (49 of 49); Lin and Xu PDFs unchanged since. arXiv:2609.17686 cites 3, but it is a position paper, not a survey (R5-5) |
| 7 | RLCR is cited by Xu and Siren's Song v3; ConfTuner by Ulmer and Zhang and Wang | 🟢 holds | Round 4 Sec 2; Xu [41] re-confirmed |
| 8 | No survey organises calibration training across domains by what the signal scores; Xu does so for forecasting and one family (T3); Lin by reward target for agents | 🟢 holds | Xu Table 3 column "Training / calibration signal"; Lin Eq. 16 (sign and form of psi) plus TIAR |
| 9 | No survey crosses that typology with the output contract | 🟢 holds | none found in 49 or in Sec 5 |
| 10 | Register split credited to Ulmer; forecast-form mapping to Xu; typed per-option contract at most partial (Lin) | 🟢 holds | matrix `TYP` 0 / 1 / 48 |
| 11 | Credit table (Xu, Lin, Li, Ulmer rows) | 🟢 holds | Xu row matches Table 3 and Sec 2; Lin row matches Eq. 16 text ("exploration bonus" is Zhang 2026d, an uncertainty reward, correctly labelled as a target, not as calibration) |

## 4. Task b: the 14 core works (arXiv API, 2026-09-26)

| v5 label | arXiv | arXiv title | First author | Match |
|----------|-------|-------------|--------------|-------|
| Rewarding Doubt | 2503.02623 | Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models | David Bani-Harouni | 🟢 |
| RLCR, Beyond Binary Rewards | 2507.16806 | Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty | Mehul Damani | 🟢 |
| Calibration-aware RL for decision-making LLMs | 2601.13284 | Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning | Duygu Nur Yaldiz | 🟢 |
| Reward functions for confidence calibration | 2607.04332 | On the effectiveness of reward functions in reinforcement learning for confidence calibration of large language models | Chee Heng Tan | 🟢 |
| TruthRL | 2509.25760 | TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning | Zhepei Wei | 🟢 |
| CAPO | 2604.12632 | Calibration-Aware Policy Optimization for Reasoning LLMs | Ziqi Wang | 🟢 |
| DCPO | 2603.09117 | Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards | Zhengzhao Ma | 🟢 |
| Behaviorally Calibrated RL | 2512.19920 | Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning | Jiayun Wu | 🟢 |
| Honesty over Accuracy | 2511.11500 | Honesty over Accuracy: Trustworthy Language Models through Reinforced Hesitation | Mohamad Amin Mohamadi | 🟢 |
| Abstain-R1 | 2604.17073 | Abstain-R1: Calibrated Abstention and Post-Refusal Clarification via Verifiable RL | Skylar Zhai | 🟢 |
| KARL | 2604.22779 | KARL: Mitigating Hallucinations in LLMs via Knowledge-Boundary-Aware Reinforcement Learning | Cheng Gao | 🟢 |
| Confidence Margin process supervision | 2604.23333 | Process Supervision of Confidence Margin for Calibrated LLM Reasoning | Liaoyaqi Wang | 🟢 |
| Semantic-level Reward | 2605.15588 | Calibrating LLMs with Semantic-level Reward | Fengfei Yu | 🟢 |
| ConfTuner | 2508.18847 | ConfTuner: Training Large Language Models to Express Their Confidence Verbally | Yibo Li | 🟢 |

## 5. Task c: competitor search, 29 Aug to 26 Sep 2026

Phrasings used (none appear in the round 1-4 logs):

| Channel | Queries |
|---------|---------|
| arXiv API (date-restricted) | calibration in abstract x title {overview, taxonomy, landscape, systematization, roadmap, perspective, lessons, primer, tutorial, "state of"}; "verbalized / verbalised / stated / expressed confidence"; "confidence expression" x survey; "know what they don't" / "self-knowledge" / "epistemic humility" x survey; "reward design" / "reward shaping" x calibration; "uncertainty-aware reinforcement" / "calibration-aware" x systematic; hedging / "epistemic markers" x position; truthfulness / honesty / refusal x reinforcement x survey; "proper scoring" x language; "calibration reward"; "confidence reward"; "reliable / trustworthy confidence" x roadmap; (calibration or calibrated) x (reinforcement or reward) x LLM; honesty / abstention / "I don't know" x reward x LLM; Brier / "log loss" / "scoring rule" x LLM; title uncertainty / confidence / calibration / honest / abstention x {survey ... position} |
| Semantic Scholar (Aug 20 to Sep 30) | "calibrated reasoning models reinforcement learning taxonomy" (ok); 5 others returned HTTP 429 |
| Web | "calibration RL LLM confidence rewards survey September 2026"; "teaching language models to know when they don't know review"; "decision models calibrated LLM RLCD survey"; "uncertainty-aware / honesty / calibrated alignment survey"; "SoK or tutorial proper scoring rules as rewards" |

Candidates read:

| Work | Id / source | Date | Type | Core works cited | Signal typology or output contract? | Threat |
|------|-------------|------|------|------------------|-------------------------------------|--------|
| Ravikumar, The Missing "I Don't Know" | arXiv:2609.17686 | 15 Sep | position (12 pp.) | 3 (TruthRL, Abstain-R1, Reinforced Hesitation) | one row "ternary reward at training time"; benchmark reform, no typology | 🟡 Low (R5-5) |
| Ibrahim and Zaki, Evaluating Decision Models for Text Annotation in CSS | arXiv:2609.24574 v2 | 21 Sep | empirical evaluation (54 pp.) | 1 (RLCR, ref [27]) | evaluates Jev and an open RLCD 0.6B model; no literature synthesis | 🟢 none (belongs in the `TYP` primary corpus) |
| Shan, A Survey on Rubric-Guided RL for Language Models | arXiv:2608.27505 | 27 Aug | survey | 0 | "calibration" only for rubric-score agreement | 🟢 none |
| Demystifying RL Post-Training of Language Models | arXiv:2608.24949 | 24 Aug | tutorial-style | 0 (0 "calibrat" hits) | no | 🟢 none |
| Rollout Efficiency in RL for Reasoning LLMs: A Taxonomy | arXiv:2609.25463 | 21 Sep | survey | 0 | no | 🟢 none |
| Probabilistic-forecasting survey | arXiv:2609.13345 | 11 Sep | survey | already cleared in round 4 | not LLM calibration training | 🟢 none |
| Primary works surfaced (not surveys) | arXiv:2609.00935 (DualStake, stake rewards for agent confidence), 2609.06419 (DualRead, GRPO medical VLM), 2609.17708 (XConf, training-free), 2609.20541 (training-free analysis), 2609.29429 (Just Ask Jev) | Sep | primary | n/a | n/a | 🟢 none; DualStake is a new T3/T5 corpus candidate |
| Grey literature | Sanity glossary "What is RLCD", MindStudio blog "RLCD vs RLHF", Anthony Maio Substack "Jev: The Language Model That Won't Talk" | Sep | blog / glossary | 0 | no | 🟢 none (motivation only, like TechCrunch and R4-7) |

Search limits: 5 of 6 Semantic Scholar queries hit HTTP 429. arXiv API title/abstract search has no stemming (`calibrat` prefix returns nothing, so full words were used). Google Scholar and OpenAlex were not used.

## 6. Verdict

| Part of v5 | Status |
|------------|--------|
| Every sentence of "The gap" | 🟢 holds against Lin Sec 8.3 / 8.3.1 and Xu Sec 4.2 / Table 3 |
| 14 core ids and titles | 🟢 all match |
| Round-4 claim fixes (R4-1 to R4-6, R4-8 marks, R4-9 bib) | 🟢 applied and correct |
| Coverage totals `RLR` 3/12/34/0, `TYP` 0/1/48/0 | 🟢 match the 49 matrix rows |
| Competitor search, last 4 weeks | 🟢 nothing pre-empts; one position paper (2609.17686) to cite |
| Supporting files | 🟠 duplicate key `li2025survey` misattributes C2 in the rendered table (R5-1); 🟡 matrix rows misplaced, stale Phase-1 sentences, stale tsv, R4-7 untracked (R5-2 to R5-6) |

The novelty claim in v5 survives. Nothing in v5 is false, no id is wrong, and no new work pre-empts it. The open items are hygiene problems in the supporting files and the bib. They do not touch the claim, but R5-1 must be fixed before the table is compiled into the paper.

AUDIT VERDICT: ACHIEVED
