# Canonical RL environments MISSED by the literal "rl environment" Scholar search

Landmark environments, suites, simulators and environment-design systems that the
Google Scholar keyword harvest in `google_scholar.md` did **not** surface, because
almost none of them put the literal phrase "RL environment" in their title.

Method and guarantees:

- Every row was verified against a fetched primary page: arXiv `/abs/` HTML, PMLR
  proceedings pages, NeurIPS proceedings, IEEE/Crossref DOI records, DBLP, OpenReview,
  Zenodo, or the project's own repository citation file.
- Nothing here is recalled from memory. Anything that could not be verified was dropped
  rather than guessed.
- Deduplicated by arXiv id. Cross-checked against the 39 arXiv ids already recorded in
  `slice_01.md` - `slice_04.md`: **zero collisions**, so this file is purely additive.
- Overlap with `google_scholar.md`: **zero**. A grep for ten of these names over all 637
  lines of the Scholar harvest returns only one hit, and that hit is a false positive
  ("smac" inside the surname "Glasmachers"). The literal-phrase search missed the entire
  canonical corpus.

Rung vocabulary:

| rung | meaning |
|------|---------|
| `handcrafted` | fixed, hand-authored tasks, levels or scenes; the env does not change |
| `configurable` | parameterised by a human through an API, DSL or scene description language |
| `auto-shaped` | instances produced by procedural generation, search, or automated mining |
| `llm-generated` | a foundation / generative model writes the tasks, assets or worlds |
| `co-adaptive` | UED, curriculum or teacher loop that adapts the env to the current agent |

## Summary table

| # | Name | Title | 1st author | Year | Venue | arXiv/DOI | domain | rung |
|---|------|-------|-----------|------|-------|-----------|--------|------|
| 1 | ALE | The Arcade Learning Environment: An Evaluation Platform for General Agents | M. G. Bellemare | 2013 | J. Artificial Intelligence Research 47:253-279 | arXiv:1207.4708; 10.1613/jair.3912 | games (Atari) | handcrafted |
| 2 | OpenAI Gym | OpenAI Gym | G. Brockman | 2016 | arXiv preprint (CoRR, no refereed venue) | arXiv:1606.01540 | general RL infra | configurable |
| 3 | Procgen | Leveraging Procedural Generation to Benchmark Reinforcement Learning | K. Cobbe | 2020 | ICML 2020, PMLR 119:2048-2056 | arXiv:1912.01588 | games (2D procedural) | auto-shaped |
| 4 | MineRL | MineRL: A Large-Scale Dataset of Minecraft Demonstrations | W. H. Guss | 2019 | IJCAI 2019 | arXiv:1907.13440 | games (Minecraft) | auto-shaped |
| 5 | Craftax | Craftax: A Lightning-Fast Benchmark for Open-Ended Reinforcement Learning | M. Matthews | 2024 | ICML 2024, PMLR 235:35104-35137 | arXiv:2402.16801 | games (open-ended) | auto-shaped |
| 6 | Crafter | Benchmarking the Spectrum of Agent Capabilities | D. Hafner | 2022 | ICLR 2022 (poster) | arXiv:2109.06780 | games (survival) | auto-shaped |
| 7 | XLand-MiniGrid | XLand-MiniGrid: Scalable Meta-Reinforcement Learning Environments in JAX | A. Nikulin | 2024 | NeurIPS 2024 Datasets and Benchmarks | arXiv:2312.12044 | games / meta-RL | auto-shaped |
| 8 | XLand | Open-Ended Learning Leads to Generally Capable Agents | Open Ended Learning Team (first named: A. Stooke) | 2021 | arXiv preprint (no refereed venue) | arXiv:2107.12808 | games (3D open-ended) | co-adaptive |
| 9 | Melting Pot | Scalable Evaluation of Multi-Agent Reinforcement Learning with Melting Pot | J. Z. Leibo | 2021 | ICML 2021, PMLR 139:6187-6199 | arXiv:2107.06857 | multi-agent (social) | handcrafted |
| 10 | Obstacle Tower | Obstacle Tower: A Generalization Challenge in Vision, Control, and Planning | A. Juliani | 2019 | IJCAI 2019 | arXiv:1902.01378 | games (3D procedural) | auto-shaped |
| 11 | Griddly | Griddly: A platform for AI research in games | C. Bamford | 2021 | Software Impacts | arXiv:2011.06363; 10.1016/j.simpa.2021.100066 | games (grid-world infra) | configurable |
| 12 | Jumanji | Jumanji: a Diverse Suite of Scalable Reinforcement Learning Environments in JAX | C. Bonnet | 2024 | ICLR 2024 | arXiv:2306.09884 | combinatorial / general RL | configurable |
| 13 | MiniHack | MiniHack the Planet: A Sandbox for Open-Ended Reinforcement Learning Research | M. Samvelyan | 2021 | NeurIPS 2021 Datasets and Benchmarks | arXiv:2109.13202 | games (NetHack sandbox) | configurable |
| 14 | Gym Retro | Gotta Learn Fast: A New Benchmark for Generalization in RL | A. Nichol | 2018 | arXiv preprint (OpenAI tech report) | arXiv:1804.03720 | games (retro consoles) | handcrafted |
| 15 | MuJoCo | MuJoCo: A physics engine for model-based control | E. Todorov | 2012 | IEEE/RSJ IROS 2012, pp. 5026-5033 | 10.1109/IROS.2012.6386109 (no arXiv) | control / physics engine | configurable |
| 16 | DM Control Suite | DeepMind Control Suite | Y. Tassa | 2018 | arXiv preprint (CoRR, DeepMind tech report) | arXiv:1801.00690 | continuous control | handcrafted |
| 17 | dm_control | dm_control: Software and Tasks for Continuous Control | Y. Tassa | 2020 | Software Impacts | arXiv:2006.12983; 10.1016/j.simpa.2020.100022 | continuous control infra | configurable |
| 18 | Brax | Brax - A Differentiable Physics Engine for Large Scale Rigid Body Simulation | C. D. Freeman | 2021 | NeurIPS 2021 Datasets and Benchmarks | arXiv:2106.13281 | control / differentiable physics | configurable |
| 19 | Isaac Gym | Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning | V. Makoviychuk | 2021 | NeurIPS 2021 Datasets and Benchmarks | arXiv:2108.10470 | robotics (GPU sim) | configurable |
| 20 | Orbit | Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments | M. Mittal | 2023 | IEEE Robotics and Automation Letters 8(6) | arXiv:2301.04195; 10.1109/LRA.2023.3270034 | robotics (sim framework) | configurable |
| 21 | Isaac Lab | Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning | M. Mittal (NVIDIA) | 2025 | arXiv preprint (no refereed venue found) | arXiv:2511.04831 | robotics (GPU sim) | configurable |
| 22 | MuJoCo Playground | MuJoCo Playground | K. Zakka | 2025 | arXiv preprint (no refereed venue found) | arXiv:2502.08844 | robotics (MJX sim-to-real) | configurable |
| 23 | MyoSuite | MyoSuite: A Contact-rich Simulation Suite for Musculoskeletal Motor Control | V. Caggiano | 2022 | L4DC 2022, PMLR 168:492-507 | arXiv:2205.13600 | musculoskeletal control | handcrafted |
| 24 | Safety-Gymnasium | Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark | J. Ji | 2023 | NeurIPS 2023 Datasets and Benchmarks | arXiv:2310.12567 | safe RL | configurable |
| 25 | Meta-World | Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning | T. Yu | 2019 | CoRL 2019, PMLR 100:1094-1100 | arXiv:1910.10897 | manipulation (multi-task) | handcrafted |
| 26 | RLBench | RLBench: The Robot Learning Benchmark & Learning Environment | S. James | 2020 | IEEE Robotics and Automation Letters | arXiv:1909.12271; 10.1109/LRA.2020.2974707 | manipulation | configurable |
| 27 | robosuite | robosuite: A Modular Simulation Framework and Benchmark for Robot Learning | Y. Zhu | 2020 | arXiv preprint (CoRR, no refereed venue) | arXiv:2009.12293 | manipulation | configurable |
| 28 | ManiSkill2 | ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills | J. Gu | 2023 | ICLR 2023 | arXiv:2302.04659 | manipulation | configurable |
| 29 | ManiSkill3 | ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI | S. Tao | 2025 | RSS 2025 (author-asserted; not proceedings-confirmed) | arXiv:2410.00425 | manipulation / embodied | configurable |
| 30 | CALVIN | CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks | O. Mees | 2022 | IEEE Robotics and Automation Letters 7(3):7327-7334 | arXiv:2112.03227; 10.1109/LRA.2022.3180108 | manipulation (language) | handcrafted |
| 31 | LIBERO | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | B. Liu | 2023 | NeurIPS 2023 Datasets and Benchmarks | arXiv:2306.03310 | manipulation (lifelong) | configurable |
| 32 | RoboCasa | RoboCasa: Large-Scale Simulation of Household Tasks for Generalist Robots | S. Nasiriany | 2024 | Robotics: Science and Systems (RSS) XX, paper 050 | arXiv:2406.02523; 10.15607/RSS.2024.XX.050 | manipulation (household) | llm-generated |
| 33 | Habitat | Habitat: A Platform for Embodied AI Research | M. Savva | 2019 | ICCV 2019 | arXiv:1904.01201 | embodied navigation | configurable |
| 34 | Habitat 2.0 | Habitat 2.0: Training Home Assistants to Rearrange their Habitat | A. Szot | 2021 | NeurIPS 2021 (main track) | arXiv:2106.14405 | embodied rearrangement | configurable |
| 35 | AI2-THOR | AI2-THOR: An Interactive 3D Environment for Visual AI | E. Kolve | 2017 | arXiv preprint (CoRR, no refereed venue) | arXiv:1712.05474 | embodied interaction | handcrafted |
| 36 | Gibson Env | Gibson Env: Real-World Perception for Embodied Agents | F. Xia | 2018 | CVPR 2018, pp. 9068-9079 | arXiv:1808.10654; 10.1109/CVPR.2018.00945 | embodied navigation | handcrafted |
| 37 | iGibson 1.0 | iGibson 1.0: a Simulation Environment for Interactive Tasks in Large Realistic Scenes | B. Shen | 2021 | IEEE/RSJ IROS 2021 | arXiv:2012.02924 | embodied interaction | handcrafted |
| 38 | iGibson 2.0 | iGibson 2.0: Object-Centric Simulation for Robot Learning of Everyday Household Tasks | C. Li | 2021 | CoRL 2021 | arXiv:2108.03272 | embodied household | configurable |
| 39 | BEHAVIOR-1K | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | C. Li | 2024 | arXiv preprint (preliminary version CoRL 2022) | arXiv:2403.09227 | embodied household | configurable |
| 40 | ALFRED | ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks | M. Shridhar | 2020 | CVPR 2020, pp. 10737-10746 | arXiv:1912.01734; 10.1109/CVPR42600.2020.01075 | embodied (language) | auto-shaped |
| 41 | ThreeDWorld | ThreeDWorld: A Platform for Interactive Multi-Modal Physical Simulation | C. Gan | 2021 | NeurIPS 2021 Datasets and Benchmarks | arXiv:2007.04954 | embodied / physical reasoning | configurable |
| 42 | PettingZoo | PettingZoo: Gym for Multi-Agent Reinforcement Learning | J. K. Terry | 2021 | NeurIPS 2021 (main track), vol. 34, pp. 15032-15043 | arXiv:2009.14471 | multi-agent infra | configurable |
| 43 | SMAC | The StarCraft Multi-Agent Challenge | M. Samvelyan | 2019 | AAMAS 2019 (extended abstract), pp. 2186-2188 | arXiv:1902.04043 | multi-agent (StarCraft II) | handcrafted |
| 44 | SMACv2 | SMACv2: An Improved Benchmark for Cooperative Multi-Agent Reinforcement Learning | B. Ellis | 2023 | NeurIPS 2023 Datasets and Benchmarks | arXiv:2212.07489 | multi-agent (StarCraft II) | auto-shaped |
| 45 | Neural MMO | Neural MMO: A Massively Multiagent Game Environment for Training and Evaluating Intelligent Agents | J. Suarez | 2019 | arXiv preprint (CoRR, no refereed venue) | arXiv:1903.00784 | multi-agent (persistent world) | auto-shaped |
| 46 | Neural MMO 2.0 | Neural MMO 2.0: A Massively Multi-task Addition to Massively Multi-agent Learning | J. Suarez | 2023 | NeurIPS 2023 Datasets and Benchmarks | arXiv:2311.03736 | multi-agent (multi-task) | configurable |
| 47 | GRF | Google Research Football: A Novel Reinforcement Learning Environment | K. Kurach | 2020 | AAAI 2020, vol. 34, pp. 4501-4510 | arXiv:1907.11180; 10.1609/aaai.v34i04.5878 | multi-agent (sports sim) | handcrafted |
| 48 | MAgent | MAgent: A Many-Agent Reinforcement Learning Platform for Artificial Collective Intelligence | L. Zheng | 2018 | AAAI 2018 (demo), vol. 32 | arXiv:1712.00600; 10.1609/aaai.v32i1.11371 | multi-agent (many-agent) | configurable |
| 49 | Hanabi Learning Env | The Hanabi Challenge: A New Frontier for AI Research | N. Bard | 2020 | Artificial Intelligence 280:103216 | arXiv:1902.00506; 10.1016/j.artint.2019.103216 | multi-agent (imperfect info) | handcrafted |
| 50 | Overcooked-AI | On the Utility of Learning about Humans for Human-AI Coordination | M. Carroll | 2019 | NeurIPS 2019 | arXiv:1910.05789 | multi-agent (human-AI) | handcrafted |
| 51 | OpenSpiel | OpenSpiel: A Framework for Reinforcement Learning in Games | M. Lanctot | 2019 | arXiv preprint (CoRR, no refereed venue) | arXiv:1908.09453 | games / multi-agent infra | configurable |
| 52 | D4RL | D4RL: Datasets for Deep Data-Driven Reinforcement Learning | J. Fu | 2020 | arXiv preprint (CoRR, no refereed venue) | arXiv:2004.07219 | offline RL data | handcrafted |
| 53 | RL Unplugged | RL Unplugged: A Suite of Benchmarks for Offline Reinforcement Learning | C. Gulcehre | 2020 | NeurIPS 2020, vol. 33, pp. 7248-7259 | arXiv:2006.13888 | offline RL data | handcrafted |
| 54 | Minari | Minari (Farama Foundation software record, v0.5.0) | O. G. Younis | 2024 | Zenodo software record (no paper exists) | 10.5281/zenodo.13767624 (concept DOI) | offline RL data infra | configurable |
| 55 | PCGRL | PCGRL: Procedural Content Generation via Reinforcement Learning | A. Khalifa | 2020 | AIIDE 2020, 16(1):95-101 | arXiv:2001.09212; 10.1609/aiide.v16i1.7416 | env design (game levels) | auto-shaped |
| 56 | POET | Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions | R. Wang | 2019 | arXiv preprint; refereed version GECCO 2019, pp. 142-151 | arXiv:1901.01753; 10.1145/3321707.3321799 | env design (open-ended) | co-adaptive |
| 57 | Enhanced POET | Enhanced POET: Open-Ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions | R. Wang | 2020 | ICML 2020, PMLR 119:9940-9951 | arXiv:2003.08536 | env design (open-ended) | co-adaptive |
| 58 | PAIRED | Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design | M. Dennis | 2020 | NeurIPS 2020, vol. 33, pp. 13049-13061 | arXiv:2012.02096 | env design (UED) | co-adaptive |
| 59 | PLR | Prioritized Level Replay | M. Jiang | 2021 | ICML 2021, PMLR 139:4940-4950 | arXiv:2010.03934 | env design (curriculum) | co-adaptive |
| 60 | Robust PLR | Replay-Guided Adversarial Environment Design | M. Jiang | 2021 | NeurIPS 2021 | arXiv:2110.02439 | env design (UED) | co-adaptive |
| 61 | ACCEL | Evolving Curricula with Regret-Based Environment Design | J. Parker-Holder | 2022 | ICML 2022, PMLR 162:17473-17498 | arXiv:2203.01302 | env design (UED) | co-adaptive |
| 62 | CoDE | Environment Generation for Zero-Shot Compositional Reinforcement Learning | I. Gur | 2021 | NeurIPS 2021, vol. 34 | arXiv:2201.08896 | env design (web tasks) | co-adaptive |
| 63 | OMNI | OMNI: Open-endedness via Models of human Notions of Interestingness | J. Zhang | 2024 | ICLR 2024 (poster) | arXiv:2306.01711 | env design (open-ended) | llm-generated |
| 64 | Genie | Genie: Generative Interactive Environments | J. Bruce | 2024 | ICML 2024, PMLR 235:4603-4623 | arXiv:2402.15391 | learned generative env | llm-generated |
| 65 | GenSim | GenSim: Generating Robotic Simulation Tasks via Large Language Models | L. Wang | 2024 | ICLR 2024 | arXiv:2310.01361 | env design (robotics tasks) | llm-generated |
| 66 | RoboGen | RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation | Y. Wang | 2024 | ICML 2024 | arXiv:2311.01455 | env design (robotics tasks) | llm-generated |
| 67 | Eurekaverse | Eurekaverse: Environment Curriculum Generation via Large Language Models | W. Liang | 2024 | CoRL 2024 | arXiv:2411.01775 | env design (locomotion curriculum) | co-adaptive |

| 68 | WebArena | WebArena: A Realistic Web Environment for Building Autonomous Agents | S. Zhou | 2024 | ICLR 2024 | arXiv:2307.13854 | LLM / agentic (web) | handcrafted |
| 69 | ALFWorld | ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | M. Shridhar | 2021 | ICLR 2021 | arXiv:2010.03768 | LLM / agentic (text + embodied) | auto-shaped |
| 70 | TextWorld | TextWorld: A Learning Environment for Text-based Games | M.-A. Cote | 2018 | Computer Games Workshop at IJCAI 2018; Springer CCIS | arXiv:1806.11532; 10.1007/978-3-030-24337-1_3 | LLM / agentic (text games) | auto-shaped |
| 71 | BALROG | BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games | D. Paglieri | 2025 | ICLR 2025 | arXiv:2411.13543 | LLM / agentic (games) | handcrafted |
| 72 | tau-bench | $\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | S. Yao | 2024 | arXiv preprint (no refereed venue indexed) | arXiv:2406.12045 | LLM / agentic (tool use) | handcrafted |
| 73 | SWE-bench | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | C. E. Jimenez | 2024 | ICLR 2024 | arXiv:2310.06770 | LLM / agentic (software) | auto-shaped |
| 74 | SWE-Gym | Training Software Engineering Agents and Verifiers with SWE-Gym | J. Pan | 2025 | ICML 2025 | arXiv:2412.21139 | LLM / agentic (software) | auto-shaped |
| 75 | WebShop | WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents | S. Yao | 2022 | NeurIPS 2022 | arXiv:2207.01206 | LLM / agentic (web) | auto-shaped |
| 76 | ScienceWorld | ScienceWorld: Is your Agent Smarter than a 5th Grader? | R. Wang | 2022 | EMNLP 2022 | arXiv:2203.07540; 10.18653/v1/2022.emnlp-main.775 | LLM / agentic (text science) | configurable |
| 77 | OSWorld | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | T. Xie | 2024 | NeurIPS 2024 | arXiv:2404.07972 | LLM / agentic (computer use) | handcrafted |
| 78 | AgentBench | AgentBench: Evaluating LLMs as Agents | X. Liu | 2024 | ICLR 2024 | arXiv:2308.03688 | LLM / agentic (multi-domain) | handcrafted |
| 79 | AppWorld | AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents | H. Trivedi | 2024 | ACL 2024 (Long Papers) | arXiv:2407.18901; 10.18653/v1/2024.acl-long.850 | LLM / agentic (apps, APIs) | configurable |
| 80 | Voyager | Voyager: An Open-Ended Embodied Agent with Large Language Models | G. Wang | 2024 | Transactions on Machine Learning Research (TMLR) | arXiv:2305.16291 | LLM / agentic (Minecraft curriculum) | llm-generated |
| 81 | SmartPlay | SmartPlay: A Benchmark for LLMs as Intelligent Agents | Y. Wu | 2024 | ICLR 2024 | arXiv:2310.01557 | LLM / agentic (games) | handcrafted |
| 82 | MLE-bench | MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering | J. S. Chan | 2025 | ICLR 2025 | arXiv:2410.07095 | LLM / agentic (ML engineering) | handcrafted |

## Rung tallies

| rung | count | share | representative entries |
|------|-------|-------|------------------------|
| `handcrafted` | 23 | 28.0% | ALE, Melting Pot, Meta-World, SMAC, Hanabi, Overcooked-AI, D4RL, OSWorld, MLE-bench |
| `configurable` | 29 | 35.4% | Gym, Griddly, MiniHack, dm_control, Isaac Gym, robosuite, ManiSkill2/3, PettingZoo, Habitat |
| `auto-shaped` | 15 | 18.3% | Procgen, Crafter, Craftax, Obstacle Tower, SMACv2, PCGRL, TextWorld, SWE-bench, WebShop |
| `llm-generated` | 6 | 7.3% | RoboCasa, OMNI, Genie, GenSim, RoboGen, Voyager |
| `co-adaptive` | 9 | 11.0% | XLand, POET, Enhanced POET, PAIRED, PLR, Robust PLR, ACCEL, CoDE, Eurekaverse |
| **total** | **82** | **100%** | |

Reading of the tallies:

| observation | evidence |
|-------------|----------|
| CROWDED: `configurable` + `handcrafted` together are 52 of 82 (63.4%) | The canonical corpus is overwhelmingly human-authored. Almost every landmark simulator, suite and benchmark ships a fixed or human-parameterised task set. |
| CROWDED: `auto-shaped` is healthy but narrow in kind | 15 entries, but 6 of them are 2D/3D game level generators (Procgen, Crafter, Craftax, Obstacle Tower, TextWorld, ALFWorld) and 3 are data-mining pipelines (SWE-bench, SWE-Gym, WebShop). Almost no procedural generation in physics-based robotics. |
| SPARSE: `llm-generated` at 6 (7.3%) | Only RoboCasa, OMNI, Genie, GenSim, RoboGen and Voyager. All are 2023 or later, and four of the six are robotics-task generators rather than full environments. |
| SPARSE: `co-adaptive` at 9 (11.0%) | Essentially one lineage: POET -> PAIRED -> PLR -> Robust PLR -> ACCEL, plus XLand, CoDE and Eurekaverse. Almost all of it runs on toy 2D domains (BipedalWalker, MiniGrid, MiniHack), not on the landmark simulators above. |
| The empty cell | No entry in this corpus is BOTH a landmark high-fidelity simulator AND `llm-generated` or `co-adaptive`. The automation rungs and the canonical simulators are disjoint sets. |

## Verified-as-non-paper artefacts (deliberately excluded from the numbered table)

These are central systems whose canonical artefact was verified to be software or a
technical report with **no** arXiv id and **no** DOI. They are listed separately so that
every row in the main table carries a resolvable identifier.

| Name | Canonical artefact | 1st author | Year | Note |
|------|-------------------|-----------|------|------|
| PyBullet | `@MISC` entry in the `bulletphysics/bullet3` README, `pybullet.org` | E. Coumans | 2016-2021 | No peer-reviewed paper exists; the Bullet SIGGRAPH item is a course note |
| Gymnasium-Robotics | Repository `README` `@software` block and `CITATION.cff` | R. de Lazcano (README) | 2022-2024 | The two in-repo records disagree on author and year; no Zenodo DOI found |
| Safety Gym | OpenAI technical report `cdn.openai.com/safexp-short.pdf` | A. Ray | 2019 | No arXiv id, no DOI; superseded for citation purposes by Safety-Gymnasium (row 24) |
| Genie 3 | Google DeepMind blog post plus its official BibTeX file | P. J. Ball (per BibTeX) | 2025 | No paper, no DOI; blog byline and BibTeX first author disagree |

## Verification caveats to carry into the `.bib`

| Entry | Caveat |
|-------|--------|
| PettingZoo | It is NOT the NeurIPS Datasets and Benchmarks track. DBLP and OpenReview both place it in NeurIPS 2021 main proceedings, vol. 34, pp. 15032-15043 |
| SMAC | Crossref returns DOI `10.65109/lvzz5205` with correct title and pages but corrupted container metadata (it names AAMAS '04). Cite AAMAS 2019 pp. 2186-2188 plus the arXiv id; do not use that DOI unqualified |
| RoboCasa | arXiv title says "Everyday Tasks"; the RSS 2024 proceedings, its official BibTeX and Crossref all say "Household Tasks". The proceedings form is used above |
| Meta-World | PMLR v100 lists 7 authors, arXiv lists 10. PMLR stamps the proceedings year 2020 although the conference was CoRL 2019 |
| ManiSkill3 | The RSS 2025 venue is asserted by the authors' own repository BibTeX and was not confirmed on an RSS proceedings index |
| Brax / MyoSuite / Safety-Gymnasium / Enhanced POET | Title punctuation and casing differ between arXiv and the refereed venue. The refereed form is used above |
| tau-bench | DBLP indexes only the CoRR record. Do not cite it as a conference paper |
| TextWorld | Venue is the Computer Games Workshop at IJCAI 2018, not the IJCAI main track |
| XLand | arXiv lists the group author literally as "Open Ended Learning Team"; the first named individual is Adam Stooke |
| Neural MMO | A third, peer-reviewed variant exists ("The Neural MMO Platform for Massively Multiagent Research", NeurIPS 2021 D&B) if an arXiv-only citation is unacceptable |
| Minari | Zenodo credits Younis et al.; the repo `CITATION.cff` credits "Minari Contributors" with a 2023 release date. The concept DOI is cited above for version independence |
| Eurekaverse | Dual-rung system: an LLM is the generator but the defining loop is curriculum co-adaptation. Counted once, under `co-adaptive` |
| Genie | Counted under `llm-generated` as the closest available rung for a generative-model-authored environment; the generator is a video world model, not a language model |

