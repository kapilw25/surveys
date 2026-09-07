# Slice 01 - google_scholar.md lines 1-130

Harvested for the RL ENVIRONMENTS survey. Every row below was checked by web search against
arXiv / publisher / proceedings pages. Nothing is recorded that a source page did not state.

- Papers in slice: 19
- Verified: 19
- UNVERIFIED: 0
- `false-positive` (RL not meaning reinforcement learning): 0
- Duplicates within slice: 0

## Summary table

| # | Title | 1st author | Year | Venue | arXiv/DOI | type | domain | rung | verified? |
|---|-------|-----------|------|-------|-----------|------|--------|------|-----------|
| 1 | Learning to Locomote: Understanding How Environment Design Matters for Deep Reinforcement Learning | D. Reda | 2020 | ACM SIGGRAPH MIG 2020 | arXiv:2010.04304; 10.1145/3424636.3426907 | design | robotics (locomotion) | configurable | yes |
| 2 | EnvPool: A Highly Parallel Reinforcement Learning Environment Execution Engine | J. Weng | 2022 | NeurIPS 2022 Datasets and Benchmarks | arXiv:2206.10558 | infra | general RL (games, control) | n/a | yes |
| 3 | Reinforcement learning algorithm for non-stationary environments | S. Padakandla | 2020 | Applied Intelligence 50(11):3590-3606 | 10.1007/s10489-020-01758-5; preprint arXiv:1905.03970 | application | transport (traffic signals), energy | n/a | yes |
| 4 | Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning | V. Lacombe | 2025 | arXiv preprint | arXiv:2509.18083 | env | LLM / agentic (symbolic reasoning) | auto-shaped | yes |
| 5 | JaxMARL: Multi-Agent RL Environments and Algorithms in JAX | A. Rutherford | 2024 | NeurIPS 2024 Datasets and Benchmarks | arXiv:2311.10090 | infra | games / multi-agent | n/a | yes |
| 6 | RoboScape-R: Unified Reward-Observation World Models for Generalizable Robotics Training via RL | Y. Tang | 2026 | CVPR 2026 (preprint Dec 2025) | arXiv:2512.03556 | env | robotics | auto-shaped | yes |
| 7 | Adversarial environment reinforcement learning algorithm for intrusion detection | G. Caminero | 2019 | Computer Networks 159:96-109 | 10.1016/j.comnet.2019.05.013 | application | security (NIDS) | co-adaptive | yes |
| 8 | Position: Automatic Environment Shaping is the Next Frontier in RL | Y. Park | 2024 | ICML 2024 (Position track), PMLR v235 | arXiv:2407.16186 | design | robotics (sim-to-real) | auto-shaped | yes |
| 9 | Automatic Generation of High-Performance RL Environments | S. Karten | 2026 | arXiv preprint | arXiv:2603.12145 | design | games / general RL infra | llm-generated | yes |
| 10 | Predictive Information Accelerates Learning in RL | K.-H. Lee | 2020 | NeurIPS 2020 | arXiv:2007.12401 | application | control (DM Control from pixels) | n/a | yes |
| 11 | Gymnasium: A Standard Interface for Reinforcement Learning Environments | M. Towers | 2024 (arXiv) / NeurIPS 2025 | NeurIPS Datasets and Benchmarks; Scholar row says 2026 | arXiv:2407.17032 | infra | general RL | n/a | yes |
| 12 | EasySO: Exploration-enhanced Reinforcement Learning for Logic Synthesis Sequence Optimization and a Comprehensive RL Environment | J. Yuan | 2023 | IEEE/ACM ICCAD 2023 | 10.1109/ICCAD57390.2023.10323973 (IEEE Xplore doc 10323973) | env | EDA (logic synthesis) | configurable | yes |
| 13 | The NetHack Learning Environment | H. Küttler | 2020 | NeurIPS 2020 | arXiv:2006.13760 | env | games | auto-shaped | yes |
| 14 | SUBER: An RL Environment with Simulated Human Behavior for Recommender Systems | N. Corecco | 2024 | ECAI 2024, FAIA vol. 392 | arXiv:2406.01631; 10.3233/FAIA240742 | env | recsys | llm-generated | yes |
| 15 | A Systematic Study on Reinforcement Learning Based Applications | K. Sivamayil | 2023 | Energies 16(3):1512 | 10.3390/en16031512 | survey | general (energy emphasis) | n/a | yes |
| 16 | SortingEnv: An Extendable RL-Environment for an Industrial Sorting Process | T. Maus | 2026 (proc.) / 2025 (conf.) | AIP Conf. Proc. 3381, 050002 (ICIEA-EU 2025) | arXiv:2503.10466 | env | industry (sorting, recycling) | configurable | yes |
| 17 | Importance of Environment Design in Reinforcement Learning: A Study of a Robotic Environment | M. Farsang | 2021 | Automation and Applied Computer Science Workshop (AACS) 2021 | arXiv:2102.10447 | design | robotics (assistive mobile robot) | handcrafted | yes |
| 18 | Adversarial RL-Based IDS for Evolving Data Environment in 6LoWPAN | A. M. Pasikhani | 2022 | IEEE Trans. Information Forensics and Security 17:3831-3846 | 10.1109/TIFS.2022.3214099 | application | security (IoT / RPL) | co-adaptive | yes |
| 19 | Creation of an RL Environment to Monitor Ocean Features with Autonomous Vehicles | N. Loizzo | 2025 | MSc thesis, Politecnico di Torino (co-tutela ICM-CSIC) | webthesis.biblio.polito.it/35258/ (no DOI) | env | science (marine / ocean monitoring) | handcrafted | yes |

## Auxiliary table: openness and citations

| # | Short name | open_source | code location | Scholar citations |
|---|-----------|-------------|---------------|-------------------|
| 1 | Learning to Locomote | unknown | project page cs.ubc.ca/~van/papers/2020-MIG-envdesign/ | 93 |
| 2 | EnvPool | yes | github.com/sail-sg/envpool | 92 |
| 3 | Non-stationary RL | unknown | - | 238 |
| 4 | Reasoning Core | yes | github.com/sileod/reasoning-core | 5 |
| 5 | JaxMARL | yes | github.com/flairox/jaxmarl | 112 |
| 6 | RoboScape-R | unknown | - | 4 |
| 7 | AE-RL (intrusion detection) | yes | github.com/gcamfer/Anomaly-ReactionRL | 280 |
| 8 | Automatic Environment Shaping | unknown | project page auto-env-shaping.github.io | 5 |
| 9 | Automatic Generation of High-Performance RL Environments | unknown | - | 1 |
| 10 | PI-SAC | unknown | - | 110 |
| 11 | Gymnasium | yes | Farama Foundation Gymnasium | 1319 |
| 12 | EasySO | unknown | - | 20 |
| 13 | NetHack Learning Environment | yes | github.com/facebookresearch/nle | 296 |
| 14 | SUBER | yes | github.com/SUBER-Team/SUBER | 17 |
| 15 | Systematic study of RL applications | n/a | - | 213 |
| 16 | SortingEnv | yes | github.com/Storm-131/Sorting_Env | 3 |
| 17 | Importance of Environment Design | unknown | - | 2 |
| 18 | Adversarial RL-based IDS (6LoWPAN) | unknown | - | 28 |
| 19 | Ocean monitoring RL environment | unknown | - | (not shown) |

## Per-paper contribution notes

### Learning to Locomote: Understanding How Environment Design Matters for Deep Reinforcement Learning

Reda, Tao and van de Panne hold the RL algorithm fixed and instead ablate the environment
itself across locomotion tasks, sweeping state representation, initial state distribution,
reward structure, control frequency, episode termination, curriculum, action space and torque
limits. The contribution is empirical evidence that these environment-side choices, not the
learner, explain much of the brittleness and irreproducibility reported in deep RL locomotion
results. It reframes the environment as a first-class design surface with measurable effects.

### EnvPool: A Highly Parallel Reinforcement Learning Environment Execution Engine

Weng and colleagues attack the environment-stepping bottleneck rather than the learner,
delivering a C++ threadpool-backed asynchronous execution engine that replaces Python-level
subprocess parallelism. It reports one million Atari frames per second and three million MuJoCo
frames per second on a DGX-A100, and 2.8x speed over Python subprocesses on a laptop, while
staying drop-in compatible with CleanRL, rl_games and DeepMind Acme. The contribution is an
infrastructure layer that makes environment throughput a tunable engineering variable.

### Reinforcement learning algorithm for non-stationary environments

Padakandla, Prabuchandran and Bhatnagar drop the stationarity assumption and combine an adapted
change-point detection procedure with a context-partitioned Q-learning scheme, so the agent
detects when the environment model has shifted and learns a separate policy per detected regime.
They validate on non-stationary random MDPs, a sensor energy management problem and traffic
signal control. Note for this survey: this is an algorithm paper that adapts to a changing
environment, not an environment contribution, and is an off-axis keyword hit.

### Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning

Lacombe, Quesnel and Sileo build an RLVR environment that procedurally generates problems in
formal domains (PDDL planning, first-order logic, context-free grammar parsing, causal reasoning
and system equation solving) rather than curating a fixed benchmark. Correctness is checked with
external symbolic tools, and a difficulty knob gives continuous control over instance hardness,
so the supply of fresh training instances is effectively unbounded. Zero-shot evaluations with
frontier LLMs establish that the generated tasks are genuinely hard.

### JaxMARL: Multi-Agent RL Environments and Algorithms in JAX

Rutherford and co-authors port a broad set of commonly used multi-agent environments plus
baseline algorithms into JAX so that environment stepping and training both run on the
accelerator, reporting end-to-end pipelines up to 12,500x faster than CPU-bound equivalents.
They also contribute SMAX, a vectorised reimplementation of the StarCraft Multi-Agent Challenge
that removes the StarCraft II engine dependency entirely. The contribution is primarily a unified
accelerated library, with SMAX as a new environment inside it.

### RoboScape-R: Unified Reward-Observation World Models for Generalizable Robotics Training via RL

Tang and colleagues replace the simulator with a learnt world model that serves both roles an RL
environment must play: it returns the next-frame observation and it returns the reward. The
reward is endogenous, derived from the model's own understanding of real-world state transition
dynamics, which removes the dependence on task-specific handcrafted reward functions and is the
paper's route to multi-scene generalisation. The pipeline pairs an action world model with a text
world model and plugs interchangeable policies into the resulting interface.

### Adversarial environment reinforcement learning algorithm for intrusion detection

Caminero, Lopez-Martin and Carro turn a supervised intrusion-detection dataset into an RL problem
by making the environment itself a learning agent: an adversary agent selects which attack sample
to present while the detector agent classifies it, so the two co-adapt during training. The
resulting AE-RL model improves weighted accuracy (>0.8) and F1 (>0.79) and is notably stronger on
under-represented attack labels. It is an early instance of the environment being an optimised,
adaptive opponent rather than a fixed data stream.

### Position: Automatic Environment Shaping is the Next Frontier in RL

Park, Margolis and Agrawal argue that sim-to-real RL success is now gated by human labour spent
shaping observations, actions, rewards and simulation dynamics, not by algorithm quality. They
support the position with an evaluation of what current shaping practice and automated shaping
methods actually achieve on a suite of robotic tasks, showing that off-the-shelf RL fails on
unshaped reference environments. The paper's contribution is an agenda: treat environment shaping
as the object to automate and benchmark.

### Automatic Generation of High-Performance RL Environments

Karten, Appapogu and Jin show that LLM agents can produce high-performance environment
implementations that previously took months of specialised engineering, using a reusable recipe
of a generic prompt template, hierarchical verification and iterative agent-assisted repair for
under $10 of compute. They demonstrate three workflows: direct translation (PokeJAX, the first
GPU-parallel Pokemon battle simulator, at 15.2M SPS under PPO, 22,320x over the TypeScript
reference), translation verified against existing implementations (throughput parity with MJX,
5x over Brax on HalfCheetah), and creation of a new environment from a web-extracted
specification (TCGJax at 717K SPS).

### Predictive Information Accelerates Learning in RL

Lee and co-authors define the predictive information as the mutual information between an agent's
past and future, and add a contrastive Conditional Entropy Bottleneck auxiliary objective to Soft
Actor-Critic to capture it. The resulting PI-SAC substantially improves sample efficiency on
pixel-based DM Control tasks over strong baselines. Note for this survey: this is a
representation-learning contribution evaluated in existing environments, an off-axis keyword hit.

### Gymnasium: A Standard Interface for Reinforcement Learning Environments

Towers, Kwiatkowski and the Farama team document the maintained successor to OpenAI Gym, whose
contribution is the `Env` abstraction and API contract itself rather than any single task. By
fixing a single interface (reset/step semantics, spaces, wrappers, vectorisation) they buy
interoperability between arbitrary benchmark environments and arbitrary training algorithms,
which is why essentially every other entry in this corpus targets this interface. Scholar lists
the row as 2026, while the arXiv preprint is 2024 and the NeurIPS Datasets and Benchmarks
appearance is 2025.

### EasySO: Exploration-enhanced Reinforcement Learning for Logic Synthesis Sequence Optimization and a Comprehensive RL Environment

Yuan and co-authors argue that prior RL formulations of logic synthesis cripple themselves by
restricting the action space to a handful of operators with fixed parameters, and so contribute a
broader environment whose actions span logic optimisation, technology mapping and post-mapping
operators together with their continuous and binary parameters. On top of that environment they
run a hybrid-action-space PPO with two actors (operator and parameter) and a budget tuner that
shifts exploration effort between the two. The environment redefinition, not just the learner, is
what unlocks escape from the local minima of earlier formulations.

### The NetHack Learning Environment

Küttler and colleagues wrap the roguelike NetHack into a scalable RL environment that is
procedurally generated, stochastic and extremely deep in content, yet cheap to simulate because
it is terminal-based rather than 3D. The pitch is a complexity-per-compute argument: NLE supports
long-horizon research into exploration, planning, skill acquisition and language-conditioned RL
at a fraction of the compute of pixel-based benchmarks. The procedural level generation is
inherited from the game; the task and reward wrappers around it are handcrafted.

### SUBER: An RL Environment with Simulated Human Behavior for Recommender Systems

Corecco, Piatti, Lanzendörfer and co-authors address the fact that on-policy RL for recommenders
needs online human interaction that nobody can afford, by building a synthetic environment whose
users are LLMs. The LLM-driven users hold profiles and memories, consume recommendations and emit
ratings, so the reward signal itself is generated by a language model rather than logged data or
a handwritten user model. Movie and book environments ship with the framework.

### A Systematic Study on Reinforcement Learning Based Applications

Sivamayil and co-authors review 127 publications applying RL across marketing, robotics, gaming,
autonomous vehicles, NLP, IoT security, recommendation, finance and energy management. The
contribution is a cross-domain map of where RL has been deployed, with a pronounced emphasis on
energy applications such as smart buildings, hybrid vehicles, smart grids and renewable resource
management. It is an applications survey rather than an environments survey.

### SortingEnv: An Extendable RL-Environment for an Industrial Sorting Process

Maus, Zengeler and Glasmachers contribute a digital-twin-style environment for industrial waste
sorting, modelling material flow with operational parameters such as belt speed and occupancy
level. Its distinctive feature is deliberate extensibility: a basic variant with discrete belt
speed actions and an advanced variant adding multiple sorting modes and richer material
composition observations, mirroring how a real plant gains sensors and machinery over time. They
benchmark PPO, DQN and A2C against a classical rule-based agent, so the environment doubles as a
testbed for agent behaviour under an evolving observation and action space.

### Importance of Environment Design in Reinforcement Learning: A Study of a Robotic Environment

Farsang and Szegletes take a small mobile collaborative robotic assistant MDP and solve the
Bellman optimality equations exactly and symbolically rather than approximately, which lets them
attribute policy changes to environment definition with no learner noise in the way. They then
show that small perturbations of the reward function and transition probabilities flip the optimal
policy. The contribution is a clean, analytically exact demonstration that environment design,
not algorithm choice, selects the behaviour.

### Adversarial RL-Based IDS for Evolving Data Environment in 6LoWPAN

Pasikhani, Clark and Gope propose an adversarial RL framework that generates resource-efficient
intrusion detectors for 6LoWPAN low-power lossy networks, covering what they claim is the most
comprehensive set of RPL routing attacks to date (wormhole, grayhole, DIO suppression, increase
rank and others). They combine adversarial RL with incremental machine learning and explicit
concept-drift detection and adaptation, so the detector tracks a non-stationary attack
distribution. They also separate black-box from grey-box ML-based adversaries for the first time
in this setting.

### Creation of an RL Environment to Monitor Ocean Features with Autonomous Vehicles

Loizzo's MSc thesis (Politecnico di Torino, co-tutela with ICM-CSIC) extends an existing
autonomous-vehicle simulation into an RL environment for detecting and tracking dynamic ocean
features such as temperature, salinity and biological phenomena. The work develops and compares
two simulation approaches with distinct reward function designs, and identifies the environment
parameters that most influence effective agent learning under marine uncertainty. Scholar lists
the record via digital.csic.es; the primary record is the Politecnico di Torino thesis
repository, 82 pages, academic year 2024/25.

## Flags and caveats

| Issue | Entries | Detail |
|-------|---------|--------|
| Off-axis keyword hit (no environment contribution) | #3, #10 | Algorithm / representation papers that merely contain the phrase "RL environment"; keep out of the environments taxonomy or use only as background |
| Applications survey, not environments survey | #15 | Cited for scope of RL deployment, not as prior art on environment design |
| Venue year mismatch vs Scholar row | #11, #6, #16 | Gymnasium: Scholar says 2026, actual arXiv 2024 / NeurIPS 2025. RoboScape-R: Scholar says 2026 proceedings, arXiv Dec 2025, CVPR 2026. SortingEnv: conference ICIEA-EU 2025, AIP proceedings volume dated 2026 |
| Repository mismatch vs Scholar row | #19 | Scholar shows digital.csic.es; primary record is Politecnico di Torino webthesis |
| Related but distinct, not duplicates | #7 and #18 | Both adversarial-RL intrusion detection; different authors, venues, years and networks |
| Title differs between preprint and journal | #3 | arXiv:1905.03970 is "Reinforcement Learning in Non-Stationary Environments"; the Applied Intelligence version is "Reinforcement learning algorithm for non-stationary environments" |
| Successor paper exists | #4 | A 2026 follow-up, arXiv:2603.02208, reframes Reasoning Core as a procedural data generation suite; check before citing which version is meant |
