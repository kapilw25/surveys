# Prior surveys - novelty scan Phase 1 (P5: calibrated decision models, the Jev / RLCD paradigm)

Scan date: 2026-09-21. Every survey below was verified against a primary record (arXiv API, Crossref, ACL Anthology or Zenodo). Nothing is listed from memory or from a search-engine summary alone.

## 0. Scope and framing

**Why the survey cannot be "about Jev".** Jev (TypeSafe AI, launched 15 Sep 2026) has no paper, no published reward function, no calibration curves and no independent benchmark. It can motivate the survey as an industry signal, but it cannot be cited as evidence for a method. The survey subject is therefore the **paradigm Jev represents**.

**The paradigm, decomposed into 8 coverage dimensions:**

| Code | Dimension | Jev property it corresponds to |
|------|-----------|--------------------------------|
| `CAL` | Confidence estimation and calibration of (language) models, incl. metrics (ECE, Brier) | "a 0.8 answer is right 80% of the time" |
| `RLC` | Calibration-aware TRAINING, especially RL with a proper-scoring-rule or calibration reward | RLCD itself |
| `DEC` | Closed-set decisions: the model picks among a predefined option space (classification, choice, scoring, judging) | Choice / Score / Noul primitives |
| `TYP` | Typed or schema-constrained output contracts (the output cannot leave the declared type) | "type-safe structured values" |
| `PAR` | Non-autoregressive / parallel single-pass output (NAR, diffusion, parallel scoring) | parallel sampler over the decision space |
| `S12` | System-1 versus System-2: fast intuitive answers versus deliberate reasoning, and the efficiency trade-off | "System One model" |
| `ESC` | Acting on confidence: abstention, reject option, learning to defer, routing and cascades | what to do with a 0.5 answer |
| `HAL` | Hallucination (the failure calibration is meant to expose) | "cannot hallucinate" claim |

## 1. Verified survey table

### Tier A - calibration and uncertainty quantification (core of `CAL`)

| # | Survey title | 1st author | Year | Venue | arXiv / DOI | Scope |
|---|--------------|-----------|------|-------|-------------|-------|
| A1 | A Survey of Confidence Estimation and Calibration in Large Language Models | J. Geng | 2023 (NAACL 2024) | NAACL 2024 (long) | arXiv:2311.08298 | White-box vs black-box confidence estimation and calibration techniques for LLMs |
| A2 | Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey | X. Liu | 2025 | KDD 2025 | arXiv:2503.15850; 10.1145/3711896.3736569 | UQ sources in LLMs (input ambiguity, reasoning divergence, decoding) plus calibration |
| A3 | A Survey on Uncertainty Quantification of Large Language Models: Taxonomy, Open Research Challenges, and Future Directions | O. Shorinwa | 2024 (journal 2025) | ACM Computing Surveys | arXiv:2412.05563; 10.1145/3744238 | UQ taxonomy; applications from chatbots to robotics |
| A4 | A Survey of Uncertainty Estimation Methods on Large Language Models | Z. Xia | 2025 | Findings of ACL 2025 | ACL 2025.findings-acl.1101 | Catalogue of LLM uncertainty-estimation methods |
| A5 | Uncertainty Quantification for Hallucination Detection in Large Language Models: Foundations, Methodology, and Future Directions | S. Kang | 2025 | arXiv preprint | arXiv:2510.12040 | UQ as a hallucination detector |
| A6 | From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantification in Large Language Models | J. Zhang | 2026 | arXiv preprint | arXiv:2601.15690 | UQ moving from an evaluation metric to a control / training signal |
| A7 | Calibration in Deep Learning: A Survey of the State-of-the-Art | C. Wang | 2023 | arXiv preprint (v4) | arXiv:2308.01222 | Post-hoc, regularisation, UQ and composition calibration methods; LLM section |
| A8 Li (S.) | Y | Y | Y | ? | . | . | . | ~ | ~ |
| A9 Lin (M.) | Y | ~ | Y | ? | ~ | . | ? | Y | ? |
| A10 Li (M.) | Y | ~ | ~ | ? | . | . | . | ~ | ~ |
| A11 Xie (L.) | Y | . | ~ | ? | . | . | . | ? | . |
| A12 Abbasli | Y | ? | ~ | ? | . | . | . | ? | ~ |
| A13 Huang (H.-Y.) | Y | ? | . | ? | . | . | . | ? | ? |
| A14 Beigi | Y | ? | . | ? | . | . | . | ? | ? |
| A8 | A Survey on the Honesty of Large Language Models | S. Li | 2024 (TMLR 2025) | TMLR | arXiv:2409.18786 | Honesty: self-knowledge, calibration, abstention; method split by probability / prompting / sampling / fine-tuning and RL |
| A9 | Uncertainty Quantification for LLM Agents: A Taxonomy, an Evaluation Protocol, and an Empirical Study | M. Lin | 2026 | arXiv preprint | arXiv:2609.07395 | UQ for agents organised by pipeline stage; deferral; uncertainty-aware RL |
| A10 | Knowledge Boundary of Large Language Models: A Survey | M. Li | 2024 (ACL 2025) | ACL 2025 | arXiv:2412.12472 | Knowledge boundaries; fine-tuning for calibration; refusal |
| A11 | A Survey of Calibration Process for Black-Box LLMs | L. Xie | 2024 | arXiv preprint | arXiv:2412.12767 | Black-box confidence estimation and calibration |
| A12 | Comparing Uncertainty Measurement and Mitigation Methods for Large Language Models: A Systematic Review | T. Abbasli | 2025 | IEEE TNNLS (accepted) | arXiv:2504.18346 | Systematic review of UQ measurement and mitigation |
| A13 | A Survey of Uncertainty Estimation in LLMs: Theory Meets Practice | H.-Y. Huang | 2024 | arXiv preprint | arXiv:2410.15326 | Theory-to-practice review of LLM uncertainty estimation |
| A14 | Rethinking the Uncertainty: A Critical Review and Analysis in the Era of Large Language Models | M. Beigi | 2024 | arXiv preprint | arXiv:2410.20199 | Critical review of uncertainty notions for LLMs |
| A15 Oh | Y | ~ | . | ? | . | . | ? | ~ | ? |
| A16 Xia (B.) | Y | . | . | ? | . | . | . | ? | ? |
| A17 Liu (G.) | Y | ~ | ~ | ? | . | . | ? | ? | ? |
| A18 Sun (X.) | Y | . | . | ? | . | . | . | ? | ? |
| A15 | Uncertainty Quantification in LLM Agents: Foundations, Emerging Challenges, and Opportunities | C. Oh | 2026 (ACL 2026) | ACL 2026 | arXiv:2602.05073 | UQ for LLM agents: foundations and open challenges |
| A16 | Uncertainty Propagation in LLM-Based Systems | B. Xia | 2026 | arXiv preprint | arXiv:2604.23505 | How uncertainty propagates through multi-component LLM systems |
| A17 | Metacognition in LLMs: Foundations, Progress, and Opportunities | G. Liu | 2026 | arXiv preprint | arXiv:2607.11881 | Metacognition incl. metacognitive accuracy as an RL training signal |
| A18 | Trust Stack for Mental Health AI: A Survey of Calibration across Human, Interaction, and Model Levels | X. Sun | 2026 | arXiv preprint | arXiv:2604.20166 | Calibrated trust across human, interaction and model levels (domain: mental health) |
| A19 Xu (X.) | ~ | Y | Y | ~ | . | . | . | . | . |
| A20 Ulmer | Y | ~ | ~ | . | . | . | . | . | . |
| A21 Zhang (M.-L.) | Y | ? | . | ~ | . | . | . | ? | ? |
| A22 He (J.) | Y | ? | . | . | . | . | . | ? | ? |
| A19 | LLM-based Agents for Forecasting and Prediction: Methods, Training, Evaluation, and Applications | X. Xu | 2026 | arXiv preprint | arXiv:2608.23058 | Forecasting agents; Sec 4.2 RL and calibration rewards (Brier, outcome, market) for the forecasting domain |
| A20 | Anthropomimetic Uncertainty: What Verbalized Uncertainty in Language Models is Missing | D. Ulmer | 2025 | arXiv preprint (v2 2026) | arXiv:2507.10587 | Verbalised uncertainty; papers labelled by register (numeric vs verbal) and elicitation (prompt, SFT, RL) |
| A21 | Uncertainty Calibration in Deep Learning: Methods, Emerging Challenges, and LLM Frontiers | M.-L. Zhang | 2026 | J. Computer Science and Technology | 10.1007/s11390-026-6426-z | Calibration methods in deep learning with an LLM section (paywalled; marks from the reference list) |
| A22 | Survey of uncertainty estimation in LLMs - Sources, methods, applications, and challenges | J. He | 2026 | Information Fusion | 10.1016/j.inffus.2025.104057 | Sources, methods and applications of LLM uncertainty estimation |

### Tier B - reinforcement learning for LLMs (where `RLC` would live)

| # | Survey title | 1st author | Year | Venue | arXiv / DOI | Scope |
|---|--------------|-----------|------|-------|-------------|-------|
| B1 | A Survey of Reinforcement Learning for Large Reasoning Models | K. Zhang | 2025 | arXiv preprint | arXiv:2509.08827 | RL (incl. RLVR) for reasoning models; rewards, algorithms, infra |
| B2 | Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle | K. Liu | 2025 | arXiv preprint | arXiv:2509.16679 | RL across pre-training, alignment and reasoning |
| B3 | A Survey of Reinforcement Learning from Human Feedback | T. Kaufmann | 2023 | TMLR | arXiv:2312.14925 | RLHF: feedback types, reward models, policy optimisation |
| B4 | A Survey of Reinforcement Learning for Large Language Models under Data Scarcity: Challenges and Solutions | Z. Yu | 2026 | arXiv preprint | arXiv:2604.17312 | RL when data is scarce, incl. synthetic data (Jev trains on synthetic data only) |

### Tier C - parallel and non-autoregressive output (`PAR`)

| # | Survey title | 1st author | Year | Venue | arXiv / DOI | Scope |
|---|--------------|-----------|------|-------|-------------|-------|
| C1 | A Survey on Non-Autoregressive Generation for Neural Machine Translation and Beyond | Y. Xiao | 2022 (journal 2023) | IEEE TPAMI | arXiv:2204.09269; 10.1109/TPAMI.2023.3277122 | NAR generation: data, modelling, training criteria, decoding |
| C2 | A Survey on Diffusion Language Models | T. Li | 2025 | arXiv preprint | arXiv:2508.10875 | DLMs as a parallel, bidirectional alternative to AR decoding |
| C3 | Discrete Diffusion in Large Language and Multimodal Models: A Survey | R. Yu | 2025 | arXiv preprint | arXiv:2506.13759 | Discrete diffusion for language and multimodal models |
| C4 | Accelerating Masked Diffusion Large Language Models: A Survey of Efficient Inference Techniques | D. Gwak | 2026 | arXiv preprint | arXiv:2607.12829 | Efficient inference for masked DLMs, incl. confidence-driven unmasking |
| C5 | Unlocking Efficiency in Large Language Model Inference: A Comprehensive Survey of Speculative Decoding | H. Xia | 2024 | Findings of ACL 2024 | arXiv:2401.07851 | Draft-then-verify: parallel verification of AR drafts |
| C6 | Speculative Decoding and Beyond: An In-Depth Survey of Techniques | Y. Hu | 2025 | arXiv preprint | arXiv:2502.19732 | Speculative decoding and related parallel schemes |
| C7 | Closer Look at Efficient Inference Methods: A Survey of Speculative Decoding | H. Ryu | 2024 | arXiv preprint | arXiv:2411.13157 | Speculative decoding methods and trade-offs |
| C8 | A Survey on Efficient Inference for Large Language Models | Z. Zhou | 2024 | arXiv preprint | arXiv:2404.14294 | Data-, model- and system-level inference efficiency |

### Tier D - closed-set decisions and judging (`DEC`)

| # | Survey title | 1st author | Year | Venue | arXiv / DOI | Scope |
|---|--------------|-----------|------|-------|-------------|-------|
| D1 | A Survey on LLM-as-a-Judge | J. Gu | 2024 | arXiv preprint (v6) | arXiv:2411.15594 | Reliability, bias and consistency of LLM judges |
| D2 | From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge | D. Li | 2024 | arXiv preprint (v7) | arXiv:2411.16594 | What to judge, how to judge, how to benchmark judges |
| D3 | LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods | H. Li | 2024 | arXiv preprint | arXiv:2412.05579 | Functionality, methodology and limits of LLM evaluators |

### Tier E - System-1 versus System-2 (`S12`)

| # | Survey title | 1st author | Year | Venue | arXiv / DOI | Scope |
|---|--------------|-----------|------|-------|-------------|-------|
| E1 | From System 1 to System 2: A Survey of Reasoning Large Language Models | Z.-Z. Li | 2025 | arXiv preprint (IEEE journal version listed on Xplore; DOI not resolved here) | arXiv:2502.17419 | The move from fast System-1 LLMs to deliberate System-2 reasoning models |
| E2 | Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models | Y. Sui | 2025 | TMLR 2025 (per ML Anthology) | arXiv:2503.16419 | Shortening or skipping reasoning; the overthinking cost |

### Tier F - acting on confidence (`ESC`)

| # | Survey title | 1st author | Year | Venue | arXiv / DOI | Scope |
|---|--------------|-----------|------|-------|-------------|-------|
| F1 | Know Your Limits: A Survey of Abstention in Large Language Models | B. Wen | 2024 (journal 2025) | TACL | arXiv:2407.18418; 10.1162/tacl_a_00754 | Abstention from query, model and human-values perspectives |
| F2 | Machine Learning with a Reject Option: A survey | K. Hendrickx | 2021 (journal 2024) | Machine Learning (Springer) | arXiv:2107.11277; 10.1007/s10994-024-06534-x | Ambiguity and novelty rejection; selective prediction |
| F3 | Learning to Defer: A Survey | J. Strong | 2025 | Zenodo preprint (not peer reviewed) | 10.5281/zenodo.17843044 | Deferral to experts: methods, theory, practical adaptations |
| F4 | Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey | Y. Moslem | 2026 | TMLR | arXiv:2603.04445 | Routing (one-shot) vs cascading (confidence-triggered escalation) |
| F5 Boudiaf | Y | . | ~ | ~ | . | . | ? | Y | ? |
| F5 | Uncertainty-Aware Decision Making in Multimodal Large Language Models | A. Boudiaf | 2026 | arXiv preprint | arXiv:2608.17084 | Signals -> calibration -> action pipeline (answer, hedge, abstain, clarify, route, escalate); no training stage |

### Tier G - hallucination (`HAL`)

| # | Survey title | 1st author | Year | Venue | arXiv / DOI | Scope |
|---|--------------|-----------|------|-------|-------------|-------|
| G1 | A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | L. Huang | 2023 (journal 2025) | ACM TOIS | arXiv:2311.05232; 10.1145/3703155 | Causes, detection, benchmarks, mitigation |
| G2 | Large language models hallucination: A comprehensive survey | A. Alansari | 2026 | Computer Science Review | 10.1016/j.cosrev.2026.100970 | Broad hallucination review |
| G3 Zhang (Y.) | ~ | ~ | ~ | . | . | . | . | . | Y |
| G3 | Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models | Y. Zhang | 2023 (v3 2025) | arXiv preprint | arXiv:2309.01219 | Hallucination detection, explanation and mitigation; v3 mentions calibration-reward RL in one sentence |

### Tier H - conformal prediction (calibrated decision SETS with guarantees)

| # | Survey title | 1st author | Year | Venue | arXiv / DOI | Scope |
|---|--------------|-----------|------|-------|-------------|-------|
| H1 | Conformal Prediction for Natural Language Processing: A Survey | M. M. Campos | 2024 | TACL | arXiv:2405.01976; 10.1162/tacl_a_00715 | Distribution-free coverage guarantees for NLP classification and generation |
| H2 | Uncertainty-aware large language models: a scoping review of conformal prediction methods | A. E. Ashby | 2026 | Phil. Trans. R. Soc. A | 10.1098/rsta.2026.0061 | Scoping review of conformal methods for LLMs |

### Not a survey (position / overview), listed for completeness

| # | Title | 1st author | Year | arXiv | Note |
|---|-------|-----------|------|-------|------|
| P1 | Human-AI Collaboration in Decision-Making: Beyond Learning to Defer | D. Leitao | 2022 | arXiv:2206.13202 | Position paper on deferral; relevant to `ESC` |

**Totals: 49 verified surveys (tiers A-H) + 1 position paper.** 32 came from the Phase 1 sweep and 17 were added by audit rounds 1-3.

## 2. Coverage matrix

> **G1 audit (2026-09-26): REFUTED, then applied.** 8 verified surveys added (A8-A14, F5), 11 marks corrected from full-text reads (`literature/notes/g1_audit.md`), and a column `RLR` added: RL with a calibration or proper-scoring-rule reward (the 2024-26 wave: Leng 2024, Bani-Harouni 2025, Damani 2025, Yaldiz 2026, Tan 2026). `RLR` marks come from the round-2 full-text re-audit (`literature/notes/rlr_marks.tsv`, `g1_reaudit.md`), which also added 4 surveys (A15-A18).

> **G1 audit round 3 (2026-09-26): REFUTED, then applied.** 5 verified surveys added (A19-A22, G3; `literature/notes/g1_audit_round3.md`). Each was re-verified here against the arXiv abstract page or Crossref before adding. A21 is paywalled, so its unreadable columns stay `?`.

> **G1 audit round 4 (2026-09-26): REFUTED on one sentence, then applied.** `RLR` resolved from full Crossref reference lists: A21, A22 and H2 `.`, G2 `~` (cites SaySelf); F5 `TYP` set to `.` per the round-2 full-text read (`literature/notes/g1_audit_round4.md`).


Legend: `Y` covered, `~` partial, `.` absent, `?` not determinable without the full text.
Marks were first assigned from the verified abstract and scope. After audit rounds 1-4, the closest surveys and the whole `RLR` column are marked from full texts or full Crossref reference lists (`g1_audit.md`, `g1_reaudit.md`, `g1_audit_round3.md`, `g1_audit_round4.md`); the other columns of distant surveys remain abstract-level.

| # | `CAL` | `RLC` | `RLR` | `DEC` | `TYP` | `PAR` | `S12` | `ESC` | `HAL` |
|---|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| A1 Geng | Y | ~ | . | Y | . | . | . | ~ | ~ |
| A2 Liu (X.) | Y | ~ | . | . | . | . | . | ~ | ~ |
| A3 Shorinwa | Y | ~ | ~ | . | . | . | . | ~ | Y |
| A4 Xia (Z.) | Y | . | . | . | . | . | . | . | ~ |
| A5 Kang | Y | . | . | . | . | . | . | ~ | Y |
| A6 Zhang (J.) | Y | ~ | . | . | . | . | ~ | ~ | ~ |
| A7 Wang | Y | . | . | Y | . | . | . | ~ | . |
| B1 Zhang (K.) | . | . | ~ | . | . | . | Y | . | . |
| B2 Liu (K.) | . | . | . | . | . | . | ~ | . | . |
| B3 Kaufmann | . | ? | . | . | . | . | . | . | . |
| B4 Yu (Z.) | . | ? | . | . | . | . | ~ | . | . |
| C1 Xiao | . | . | . | . | . | Y | . | . | . |
| C2 Li (T.) | . | . | . | . | . | Y | . | . | . |
| C3 Yu (R.) | . | . | . | . | . | Y | . | . | . |
| C4 Gwak | ~ | . | . | . | . | Y | . | . | . |
| C5 Xia (H.) | . | . | . | . | . | ~ | . | . | . |
| C6 Hu | . | . | . | . | . | ~ | . | . | . |
| C7 Ryu | . | . | . | . | . | ~ | . | . | . |
| C8 Zhou | . | . | . | . | . | ~ | ~ | . | . |
| D1 Gu | ~ | . | . | Y | . | . | . | . | . |
| D2 Li (D.) | ~ | . | ~ | Y | . | . | . | . | . |
| D3 Li (H.) | ~ | . | . | Y | . | . | . | . | . |
| E1 Li (Z.-Z.) | . | . | . | . | . | . | Y | . | . |
| E2 Sui | . | . | . | . | . | . | Y | ~ | . |
| F1 Wen | ~ | ~ | ~ | . | . | . | . | Y | ~ |
| F2 Hendrickx | ~ | . | . | Y | . | . | . | Y | . |
| F3 Strong | ~ | . | . | Y | . | . | . | Y | . |
| F4 Moslem | ~ | . | . | . | . | . | ~ | Y | . |
| G1 Huang | ~ | . | . | . | . | . | . | . | Y |
| G2 Alansari | ~ | . | ~ | . | . | . | . | . | Y |
| H1 Campos | Y | . | . | Y | . | . | . | ~ | . |
| H2 Ashby | Y | . | . | ~ | . | . | . | ~ | . |

> ⚠️ **Sections 2a, 3 and 5 below are the Phase 1 snapshot** (32 surveys, abstract-level marks), kept for the search log. They are superseded by the audited matrix above and by `novelty_gap.md` v5 (round-5 audit: ACHIEVED). Where they disagree (e.g. `RLC` and `RLR` now have `Y` marks, `TYP` has one `~`), the matrix above is correct.

### 2a. Breadth ranking (dimensions reached, `Y` or `~`, out of 8)

| Reach | Surveys |
|-------|---------|
| 5 | A1 Geng |
| 4 | A2 Liu (X.) |
| 3 | A3 Shorinwa, A5 Kang, A7 Wang, F1 Wen, F2 Hendrickx, F3 Strong, F4 Moslem, H1 Campos, H2 Ashby |
| 2 | A4, A6 (+3 `?`), C4, C8, D1, D2, D3, E2, G1, G2 |
| 1 or less | B1-B4 (with `?` on `RLC`), C1-C3, C5-C7, E1 |

No survey reaches more than 5 of 8, and none reaches `RLC` or `TYP` with a `Y`.

## 3. Candidate empty cells

### 3.0 The strongest negative result: no survey of calibration-aware RL

The `RLC` column has **zero `Y`**. The best coverage is `~` from the two general calibration surveys (A1, A2), which treat training-time calibration as one technique among many. A dedicated query for surveys of RL-for-calibration returned **only primary method papers** (Section 4), all from 2025-2026. RLCD, the method Jev is named after, sits in a cell with no incumbent survey. Caveat: B1-B4 are `?` on `RLC` because RLHF is known to affect calibration and those surveys may discuss it; this needs a full-text check.

### 3.1 The two columns with no `Y` at all

| Column | Status | Evidence |
|--------|--------|----------|
| `RLC` calibration-aware training | no survey | Section 3.0 |
| `TYP` typed / schema-constrained outputs | **no survey exists, not even a `~`** | A targeted sweep returned only benchmarks and studies: JSONSchemaBench (arXiv:2501.10868) and "Let Me Speak Freely?" (arXiv:2408.02442), plus vendor docs and blogs |

These two uncovered columns are exactly Jev's two claimed innovations: the training method (RLCD) and the output contract (type-safe values).

### 3.2 Empty pairs (each dimension covered somewhere, never jointly)

| Pair | Nearest coverage | Gap |
|------|------------------|-----|
| `RLC` x `DEC` | none as a survey; closest primary work is Yaldiz et al. 2026 (arXiv:2601.13284) | Calibration-aware RL for closed-set decisions has method papers but no synthesis |
| `CAL` x `TYP` | none | Calibrated probability PER declared option (Jev's output) is not treated anywhere; typed-output work measures validity, not calibration |
| `CAL` x `PAR` | C4 Gwak (`~`) | Diffusion and NAR decoders use confidence as a decoding signal (unmasking order); none of the surveyed works treats that confidence's calibration as the object of study |
| `RLC` x `ESC` | F4 Moslem (`ESC` only); primary: Chuang et al. 2024 (arXiv:2410.13284) | Training confidence so that thresholds, abstention and escalation actually work is not synthesised |
| `S12` x `ESC` x `CAL` | F4 Moslem (`~` `S12`, `~` `CAL`) | A calibrated System-1 model as the gate to a System-2 model is described as routing practice, not as a calibration requirement |

### 3.3 The conjunction, honestly assessed

**Jev's paradigm = `RLC` + `DEC` + `TYP` + `PAR` + `ESC`**, with `CAL` as the property that ties them together. No verified survey holds more than one of {`RLC`, `TYP`, `PAR`} at `Y`, and none holds `RLC` or `TYP` at all.

| Threat | Why it matters | What would clear it |
|--------|---------------|---------------------|
| **A6 Zhang 2026** (`?` x3) | "UQ as an active signal" may include UQ as an RL training signal and as a routing/abstention signal, which would partly occupy `RLC` and `ESC` | Full-text read; **the single largest threat** |
| A1 Geng / A2 Liu | Both may devote a section to calibration-aware fine-tuning | Full-text read of their training-method sections |
| B1-B3 RL surveys | May discuss RLHF-induced miscalibration and calibration rewards | Full-text keyword check (calibrat, Brier, scoring rule, ECE) |
| **Thin literature** | The `RLC` population found so far is ~5 method papers (2025-2026). That may be too thin for a CSUR-scale survey | Phase 1b harvest of primary works; if under ~40, consider a survey + position hybrid |
| **No Jev paper** | The motivating system is uncitable as method evidence | Frame around the paradigm; cite Jev only as industry motivation |

**Honest read:** the gap is real at the level of the conjunction and at two whole columns (`RLC`, `TYP`), and it matches Jev's claimed innovations exactly. It is **not yet confirmed**: A6 is unread, four RL surveys are `?` on `RLC`, and the primary literature may be too young to sustain a full survey. Do not write `NOVELTY CONFIRMED` until Phase 1b and the adversarial audit are done.

## 4. Closest primary works (not surveys)

| # | Title | 1st author | Year | Venue | arXiv | Cells |
|---|-------|-----------|------|-------|-------|-------|
| W1 | Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning | D. N. Yaldiz | 2026 | arXiv preprint | 2601.13284 | `RLC` x `DEC` - **closest single paper to RLCD** |
| W2 | Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models | D. Bani-Harouni | 2025 | ICLR 2026 | 2503.02623 | `RLC` x `CAL`; log-scoring-rule reward (the "prior work" critics cite against RLCD) |
| W3 | Process Supervision of Confidence Margin for Calibrated LLM Reasoning | L. Wang | 2026 | arXiv preprint | 2604.23333 | `RLC` at process level |
| W4 | Calibrating LLMs with Semantic-level Reward | F. Yu | 2026 | arXiv preprint | 2605.15588 | `RLC` |
| W5 | TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning | Z. Wei | 2025 | arXiv preprint | 2509.25760 | `RLC` x `ESC` (abstention-aware reward) |
| W6 | Learning to Route LLMs with Confidence Tokens | Y.-N. Chuang | 2024 | arXiv preprint | 2410.13284 | `CAL` x `ESC` |
| W7 | Is Escalation Worth It? A Decision-Theoretic Characterization of LLM Cascades | D. Bouchard | 2026 | arXiv preprint | 2605.06350 | `ESC` x `S12` |
| W8 | JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models | S. Geng | 2025 | arXiv preprint | 2501.10868 | `TYP` (evidence, not a survey) |
| W9 | Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models | Z. R. Tam | 2024 | arXiv preprint | 2408.02442 | `TYP`: format constraints can cost accuracy |
| W10 | Jev (TypeSafe AI) | - | 2026 | **no paper** | - | Industry motivation only (TechCrunch, 18 Sep 2026); not citable as method evidence |

## 5. Verification notes and caveats

| Item | Status |
|------|--------|
| 38 arXiv ids (37 in one bulk query, incl. all primary works, + 1 conformal survey) | Resolved via the arXiv API (export.arxiv.org, https) on 2026-09-21: exact title, first author, first-version date |
| 9 journal DOIs | Resolved via Crossref: A2 KDD, A3 CSUR, G1 TOIS, F2 MLJ, F1 TACL, G2 CSR, C1 TPAMI, H1 TACL, H2 Phil Trans A |
| A4 | Resolved via the ACL Anthology BibTeX (2025.findings-acl.1101) |
| F3 | Resolved via the Zenodo API; it is a **preprint, not peer reviewed** |
| Venue claims NOT DOI-resolved | A1 NAACL 2024 and C5 ACL Findings 2024 (ACL Anthology listings seen in search); E1 IEEE journal version (Xplore listing only); E2 TMLR (ML Anthology listing); D1 journal version (not checked). Cite these by arXiv id until resolved |
| Coverage marks | Abstract/scope level only. Every `?` and every `~` for the three closest threats (A6, A1, A2) needs a full-text read before any novelty claim |
| Name note | P1's first author is Diogo **Leitao**, unrelated to Jev's founder Diogo Almeida |

## 6. Search log (for the methodology section)

| # | Query / channel | Purpose |
|---|-----------------|---------|
| 1 | "survey confidence estimation and calibration in large language models" | `CAL` |
| 2 | "survey uncertainty quantification large language models taxonomy 2025" | `CAL` |
| 3 | "survey abstention large language models 'know your limits'" | `ESC` |
| 4 | "survey reinforcement learning large reasoning models RLVR 2025" | `RLC` host tier |
| 5 | "reinforcement learning calibration reward LLM confidence 'Rewarding Doubt'" | `RLC` primaries |
| 6 | "survey machine learning with a reject option selective prediction" | `ESC` |
| 7 | "'A Survey on Diffusion Language Models' arXiv 2025" | `PAR` |
| 8 | "survey non-autoregressive generation neural machine translation and beyond" | `PAR` |
| 9 | "survey structured output generation constrained decoding LLM JSON schema" | `TYP` |
| 10 | "'From System 1 to System 2' survey reasoning LLM" | `S12` |
| 11 | "'Stop Overthinking' survey efficient reasoning LLM" | `S12` |
| 12 | "'A Survey on LLM-as-a-Judge' arXiv" | `DEC` |
| 13 | "survey hallucination in large language models taxonomy ACM" | `HAL` |
| 14 | "survey calibration in deep learning state of the art methods" | `CAL` |
| 15 | "survey speculative decoding parallel decoding LLM inference" | `PAR` |
| 16 | "survey reinforcement learning for calibration uncertainty-aware reward LLM verbalized confidence" | `RLC` (dedicated negative test) |
| 17 | "survey structured output LLM typed output function calling tool use survey" | `TYP` (dedicated negative test) |
| 18 | "survey LLMs for text classification decision making zero-shot classification" | `DEC` |
| 19 | "survey LLM routing model cascades confidence-based escalation" | `ESC` |
| 20 | "survey learning to defer human-AI decision making" | `ESC` |
| 21 | "survey conformal prediction NLP LLM" | `CAL` x `DEC` |
| V | arXiv API bulk query; Crossref works API; ACL Anthology BibTeX; Zenodo records API | Metadata verification |

## 7. Recommended Phase 1b top-up

1. **Full-text reads**, in priority order: A6 (largest threat), A1 and A2 training-method sections, B1-B3 keyword check for calibration.
2. **Primary-work harvest for `RLC`** (to test the thin-literature risk): queries on "proper scoring rule" fine-tuning, "reward calibration" RLHF overconfidence, "verbalized confidence" training, "calibration-aware" RLVR.
3. **`TYP` re-check** in 4-8 weeks: a structured-output survey is the most likely thing to appear and would close one of the two empty columns.
4. **Candidate organising axes for Phase 2** (hypotheses, not decisions):
   - where calibration is induced: post-hoc -> fine-tuning -> RL reward
   - what the output contract is: free text -> constrained text -> typed decision
   - what a decision costs: System-2 generation -> System-1 single pass
   A 2D map of "how confidence is obtained" x "what the output contract is" would place every tier above in one figure.
5. Then write `novelty_gap.md` and run the mandatory adversarial audit before any `NOVELTY CONFIRMED` line.
