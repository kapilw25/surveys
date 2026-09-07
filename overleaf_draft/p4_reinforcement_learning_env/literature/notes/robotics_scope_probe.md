# P4 robotics-scope probe: is "RL environments for Robotics and Embodied AI" already taken?

**Proposed P4.** A survey of the environments/simulators robots are trained in, organised by a
DESIGN AUTOMATION ladder: handcrafted -> configurable -> auto-shaped (procedural/HPO) ->
LLM-generated -> co-adaptive (UED/curriculum).

**Stance of this probe.** Default-assume the space IS taken and try to prove it. A false "open"
is worse than a false "occupied".

**Verification rule.** Every row below was fetched from a primary record during this probe
(arXiv abstract page, arXiv HTML full text, or the Crossref works API). Anything that could not be
resolved to a primary record is listed in the "omitted" table at the end and is NOT used as
evidence. WebSearch was unavailable for this session (budget exhausted), so discovery ran through
arXiv full-text search HTML, arXiv HTML full text, Crossref and OpenAlex; DBLP was intermittently
unreachable, so a few venue fields stay "arXiv preprint only" rather than being guessed. Wave
coverage in Q2.2 was measured by grepping arXiv HTML full texts, not inferred from abstracts.

---

## Q1. Is the robotics/embodied simulator survey space already occupied?

### Q1.1 Verified surveys

| # | Exact title | 1st author | Year | Venue | ID | Organising axis |
|---|---|---|---|---|---|---|
| 1 | A Survey of Embodied AI: From Simulators to Research Tasks | Jiafei Duan | 2022 | IEEE Trans. Emerging Topics in Computational Intelligence 6:230-244 | arXiv:2103.04918; DOI 10.1109/TETCI.2022.3141105 | simulator *platform features* first, then research tasks (visual exploration, navigation, QA) |
| 2 | A Survey: Learning Embodied Intelligence from Physical Simulators and World Models | Xiaoxiao Long | 2025 (v3, 49 pp) | arXiv preprint only | arXiv:2507.00917 | two-part: physical simulators vs world models; simulators sliced by physical properties, rendering, sensor/joint types |
| 3 | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | Elie Aljalbout | 2025 (arXiv) / 2026 | Annual Review of Control, Robotics, and Autonomous Systems 2026 | arXiv:2510.20808 | causes of the sim-real gap, then mitigations (domain randomisation, real-to-sim, abstractions, sim-real co-training) |
| 4 | A Survey of Sim-to-Real Methods in RL: Progress, Prospects and Challenges with Foundation Models | Longchao Da | 2025 | arXiv preprint only | arXiv:2502.13187 | the four MDP elements: state, action, transition, reward |
| 5 | A Review of Physics Simulators for Robotic Applications | Jack Collins | 2021 | IEEE Access | DOI 10.1109/ACCESS.2021.3068769 | engine-by-engine feature and fidelity comparison, by application area |
| 6 | Robot Learning From Randomized Simulations: A Review | Fabio Muratore | 2022 | Frontiers in Robotics and AI 9:799893 | arXiv:2111.00956; DOI 10.3389/frobt.2022.799893 | domain-randomisation method families (static vs adaptive) |
| 7 | Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey | Wenshuai Zhao | 2020 | IEEE SSCI 2020, pp. 737-744 | arXiv:2009.13303; DOI 10.1109/SSCI47803.2020.9308468 | transfer technique family |
| 8 | Sim2Real in Robotics and Automation: Applications and Challenges | Sebastian Hofer | 2021 | IEEE Trans. Automation Science and Engineering 18(2):398-400 | DOI 10.1109/TASE.2021.3064065 | **NOT a survey: a three-page guest editorial for a special issue. Do not cite it as a survey** |
| 9 | A Review of Nine Physics Engines for Reinforcement Learning Research | Michael Kaup | 2024 | arXiv preprint only | arXiv:2407.08590 | nine named engines scored on popularity, features, quality, usability, RL capability |
| 10 | Comparing Popular Simulation Environments in the Scope of Robotics and Reinforcement Learning | Marian Korber | 2021 | arXiv preprint only | arXiv:2103.04616 | runtime benchmarking of four simulators across hardware |
| 11 | Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI | Yang Liu | 2024 (v8, 2025) | arXiv preprint only | arXiv:2407.06886 | embodied perception / interaction / agents / sim-to-real |
| 12 | A Survey of Zero-shot Generalisation in Deep Reinforcement Learning | Robert Kirk | 2023 | JAIR 76:201-264 | arXiv:2111.09794 | benchmark construction (how environments are varied) and solution-method families |
| 13 | Curriculum Learning for Reinforcement Learning Domains: A Framework and Survey | Sanmit Narvekar | 2020 | JMLR 21(181):1-50 | arXiv:2003.04960 | curriculum framework: *task generation*, sequencing, transfer |
| 14 | Automatic Curriculum Learning For Deep RL: A Short Survey | Remy Portelas | 2020 | IJCAI 2020 | arXiv:2003.04664 | ACL objectives and teacher mechanisms |
| 15 | Intelligent Automation for Embodied Benchmark Construction: Pipelines, Embodiments, Simulators, and Trends | Jinshan Lai | 2026 | arXiv preprint only | arXiv:2606.12207 | five-stage construction pipeline x a four-level automation rubric (see Q1.3) |
| 16 | Robot Learning in the Era of Foundation Models: A Survey | Xuan Xiao | 2023 | arXiv preprint only | arXiv:2311.14379 | infrastructure (simulators, datasets, models) then application domains |
| 17 | Foundation models in robotics: Applications, challenges, and the future | Roya Firoozi | 2023 (arXiv) / 2024 | Int. Journal of Robotics Research | arXiv:2312.07843; DOI 10.1177/02783649241281508 | perception / decision-making / control |
| 18 | A review of platforms for simulating embodied agents in 3D virtual environments | Deepti Prit Kaur | 2022 (online) / 2023 (print) | Artificial Intelligence Review 56(4):3711-3753 | DOI 10.1007/s10462-022-10253-x | platform-by-platform comparison of embodied 3D simulation platforms |
| 19 | Crossing the Reality Gap: A Survey on Sim-to-Real Transferability of Robot Controllers in Reinforcement Learning | Erica Salvato | 2021 | IEEE Access 9:153171-153187 | DOI 10.1109/ACCESS.2021.3126658 | approaches to the reality gap and their shortcomings |
| 20 | A Survey of Sim-to-Real Transfer Techniques Applied to Reinforcement Learning for Bioinspired Robots | Wei Zhu | 2023 | IEEE Trans. Neural Networks and Learning Systems 34(7):3444-3459 | DOI 10.1109/TNNLS.2021.3112718 | embodiment scope (bioinspired) then four technique groups |
| 21 | A Survey on Sim-to-Real Transfer Methods for Robotic Manipulation | Andrei Vladimirovich Pitkevich | 2024 | IEEE SISY 2024, pp. 000259-000266 | DOI 10.1109/SISY62279.2024.10737545 | sim2real method, scoped to manipulation |
| 22 | A Review of Differentiable Simulators | Rhys Newbury | 2024 | IEEE Access (per arXiv comments) | arXiv:2407.05560 | differentiable-simulator design trade-offs (versatility, speed, gradient accuracy) |
| 23 | A Survey of Robotic Navigation and Manipulation with Physics Simulators in the Era of Embodied AI | Lik Hang Kenny Wong | 2025 | arXiv preprint only ("Under Review") | arXiv:2505.01458 | simulator property and hardware requirement, crossed with navigation vs manipulation |
| 24 | Choosing the Arena: A Systematic Review of Simulators for Deep Reinforcement Learning in Mobile Robot Navigation | Zakaria Haja | 2025 | Int. Journal of Advanced Computer Science and Applications 16(12) | DOI 10.14569/IJACSA.2025.0161262 | three simulator archetypes (ROS-centric, versatile, GPU-native); PRISMA over 87 studies |
| 25 | NVIDIA Isaac Sim: Enabling Scalable, GPU-Accelerated Simulation for Robotics | Sicong Gao | 2026 | arXiv preprint only | arXiv:2606.03551 | single-platform deep dive plus cross-simulator comparison |
| 26 | Automated Reinforcement Learning (AutoRL): A Survey and Open Problems | Jack Parker-Holder | 2022 | JAIR 74:517-568 | arXiv:2201.03916; DOI 10.1613/jair.1.13596 | *which RL design choice is being automated*, crossed with automation method family. The closest generic match to P4's automation idea, but the subject is the agent's training pipeline. Its abstract does not name environment design, so environment coverage is UNCONFIRMED from the primary record |
| 27 | Increasing Generality in Machine Learning through Procedural Content Generation | Sebastian Risi | 2019 (arXiv) / 2020 | Nature Machine Intelligence | arXiv:1911.13071; DOI 10.1038/s42256-020-0208-z | PCG method families imported from games, and their role in RL generalisation and sim-to-real. A games-PCG review with no rung above PCG |

### Q1.2 Does any of them organise by DESIGN AUTOMATION?

Legend: `spine` = it is the primary axis; `partial` = a subsection or a column; `absent`.

| Survey | handcrafted vs configurable | procedural / auto-shaped | LLM-generated | co-adaptive (UED / curriculum) | design automation as the spine? |
|---|:--:|:--:|:--:|:--:|:--:|
| Duan'22 (2103.04918) | partial | absent | absent | absent | no |
| Long'25 (2507.00917) | absent | absent | absent | absent | no (verified against its section list: physics, rendering, sensors) |
| Aljalbout'26 (2510.20808) | partial | partial | absent | absent | no |
| Da'25 (2502.13187) | partial | partial | partial | absent | no (spine is the MDP tuple) |
| Collins'21 / Kaup'24 / Korber'21 | partial | absent | absent | absent | no (engine benchmarking) |
| Muratore'22 (frobt.2022.799893) | absent | spine (randomisation) | absent | partial | no |
| Kirk'23 (2111.09794) | partial | partial | absent | partial | no |
| Narvekar'20 (2003.04960) | absent | partial | absent | spine (curriculum) | no |
| Portelas'20 (2003.04664) | absent | partial | absent | spine (ACL) | no |
| Parker-Holder'22 AutoRL (2201.03916) | partial | partial | absent (predates the wave) | partial | no: it automates the *agent's* design choices, not the environment catalogue |
| Risi'20 PCG (1911.13071) | partial | spine (PCG) | absent | partial | no: games-PCG scope, no rung above PCG, no robot simulators |
| Ye'26 (2604.26509) | absent | partial | partial | absent | no, but see Q2.2: it does run structure-driven -> controllable -> agentic *within 3D scene content* |
| **Lai'26 (2606.12207)** | **spine** | **spine** | **spine** | **spine** | **YES, but for benchmark construction, not training** |

Of 27 verified items, 26 do not use design automation as the spine. They taxonomise by simulator
platform, by physics engine, by research task, by embodiment, by sim2real technique family, by MDP
element, or by curriculum objective. **No survey of unsupervised environment design exists**: arXiv
full-text search, Crossref and an OpenAlex title sweep all returned UED method papers and zero UED
reviews. The co-adaptive rung of P4's ladder is genuinely unoccupied by any review.

### Q1.3 The one that hurts: Lai et al. 2026

Verified from the arXiv abstract page and the arXiv HTML full text of arXiv:2606.12207.

| Item | Value |
|---|---|
| Exact title | Intelligent Automation for Embodied Benchmark Construction: Pipelines, Embodiments, Simulators, and Trends |
| First author | Jinshan Lai (10 authors) |
| Date / venue | submitted 10 June 2026; arXiv preprint only |
| Its automation ladder | "Construction Automation and Auditability Rubric (CAAR)": **manual -> traditional automation -> foundation-model-assisted -> agentic closed-loop** |
| P4's proposed ladder | handcrafted -> configurable -> auto-shaped -> LLM-generated -> co-adaptive |
| Systems it already names | GenSim, RoboGen, Holodeck, RoboCasa, ProcTHOR, Habitat, Isaac Sim, ManiSkill, RLBench |
| Its scope | EVALUATION benchmark construction only ("requirement and task construction, data acquisition, data cleaning and annotation, benchmark suite generation and metric definition, and evaluation execution") |
| Its headline finding | automation shifts cost toward validation, auditability, version control and governance rather than reducing it |

**Reading.** The four-rung ladder P4 proposes is already in print for the neighbouring artefact.
The single thing that separates P4 from Lai'26 is training-vs-evaluation. That is a real
difference, but it is one sentence wide, and Lai'26 is already cited inside the authors' own P3
competitor table, so a reviewer will find it immediately.

### Q1 verdict

**PARTIALLY OCCUPIED.** Twenty-six verified surveys (row 8 is a guest editorial, not a survey)
already cover robot simulators, physics
engines, differentiable simulators, sim-to-real, domain randomisation, PCG and curricula, so the
*subject matter* is thoroughly mapped; none of them uses design automation as its spine for
*training* environments, but Lai'26 (2606.12207) uses an almost isomorphic four-rung automation
ladder for embodied *benchmark* construction, so the axis itself is no longer virgin territory.

---

## Q2. Is the generative / LLM environment-generation wave already surveyed?

### Q2.1 The primary systems (all verified against arXiv abstract pages)

| System (exact title) | 1st author | Year | ID | Venue | Generates |
|---|---|---|---|---|---|
| GenSim: Generating Robotic Simulation Tasks via Large Language Models | Lirui Wang | 2023 | 2310.01361 | ICLR 2024 | task code + expert demos |
| RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation | Yufei Wang | 2023 | 2311.01455 | ICML 2024 | tasks + scenes + supervision |
| Holodeck: Language Guided Generation of 3D Embodied AI Environments | Yue Yang | 2023 | 2312.09067 | CVPR 2024 | 3D scenes from a prompt |
| RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots | Soroush Nasiriany | 2024 | 2406.02523 | RSS 2024 | scenes + assets + demo trajectories |
| Gen2Sim: Scaling up Robot Learning in Simulation with Generative Models | Pushkal Katara | 2023 (arXiv) / 2024 | ICRA 2024 (DOI 10.1109/ICRA57147.2024.10610566) | 2310.18308 | assets, task descriptions, rewards |
| Eurekaverse: Environment Curriculum Generation via Large Language Models | William Liang | 2024 | 2411.01775 | CoRL 2024 | terrain curriculum as code |
| MetaUrban: An Embodied AI Simulation Platform for Urban Micromobility | Wayne Wu | 2024 | 2407.08725 | arXiv technical report | compositional urban scenes |
| DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning | Zhenyu Jiang | 2024 | 2410.24185 | ICRA 2025 | demonstrations (21k from 60) |
| Eureka: Human-Level Reward Design via Coding Large Language Models | Yecheng Jason Ma | 2023 | 2310.12931 | ICLR 2024 | reward code |
| Text2Reward: Reward Shaping with Language Models for Reinforcement Learning | Tianbao Xie | 2023 | 2309.11489 | ICLR 2024 | dense reward programs |
| GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs | Pu Hua | 2024 | 2410.03645 | CoRL 2024 | task code + demonstrations |
| MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | Ajay Mandlekar | 2023 | 2310.17596 | CoRL 2023 | demonstrations (50k+ from ~200) |
| DrEureka: Language Model Guided Sim-To-Real Transfer | Yecheng Jason Ma | 2024 | 2406.01967 | RSS 2024 | reward + domain-randomisation configs |
| ProcTHOR: Large-Scale Embodied AI Using Procedural Generation | Matt Deitke | 2022 | 2206.06994 | NeurIPS 2022 | procedural interactive houses |
| Infinite Photorealistic Worlds using Procedural Generation (Infinigen) | Alexander Raistrick | 2023 | 2306.09310 | CVPR 2023 | procedural 3D worlds + labels |
| RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizable Robot Learning | Haoran Geng | 2025 | 2504.18904 | arXiv preprint only | platform + synthetic dataset + benchmark |
| Automated Creation of Digital Cousins for Robust Policy Learning (ACDC) | Tianyuan Dai | 2024 | 2410.07408 | CoRL 2024 | "digital cousin" scenes from one real image |
| BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | Chengshu Li | 2024 | 2403.09227 | arXiv record shows no venue for this version | scenes/activities + OmniGibson |
| Learning Visual Parkour from Generated Images (LUCIDSim) | Alan Yu | 2024 | 2411.00083 | arXiv preprint only | generated egocentric RGB for training |
| Towards Generalist Robots: A Promising Paradigm via Generative Simulation | Zhou Xian | 2023 | 2305.10455 | arXiv position paper | the "generative simulation" paradigm itself |
| RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | Tianxing Chen | 2025 | 2506.18088 | arXiv preprint only | randomised scenes + demonstrations |
| EmbodiedGen: Towards a Generative 3D World Engine for Embodied Intelligence | Xinjie Wang | 2025 | 2506.10600 | arXiv preprint only | physical 3D assets/scenes exported as URDF |
| MetaScenes: Towards Automated Replica Creation for Real-world 3D Scans | Huangyue Yu | 2025 | 2505.02388 | CVPR 2025 | interactive replicas of real scans |
| GenDexHand: Generative Simulation for Dexterous Hands | Feng Chen | 2025 | 2511.01791 | arXiv preprint only | tasks + environments, VLM-feedback loop |
| Genie Sim 3.0: A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot | Chenghao Yin | 2026 | 2601.02078 | arXiv preprint only | LLM-built scenes + synthetic data |
| RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies | Jenai Xuning Yang | 2026 | 2604.09860 | RSS 2026 | LLM-enabled scenes + tasks |
| Generative Simulation for Policy Learning in Physical Human-Robot Interaction | Junxiang Wang | 2026 | 2604.08664 | arXiv preprint only | scenes + soft-body humans + trajectories |
| PerceptTwin: Semantic Scene Reconstruction for Iterative LLM Planning and Verification | Charlie Gauthier | 2026 | 2606.04226 | ICRA 2026 | interactive sim built from robot perception |

Title corrections worth carrying into the bibliography: "Infinigen", "ACDC" and "LUCIDSim" are
project names that do NOT appear in the paper titles; RoboGen, DexMimicGen and MimicGen have longer
official titles than the ones commonly quoted.

### Q2.2 Surveys that already cover part of this wave

Coverage was measured by grepping the arXiv HTML full text (bibliographies included) for system
names, so the counts below are occurrence counts, not impressions.

| Survey | 1st author | Year | Venue | ID | Organising axis | Wave coverage (full-text hit counts) |
|---|---|---|---|---|---|---|
| 3D Generation for Embodied AI and Robotic Simulation: A Survey | Tianwei Ye | 2026 | arXiv preprint only (27 pp) | 2604.26509 | three roles: Data Generator / Simulation Environments (structure-driven -> controllable -> **agentic**) / Sim2Real Bridge | **the sharpest competitor.** Holodeck 6, ProcTHOR 8, RoboCasa 4, Gen2Sim 5, GenSim2 4, MimicGen 7, Infinigen 4, RoboTwin 6, Genesis 9. **RoboGen 0, Eureka 0, GenSim v1 0.** "reward function" appears once; "curriculum" 0 |
| 3D Scene Generation: A Survey | Haozhe Xie | 2025 (v2 2026) | accepted by IJCV | 2505.05474 | procedural / neural-3D / image-based / video-based generation | robotics is one application subsection. RoboGen 3, Eurekaverse 3, Holodeck 3, ProcTHOR 3, Infinigen 6, RoboCasa 1. GenSim 0, Gen2Sim 0, Eureka 0 |
| Survey on Large Language Model-Enhanced Reinforcement Learning: Concept, Taxonomy, and Methods | Yuji Cao | 2024 | IEEE Trans. Neural Networks and Learning Systems | arXiv:2404.00282; DOI 10.1109/TNNLS.2024.3497992 | four LLM roles in RL: information processor / **reward designer** / decision-maker / generator | **owns the reward-generation cell.** Eureka 16, Text2Reward 3, "reward function" 49. GenSim / RoboGen / Holodeck / RoboCasa / Gen2Sim / ProcTHOR / Infinigen all 0: no scene or environment generation |
| Automatic Scene Generation: State-of-the-Art Techniques, Models, Datasets, Challenges, and Future Prospects | Awal Ahmed Fime | 2024 (arXiv) / 2025 | IEEE Access 13:95753-95796 | arXiv:2410.01816; DOI 10.1109/ACCESS.2025.3574298 | generative model family (VAE / GAN / Transformer / Diffusion) | graphics-first (COCO-Stuff, Visual Genome, FID/IS); robotics named as a motivating application only |
| Intelligent Automation for Embodied Benchmark Construction | Jinshan Lai | 2026 | arXiv preprint only | 2606.12207 | pipeline stage x CAAR automation level | names GenSim, RoboGen, Holodeck, RoboCasa, ProcTHOR; evaluation-scoped |
| Generative Physical AI in Vision: A Survey | Daochang Liu | 2025 | arXiv preprint only | 2501.10928 | explicit simulation vs implicit learned physics | zero hits on all wave-system probe terms; vision/world-simulator framing |
| From Visual Synthesis to Interactive Worlds: Toward Production-Ready 3D Asset Generation | Jiafeng Wu | 2026 | arXiv preprint only | 2604.23629 | asset classes: objects / characters / scenes | graphics/game-asset framing. Holodeck 6, ProcTHOR 7, Infinigen 10, but GenSim 0, RoboGen 0 |
| Real-World Robot Applications of Foundation Models: A Review | Kento Kawaharazuka | 2024 | Advanced Robotics, DOI 10.1080/01691864.2024.2408593 | arXiv:2402.05741 | input-output relations, component replacement in real robot systems | explicitly real-world, not simulation; all six wave systems 0 except Eureka 2 in passing |
| Robot Learning in the Era of Foundation Models: A Survey | Xuan Xiao | 2023 (arXiv) / 2025 | Neurocomputing, DOI 10.1016/j.neucom.2025.129963 | 2311.14379 | infrastructure then application domain | no arXiv HTML available, so assessed from the abstract only: simulators treated as infrastructure, generation not the subject. Weakest row here |
| Foundation models in robotics: Applications, challenges, and the future | Roya Firoozi | 2023 (arXiv) / 2024 | Int. Journal of Robotics Research | arXiv:2312.07843; DOI 10.1177/02783649241281508 | perception / decision-making / control | all six wave systems 0; "reward function" 5, "curriculum" 1 |

### Q2.3 What is and is not covered

| Slice of the wave | Example systems | Already surveyed? | By whom |
|---|---|:--:|---|
| asset and scene generation | Holodeck, ProcTHOR, Infinigen, MetaScenes, EmbodiedGen | **yes, squarely** | Ye'26 (2604.26509), Xie'25 (2505.05474, IJCV), Fime'25 (IEEE Access), Wu'26 (2604.23629) |
| reward generation | Eureka, Text2Reward, DrEureka | **yes** | Cao'24 (2404.00282, IEEE TNNLS): "reward designer" is one of its four spine categories, 49 mentions of "reward function", Eureka 16 |
| task generation | GenSim, GenSim2, RoboGen | partial | Lai'26 (2606.12207), evaluation-scoped; Ye'26 has GenSim2 but zero RoboGen and zero GenSim v1 |
| demonstration/data generation | MimicGen, DexMimicGen, RoboTwin 2.0 | partial | Lai'26 (data-acquisition stage); Ye'26 (MimicGen 7, RoboTwin 6) |
| environment curriculum via foundation models | Eurekaverse | **no survey found** | Eurekaverse appears only as a passing clause in an IJCV *scene-generation* survey's application section |
| unsupervised environment design / co-adaptive | the UED line (Dennis, Jiang, Parker-Holder et al.) | **no survey found** | arXiv, Crossref and an OpenAlex title sweep all return method papers and zero reviews |
| scene + task + reward + curriculum as ONE loop | RoboGen, Gen2Sim | **no survey found** | Ye'26 has 1 mention of "reward function" and 0 of "curriculum"; Cao'24 has 49 of "reward function" and 0 of every scene-generation system. The two halves are surveyed in disjoint venues under disjoint axes |

Ye'26 also states its own open problem in a form P4 can quote: few works report generation cost or
throughput, so it is unclear whether agentic pipelines can produce the thousands of environments
large-scale policy training needs.

### Q2 verdict

**PARTIALLY OCCUPIED, and more occupied than it first looked.** The scene/asset half is squarely
surveyed (four verified surveys, one IJCV-accepted, one in IEEE Access) and the reward half is
squarely surveyed by Cao'24 in IEEE TNNLS, so any claim that "no survey covers the generative wave"
would be refuted on sight; what remains genuinely unsurveyed is the environment-curriculum / UED rung
and the unification of scene + task + reward + curriculum as a single generate-train-evaluate loop.

---

## Q3. Self-overlap with the authors' own P3

### Q3.1 What P3 already is

| Item | Value |
|---|---|
| Title | Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence |
| Corpus | 160 web-verified benchmarks, 2017-2026 |
| Lanes | policy suites 37, embodied agents 85, world-model evaluation 34, prediction-to-action bridges 4 |
| Spine | evaluation mode (open-loop / closed-loop / bridge) x robotic capability x model family |
| Source of truth checked | `docs/assets/catalog_p3.js` (160 rows) and `overleaf_draft/p3_action_bench/paper_benchmark/novelty_gap_B_benchmark.md` |

### Q3.2 How much of P3 a robotics-scoped P4 would re-catalogue

Counted programmatically over the 160 catalogue rows. An entry counts as re-catalogued if it is an
interactive simulated environment that an RL/IL agent is actually trained or rolled out in, rather
than an offline dataset, a video-QA probe, a real-hardware-only protocol, or a generation-quality
benchmark.

| P3 lane | Rows | Interactive sim environments P4 would have to list | Not re-catalogued |
|---|--:|--:|--:|
| policy suites | 37 | 34 | 3 (FMB, RoboAgent, RoboArena: real hardware) |
| embodied agents | 85 | 60 | 25 (datasets and video/QA probes: nuScenes, JRDB, OpenEQA, CLEVRER-style causal probes, PlanBench, ToMi, ...) |
| world-model evaluation | 34 | 0 | 34 (generation-quality suites, no agent loop) |
| prediction-to-action bridges | 4 | 2 | 2 |
| **total** | **160** | **96 (60%)** | **64 (40%)** |

Named collisions the authors already flagged: LIBERO, CALVIN, ManiSkill, Meta-World, RLBench,
Habitat, BEHAVIOR, robosuite, ARNOLD, RoboCasa, FurnitureBench, Isaac. The catalogue also already
contains iGibson, Gibson Env, Legged Gym, Brax, CARLA, MetaDrive, ProcTHOR, VirtualHome, SoftGym,
SoundSpaces, Waymax, GRUtopia, LEGENT, EmbodiedCity, HumanoidBench, Overcooked-AI, SMAC and Melting
Pot, which is most of the canon a robotics RL-environments survey would open with.

### Q3.3 The complication nobody has flagged yet

The five existing P4 harvest slices (`literature/notes/slice_01.md` to `slice_05.md`, about 200 rows)
are **not** a robotics corpus. They are a cross-domain "RL environment" corpus already tagged with
the design-automation rung.

| Domain in the current P4 harvest | Approximate rows |
|---|--:|
| power / energy | 15 |
| robotics (all sub-flavours) | 13 |
| transport / driving | 7 |
| science (chemistry, space, marine, optics) | 7 |
| security | 4 |
| games / general RL / LLM-agentic | 10 |
| EDA / compilers / HPC | 5 |
| medical, finance, agriculture, manufacturing, buildings, aerospace, sports | the remainder |

Not one of GenSim, RoboGen, Habitat, ManiSkill, Isaac Gym, LIBERO or Meta-World appears anywhere in
the harvest. So the harvest that exists and the title that is proposed point in opposite directions:
the harvest is cross-domain, the title is robotics-only.

### Q3.4 Candidate differentiators, honestly scored

| Candidate differentiator | Does it survive a reviewer? | Why |
|---|:--:|---|
| "P3 catalogues evaluation benchmarks, P4 catalogues training environments" | weak | 96 of the 160 objects are literally the same objects. Re-tagging the same corpus with a new column reads as a re-cut, not a new survey |
| "P4's spine is design automation, P3's is evaluation mode" | weak-to-moderate | a genuinely different axis, but Lai'26 (2606.12207) already published a four-rung automation ladder over the same embodied-simulator population, and P3 already cites Lai'26 |
| "P4 adds the generative wave (GenSim, RoboGen, Eureka) that P3 omits" | weak | true that P3 omits the generators, but Ye'26 (2604.26509) already covers the scene half and Cao'24 (2404.00282, IEEE TNNLS) already covers the reward half. This differentiates P4 from P3 while walking into two other incumbents |
| **"P4 is cross-domain: the design-automation ladder across robotics, energy, driving, security, EDA, recommendation, science; robotics is one column, not the subject"** | **strongest available** | it changes the *population*, not just the axis. P3's 160 rows become at most one column of P4's matrix, and no verified survey anywhere runs the automation ladder across domains. It is also what the existing 200-row harvest already is |
| "P4 covers the rung no one surveys: environment curriculum and co-adaptive UED" | moderate, and additive | verified unoccupied (Q2.3), but it is one rung, not a survey. Strongest as the *payload chapter* inside the cross-domain framing |
| "P4 unifies scene + task + reward + curriculum as one generate-train-evaluate loop" | moderate | verified that no survey does this (the halves sit in disjoint venues), but it is an argument about *synthesis*, which reviewers discount unless the corpus is also new |

### Q3 verdict

**SEVERE OVERLAP as proposed.** With the title "RL environments for Robotics and Embodied AI", 96 of
P3's 160 catalogue entries (60%) fall inside P4's scope, and both papers would then be the same
authors cataloguing the same simulators twice within a year. The overlap becomes MANAGEABLE only if
P4 drops the robotics-only framing and keeps the population cross-domain, with robotics as one
column of a design-automation matrix and the unsurveyed reward-generation and curriculum rungs as
the contribution.

---

## Omitted: leads that could not be resolved to a primary record during this probe

| Lead | Why omitted |
|---|---|
| CoEnv (2604.05484), SkillComposer (2608.14944), STEP (2608.27225), RLDX-1 (2605.03269) | seen in arXiv search listings, never opened as an abstract page; UNVERIFIED, not used as evidence |
| "A Survey of Sim-to-Real Transfer Methods in Robot Learning" (Daniyal Musadiq, 2026) | OpenAlex only, Zenodo-hosted with two duplicate DOIs, no venue, no arXiv record. UNVERIFIED, do not cite |
| "Surveying Failure Detection and Sim-to-Real Transfer in Robot Manipulation: A Unified Taxonomy and the Reporting-Incompatibility Problem" (Aarav Bedi, 2026) | ResearchGate-hosted only, no venue, not corroborable. UNVERIFIED, do not cite |
| Whether Ye'26 (2604.26509) has since been accepted anywhere | arXiv comments show no venue as of v3. Left as "arXiv preprint only" |
| Venue fields for MetaUrban, RoboVerse, LUCIDSim, BEHAVIOR-1K (current version), RoboTwin 2.0, EmbodiedGen, GenDexHand, Genie Sim 3.0 | DBLP was unreachable and Crossref returned no match; left as "arXiv preprint only" rather than filled from memory. Gen2Sim was closed to ICRA 2024 via Crossref |
| A survey of generative simulation / environment generation for robot learning, searched in Crossref as well as arXiv | Crossref returns no such survey; the only near hits are a dissertation ("Modeling the Physical World: Generative World Models for Robot Learning", Siyuan Zhou, DOI 10.14711/thesis-hdl172513) and a path-planning survey. Recorded as an absence |
| A dedicated survey of unsupervised environment design, or of LLM reward design *for robot RL* | searched via arXiv full-text search. The reward-design surveys that do exist are LLM-alignment surveys, not robotics: "A Survey on Progress in LLM Alignment from the Perspective of Reward Design" (Miaomiao Ji, 2025, arXiv:2505.02666) and "Reward Engineering for Software Tasks: A Survey of Reinforcement Learning Approaches" (Md Rayhanul Masud, 2026, arXiv:2601.19100). Recorded as an absence in robotics, not as a verified negative |
