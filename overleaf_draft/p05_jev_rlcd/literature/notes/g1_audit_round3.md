# G1 audit (round 3): P5 novelty claim version 3

Audit date: 2026-09-26. Stance: default REFUTED. Target: `novelty_gap.md` version 3.

Method: I re-resolved all 14 core works through the arXiv API (all 14 titles, first authors and ids match). I downloaded the latest arXiv PDF of 15 of the 44 surveys, converted them with pdftotext, joined hyphenated line breaks, and searched each full text for the 14 core works by title words, first-author surname, method name and arXiv id. Every hit was read in context (most were false positives such as "Karl Cobbe" or other "Tan et al."). For task b I ran 20+ arXiv API queries (title and abstract, cs.CL / cs.LG / cs.AI), 10 web searches with varied phrasing, and a Semantic Scholar "who cites this" pass over all 14 core works, filtered for survey, review, position, tutorial or SoK titles. OpenAlex returned HTTP 429 for every call and was not used. For 5 survey-like citers I downloaded and read the full text. The one paywalled survey was checked through its Crossref reference list.

## 1. Findings (most severe first)

| # | Finding | Evidence (verified) | Severity | Fix |
|---|---------|---------------------|----------|-----|
| R3-1 | **Claim (2) is false.** Li 2024 and Lin 2026 are not the only surveys with a calibration-reward subsection. Xu et al. 2026, a survey of LLM forecasting agents in ACM CSUR format, has Sec 4.2 "Reinforcement Learning and Calibration". It has two sub-paragraphs: "Outcome and Market Rewards" and "Dense and Calibration Rewards". Together they cover 2025-26 proper-scoring-rule RL: Turtel 2025 (negative-Brier reward with GRPO or ReMax, arXiv:2505.17989), Chandak 2026 (accuracy plus Brier reward, ICML 2026), RLCR (Damani, arXiv:2507.16806, a core work), and Singh 2026 (state-conditioned empirical-rate reward, arXiv:2607.00164). It also contrasts proper-score training with an external Beta-Bernoulli calibrator (Dai 2026, arXiv:2605.27668). Turtel 2025 and Singh 2026 are already in this project's corpus, tagged "RL calibration reward". So the forecasting strand of the 2025-26 wave already has a synthesis | Xu (X.) et al., "LLM-based Agents for Forecasting and Prediction: Methods, Training, Evaluation, and Applications", arXiv:2608.23058 (24 Aug 2026), Sec 4.2 and Table 3 | 🔴 **High** | Add it as survey 45 (`RLR` `Y` for the forecasting domain). Restate the gap as general-domain (QA, reasoning, decision) calibration-reward RL, and credit Xu 2026 for the forecasting strand |
| R3-2 | **Claim (3) is partly pre-empted, in the forecasting domain.** Xu 2026 Table 3 has a column "Training / calibration signal" with values such as delayed Brier reward, accuracy + Brier reward, market-price reward, correctness + proper-score reward and state-conditioned empirical-rate reward. That is an organisation by what the reward scores. Its "Connected modalities" column maps each method to its output (for example "Reasoning to stated confidence", "Evidence state to probability", "Score to calibrated probability"). Sec 2 also ties each forecast form (event probability, predictive distribution, quantile, point) to its proper scoring rule. This is an output-form axis, but not the typed per-option contract | arXiv:2608.23058, Table 3, Sec 2.1-2.2, Sec 4.2 | 🔴 **High** | "No survey organises calibration training by what the reward scores" is false as worded. Restrict it to "outside forecasting" or "across domains", and note that Xu 2026 does this for one domain and one family (T3) only |
| R3-3 | **The 44-survey set is incomplete, and 4 more survey-type works cite core works.** Claim (1) is true only because it is scoped to the 44. (a) Xu 2026 cites RLCR. (b) Siren's Song v3 cites RLCR in one sentence: "calibration can be further optimized through calibration-reward-based reinforcement learning". (c) The JCST 2026 calibration survey cites ConfTuner (Crossref ref CR146). (d) Ulmer 2025 v2 cites ConfTuner | (a) arXiv:2608.23058; (b) Zhang (Y.) et al., "Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models", arXiv:2309.01219v3 (updated 14 Sep 2025); (c) Zhang (M.-L.) and Wang (D.-B.), "Uncertainty Calibration in Deep Learning: Methods, Emerging Challenges, and LLM Frontiers", J. Computer Science and Technology 41(1):318-340, 2026, DOI 10.1007/s11390-026-6426-z (paywalled, reference list only); (d) Ulmer et al., "Anthropomimetic Uncertainty: What Verbalized Uncertainty in Language Models is Missing", arXiv:2507.10587v2 (20 Feb 2026) | 🟠 Medium | Add all four to the survey table (48 in total). Replace "none of the 44 cites any" with "no survey cites more than one of the 14, and none covers them as a family" |
| R3-4 | **The output-contract axis (free text vs numeric) already exists as an annotation axis.** Ulmer 2025 surveys verbalized-uncertainty papers. Its Fig. 2 and Table 6 label each paper by register (numerical 0-1 / 0-100 vs verbal or fluent) and by elicitation method (prompting, SFT, RL). The RL methods covered are LACIE, Band 2024, Tao 2024, SaySelf and Leng 2025 | arXiv:2507.10587v2, Sec 3.2, Fig. 2, Table 6 | 🟠 Medium | Credit Ulmer 2025 for the verbal-vs-numeric register split. The new part of the output-contract axis is the typed per-option decision contract, crossed with the reward family |
| R3-5 | **ConfTuner is not RL, yet it is counted among the "14 core ... RL" works.** ConfTuner fine-tunes with a tokenized Brier-score loss (NeurIPS 2025). Round 2's own Sec 5 files it under T1 (supervised). The gap sentence calls the 14 "core works" of "reinforcement learning whose reward is a calibration ... objective" | arXiv:2508.18847 abstract; `g1_reaudit.md` Sec 5 | 🟡 Low-Medium | Say "14 core calibration-training works (13 RL, plus ConfTuner as the supervised proper-scoring counterpart)", or swap in an RL work |
| R3-6 | **Lin 2026's subsection is not agents only.** Sec 8.3 also covers 2024 single-turn precursors (R-Tuning with its objective written out, Band 2024, Leng 2024, SaySelf) before the 2026 agent works (Zhou 2026c, Pan 2026b TIAR, Zhang 2026d) | arXiv:2609.07395, Sec 8.3 and 8.3.1 | 🟡 Low | "Li 2024 covers 2024 methods; Lin 2026 covers 2024 single-turn precursors and 2026 agent methods" |
| R3-7 | **One more related-work section splits action-level from report-level rewards.** Che 2026 separates advantage reweighting, knowledge-boundary and clarification rewards, and "confidence-shaped rewards". It argues that the action-level (abstain) alternative fails where the Brier-on-reported-confidence repair works. That is a T3 vs T4 contrast. No related-work section found has all five families or an output-contract axis | Che (X.) et al., "Abstention as an Action Can Kill Both the Reward Gradient and the KL Anchor ...", arXiv:2608.00301, Sec 6 | 🟡 Low | Cite with Damani 2025 and Tan 2026 as seeds of the T3/T4 split |
| R3-8 | **Claim (1) holds for the 15 surveys I checked.** 0 of 15 cite any of the 14 core works (table in Sec 2) | full-text search, Sec 2 | 🟢 Clears | Keep it, with the R3-3 caveat |
| R3-9 | **Claim (4) holds.** No new survey has typed per-option decision outputs. Xu 2026 has output forms (event probability, distribution, quantile, point) but no schema or typed contract. Ulmer 2025 has registers only | Sec 3 | 🟢 Clears | Keep it |

## 2. Task a: per-survey check (15 of the 44)

| Survey | arXiv | Core works cited | False positives read and rejected |
|--------|-------|------------------|-----------------------------------|
| A9 Lin (M.) 2026 | 2609.07395 | 0 | "Karl Johan Astrom" (not KARL) |
| A17 Liu (G. K.-M.) 2026 | 2607.11881 | 0 | "Tan et al. [268]" is sparse sub-networks, not Tan 2026. RL coverage is RLMF [181] and Leng 2024 only |
| A15 Oh 2026 | 2602.05073 | 0 | none |
| A6 Zhang (J.) 2026 | 2601.15690 | 0 | "Karl Cobbe" |
| A8 Li (S.) 2024 | 2409.18786 | 0 | "Karl Cobbe" |
| A3 Shorinwa 2024/25 | 2412.05563 | 0 | "Yaldiz" as a MARS co-author; "express their confidence verbally" in a LACIE sentence; "Karl Cobbe" |
| F1 Wen 2024/25 | 2407.18418 | 0 | none |
| F4 Moslem 2026 | 2603.04445 | 0 | "Karl Cobbe" (WebGPT author list) |
| F5 Boudiaf 2026 | 2608.17084 | 0 | none |
| B1 Zhang (K.) 2025 | 2509.08827 | 0 | "LA-CDM [Bani-Harouni, 2025]" is arXiv:2506.13474, not Rewarding Doubt; "CAPO [Xie 2025b]" is arXiv:2508.02298 (credit assignment), not Wang 2026 CAPO; "Tan et al. 2025a" is RIPT-VLA |
| B2 Liu (K.) 2025 | 2509.16679 | 0 | "Karl Cobbe" |
| B4 Yu (Z.) 2026 | 2604.17312 | 0 | "Tan et al. 2025b" is DEPO |
| A2 Liu (X.) 2025 | 2503.15850 | 0 | "Karl Cobbe" |
| A10 Li (M.) 2024/25 | 2412.12472 | 0 | "Tan et al. 2024" is model editing |
| A5 Kang 2025 | 2510.12040 | 0 | "Yaldiz" is a co-author of the survey |

Tally: **15 checked, 0 cite any core work.**

## 3. Task b: new survey-type competitors (all verified)

| Work | Id | Type | Cites core | Calibration-reward coverage | Threat |
|------|----|------|-----------|-----------------------------|--------|
| Xu (X.) et al. 2026, LLM-based Agents for Forecasting and Prediction | arXiv:2608.23058 | survey (ACM CSUR format) | RLCR | Sec 4.2 subsection; Table 3 organised by training / calibration signal | **High** (R3-1, R3-2) |
| Ulmer et al. 2025, Anthropomimetic Uncertainty | arXiv:2507.10587v2 | position + survey | ConfTuner | 2024 RL methods; register x elicitation annotation | Medium (R3-4) |
| Zhang (Y.) et al., Siren's Song (v3, 2025) | arXiv:2309.01219v3 | survey | RLCR | one sentence | 🟡 Low |
| Zhang (M.-L.) and Wang (D.-B.) 2026, Uncertainty Calibration in Deep Learning ... LLM Frontiers | DOI 10.1007/s11390-026-6426-z | survey (JCST) | ConfTuner | not determinable (paywalled) | 🟡 Low-Medium |
| He et al. 2026, Survey of uncertainty estimation in LLMs (Information Fusion) | DOI 10.1016/j.inffus.2025.104057 | survey | none (Crossref refs) | none | 🟢 None; add to table |

Checked and clear (0 core citations or no calibration-reward section): Yang (X.) 2026 Reliable and Responsible FMs (arXiv:2602.08145); Tie 2025 post-training survey (2503.06072); Srivastava 2025/26 technical RL survey (2507.04136); Shan 2026 rubric-RL survey (2608.27505); Zhang (G.) agentic RL landscape (2509.02547); Liu (P.) 2026 RLHF statistical perspective (2604.02507); Cai 2026 statistical control survey (2609.20973); Gumaan 2025 (2507.22915); Wu 2025 adaptive reasoning (2511.10788). Position papers that cite core works but do not synthesise them: Pres 2026 (2608.05188, RLCR); Chen (T.) 2026 (2605.19220, Rewarding Doubt); Liu (E.) 2025 (2512.21577, behaviourally calibrated RL); Ravikumar 2026 (2609.17686, already R8 in round 2).

## 4. Task c: related-work sections

| Source | Organises by what the reward scores | Output contract | Pre-empts T1-T5 + contract? |
|--------|-------------------------------------|-----------------|------------------------------|
| Tan 2026 (2607.04332) Sec 2 | clipped log-loss vs Brier after SFT vs two-stage alignment vs behavioural-calibration rewards (T3 only) | no | No |
| Damani 2025 (2507.16806) Sec 5 | listener / RM confidence / proper-scoring (T2, T3) | no | No |
| Che 2026 (2608.00301) Sec 6 | advantage reweighting / boundary and clarification / confidence-shaped (T3 vs T4) | no | No |
| Liu (G. K.-M.) 2026 RLMF (2606.32032) | internal-confidence rewards vs direct Brier optimisation vs advantage scaling | "faithful numerical uncertainty" vs linguistic | No (partial output split) |
| Xu 2026 survey Table 3 | yes, for forecasting only | output mapping column | Partial (one domain) |

## 5. Verdict

| Part of claim v3 | Status |
|------------------|--------|
| (1) None of the 44 cites any of the 14 core works | **Holds for the 44** (15 re-checked, 0 hits). But the 44 is incomplete: 4 surveys outside it cite RLCR or ConfTuner |
| (2) The only surveys with a calibration-reward subsection are Li 2024 and Lin 2026 | **Refuted**: Xu 2026 (arXiv:2608.23058) Sec 4.2, covering 2025-26 methods |
| (3) No survey organises calibration training by what the reward scores or by output contract | **Refuted as worded**: Xu 2026 Table 3 does it for forecasting; Ulmer 2025 has the verbal vs numeric register axis. The five-family cross-domain typology and the typed per-option contract remain unclaimed |
| (4) Typed per-option outputs have at most partial coverage | **Holds** |

**Replacement wording that survives:**

"The 2025-26 wave of reinforcement learning whose reward is a calibration or proper-scoring-rule objective has no cross-domain synthesis. The one survey with a dedicated 2025-26 subsection, Xu et al. 2026 (arXiv:2608.23058), covers the forecasting strand only (Brier, outcome and market rewards). Li 2024 covers 2024 methods, and Lin 2026 covers 2024 single-turn precursors and 2026 agent methods. Across 48 verified surveys, no survey cites more than one of the 14 core general-domain works (RLCR is cited by Xu 2026 and Siren's Song; ConfTuner by Ulmer 2025 and Zhang and Wang 2026). No survey organises calibration training across domains by what the training signal scores (supervised targets, reward-model calibration, proper-scoring RL, action-targeted rewards, process- and meaning-level rewards). No survey crosses that typology with the output contract the confidence is trained into; the verbal vs numeric register split is credited to Ulmer 2025, and the typed per-option decision contract has at most partial coverage."

AUDIT VERDICT: REFUTED
