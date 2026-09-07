# Prior surveys - novelty scan Phase 1 (RL ENVIRONMENTS as a designed artifact)

Scope of this scan: existing surveys, reviews, taxonomies and survey-grade theses that could
already occupy the cell "the RL environment as a designed artifact" (simulators, gyms,
benchmark suites, environment design, environment generation). Every row was resolved to a
live arXiv `/abs/` page, a Crossref DOI record, or a publisher landing page before being
recorded. Candidates that could not be resolved were dropped, not guessed.

| Scan statistic | Value |
|----------------|-------|
| Surveys / reviews verified and retained | 99 |
| Verification channels | arXiv abstract pages, Crossref REST API, JAIR / Frontiers / publisher pages, ar5iv tables of contents |
| Non-survey artifacts retained and flagged | 4 (2 PhD theses, 1 position paper, 1 reproducibility study) |
| Records dropped as unverifiable | all unresolved candidates omitted |
| Known recall limit | the session WebSearch quota (200 calls) was exhausted mid-scan; later recall came from Crossref and arXiv exact-record lookups, which under-recall survey-shaped titles. See section 5. |

Tiering used throughout:

| Tier | Meaning |
|------|---------|
| **A** | Environment-centric. These are the actual competitors for the cell. |
| **B** | Environment generation, curriculum, open-endedness, generalisation. |
| **C** | Simulators, sim-to-real, reward specification. |
| **D** | One level up: general or domain RL surveys that contain an environments/benchmarks section. |
| **E** | Benchmark practice, reproducibility and RL software/frameworks. |
| **F** | Domain-specific environment and simulator surveys (traffic, power, drones, networking, driving, cyber, EDA). |

## 1. Verified survey table

### Tier A - environment-centric

| # | Survey title | 1st author | Year | Venue | arXiv/DOI | scope |
|---|--------------|-----------|------|-------|-----------|-------|
| A1 | From Pixels to Digital Agents: An Empirical Study on the Taxonomy and Technological Trends of Reinforcement Learning Environments | L. Luo | 2026 | arXiv preprint (v1 25 Mar 2026) | arXiv:2603.23964 | Data-driven taxonomy over >2,000 distilled RL environment papers, classified by application domain and cognitive capability |
| A2 | Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application | J. Li | 2026 | arXiv preprint (10 Jun 2026, 63 pp.) | arXiv:2606.12191 | Full lifecycle of LLM-agent environments: 8 attributes x 8 domains, symbolic vs neural synthesis, evaluation per paradigm, agent-environment co-evolution, Environment-as-a-Service |
| A3 | A review of reinforcement learning: A tripartite framework of environment design, algorithmic innovation, and application scenarios | Y. Liu | 2026 | Array 30:100812 | 10.1016/j.array.2026.100812 | General RL review whose first of three top-level axes is environment design |
| A4 | The Landscape of Agentic Reinforcement Learning for LLMs: A Survey | G. Zhang | 2025 | TMLR (arXiv 2 Sep 2025) | arXiv:2509.02547 | Agentic RL for LLMs; consolidates open-source environments, benchmarks and frameworks into a compendium |
| A5 | Scalable Environments Drive Generalizable Agents *(position paper)* | J. Zhang | 2026 | arXiv preprint (18 May 2026) | arXiv:2605.18181 | Argues generalisation needs environment scaling; separates trajectory vs task vs environment scaling; programmatic generators and generative world models |
| A6 | A survey of benchmarks for reinforcement learning algorithms | B. Stapelberg | 2020 | South African Computer Journal 32(2) | 10.18489/sacj.v32i2.746 | Catalogue and comparison of RL benchmark suites and evaluation practice |
| A7 | Automated Reinforcement Learning (AutoRL): A Survey and Open Problems | J. Parker-Holder | 2022 | JAIR 74:517-568 | 10.1613/jair.1.13596 | Automating RL design choices: meta-learning, evolution, HPO, architecture and (briefly) environment design choices |
| A8 | Structure in Deep Reinforcement Learning: A Survey and Open Problems | A. Mohan | 2023 | JAIR 79:1167-1236 | arXiv:2306.16021 | Design-pattern survey of inductive bias in deep RL; contains an explicit environment-generation pattern |
| A9 | A Survey of Text Games for Reinforcement Learning Informed by Natural Language | P. Osborne | 2022 | TACL 10:873-887 | 10.1162/tacl_a_00495 | Catalogue of text-game RL environments and their language-grounding demands |
| A10 | Intelligent Automation for Embodied Benchmark Construction: Pipelines, Embodiments, Simulators, and Trends | J. Lai | 2026 | arXiv preprint (10 Jun 2026) | arXiv:2606.12207 | Five-stage embodied benchmark construction pipeline, with an explicit four-rung automation ladder (manual curation -> traditional automation -> foundation-model assistance -> agentic closed-loop) applied at each stage, plus construction-cost and governance analysis |
| A11 | A Survey on Simulation Environments for Reinforcement Learning | T. Kim | 2021 | 18th Int. Conf. on Ubiquitous Robots (UR), pp. 63-67 | 10.1109/UR52253.2021.9494694 | Direct survey of simulation environments used for RL research (short paper) |

### Tier B - generation, curriculum, open-endedness, generalisation

| # | Survey title | 1st author | Year | Venue | arXiv/DOI | scope |
|---|--------------|-----------|------|-------|-----------|-------|
| B1 | Learning Curricula in Open-Ended Worlds *(PhD dissertation)* | M. Jiang | 2023 | PhD thesis, arXiv (3 Dec 2023) | arXiv:2312.03126 | Unsupervised environment design and minimax-regret autocurricula over generated environments |
| B2 | Robust Agents in Open-Ended Worlds *(PhD thesis)* | M. Samvelyan | 2025 | PhD thesis, arXiv (9 Dec 2025) | arXiv:2512.08139 | PCG sandbox (MiniHack), adversarial curricula (Maestro), quality-diversity adversary search, extended to LLM inputs |
| B3 | Automatic Curriculum Learning For Deep RL: A Short Survey | R. Portelas | 2020 | IJCAI 2020, pp. 4819-4825 | 10.24963/ijcai.2020/671 | Typology of automatic curriculum learning mechanisms for deep RL |
| B4 | Curriculum Learning for Reinforcement Learning Domains: A Framework and Survey | S. Narvekar | 2020 | JMLR 21(181):1-50 | arXiv:2003.04960 | Framework plus survey of curriculum generation, task sequencing and transfer |
| B5 | Increasing generality in machine learning through procedural content generation | S. Risi | 2020 | Nature Machine Intelligence 2:428-436 | 10.1038/s42256-020-0208-z | Perspective arguing PCG is the route to general agents; PCG-based RL benchmarks |
| B6 | Search-Based Procedural Content Generation: A Taxonomy and Survey | J. Togelius | 2011 | IEEE Trans. Computational Intelligence and AI in Games 3(3):172-186 | 10.1109/TCIAIG.2011.2148116 | Taxonomy of search-based PCG for games |
| B7 | Procedural Content Generation via Machine Learning (PCGML) | A. Summerville | 2018 | IEEE Trans. Games 10(3):257-270 | 10.1109/TG.2018.2846639 | Survey of learned generative models of game content |
| B8 | Deep learning for procedural content generation | J. Liu | 2021 | Neural Computing and Applications 33:19-37 | 10.1007/s00521-020-05383-8 | Survey of deep generative and deep RL methods for content generation |
| B9 | A Survey of Zero-shot Generalisation in Deep Reinforcement Learning | R. Kirk | 2023 | JAIR 76:201-264 | 10.1613/jair.1.14174; arXiv:2111.09794 | Formalises ZSG; explicitly categorises ZSG benchmarks, many of them procedurally generated |
| B10 | Quality Diversity: A New Frontier for Evolutionary Computation | J. K. Pugh | 2016 | Frontiers in Robotics and AI 3:40 | 10.3389/frobt.2016.00040 | Foundational quality-diversity survey; divergent search and open-endedness |
| B11 | Transfer Learning in Deep Reinforcement Learning: A Survey | Z. Zhu | 2023 | IEEE Trans. Pattern Analysis and Machine Intelligence 45(11):13344-13362 | 10.1109/TPAMI.2023.3292075 | Categorises transfer by goal, methodology, RL backbone and application |
| B12 | Curriculum Learning: A Survey | P. Soviany | 2022 | International Journal of Computer Vision | arXiv:2101.10382 | Cross-domain easy-to-hard curriculum taxonomy; data ordering rather than environment construction |
| B13 | A Survey on Curriculum Learning | X. Wang | 2021 | IEEE Trans. Pattern Analysis and Machine Intelligence | arXiv:2010.13166 | Motivations, theory and applications of curriculum learning across CV and NLP |
| B14 | A Survey on Safety-Critical Driving Scenario Generation - A Methodological Perspective | W. Ding | 2023 | IEEE Trans. Intelligent Transportation Systems (arXiv v1 2022) | arXiv:2202.02215 | Data-driven, adversarial and knowledge-based generation of driving scenarios, plus simulation tools and fidelity/diversity/controllability criteria |
| B15 | Procedural content generation for games: A survey | M. Hendrikx | 2013 | ACM Trans. Multimedia Computing, Communications, and Applications 9(1):1-22 | 10.1145/2422956.2422957 | Layered survey of PCG methods organised by content type |
| B16 | The Quest for Content: A Survey of Search-Based Procedural Content Generation for Video Games | M. Zamorano | 2023 | arXiv preprint | arXiv:2311.04710 | Systematic survey of search-based PCG literature 2011-2022 |
| B17 | Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration | M. Farrokhi Maleki | 2024 | AIIDE-24 | arXiv:2410.15644 | Compares search-based, ML, traditional and LLM-based content generation and their combinations |
| B18 | Quality-Diversity Optimization: a novel branch of stochastic optimization | K. Chatzilygeroudis | 2021 | Springer book chapter | arXiv:2012.04322 | Review of QD algorithms that illuminate a behaviour space rather than return a single optimum |
| B19 | Quality and Diversity Optimization: A Unifying Modular Framework | A. Cully | 2018 | IEEE Trans. Evolutionary Computation 22(2):245-259 | 10.1109/TEVC.2017.2704781 | Unifying modular framework subsuming novelty search and MAP-Elites |
| B20 | Open-Ended Learning: A Conceptual Framework Based on Representational Redescription | S. Doncieux | 2018 | Frontiers in Neurorobotics 12 | 10.3389/fnbot.2018.00059 | Conceptual framework for open-ended learning agents that redescribe their own representations |
| B21 | Why Open-Endedness Matters | K. O. Stanley | 2019 | Artificial Life 25(3):232-235 | 10.1162/artl_a_00294 | Perspective framing open-endedness as a core AI/ALife goal |
| B22 | Intrinsic motivations and open-ended learning | G. Baldassarre | 2019 | arXiv preprint | arXiv:1912.13263 | Cross-disciplinary taxonomy of intrinsic motivation types for open-ended skill learning |
| B23 | Autotelic Agents with Intrinsically Motivated Goal-Conditioned Reinforcement Learning: a Short Survey | C. Colas | 2022 | JAIR 74:1159-1199 | arXiv:2012.09830; 10.1613/jair.1.13554 | Agents that represent, generate and select their own goals; goal generation as the automation locus |
| B24 | Open-Endedness is Essential for Artificial Superhuman Intelligence *(position paper)* | E. Hughes | 2024 | arXiv preprint | arXiv:2406.04268 | Defines open-endedness via novelty and learnability and sketches a foundation-model route to it |
| B25 | A Survey on Self-play Methods in Reinforcement Learning | R. Zhang | 2024 | arXiv preprint | arXiv:2408.01072 | Unified framework and taxonomy for self-play autocurricula in multi-agent RL |
| B26 | Large Language Models and Games: A Survey and Roadmap | R. Gallotta | 2024 | IEEE Trans. Games | arXiv:2402.18659 | LLM roles in and for games, including content, level and world generation |
| B27 | GPT for Games: An Updated Scoping Review (2020-2024) | D. Yang | 2024 | IEEE Trans. Games | arXiv:2411.00308 | Scoping review of 177 GPT-in-games papers with PCG as a leading application area |
| B28 | Foundation Models for Decision Making: Problems, Methods, and Opportunities | S. Yang | 2023 | arXiv preprint | arXiv:2303.04129 | Foundation models as agents, environment models and generative simulators for decision making |
| B29 | Games for Artificial Intelligence Research: A Review and Perspectives | C. Hu | 2023 | IEEE Trans. Artificial Intelligence | arXiv:2304.13269 | Review of game platforms used as AI testbeds, matching AI techniques to environment properties |

### Tier C - simulators, sim-to-real, reward specification

| # | Survey title | 1st author | Year | Venue | arXiv/DOI | scope |
|---|--------------|-----------|------|-------|-----------|-------|
| C1 | A Survey of Embodied AI: From Simulators to Research Tasks | J. Duan | 2022 | IEEE Trans. Emerging Topics in Computational Intelligence 6(2):230-244 | 10.1109/TETCI.2022.3141105; arXiv:2103.04918 | Scores 9 embodied-AI simulators against 7 features, then surveys the research tasks built on them |
| C2 | A Review of Physics Simulators for Robotic Applications | J. Collins | 2021 | IEEE Access 9:51416-51431 | 10.1109/ACCESS.2021.3068769 | Indexes and compares physics simulators across robotics sub-domains with selection guidance |
| C3 | A review of platforms for simulating embodied agents in 3D virtual environments | D. P. Kaur | 2022 | Artificial Intelligence Review 56:3711-3753 | 10.1007/s10462-022-10253-x | Comparative review of 22 embodied-agent simulation platforms by visual environment and physics |
| C4 | Survey of Simulators for Aerial Robots: An Overview and In-Depth Systematic Comparisons | C. A. Dimmig | 2023 (arXiv) / 2025 (journal) | IEEE Robotics and Automation Magazine 32:153-166 | arXiv:2311.02296; 10.1109/MRA.2024.3433171 | Overview of 44 UAV simulators, in-depth comparison of 14, plus selection decision factors |
| C5 | A Survey of Robotic Navigation and Manipulation with Physics Simulators in the Era of Embodied AI | L. H. K. Wong | 2025 | arXiv preprint, under review | arXiv:2505.01458 | Simulator properties, features, hardware requirements, benchmark datasets and metrics |
| C6 | A Survey: Learning Embodied Intelligence from Physical Simulators and World Models | X. Long | 2025 | arXiv preprint (49 pp.) | arXiv:2507.00917 | Joint review of physical simulators and learned world models as training/evaluation environments |
| C7 | World Model for Robot Learning: A Comprehensive Survey | B. Hou | 2026 | arXiv preprint (43 pp.) | arXiv:2605.00080 | World models as learned simulators for RL, planning, evaluation and data generation |
| C8 | Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI | Y. Liu | 2024 | arXiv preprint | arXiv:2407.06886 | Broad embodied-AI review covering robots, simulators, datasets and tasks |
| C9 | Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey | W. Zhao | 2020 | IEEE SSCI 2020, pp. 737-744 | 10.1109/SSCI47803.2020.9308468; arXiv:2009.13303 | Domain randomisation, domain adaptation, imitation, meta-learning, distillation |
| C10 | Crossing the Reality Gap: A Survey on Sim-to-Real Transferability of Robot Controllers in Reinforcement Learning | E. Salvato | 2021 | IEEE Access 9:153171-153187 | 10.1109/ACCESS.2021.3126658 | Transferability of RL-learned robot controllers from simulation to hardware |
| C11 | Robot Learning From Randomized Simulations: A Review | F. Muratore | 2022 | Frontiers in Robotics and AI 9:799893 | 10.3389/frobt.2022.799893 | The dedicated domain-randomisation review under a different title |
| C12 | A Survey of Sim-to-Real Transfer Techniques Applied to Reinforcement Learning for Bioinspired Robots | W. Zhu | 2023 | IEEE Trans. Neural Networks and Learning Systems 34:3444-3459 | 10.1109/TNNLS.2021.3112718 | Sim-to-real for RL on bioinspired and legged morphologies |
| C13 | A Survey of Sim-to-Real Methods in RL: Progress, Prospects and Challenges with Foundation Models | L. Da | 2025 | arXiv preprint | arXiv:2502.13187 | Organises sim-to-real methods by MDP element, adds the foundation-model wave |
| C14 | Reward Models in Deep Reinforcement Learning: A Survey | R. Yu | 2025 | IJCAI 2025 Survey Track | arXiv:2506.15421 | Taxonomy of reward modelling by source, mechanism and learning paradigm, plus reward-model evaluation |
| C15 | A Survey of Reinforcement Learning from Human Feedback | T. Kaufmann | 2023 | TMLR (2025) | arXiv:2312.14925 | RLHF and preference-based RL as reward-function replacement |
| C16 | Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback | S. Casper | 2023 | arXiv preprint (cs.AI) | arXiv:2307.15217 | Position/review enumerating tractable vs fundamental RLHF problems, auditing and disclosure standards |
| C17 | A survey of inverse reinforcement learning: Challenges, methods and progress | S. Arora | 2021 | Artificial Intelligence 297:103500 | 10.1016/j.artint.2021.103500; arXiv:1806.06877 | Inferring reward functions from behaviour |
| C18 | A Survey on Progress in LLM Alignment from the Perspective of Reward Design | M. Ji | 2025 | arXiv preprint | arXiv:2505.02666 | Reward mechanisms for alignment: frameworks, construction, optimisation |
| C19 | A Review of Nine Physics Engines for Reinforcement Learning Research | M. Kaup | 2024 | arXiv preprint | arXiv:2407.08590 | Comparative review of Brax, Chrono, Gazebo, MuJoCo, ODE, PhysX, PyBullet, Webots and Unity as RL simulation backends |

### Tier D - one level up (general or domain RL surveys with an environments/benchmarks section)

| # | Survey title | 1st author | Year | Venue | arXiv/DOI | environments/benchmarks section? |
|---|--------------|-----------|------|-------|-----------|----------------------------------|
| D1 | Deep Reinforcement Learning: A Brief Survey *(journal title; the arXiv version is titled "A Brief Survey of Deep Reinforcement Learning")* | K. Arulkumaran | 2017 | IEEE Signal Processing Magazine 34(6):26-38 | arXiv:1708.05866; 10.1109/MSP.2017.2743240 | Yes - Sec. VI-H "Benchmarks" (ALE, ViZDoom, TorchCraft, SC2LE, DeepMind Lab, Malmo, MuJoCo, OpenAI Gym) |
| D2 | Deep Reinforcement Learning: An Overview | Y. Li | 2017 | arXiv preprint | arXiv:1701.07274 | Yes - Sec. 7.8 "Testbeds", inside the Resources chapter |
| D3 | An Introduction to Deep Reinforcement Learning | V. Francois-Lavet | 2018 | Foundations and Trends in Machine Learning 11(3-4):219-354 | 10.1561/2200000071; arXiv:1811.12560 | Yes - Ch. 9 "Benchmarking Deep RL" (9.1 benchmark environments, 9.2 best practice, 9.3 open-source software) |
| D4 | Model-based Reinforcement Learning: A Survey | T. M. Moerland | 2023 | Foundations and Trends in Machine Learning 16(1):1-118 | 10.1561/2200000086; arXiv:2006.16712 | No - 12 sections, none on testbeds |
| D5 | Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems | S. Levine | 2020 | arXiv preprint | arXiv:2005.01643 | Partial - Sec. 6 "Applications and Evaluation", no standalone benchmark-suite section |
| D6 | A Survey on Offline Reinforcement Learning: Taxonomy, Review, and Open Problems | R. Figueiredo Prudencio | 2024 | IEEE Trans. Neural Networks and Learning Systems 35:10237-10257 | 10.1109/TNNLS.2023.3250269; arXiv:2203.01387 | Yes - reviews existing benchmarks' properties and shortcomings |
| D7 | Deep Reinforcement Learning that Matters *(reproducibility study)* | P. Henderson | 2018 | AAAI-18 | arXiv:1709.06560 | Yes in effect - its subject matter is benchmark-environment variance and reporting standards |
| D8 | Deep Reinforcement Learning for Autonomous Driving: A Survey | B. R. Kiran | 2020 (arXiv) / 2022 (journal) | IEEE Trans. Intelligent Transportation Systems 23:4909-4926 | arXiv:2002.00444; 10.1109/TITS.2021.3054625 | Yes - explicit simulators section |
| D9 | Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes | C. Tang | 2024 | Annual Review of Control, Robotics, and Autonomous Systems | arXiv:2408.03539 | No - simulator use appears only as a taxonomy axis in Sec. 3.3 |
| D10 | Reinforcement learning in robotics: A survey | J. Kober | 2013 | International Journal of Robotics Research 32(11):1238-1274 | 10.1177/0278364913495721 | No - pre-dates the benchmark-suite era |
| D11 | Testing reinforcement learning systems: A comprehensive review | A. Sunba | 2026 | Journal of Systems and Software | 10.1016/j.jss.2025.112563 | Partial - test oracles and environment perturbation, but the object under test is the agent |
| D12 | Taxonomy and Trends in Reinforcement Learning for Robotics and Control Systems: A Structured Review | K. Ter | 2025 | arXiv preprint | arXiv:2510.21758 | Partial - taxonomy by task family, no simulator catalogue evidenced on the abstract page |
| D13 | Survey on Large Language Model-Enhanced Reinforcement Learning: Concept, Taxonomy, and Methods | Y. Cao | 2025 | IEEE Trans. Neural Networks and Learning Systems 36:9737-9757 | 10.1109/TNNLS.2024.3497992 | Partial - LLM as reward designer and as world/environment model |
| D14 | Deep Reinforcement Learning in the Era of Foundation Models: A Survey | I. D. Mienye | 2026 | Computers 15(1):40 | 10.3390/computers15010040 | Partial - benchmarks and open problems section |
| D15 | Reinforcement learning for crop management support: Review, prospects and challenges | R. Gautron | 2022 | Computers and Electronics in Agriculture 200:107182 | 10.1016/j.compag.2022.107182 | Yes for its domain - crop-simulator-backed environments |
| D16 | A Systematic Study on Reinforcement Learning Based Applications | K. Sivamayil | 2023 | Energies 16(3):1512 | 10.3390/en16031512 | No - applications review (127 papers), energy-weighted |
| D17 | A Survey of Reinforcement Learning Informed by Natural Language | J. Luketina | 2019 | IJCAI 2019, pp. 6309-6317 | 10.24963/ijcai.2019/880 | Partial - language-conditioned environments as a class |
| D18 | A Survey of Deep Reinforcement Learning in Video Games | K. Shao | 2019 | arXiv preprint | arXiv:1912.10944 | Yes for its domain - catalogues arcade, first-person and RTS game environments from 2D to 3D and single- to multi-agent |
| D19 | A survey of Reinforcement Learning for Electronic Design Automation | H. Zhu | 2024 | ISEDA 2024, pp. 717-721 | 10.1109/ISEDA62518.2024.10617712 | Partial - EDA task formulations (placement, routing, logic synthesis); the environment is the EDA toolchain, treated as given |

### Tier E - benchmark practice, reproducibility, RL software

| # | Survey title | 1st author | Year | Venue | arXiv/DOI | scope |
|---|--------------|-----------|------|-------|-----------|-------|
| E1 | A Review for Deep Reinforcement Learning in Atari: Benchmarks, Challenges, and Solutions | J. Fan | 2021 | arXiv preprint | arXiv:2112.04145 | Review of the Atari/ALE benchmark family, its evaluation metrics and its superhuman-scoring problems |
| E2 | Provably Safe Reinforcement Learning: Conceptual Analysis, Survey, and Benchmarking | H. Krasowski | 2023 | TMLR | arXiv:2205.06750 | Survey plus empirical benchmarking of provably safe RL families on shared control tasks |
| E3 | A Comparison of Reinforcement Learning Frameworks for Software Testing Tasks | P. S. N. Mindom | 2023 | Empirical Software Engineering | arXiv:2208.12136 | Empirical comparison of Stable-Baselines3, Keras-RL and Tensorforce on shared tasks |
| E4 | Review, Analysis and Design of a Comprehensive Deep Reinforcement Learning Framework | N. D. Nguyen | 2020 | arXiv preprint | arXiv:2002.11883 | Reviews DRL software architecture practice, then proposes a unified framework (part review, part system paper) |
| E5 | Reproducibility of Benchmarked Deep Reinforcement Learning Tasks for Continuous Control | R. Islam | 2017 | ICML 2017 Reproducibility in ML Workshop | arXiv:1708.04133 | Meta-study of variance and reproducibility on standard continuous-control benchmark tasks |
| E6 | A Survey on Reproducibility by Evaluating Deep Reinforcement Learning Algorithms on Real-World Robots | N. A. Lynnerup | 2019 | CoRL 2019 | arXiv:1909.03772 | Reproducibility obstacles and a standardised evaluation protocol on physical robot platforms |
| E7 | Systematic choice of video game benchmarks in Deep Reinforcement Learning | E. Gomes | 2021 | SBGames 2021 | 10.1109/SBGames54170.2021.00028 | Methodological study of how video-game benchmark environments get selected for DRL evaluation |

### Tier F - domain-specific environment and simulator surveys

| # | Survey title | 1st author | Year | Venue | arXiv/DOI | scope |
|---|--------------|-----------|------|-------|-----------|-------|
| F1 | A survey on how network simulators serve reinforcement learning in wireless networks | S. Ergun | 2023 | Computer Networks 234:109934 | 10.1016/j.comnet.2023.109934 | Network simulators as RL environment infrastructure for wireless networking |
| F2 | Reinforcement learning-based drone simulators: survey, practice, and challenge | J. H. Chan | 2024 | Artificial Intelligence Review 57 | 10.1007/s10462-024-10933-w | Drone and UAV simulators used as RL environments, with practice notes and open challenges |
| F3 | A Comprehensive Review of Reinforcement Learning for Autonomous Driving in the CARLA Simulator | E. Delavari | 2025 | arXiv preprint | arXiv:2509.08221 | About 100 papers training and testing RL policies inside one simulator; consolidates MDP formulations and metrics |
| F4 | Optimizing Power Grid Topologies with Reinforcement Learning: A Survey of Methods and Challenges | E. van der Sar | 2025 | arXiv preprint | arXiv:2504.08210 | Grid-topology RL organised around the L2RPN / Grid2Op competition environments |
| F5 | Graph reinforcement learning for power grids: A comprehensive survey | M. Hassouna | 2026 | Energy and AI 23:100671 | 10.1016/j.egyai.2025.100671; arXiv:2407.04522 | Graph RL for transmission and distribution grids, energy markets and EV charging |
| F6 | A Review of Deep Reinforcement Learning for Smart Building Energy Management | L. Yu | 2021 | IEEE Internet of Things Journal 8(15):12046-12063 | arXiv:2008.05074 | DRL for building energy management organised by system scale, device to district |
| F7 | Deep Reinforcement Learning for Autonomous Cyber Defence: A Survey | G. Palmer | 2023 | arXiv preprint | arXiv:2310.07745 | Includes a dedicated review of current autonomous-cyber-defence environments used to benchmark DRL agents |
| F8 | A Survey on Reinforcement Learning Models and Algorithms for Traffic Signal Control | K.-L. A. Yau | 2017 | ACM Computing Surveys 50:1-38 | 10.1145/3068287 | CSUR-style survey of RL formulations for traffic signal control |
| F9 | Recent Advances in Reinforcement Learning for Traffic Signal Control | H. Wei | 2021 | ACM SIGKDD Explorations Newsletter 22 | 10.1145/3447556.3447565 | TSC models plus their simulation environments and evaluation protocols |
| F10 | A survey on deep reinforcement learning approaches for traffic signal control | H. Zhao | 2024 | Engineering Applications of Artificial Intelligence 133:108100 | 10.1016/j.engappai.2024.108100 | DRL TSC methods and the simulators and benchmarks they are evaluated on |
| F11 | Intelligent traffic signal control based on reinforcement learning: a survey | H. Xiao | 2026 | Artificial Intelligence Review 59 | 10.1007/s10462-026-11530-9 | Recent RL-based TSC survey covering simulation platforms and benchmarks |
| F12 | Traffic Light Control using Reinforcement Learning: A Survey and an Open Source Implementation | C. Paduraru | 2022 | VEHITS 2022 | 10.5220/0011040300003191 | RL traffic-light control survey paired with a released open-source environment |
| F13 | Reinforcement Learning for Electronic Design Automation: Successes and Opportunities | M. E. Taylor | 2021 | ISPD 2021 | 10.1145/3439706.3446882 | Invited overview of RL successes and open problems in EDA and physical design |
| F14 | A Survey of Reinforcement Learning Algorithms for Dynamically Varying Environments | S. Padakandla | 2021 | ACM Computing Surveys 54:1-25 | 10.1145/3459991; arXiv:2005.10619 | Algorithm-centric survey of RL under non-stationary environments; the environment is a problem property, not an artifact |

## 2. Coverage matrix

Marks: `Y` = covered as a first-class part of the survey, `~` = partial, one subsection or a
passing treatment, `.` = absent.

Dimensions:

| Key | Dimension |
|-----|-----------|
| `CAT` | environment catalogue (enumerates concrete environments / benchmarks / simulators) |
| `DES` | environment DESIGN methods (how an environment is deliberately constructed or shaped) |
| `GEN` | auto-generation / PCG |
| `UED` | UED / automatic curriculum |
| `INF` | execution infrastructure (APIs, vectorisation, throughput, Environment-as-a-Service) |
| `DOM` | domain-specific gyms (energy / agriculture / medical / EDA / industrial) |
| `EVL` | evaluation OF environments (the environment itself as the object assessed) |
| `LLM` | LLM-generated environments |

### 2a. Tier A - environment-centric

| Dimension | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 | A10 | A11 |
|-----------|----|----|----|----|----|----|----|----|----|-----|-----|
| CAT environment catalogue | Y | Y | ~ | Y | ~ | Y | . | . | Y | Y | Y |
| DES environment design methods | ~ | Y | Y | . | ~ | . | ~ | ~ | . | Y | ~ |
| GEN auto-generation / PCG | ~ | Y | ~ | . | Y | . | ~ | ~ | ~ | Y | . |
| UED automatic curriculum | . | ~ | ~ | . | ~ | . | Y | ~ | . | . | . |
| INF execution infrastructure | . | ~ | . | ~ | ~ | ~ | . | . | . | ~ | Y |
| DOM domain-specific gyms | ~ | . | ~ | . | . | . | . | . | . | ~ | . |
| EVL evaluation OF environments | ~ | Y | . | ~ | . | ~ | . | . | ~ | Y | ~ |
| LLM LLM-generated environments | ~ | Y | . | ~ | Y | . | . | . | . | Y | . |

### 2b. Tier B - generation, curriculum, open-endedness, generalisation

| Dimension | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 | B11 |
|-----------|----|----|----|----|----|----|----|----|----|-----|-----|
| CAT environment catalogue | ~ | ~ | . | ~ | ~ | . | . | . | ~ | . | ~ |
| DES environment design methods | Y | ~ | ~ | ~ | ~ | ~ | . | ~ | ~ | . | . |
| GEN auto-generation / PCG | Y | Y | ~ | ~ | Y | Y | Y | Y | ~ | ~ | . |
| UED automatic curriculum | Y | Y | Y | Y | ~ | . | . | . | ~ | ~ | ~ |
| INF execution infrastructure | . | . | . | . | . | . | . | . | . | . | . |
| DOM domain-specific gyms | . | . | . | . | . | . | . | . | . | . | . |
| EVL evaluation OF environments | ~ | ~ | . | . | ~ | ~ | ~ | . | Y | . | . |
| LLM LLM-generated environments | . | ~ | . | . | . | . | . | . | . | . | . |

### 2b-ii. Tier B continued - curriculum, PCG, quality-diversity, open-endedness, LLM-and-games

| Dimension | B12 | B13 | B14 | B15 | B16 | B17 | B18 | B19 | B20 | B21 | B22 | B23 | B24 | B25 | B26 | B27 | B28 | B29 |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| CAT environment catalogue | . | . | ~ | . | . | . | . | . | . | . | . | ~ | . | ~ | ~ | ~ | ~ | Y |
| DES environment design methods | . | . | Y | ~ | ~ | ~ | . | . | ~ | . | . | ~ | . | . | ~ | . | ~ | ~ |
| GEN auto-generation / PCG | . | . | Y | Y | Y | Y | ~ | ~ | . | ~ | . | ~ | ~ | ~ | ~ | ~ | ~ | . |
| UED automatic curriculum | Y | Y | ~ | . | . | . | ~ | ~ | ~ | ~ | ~ | Y | Y | Y | . | . | . | . |
| INF execution infrastructure | . | . | ~ | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| DOM domain-specific gyms | . | . | Y | . | . | . | . | . | . | . | . | . | . | . | . | . | . | ~ |
| EVL evaluation OF environments | . | . | ~ | . | ~ | ~ | . | . | . | . | . | . | ~ | . | . | . | ~ | ~ |
| LLM LLM-generated environments | . | . | . | . | . | Y | . | . | . | . | . | . | ~ | . | Y | Y | Y | . |

### 2c. Tier C - simulators, sim-to-real, reward specification

| Dimension | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 | C14 | C15 | C16 | C17 | C18 | C19 |
|-----------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| CAT environment catalogue | Y | Y | Y | Y | Y | Y | ~ | Y | . | . | . | . | ~ | . | . | . | . | . | Y |
| DES environment design methods | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | Y | ~ | Y | Y | ~ | ~ | ~ | Y | . |
| GEN auto-generation / PCG | . | . | . | . | . | . | ~ | . | . | . | ~ | . | ~ | . | . | . | . | . | . |
| UED automatic curriculum | . | . | . | . | . | . | . | . | . | . | ~ | . | . | . | . | . | . | . | . |
| INF execution infrastructure | Y | Y | Y | Y | Y | ~ | . | ~ | . | . | . | . | . | . | . | . | . | . | Y |
| DOM domain-specific gyms | . | ~ | . | ~ | ~ | . | . | . | . | . | . | ~ | . | . | . | . | . | . | . |
| EVL evaluation OF environments | Y | Y | ~ | Y | ~ | ~ | ~ | ~ | . | . | ~ | . | . | ~ | . | ~ | . | . | Y |
| LLM LLM-generated environments | . | . | . | . | . | ~ | ~ | . | . | . | . | . | ~ | . | ~ | . | . | ~ | . |

Note on Tier C row `EVL`: the `Y` marks are *simulator* comparisons (fidelity, feature coverage,
hardware cost). That is the closest anything in this corpus comes to grading an environment as
an artifact, and it stops at the simulator engine; it never reaches task design, reward
specification quality, difficulty calibration or reusability.

### 2d. Tier D - one level up

| Dimension | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 | D14 | D15 | D16 | D17 | D18 | D19 |
|-----------|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| CAT environment catalogue | Y | Y | Y | . | ~ | Y | ~ | Y | ~ | . | ~ | ~ | . | ~ | ~ | ~ | ~ | Y | ~ |
| DES environment design methods | . | . | ~ | ~ | . | . | ~ | ~ | ~ | ~ | . | . | ~ | . | ~ | . | . | ~ | . |
| GEN auto-generation / PCG | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| UED automatic curriculum | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| INF execution infrastructure | ~ | ~ | Y | . | . | ~ | ~ | ~ | . | . | . | . | . | . | . | . | . | ~ | . |
| DOM domain-specific gyms | . | . | . | . | . | . | . | Y | ~ | ~ | . | ~ | . | . | Y | ~ | . | Y | Y |
| EVL evaluation OF environments | . | . | ~ | . | ~ | Y | Y | . | . | . | ~ | . | . | . | . | . | . | . | . |
| LLM LLM-generated environments | . | . | . | . | . | . | . | . | . | . | . | . | ~ | ~ | . | . | . | . | . |

### 2e. Tier E - benchmark practice, reproducibility, RL software

| Dimension | E1 | E2 | E3 | E4 | E5 | E6 | E7 |
|-----------|-----|-----|-----|-----|-----|-----|-----|
| CAT environment catalogue | Y | ~ | . | . | ~ | ~ | Y |
| DES environment design methods | . | ~ | . | ~ | . | . | . |
| GEN auto-generation / PCG | . | . | . | . | . | . | . |
| UED automatic curriculum | . | . | . | . | . | . | . |
| INF execution infrastructure | ~ | ~ | Y | Y | ~ | ~ | . |
| DOM domain-specific gyms | . | . | . | . | . | . | . |
| EVL evaluation OF environments | Y | Y | Y | ~ | Y | Y | Y |
| LLM LLM-generated environments | . | . | . | . | . | . | . |

### 2f. Tier F - domain-specific environment and simulator surveys

| Dimension | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | F11 | F12 | F13 | F14 |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| CAT environment catalogue | Y | Y | Y | Y | ~ | ~ | Y | ~ | Y | Y | Y | ~ | . | . |
| DES environment design methods | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | . | . | ~ | ~ | ~ |
| GEN auto-generation / PCG | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| UED automatic curriculum | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| INF execution infrastructure | Y | Y | ~ | ~ | . | . | ~ | . | ~ | ~ | ~ | Y | . | . |
| DOM domain-specific gyms | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | . |
| EVL evaluation OF environments | ~ | Y | ~ | ~ | . | . | ~ | . | Y | ~ | ~ | . | . | . |
| LLM LLM-generated environments | . | . | . | . | . | . | . | . | . | . | . | . | . | . |

### 2g. Breadth ranking (how many of the 8 dimensions each survey reaches)

| Survey | `Y` | `Y`+`~` | Character |
|--------|-----|---------|-----------|
| A2 Agentic Environment Engineering | 4 | 7 | Broadest environment-lifecycle coverage anywhere, but LLM-agent silo only |
| A1 From Pixels to Digital Agents | 2 | 7 | Broadest catalogue, thin on design method |
| C5 Physics Simulators for Navigation and Manipulation | 3 | 6 | Deepest on the infrastructure rung, nothing on generation |
| C1 Embodied AI: From Simulators to Research Tasks | 3 | 5 | Simulator feature-scoring, the nearest thing to grading environments |
| B1 Learning Curricula in Open-Ended Worlds | 3 | 6 | Deepest on the UED rung, no infrastructure, no domain gyms |
| A3 Array tripartite review | 2 | 6 | The only survey naming environment design as a top-level axis |
| B9 Zero-shot Generalisation | 1 | 6 | Environments as instruments for measuring generalisation |
| B14 Safety-Critical Driving Scenario Generation | 3 | 7 | The only survey that joins generation, a domain, and artifact-quality criteria; single domain only |
| B17 PCG in Games with LLM Integration | 2 | 4 | The only survey spanning search-based, ML and LLM generation in one taxonomy; games content only |
| A7 AutoRL | 1 | 4 | Automates RL design choices; environment design is a minor sub-case |

## 3. Candidate empty cells

### 3.0 The strongest negative result: no dedicated UED survey exists

A dedicated sweep for a survey or review of **unsupervised environment design** returned
nothing. Every artifact with "environment design" in the title is a primary method paper:
PAIRED (arXiv:2012.02096), PLR and Robust PLR (arXiv:2110.02439), ACCEL (arXiv:2203.01302),
MAESTRO (arXiv:2303.03376), DRED (arXiv:2402.03479), TRACED (arXiv:2506.19997), PACE
(arXiv:2605.01358) and similar. The only review-shaped coverage is B1, a PhD dissertation,
and the environment-generation subsections inside B9. **The rung of the ladder that the
proposed survey most needs to own has no incumbent survey at all.** This was confirmed
through three independent channels (arXiv title-and-abstract phrase search, OpenAlex title
search, and web search) before being recorded.

### 3.1 No single dimension is empty (revised after Tiers E and F)

The first draft of this section claimed `EVL` was universally empty and treated `DOM` and
`INF` as thin. Tiers E and F refute all three claims. State the position plainly:

| Dimension | Status after 99 surveys | Who fills it |
|-----------|-------------------------|--------------|
| `CAT` | Filled | A1, A6, A11, C1-C5, E1, E7, F1-F4, F7, F9-F11 |
| `DES` | Filled | A2, A3, A10, B1, C11, C13, C14, C18 |
| `GEN` | Filled | A2, A5, B5-B8, B14-B17 |
| `UED` | Filled by method papers only, **no survey** | B1 (thesis), B3, B4, B23-B25; see 3.0 |
| `INF` | Filled | A11, C1-C5, C19, E3, E4, F1, F2, F12 |
| `DOM` | Filled | F1-F14, D8, D15, D19 |
| `EVL` | Filled | A10, C1, C2, C4, C19, E1-E3, E5-E7, F2, F9 |
| `LLM` | Filled | A2, A5, A10, B17, B26-B28 |

**Conclusion: there is no empty single cell.** The novelty claim must rest on pairs and on
the UED-survey gap, not on any one dimension. Two genuine single-topic absences did survive
the sweep, and both are narrower than a dimension:

| Absence | Evidence |
|---------|----------|
| **No survey of the general-purpose RL library and API ecosystem** (Gym / Gymnasium / RLlib / Stable-Baselines / CleanRL) | Closest verified items are C19 (physics engines), E3 (three libraries, scoped to software-testing tasks) and E4 (part review, part system paper). Gymnasium itself (arXiv:2407.17032) is a library paper, not a survey. |
| **No survey of medical or agricultural RL gyms** | Both domains have primary environment papers (gym-DSSAT, CropGym, HistoGym and similar) but no survey of them, whereas traffic has five, power has three and EDA has two. |

### 3.1b The dimension formerly claimed empty

| Dimension | Best existing coverage | Why it is still empty |
|-----------|------------------------|-----------------------|
| **`EVL`, evaluation OF environments as artifacts** | **A10 is now the closest and it is close.** Its whole thesis is that automating benchmark construction shifts cost toward validation, auditability, version control and long-term governance, and it argues for pipelines that are diagnosable, auditable and responsibly refreshable. B14 names fidelity, efficiency, diversity, transferability and controllability for *generated* driving scenarios. Otherwise C1, C2, C4 grade *simulator engines*; B9 grades *generalisation protocols*; D6 lists benchmark *shortcomings*; D11 tests the *agent-plus-system* | **This dimension can no longer be claimed as empty.** A10 treats the constructed artifact's validation and governance as a first-class concern. What survives is narrower: A10's object is an *embodied evaluation benchmark* (task specs, demonstrations, annotations, metrics, release policy), not a *training environment*, and it does not assess difficulty calibration, reward-specification soundness or reusability of an environment as a learning surface. |

### 3.2 Empty pairs (each dimension covered somewhere, never jointly)

| Pair | Nearest survey to the pair | Gap |
|------|---------------------------|-----|
| **`DES` x `INF`** design methods x execution infrastructure | A2 (design `Y`, infra `~`), C5/C1 (infra `Y`, design `~`) | Nobody joins "how the environment is specified" to "how it is executed at scale". Gymnasium / EnvPool / JAX / Environment-as-a-Service and PCG / UED are disjoint literatures with disjoint author sets. |
| **`GEN` + `UED` + `LLM` as one ordered ladder** | B17 (search-based + ML + LLM generation in one taxonomy, games content only), A2 (symbolic vs neural synthesis, LLM agents only), B1 (UED), B5/B8 (PCG) | PCG, UED and LLM environment synthesis are never placed on a single ordered automation spine *for RL environments*. B17 spans the generation rungs but its object is game content, not RL environments, and it omits UED entirely. A2 offers a paradigm dichotomy, not a degree ladder, and excludes non-LLM RL. |
| **`DOM` x `GEN`** domain gyms x auto-generation | Nothing. The nearest are D15 (agriculture `Y`, generation `.`) and A3 (design `Y`, domain `~`) | **The best-evidenced empty pair in this scan.** Tier F now holds 14 verified domain surveys covering traffic, power grids, drones, wireless networking, driving, cyber defence and EDA. The `GEN` row of the Tier F matrix is `.` for all 14, and the `UED` row is `.` for all 14. Domain literatures catalogue their simulators and review their algorithms; not one asks how its environments could be generated rather than hand-built. |
| **`CAT` x `EVL`** catalogue x environment evaluation | A6, A1, C1 | Catalogues enumerate; simulator reviews score engines. A catalogue carrying a per-environment design-quality assessment does not exist. |
| **`INF` x `EVL`** infrastructure x environment evaluation | C5 | Throughput is measured, artifact quality is not. Nobody asks whether a 1M-steps-per-second environment is a *better designed* environment. |

### 3.3 The proposed organising axis, honestly assessed

Proposed spine: **degree of environment design automation**, ordered roughly as
`handcrafted -> configurable / parameterised -> procedurally generated -> adaptively generated (UED / auto-curriculum) -> learned or LLM-synthesised`.

| Competitor | How close it comes | Residual gap |
|-----------|--------------------|--------------|
| **A10** Lai et al. 2026, arXiv:2606.12207 | **The axis itself, already published.** An explicit four-rung ladder - manual curation, traditional automation, foundation-model assistance, agentic closed-loop - applied stage by stage across a five-stage construction pipeline, over embodiments and simulators, with cost and governance analysis on top. This is the proposed spine, in print, since 10 Jun 2026. | Object is *embodied benchmark construction for evaluation*, not RL environments as training artifacts. No UED or adaptive-curriculum rung. No non-embodied RL (games, classical control, LLM-agent environments). No domain-specific gyms outside embodied AI. The ladder is applied to a construction pipeline, not used to classify a corpus of environments. |
| **A2** Li et al. 2026, arXiv:2606.12191 | Closest. Splits automated environment synthesis into symbolic vs neural paradigms and adds three environment-evolution paradigms (neural-driven, difficulty-driven, scaling-driven). Also covers evaluation and Environment-as-a-Service. | Scope is LLM-agent environments only: no robotics, control, games or domain gyms. Its spine is a lifecycle (model, synthesise, evaluate, apply), not a degree ladder, and the handcrafted and configurable rungs are not rungs at all. |
| **A3** Liu et al. 2026, Array 30:100812 | Names environment design as one of three top-level axes, and its environment-design dimension set reportedly includes "degree of human involvement", which is the automation axis under another name. | One dimension among six inside an algorithms-and-applications review; not the organising spine. The dimension list is reported-not-read (see caveats), so this needs a full-text check before the novelty claim is finalised. **This is the single largest threat.** |
| **A1** Luo et al. 2026, arXiv:2603.23964 | Largest environment-specific taxonomy in existence (>2,000 papers); its trend analysis narrates the drift from toy problems to generated and foundation-model environments. | Classified by application domain and cognitive capability plus a bibliometric time axis. Automation is a trend it observes, never the axis it classifies by. No UED, no infrastructure, no design-method taxonomy. |
| *(runner-up)* **A7** Parker-Holder et al. 2022, JAIR 74 | The word "automated" is in the title, and it does treat automating RL design choices including some environment-side choices. | AutoRL automates the *agent's* design choices (hyperparameters, architecture, algorithm, reward). The environment is the fixed backdrop, not the artifact being automated. Opposite object. |

**Honest read (revised after A10 was found).** The axis is **occupied**. A10 publishes the
four-rung automation ladder outright, in June 2026, over embodiments and simulators. The
earlier reading of this section - "not yet occupied, but no longer safe" - was wrong, and it
was wrong because A10 does not use the words "reinforcement learning environment" in its
title and so did not surface in environment-phrased queries. A survey pitched as "RL
environments organised by degree of design automation" would now read as A10 with the scope
moved sideways, and a reviewer who knows A10 would say so.

The surrounding threats compound this. A3 names "degree of human involvement" as an
environment-design dimension. A2 has the symbolic/neural synthesis split for LLM-agent
environments. A1 owns the catalogue. A7 owns the word "automated" but points it at the agent.
Four independent groups converged on automation-as-organising-principle within roughly four
months.

What genuinely survives is narrower than the original framing and must be stated as such:

| Surviving claim | Why A10 does not take it |
|-----------------|--------------------------|
| The ladder applied to **training** environments, not evaluation benchmarks | A10's object is a benchmark construction pipeline whose output is an evaluation suite; the RL training loop is out of scope |
| **UED / adaptive generation as its own rung** between procedural and foundation-model generation | A10's ladder has no adaptive-curriculum rung at all, and no survey of UED exists (section 3.0) |
| Coverage **across** embodied AI, classical control, games and LLM-agent environments in one table | A10 is embodied-only; A2 is LLM-agent-only; neither crosses |
| **`INF` as a rung property** (throughput, vectorisation, Environment-as-a-Service) | A10 does not carry it. `INF` is filled elsewhere (A11, C1-C5, C19, F1, F2), but always as a simulator-selection topic, never as a consequence of where an environment sits on the automation ladder. No survey of the Gym / Gymnasium / RLlib / Stable-Baselines ecosystem exists at all. |
| **Domain gyms placed on the ladder** | Tier F's 14 domain surveys are `.` on `GEN` and `.` on `UED` without exception (section 3.2) |

Recommendation: do not pitch this survey on the automation axis alone. Either pitch it on the
UED-rung gap plus cross-domain span, or reframe the contribution entirely. The parent should
treat this as a material change to the Phase 1 result.

The defensible novelty is therefore the **conjunction**, not the bare axis:
one ordered automation ladder that (a) spans classical RL, robotics and LLM-agent
environments in the same table, (b) carries execution infrastructure (`INF`) as a property of
each rung rather than a separate topic, (c) places domain-specific gyms (`DOM`) on the same
ladder, and (d) treats environments as artifacts to be evaluated (`EVL`). No verified survey
covers `INF`, `DOM` and `EVL` together, and only A2 covers even two of them.

## 4. Verification notes and caveats

| Item | Caveat |
|------|--------|
| A3 | Crossref metadata fully verified (Liu, Xiong, Yang, Shen; Array vol. 30, art. 100812, 2026). Full text sits behind an Elsevier 403 for automated fetch, and the linkinghub redirect returns only a stub. The reported environment-design dimensions (simulator type, fidelity level, randomisation strategy, learning paradigm, degree of human involvement, safety constraints) come from indexed abstract summaries, **not** from a page read. Treat as reported-not-read. |
| A5, B1, B2, D7 | Not surveys. A5 is a position paper; B1 and B2 are PhD theses whose related-work chapters function as surveys of UED/PCG; D7 is a reproducibility study. Retained because they are the closest survey-grade coverage of specific rungs. |
| B9 vs A8 | Both resolve under JAIR DOIs (10.1613/jair.1.14174 for Kirk, 10.1613/jair.1.13596 for Parker-Holder, and JAIR 79 for Mohan). Do not conflate the records when citing. |
| B10 | Quality-diversity diversifies *solutions*, not *environments*. Retained only to close the open-endedness query shape; almost every environment dimension is legitimately absent. |
| B6, B7, B8 | Games-PCG lineage rather than RL-environment surveys. Retained because they are the canonical prior art for the auto-generation rung. |
| C16 | Casper et al. is recorded conservatively as an arXiv preprint: the arXiv abstract page carries no journal reference, despite the paper commonly being cited as TMLR. |
| D6 | Crossref gives IEEE TNNLS 35:10237-10257, 2024. Some secondary sources list 2023; the Crossref record is authoritative here. |
| D12 | The abstract page evidences an RL-for-robotics task taxonomy but not a simulator or environment catalogue section, so its `CAT` mark is conservative. |
| Provenance | Tier A, B and most of Tier D were fetched and verified directly in this session. Tier C and the Tier D general-RL entries came from a delegated sweep. **28 DOIs across all tiers were then independently re-resolved through the Crossref REST API; all 28 matched on title, first author and venue.** That pass also corrected five records: Arulkumaran's journal title differs from the arXiv title; Dimmig's journal version is 2025 IEEE RAM 32:153-166 not 2023; Prudencio is 2024 TNNLS 35:10237-10257 not 2023; Kaur is AI Review 56:3711-3753; Osborne is TACL 10:873-887. |
| No standalone survey found | (a) reward *shaping* - no survey/review/overview-titled paper covers shaping itself; closest are C14, C17, C15, C16. (b) domain *randomisation* - none other than C11, which is that survey under a different title. Both absences are findings, not scan failures. |
| UED method-paper ids in 3.0 | The seven primary-method arXiv ids cited in section 3.0 as evidence that "environment design" titles are all method papers were each fetched and confirmed on their arXiv abstract page: 2012.02096 = Dennis, "Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design" (PAIRED); 2110.02439 = Jiang, "Replay-Guided Adversarial Environment Design"; 2203.01302 = Parker-Holder, "Evolving Curricula with Regret-Based Environment Design" (ACCEL); 2303.03376 = Samvelyan, "MAESTRO: Open-Ended Environment Design for Multi-Agent Reinforcement Learning"; 2402.03479 = Garcin, "DRED: Zero-Shot Transfer in Reinforcement Learning via Data-Regularised Environment Design"; 2506.19997 = Cho, "TRACED: Transition-aware Regret Approximation with Co-learnability for Environment Design"; 2605.01358 = Yuan, "PACE: Parameter Change for Unsupervised Environment Design". None is a survey. |
| Domain-gym probe result | A dedicated Crossref sweep across energy, EDA, medical, HVAC, traffic and industrial phrasings returned almost entirely *environments* (Microgrid Resilience Gym, GreenLight-Gym, Gym-ANM, gym-DSSAT and similar) and *method* reviews, not environment catalogues. Only D19 surfaced as a domain survey, and it treats the toolchain as given. This is direct evidence for the `DOM` x `GEN` empty pair: the domain literatures ship environments and review algorithms, but nobody catalogues those environments as designed artifacts. |
| Independent discovery cross-check | After the primary sweeps, a separate OpenAlex API pass was run over five environment-survey queries. It surfaced exactly one addition not already held (D18, Shao 2019) and otherwise returned only records already in this table or off-topic ML surveys. **No competitor to the automation axis was found by that independent channel**, which raises but does not prove confidence in the gap. |

## 5. Recommended Phase 1b top-up

| Action | Reason |
|--------|--------|
| Obtain A3 full text and read its environment-design dimension list verbatim | Decides whether "degree of human involvement" is a competing spine or a one-line dimension. This single check gates the whole novelty claim. |
| Re-run the free-text sweeps once the WebSearch quota resets | Crossref and arXiv-abs verification is exact-match and under-recalls survey-shaped titles |
| Sweep specifically for: "environment engineering" survey, "gym" survey, "benchmark design" survey, "simulation fidelity" survey, RLVR / verifier-environment surveys, "environment scaling" survey | These phrasings were not reachable within the exhausted quota and are where a 2026 scoop would most plausibly sit |
| Sweep for a dedicated Environment-as-a-Service / RL environment marketplace survey | A2 names it as a future direction; a dedicated survey would take the `INF` rung |
| Sweep the domain-gym literatures directly (energy, EDA, agriculture, medical) for review articles that catalogue *environments* rather than *methods* | `DOM` is currently marked from a thin evidence base; a domain-side environments review would weaken the `DOM` x `GEN` empty pair |

## A3/A2/A1 full-text verification

Phase 1b top-up, executed to close the "reported-not-read" caveat on A3 and to read A2 and A1
in full rather than from abstracts. The headline result is that **the single largest threat
recorded in section 3.3 does not survive verification**: the "degree of human involvement"
dimension attributed to A3 is not present in any evidence channel that could be reached, and
two independent channels positively contradict it. Offsetting that, **A2 turns out to cover
UED directly**, which was missed at abstract level and which erodes one of the four surviving
claims in section 3.3.

### 0. Evidence channels used, and what each returned

| Channel | A3 (Array) | A2 (2606.12191) | A1 (2603.23964) |
|---------|-----------|-----------------|-----------------|
| Crossref REST record | Retrieved: title, 4 authors, vol. 30, art. 100812, 139 references, CC-BY, online 8 Apr 2026, issue July 2026 | n/a | n/a |
| Crossref reference list (139 titles) | **Retrieved in full and keyword-scanned** | n/a | n/a |
| OpenAlex `abstract_inverted_index`, reconstructed locally | **Retrieved: verbatim publisher abstract** | n/a | n/a |
| arXiv HTML body, downloaded and keyword-scanned locally | n/a | **Retrieved, 401,884 chars of text** | **Retrieved, 211,933 chars of text** |
| ScienceDirect HTML | HTTP 403 (WAF block page, 1.21 MB, no article text) | n/a | n/a |
| ScienceDirect `pdfft` endpoint | HTTP 403 | n/a | n/a |
| `ars.els-cdn.com` PDF | HTTP 403 | n/a | n/a |
| Elsevier TDM API (`api.elsevier.com`) | Rejected, no institutional key | n/a | n/a |
| `r.jina.ai` reader proxy | HTTP 401, network reputation block | n/a | n/a |
| Unpaywall / CORE / DOAJ / Europe PMC / OpenAIRE / fatcat / colab.ws | **No repository copy anywhere.** Unpaywall reports gold OA with `any_repository_has_fulltext: false` and the publisher page as the only location; DOAJ 0 hits; Europe PMC 0 hits | n/a | n/a |
| Browser automation | Not attempted (the browser tool requires an interactive user confirmation that a subagent cannot issue) | n/a | n/a |

**Honest statement of the A3 limit.** The A3 body text could not be read. Every automated route
to Elsevier is blocked and no mirror exists. What was obtained instead is the **verbatim
publisher abstract** and the **complete 139-item reference list**, which are two independent,
authoritative, non-derived channels. The verdict below rests on those two, not on a body read.

### 1. A3 - Liu et al. 2026, Array 30:100812

#### 1a. Bibliographic record, verified

| Field | Verified value |
|-------|----------------|
| Exact title | A review of reinforcement learning: A tripartite framework of environment design, algorithmic innovation, and application scenarios |
| Authors | Yingli Liu; Zheng Xiong; Ling Yang (corresponding); Tao Shen |
| Year / venue | 2026, *Array* (Elsevier), vol. 30, article 100812, ISSN 2590-0056 |
| DOI | 10.1016/j.array.2026.100812 - **verified, not assumed** |
| PII | S2590005626001359 |
| Dates | Published online 8 April 2026; issue dated July 2026 |
| Access | Gold OA, CC BY 4.0, but publisher-only; no repository copy |
| Reference count | 139 |
| Funder | Major Science and Technology Projects in Yunnan Province, 202302AG050009 |

The prior record in section 1 (Tier A, row A3) is **correct in every field**. Nothing needs
amending there.

#### 1b. Does "degree of human involvement" appear? No evidence for it; positive evidence against

| Test | Result |
|------|--------|
| Environment-design dimensions named in the **verbatim publisher abstract** | feature distribution; reward mechanism; dynamic uncertainty; scalability. Their stated effect is on "learning stability and generalisation ability". That is **four** dimensions, and the axis of interest is not among them. |
| Does the abstract contain "human involvement", "human-in-the-loop", "manual", "automation", "handcrafted", or "procedural"? | **No.** None of these strings appears. |
| Previously reported dimension set (simulator type, fidelity level, randomisation strategy, learning paradigm, degree of human involvement, safety constraints) | **Not corroborated by any channel.** None of "simulator", "fidelity", "randomisation", "human involvement" or "safety constraints" appears in the verbatim abstract. This list appears to have originated from an indexed secondary summary and should be treated as unreliable. |
| 139-item reference list, scanned for the environment-design-automation literature | "unsupervised environment design" 0; PAIRED 0; prioritised level replay 0; ACCEL 0; minimax regret 0; procedural / PCG 0; domain randomisation 0; "environment design" 0; "human involvement" 0; world model 0; LLM / large language model 0. |
| What the 139 references actually are | Classical algorithm papers (TD, Q-learning, DQN, Rainbow, REINFORCE, PPO, TRPO, DDPG, TD3, A3C, MAML) plus a very long applications tail: first-person-shooter game RL (~12 refs), robot navigation, energy and smart grid (CityLearn, PowerGym, grid topology control), industrial process control, and a very heavy medical block (epilepsy, diabetes, cancer chemotherapy, de novo drug design, ~45 refs). |

#### 1c. Coverage against our eight dimensions

| Dimension | A3 verdict | Basis |
|-----------|-----------|-------|
| `CAT` environment catalogue | `~` | CARLA, MetaDrive, CityLearn, PowerGym and VizDoom appear as cited application platforms, not as a catalogue |
| `DES` environment design methods | `~` | "Environment design" in A3 means **MDP formulation properties for deployment** (feature distribution, reward mechanism, dynamic uncertainty, scalability), not how the environment artifact is constructed |
| `GEN` auto-generation / PCG | `.` | 0 references on PCG, procedural generation or generative environments |
| `UED` automatic curriculum | `.` | 0 references on UED; the single "curriculum" reference is an application paper on grid topology controllers |
| `INF` execution infrastructure | `.` | No evidence in abstract or references |
| `DOM` domain-specific gyms | `Y` | Energy and smart grids, industrial process control, healthcare, autonomous driving and AI assistants are named application dimensions with dedicated reference blocks |
| `EVL` evaluation OF environments | `.` | Evaluation metrics are for *agents in* applications, not for environments as artifacts |
| `LLM` LLM-generated environments | `~` | LLM integration is listed as a future solution direction only |

This revises the section 2a marks for A3 from `~ Y ~ ~ . ~ . .` to `~ ~ . . . Y . ~`.

#### 1d. Verdict

| Question | Answer |
|----------|--------|
| Is environment design a top-level axis? | **Yes.** It is the first leg of a three-leg framework: environment design, algorithmic innovation, application scenarios. |
| Is "degree of human involvement" one of its dimensions? | **No evidence, and two channels contradict it.** |
| Is the automation ladder its organising spine? | **No.** The organising spine is the three-way interaction between environment formulation, algorithm choice and deployment constraint. Within the environment leg the sub-axes are MDP-formulation properties. |
| What population does it classify? | Not a population of environments at all. It is an **engineering-deployment review of RL itself**, organised by application field. |
| Does it cover UED? | No. | 
| Does it cover infrastructure? | No. |
| Does it cover domain gyms? | Yes, as application fields - this is its strongest overlap with us. |
| Does it cover environment evaluation? | No. |
| **VERDICT** | **DISTINCT.** A3 shares a word ("environment design") and a domain span, not an axis. |

**Residual risk.** Low but non-zero. If the unread body contains a table of environment-design
dimensions richer than the abstract's four, and if that table happens to include a
human-involvement axis, the assessment would change. Given that 0 of 139 references touch the
environment-design-automation literature, a substantive treatment of that axis is close to
impossible: a review cannot organise around an axis it cites nothing for. Recommended residual
action is a single manual open of the PDF in a browser to confirm, but this should **no longer
be treated as gating the novelty claim**.

### 2. A2 - Li et al. 2026, arXiv:2606.12191

#### 2a. Record, verified

| Field | Verified value |
|-------|----------------|
| Exact title | Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application |
| First author | Jiachun Li (15 authors; Kang Liu and Jun Zhao last) |
| Submitted | 10 June 2026; 63 pages, 10 figures |
| Structure | 8 sections: Introduction, Preliminaries, Environment Attribute, Environment Domain, Environment Synthesis, Agent Evolution, Environment Evolution, Challenges and Future Directions |
| Self-declared positioning | Organised around the environment **lifecycle** (modelling, construction, evaluation, application), explicitly contrasted against prior agent-centric surveys |

#### 2b. Correction to the existing record - A2 DOES cover UED

The section 3.3 row for A2 says its scope is "LLM-agent environments only: no robotics,
control, games or domain gyms", and section 2a marks its `UED` cell `~`. **Both are wrong.**
Body-text evidence:

| Finding | Evidence from the downloaded body text |
|---------|----------------------------------------|
| UED is named and explained | "unsupervised environment design" appears 4 times, twice in running prose in section VII-B |
| The canonical UED methods are all present and tabulated | A table under "Difficulty-Driven Evolution (section VII-B)" carries rows for POET, PAIRED, DCD, ACCEL, MAESTRO and ReMiDi, each tagged with signal type (Explicit / Implicit), domain, observation type and signal (Regret) |
| Regret is treated as the mechanism | PAIRED is described as using regret between antagonist and protagonist returns to steer an adversarial environment generator; ACCEL as editing and preserving high-value levels by regret-style signals to avoid curriculum collapse |
| The domains tagged are not LLM-only | The UED table rows carry domains "Game", "Robotics" and "Embodied" |
| "curriculum" appears 34 times | Two dedicated subsections: VII-B1 Explicit Curriculum Signals, VII-B2 Implicit Curriculum Mechanisms |

So A2's `UED` mark should be **`Y`, not `~`**, and A2's game/robotics/embodied coverage is real
(embodied 90 mentions, game 165, robotic 13, simulator 17), delivered through sections IV-C
Embodied and IV-D Game.

#### 2c. What A2 still does not do

| Test | Result |
|------|--------|
| Is the spine a degree-of-automation ladder? | **No.** The spine is a lifecycle. The synthesis chapter splits on **Symbolic vs Neural**, a paradigm dichotomy. Within symbolic synthesis the sub-split is Task-Driven / Real-World-Driven / De Novo, and A2 states this is by "the source of synthesis logic and the degree of design freedom". *Degree of design freedom* is the nearest phrase in any surveyed work to our axis, but it partitions three synthesis techniques, not an ordered ladder, and it never reaches a handcrafted or configurable rung. |
| Does "degree of automation", "automation level", "level of automation", "handcrafted" or "human involvement" appear? | **0 occurrences of every one of them.** "hand-crafted" 1, "manually designed" 2, all in passing. |
| Classical RL / continuous control? | **No.** MuJoCo 0, Brax 0, Isaac 0, JAX 0, ProcGen 0, "procedural content generation" 0, "procedurally generated" 0, "classical control" 0, "continuous control" 1. Gymnasium 2, OpenAI Gym 3, MiniGrid 2, all in passing. |
| Domain-specific gyms (energy, agriculture, medical, EDA)? | **No.** CityLearn 0, gym-ANM 0, Grid2Op 0, "power grid" 0, HVAC 0, agriculture 0, crop 0, EDA 0, VerilogEval 0. Its section IV-G "Domain-Specific" is LLM-agent verticals: Biomedical and Healthcare, Science and Technology, Finance and Investment. |
| Execution infrastructure as a surveyed rung? | **No, it is a future direction.** Environment-as-a-Service appears 5 times, all inside section VIII-A "Challenges and Future Directions", where A2 *advocates* EaaS as a proposal for standardised, cloud-hosted, unified-API environments. EnvPool 0, throughput 0, "vectorised" 0 (the 2 "vectoriz" hits are the title of a diffusion paper). |
| Environment evaluation as an artifact? | **Yes, genuinely.** Section V-C "Quality Control and Evaluation of Environments" with four named criteria: Correctness, Diversity, Complexity, Fidelity. |

#### 2d. Verdict

| Question | Answer |
|----------|--------|
| Is the scope LLM-agent environments only? | **Not exactly.** The *frame* is LLM agents, but the coverage reaches games, robotics and embodied tasks, and it does cover UED. It does **not** reach classical control, procedural-generation-for-RL, or domain gyms. |
| Does it touch UED? | **Yes, materially.** This is a correction to the prior record. |
| Does it use an automation ladder? | No. Lifecycle spine; symbolic/neural dichotomy for synthesis. |
| **VERDICT** | **ADJACENT, and it is now the closest of the three.** It occupies environment synthesis + environment evaluation + UED in one document, and names EaaS. What it does not do is order those into a ladder, cross into classical RL and domain gyms, or treat infrastructure as anything but a future proposal. |

### 3. A1 - Luo et al. 2026, arXiv:2603.23964

#### 3a. Record, verified

| Field | Verified value |
|-------|----------------|
| Exact title | From Pixels to Digital Agents: An Empirical Study on the Taxonomy and Technological Trends of Reinforcement Learning Environments |
| Authors | Lijing Luo; Yiben Luo; Alexey Gorbatovski; Sergey Kovalchuk; Xiaodan Liang |
| Dates | v1 25 March 2026; v2 13 April 2026 |
| Extent | 32 pages main text, 18 figures, plus appendices A-C on data collection, annotation protocol and raw data |

#### 3b. What it actually classifies by

A1 states its dimensions explicitly in the opening of section 4: multi-modal span, application
domains, agent capabilities, observability (information completeness), action space, reward
formulation, and agent population. Seven dimensions.

| Candidate axis | Present in A1? |
|----------------|----------------|
| Application domain | **Yes**, section 4.5, six domain groups |
| Cognitive / agent capability | **Yes**, section 4.3, eight capability classes |
| Observability, action space, reward formulation, modality, agent population | **Yes**, sections 4.1-4.4, 2.5-2.6 |
| Bibliometric / chronological | **Yes**, section 5 is an era-by-era trajectory (2015-2017, 2017-2022, 2022-2023, 2024-present) |
| **Degree of design automation** | **No.** "design automation" 0; "degree of automation" 0; "automation level" 0; "level of automation" 0; "human involvement" 0; "handcrafted" 0; "automatically generated" 0; "LLM-generated" 0. "environment design" occurs 3 times, all rhetorical (an evolutionary trajectory of environment design; a shift in reward architecture; a note that the lexicon of environment design changed with LLMs) |

So **design automation is neither an axis nor even a named trend in A1**. This is a slight
strengthening of the prior record, which said automation was "a trend it observes". It is
observed only in the weaker sense that the catalogue's chronological grouping labels one era
"Procedural Generation, Meta-Learning and Embodied AI (2018-2022)" and another "Standardized
Suites and Hardware Acceleration (2020-2023)".

#### 3c. Coverage checks

| Test | Result |
|------|--------|
| UED | **Absent.** "unsupervised environment design" 0, PAIRED 0, MAESTRO 0, "minimax regret" 0, "prioritised/prioritized level replay" 0. The 14 "accel" substring hits are all *accelerate/acceleration*, none is the ACCEL method. |
| PCG | Present **as catalogue rows only**: ProcGen 6, MiniGrid 4, "procedurally generated" 8, domain randomisation 2. No PCG method taxonomy. |
| Infrastructure | **Catalogue labels, not analysis.** Brax 8, Isaac 5, JAX 4, MuJoCo 15 appear as table entries under an era heading naming hardware acceleration; throughput 0, EnvPool 0, Gymnasium 0, "Environment-as-a-Service" 0. |
| Environment evaluation as artifact | **Absent.** "evaluation of environments" 0, "benchmark quality" 0. "reproducib*" 4, raised as a field-level concern, never developed into criteria. |
| Domain gyms | **Present as catalogue rows.** CityLearn 2 (energy), "smart grid" 1, sepsis 3 and Med-PaLM 4 (medical), VerilogEval 5 (hardware/EDA-adjacent), Geneformer 4 (bio), finance 5. Agriculture 0, crop 0, HVAC 0, SUMO 0. |

#### 3d. Verdict

| Question | Answer |
|----------|--------|
| What is it classified by? | Seven agent- and task-facing dimensions plus a chronological trajectory. A large-scale empirical/bibliometric taxonomy. |
| Is design automation the axis? | **No, and it is not even an observed trend by name.** |
| **VERDICT** | **DISTINCT.** A1 owns the catalogue and the bibliometrics. It does not compete for the automation axis, and it is the weakest of the three threats. |

### 4. Negative result re-confirmed: no dedicated UED survey exists

Re-run this session on a corrected arXiv API query (the first attempt used a malformed
`search_query` and silently returned 0 for everything; it was caught by two positive controls
before any result was recorded).

| Query | Total results | Survey-shaped titles |
|-------|--------------|----------------------|
| *positive control* `all:"unsupervised environment design"` | 38 | - (control returned the expected UED method papers) |
| *positive control* `ti:"survey" AND ti:"reinforcement"` | 204 | - (control returned the expected RL surveys) |
| `all:"unsupervised environment design"` | 38 | **0** |
| `all:"environment design" AND cat:cs.LG` | 116 | **0** |
| `all:"environment design" AND cat:cs.AI` | 124 | **0** |
| `all:"adversarial environment design"` | 3 | **0** |
| `all:"level replay" AND all:"reinforcement learning"` | 7 | **0** |
| `abs:"unsupervised environment design" AND (ti:survey OR ti:review OR ti:taxonomy OR ti:overview)` | 0 | **0** |
| `all:"autocurricula" AND (ti:survey OR ti:review)` | 0 | **0** |
| `ti:"open-endedness" AND (ti:survey OR ti:review)` | 0 | **0** |
| `ti:"environment generation" AND (ti:survey OR ti:review)` | 1 | 1, but it is **AI-powered Contextual 3D Environment Generation: A Systematic Review** (arXiv:2506.05449), which is 3D scene/graphics generation, not RL UED |
| Crossref `query.bibliographic`, top 100 | very noisy | 0 relevant; the only near-title is *Unsupervised Representation Learning in Deep RL: A Review*, a different subject |

**Answer: NO. No dedicated survey or review of unsupervised environment design exists.** Across
240 arXiv papers in cs.LG and cs.AI containing the phrase "environment design", not one carries
a survey-shaped title. The closest review-grade coverage remains B1 (Jiang's PhD dissertation)
and, as newly established above, **section VII-B of A2**.

| Caveat | Detail |
|--------|--------|
| Channel count this session | arXiv API (primary, multiple query shapes with positive controls) and Crossref. **OpenAlex returned HTTP 429 with a ~19 h Retry-After and could not be re-run**; Semantic Scholar and DBLP were also rate-limited or connection-reset. The prior session's independent OpenAlex title search and web search already returned the same negative, so the finding rests on three channels across two sessions, but only two were live this session. |
| Strength | The negative is strong for **title-level** survey detection. It cannot exclude a UED review chapter inside a book or a non-arXiv journal review that avoids the phrase entirely. |

### 5. Net effect on the section 3.3 novelty claim

| Section 3.3 element | Status after this verification |
|--------------------|-------------------------------|
| "A3 is the single largest threat" | **Withdrawn.** A3 is DISTINCT. The "degree of human involvement" dimension is unsupported by the verbatim abstract and contradicted by a 139-item reference list containing zero environment-design-automation citations. |
| "A2 scope is LLM-agent only, no robotics/games" | **Corrected.** A2 covers games, robotics and embodied tasks, and covers UED with a tabulated method comparison. |
| Surviving claim: "UED as its own rung, since no UED survey exists" | **Weakened but not lost.** No dedicated UED survey exists (re-confirmed on a corrected query). However A2 now demonstrably tabulates POET/PAIRED/DCD/ACCEL/MAESTRO/ReMiDi under difficulty-driven environment evolution, so we can no longer claim UED is untouched by any survey. The defensible form is "no survey places UED as a rung on an ordered automation ladder", not "no survey covers UED". |
| Surviving claim: cross-domain span in one table | **Strengthened.** Verified by exclusion: A1 has domain gyms but no automation axis and no UED; A2 has UED and synthesis but zero energy/agriculture/EDA gyms and zero classical control; A3 has domain breadth but no generation, no UED and no infrastructure. **No single work holds both ends.** |
| Surviving claim: `INF` as a rung property | **Strengthened.** Verified as empty in all three: throughput 0 in both A1 and A2; EnvPool 0 in both; A2's EaaS is confined to its future-work section; A1's hardware-acceleration content is catalogue labels. |
| Surviving claim: `EVL` environments as artifacts | **Held, narrowly, and contested by A2 not A3.** A2 section V-C names Correctness, Diversity, Complexity, Fidelity for *synthesised* environments. A1 and A3 have nothing. The residual space is evaluation of *given, non-synthesised* environments: difficulty calibration, reward-specification soundness, reusability. |
| A10 (Lai et al., arXiv:2606.12207) | **Untouched by this pass and still the primary threat to the bare axis.** Section 3.3's conclusion that the axis is occupied by A10 stands; nothing here reverses it. The re-ranking is only among A1/A2/A3. |

**Revised threat ranking:** A10 > A2 > A1 > A3. A3 drops from first to last.
