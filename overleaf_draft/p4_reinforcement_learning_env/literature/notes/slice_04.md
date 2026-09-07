# Slice 04 - google_scholar.md lines 401-520

Harvested and web-verified for the RL-environments survey. Every row below was checked against at
least one authoritative record (Crossref DOI, publisher page, ACL Anthology, PMLR, or OpenReview).
No metadata field is guessed; anything not confirmed is written as `unconfirmed`.

Boundary note: entry 1 has its title line at 398, just above the slice, but its body text falls
inside lines 401-402. It is included here for completeness and may overlap with slice 03.

## Verification table

| # | Title | 1st author | Year | Venue | arXiv/DOI | type | domain | rung | verified? |
|---|-------|-----------|------|-------|-----------|------|--------|------|-----------|
| 1 | A reinforcement learning model for material handling task assignment and route planning in dynamic production logistics environment | Y. Jeong | 2021 | Procedia CIRP 104, 1807-1812 | 10.1016/j.procir.2021.11.305 | application | manufacturing / logistics | handcrafted | VERIFIED |
| 2 | A Reinforcement Learning Approach to Find Optimal Propulsion Strategy for Microrobots Swimming at Low Reynolds Number | I. Jebellat | 2024 | Robotics and Autonomous Systems 175, 104659 | 10.1016/j.robot.2024.104659 | application | robotics / microrobotics | handcrafted | VERIFIED |
| 3 | Sustainability of Data Center Digital Twins with Reinforcement Learning | S. Sarkar | 2024 | AAAI 38(21), 23832-23834 | 10.1609/aaai.v38i21.30580 | env | power / energy (data centres) | configurable | VERIFIED |
| 4 | A General Approach of Automated Environment Design for Learning the Optimal Power Flow | T. Wolgast | 2025 | ACM e-Energy '25, 108-121 | arXiv:2505.07832; 10.1145/3679240.3734626 | design | power / energy | auto-shaped | VERIFIED |
| 5 | Reinforcement Learning Energy Management for Fuel Cell Hybrid Systems: A Review | Q. Li | 2022 (issue 2023) | IEEE Industrial Electronics Magazine 17, 45-54 | 10.1109/MIE.2022.3148568 | survey | power / energy (vehicles) | n/a | VERIFIED |
| 6 | Behavioural Cloning based RL Agents for District Energy Management | S. R. Kumar | 2022 | ACM BuildSys '22 / RLEM workshop, 466-470 | 10.1145/3563357.3566165 | application | power / energy (buildings) | handcrafted | VERIFIED |
| 7 | Enhancing RL Safety with Counterfactual LLM Reasoning | D. Gross | 2024 | ICTSS 2024, LNCS, 23-29 | arXiv:2409.10188; 10.1007/978-3-031-80889-0_2 | infra | safety / verification | n/a | VERIFIED |
| 8 | Deep reinforcement learning for semiconductor production scheduling | B. Waschneck | 2018 | IEEE ASMC 2018, 301-306 | 10.1109/ASMC.2018.8373191 | application | manufacturing / semiconductor | handcrafted | VERIFIED |
| 9 | Robust Attitude Control of an Agile Aircraft Using Improved Q-Learning | M. Zahmatkesh | 2022 | Actuators 11(12), 374 | 10.3390/act11120374 | application | aerospace | handcrafted | VERIFIED |
| 10 | UPEGSim: An RL-Enabled Simulator for Unmanned Underwater Vehicles Dedicated in the Underwater Pursuit-Evasion Game | J. Xu | 2025 | IEEE Internet of Things Journal 12, 2334-2346 | 10.1109/JIOT.2024.3472700 | env | robotics / marine | configurable | VERIFIED |
| 11 | PCTL Model Checking for Temporal RL Policy Safety Explanations | D. Gross | 2025 | ACM SAC '25, 1514-1521 | 10.1145/3672608.3707759 | infra | safety / verification | n/a | VERIFIED |
| 12 | A dynamic approach to support outbreak management using reinforcement learning and semi-connected SEIQR models | Y. Kao | 2024 | BMC Public Health 24, 751 | 10.1186/s12889-024-18251-0 | env | medical / epidemiology | handcrafted | VERIFIED |
| 13 | A Geometric Lens on RL Environment Complexity Based on Ricci Curvature | A. Saheb Pasand | 2025 | RLC 2025 workshop (OpenReview `ab45VX83Z1`; exact workshop name unconfirmed) | no arXiv/DOI found | design | general RL / analysis | auto-shaped | VERIFIED (venue partial) |
| 14 | Reinforcement Learning for Molecular Design Guided by Quantum Mechanics (MolGym) | G. N. C. Simm | 2020 | ICML 2020, PMLR 119, 8959-8969 | arXiv:2002.07717 | env | science / chemistry | configurable | VERIFIED |
| 15 | Optimization of global production scheduling with deep reinforcement learning | B. Waschneck | 2018 | Procedia CIRP 72, 1264-1269 | 10.1016/j.procir.2018.03.212 | application | manufacturing / semiconductor | handcrafted | VERIFIED |
| 16 | Decision-making and confrontation in close-range air combat based on reinforcement learning | M. Yang | 2025 | Chinese Journal of Aeronautics 38(9), 103526 | 10.1016/j.cja.2025.103526 | application | aerospace / defence | handcrafted | VERIFIED |
| 17 | Towards a Robot Simulation Framework for E-waste Disassembly Using Reinforcement Learning | C. B. Kristensen | 2019 | Procedia Manufacturing 38 (FAIM 2019), 225-232 | 10.1016/j.promfg.2020.01.030 | infra | robotics / recycling | configurable | VERIFIED |
| 18 | Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code | H. Chae | 2024 | EMNLP 2024 (main) | arXiv:2409.19715 | env | LLM / agentic (code) | configurable | VERIFIED |
| 19 | Robust Design for IRS-Assisted MISO-NOMA Systems: A DRL-Based Approach | A. Waraiet | 2023 (issue 2024) | IEEE Wireless Communications Letters 13(3), 592-596 | 10.1109/LWC.2023.3335622 | application | wireless communications | handcrafted | VERIFIED |
| 20 | Comparison of Various Reinforcement Learning Environments in the Context of Continuum Robot Control | J. Kolota | 2023 | Applied Sciences 13(16), 9153 | 10.3390/app13169153 | design | robotics | handcrafted | VERIFIED |

## Open source and citations (as shown in the source file)

| # | Short name | open_source | evidence | citations |
|---|-----------|-------------|----------|-----------|
| 1 | Jeong SPL logistics | unknown | - | 19 |
| 2 | Jebellat microswimmers | unknown | - | 37 |
| 3 | DCRL-Green | yes | github.com/HewlettPackard/dc-rl (legacy branch = DCRL-Green, now SustainDC) | 29 |
| 4 | Automated OPF env design | yes | github.com/Digitalized-Energy-Systems/opfgym | 2 |
| 5 | Fuel cell EMS review | n/a | - | 97 |
| 6 | BC district energy | unknown | built on CityLearn, which is itself open | 10 |
| 7 | Counterfactual LLM safety | unknown | - | 8 |
| 8 | DRL semiconductor scheduling | unknown | - | 217 |
| 9 | Agile aircraft Q-learning | unknown | - | 24 |
| 10 | UPEGSim | unknown | - | 10 |
| 11 | PCTL policy explanations | unknown | - | 4 |
| 12 | SEIQR outbreak RL | unknown | supplementary files on BMC, code not confirmed | 9 |
| 13 | Ricci curvature complexity | unknown | - | none shown |
| 14 | MolGym | yes | github.com/gncs/molgym | 168 |
| 15 | Global production scheduling | unknown | - | 536 |
| 16 | Close-range air combat | unknown | 6-DOF F-16 model from open aerodynamic data | 11 |
| 17 | E-waste disassembly framework | unknown | ROS / Gazebo / MoveIt stack is open | 49 |
| 18 | Coffee-Gym | yes | huggingface.co/spaces/Coffee-Gym/Project-Coffee-Gym | 13 |
| 19 | IRS-assisted MISO-NOMA | unknown | - | 27 |
| 20 | Continuum robot env comparison | unknown | - | 17 |

## Notes

### A reinforcement learning model for material handling task assignment and route planning in dynamic production logistics environment

Applies RL to combined task assignment and route planning for material handling in smart production
logistics, using an empirical case from the automotive industry. The contribution is an architecture
that slots RL into a smart production logistics stack plus a mapping of the RL elements (environment,
state, reward, value, policy) onto that domain. It is a domain application rather than a study of
environment design, although the element-by-element mapping is a useful citation for how practitioners
translate a factory into an MDP.

### A Reinforcement Learning Approach to Find Optimal Propulsion Strategy for Microrobots Swimming at Low Reynolds Number

Uses Q-learning to discover propulsion gaits for microswimmers that generate net displacement at low
Reynolds number by expanding and contracting active rods. Introduces "Basic Coding", a discretisation
scheme for state and action encoding that the authors claim transfers to any discrete RL environment,
and shows the learned phase differences converge towards the theoretical optimum as elastic and
electrostatic effects are added. Classified as `application`, but the Basic Coding scheme sits on the
boundary with environment representation design and could be cited in that context.

### Sustainability of Data Center Digital Twins with Reinforcement Learning

Presents DCRL-Green, a multi-agent RL environment built on a data centre digital twin that jointly
exposes cooling control, flexible workload shifting against renewable availability, and UPS battery
storage. The environment is explicitly framed as a modular, configurable, scalable platform on which
the community can benchmark single-agent and multi-agent controllers and subclass the defaults.
It is one of the clearer examples in this slice of an environment released as the primary artefact,
and it later grew into SustainDC.

### A General Approach of Automated Environment Design for Learning the Optimal Power Flow

Reframes RL environment design as a multi-objective optimisation problem and solves it with standard
hyperparameter optimisation machinery, so that reward formulation, observation set, and action space
are searched rather than hand-tuned. Across five OPF benchmark environments the automatically designed
environments beat a carefully hand-built baseline, and statistical analysis identifies which design
decisions carry the most performance weight. This is the strongest `design`-type paper in the slice
and a direct precedent for any claim about automating environment design.

### Reinforcement Learning Energy Management for Fuel Cell Hybrid Systems: A Review

A review of RL-based energy management strategies for fuel cell hybrid systems, deliberately split
into the environment side and the agent side. The environment half surveys training-environment
construction and reward function settings, which makes it an unusual survey for our purposes because
it treats environment specification as a first-class review axis rather than an implementation detail.
Useful as evidence that domain surveys already sense the environment-design gap without naming it.

### Behavioural Cloning based RL Agents for District Energy Management

Injects domain knowledge into a district energy management RL setup by pre-training the policy network
with behavioural cloning of a heuristic rule-based controller, then improving it with RL against the
reward. Implemented in CityLearn over electrical storage for five buildings, giving roughly 3.8 per
cent over the rule-based controller and about 20 per cent over pure RL. The knowledge injection is on
the policy side, not the environment side, so this is an application of an existing environment.

### Enhancing RL Safety with Counterfactual LLM Reasoning

Takes a trained policy plus the MDP describing its environment and uses counterfactual LLM reasoning
over extracted states to both explain and improve policy safety after training. The method is tooling
that wraps an environment and a policy rather than a new environment, and it sits in the same
verification line as the authors' COOL-MC work. Relevant to a survey chapter on environment-side
tooling and analysis rather than environment construction.

### Deep reinforcement learning for semiconductor production scheduling

Applies DeepMind-style DQN agents cooperatively to semiconductor fab scheduling, training each agent
against flexible user-defined objectives inside a simulated production environment. Benchmarks against
standard dispatching heuristics show the agents can optimise production autonomously for different
targets. A canonical high-citation industrial application of RL in a hand-built simulation environment.

### Robust Attitude Control of an Agile Aircraft Using Improved Q-Learning

Builds a detailed mathematical model of a truss-braced wing regional aircraft with low inherent
stability and turns it into an RL environment, then trains an improved Q-learning attitude controller.
A Fuzzy Action Assignment method converts the discrete trained Q-table into continuous control commands,
and the controller holds attitude under measurement noise, atmospheric disturbance, actuator faults,
and model uncertainty. The environment is constructed by hand from first-principles dynamics.

### UPEGSim: An RL-Enabled Simulator for Unmanned Underwater Vehicles Dedicated in the Underwater Pursuit-Evasion Game

Releases a Gazebo and ROS based simulator that turns the underwater pursuit-evasion game into a trainable
RL environment for unmanned underwater vehicles, avoiding the cost and risk of sea trials. Alongside the
simulator the authors give ETFDU, a training framework combining decentralised multi-agent training and
execution, scene-transfer training, and decision-transformer offline RL. The simulator is the headline
artefact, which makes this a clean `env` entry for the marine robotics cell.

### PCTL Model Checking for Temporal RL Policy Safety Explanations

Combines local explainable RL with PCTL probabilistic model checking so that safety explanations carry
temporal context instead of being single-decision attributions. The pipeline takes five inputs: the MDP
of the RL environment, the trained policy, a PCTL safety formula, a local explainability method, and a
PCTL explanation formula. Like its sibling paper it is environment-adjacent infrastructure for
verification, not a new environment.

### A dynamic approach to support outbreak management using reinforcement learning and semi-connected SEIQR models

Constructs a bespoke RL environment of four semi-connected regions modelled on Tokyo, Osaka, Okinawa,
and Hokkaido, each governed by an SEIQR compartmental model with a transport hub linking it to the
others, and with population allocation and inter-regional travel set by population-weighted density.
The agent learns containment policies that trade disease control against economic activity. Classified
as `env` because the simulator, not the algorithm, is the substantive contribution.

### A Geometric Lens on RL Environment Complexity Based on Ricci Curvature

Introduces Ollivier-Ricci Curvature as an information-geometric measure of the local structure of an RL
environment and connects it to the Successor Representation, giving a reward-free geometric reading of
environment dynamics. Positive and negative curvature identify states where random walks converge or
diverge, curvature correlates with established environment complexity metrics while giving both local
and global readings, and an ORC-based intrinsic reward pushes agents away from convergent traps.
A strong `design` entry: it is complexity analysis of environments as objects in their own right.

### Reinforcement Learning for Molecular Design Guided by Quantum Mechanics (MolGym)

Formulates molecular design directly in Cartesian coordinates, widening the class of constructible
molecules relative to graph-based formulations, and derives the reward from physical quantities such as
energy computed by fast quantum-chemical methods. The paper releases MolGym, an RL environment with
several molecular design tasks plus baselines. The interesting feature for our survey is that the reward
is grounded in a physics oracle rather than hand-shaped, which is a distinct rung of reward provenance.

### Optimization of global production scheduling with deep reinforcement learning

Near-duplicate companion to the ASMC 2018 paper by the same Fraunhofer and Infineon team: cooperative
DQN agents are trained with user-defined objectives to optimise global production scheduling, validated
on a small scenario. The two papers should be treated as one contribution with two venues when counting
distinct works, though they are separate publications with separate DOIs. This is the more heavily cited
of the pair.

### Decision-making and confrontation in close-range air combat based on reinforcement learning

Builds a close-range air combat environment around a six-degree-of-freedom F-16 model derived from
open aerodynamic data, with airborne equipment and a 3D visual simulation platform, and folds expert
strategy priors, curiosity-driven rewards, and curriculum learning into the environment. An optimised
self-play scheme with LSTM layers reaches over 90 per cent win rate against classical single-agent
baselines and over 75 per cent against humans. Note the curriculum and curiosity components: the rung
is hand-authored but staged, which is a step above a static environment.

### Towards a Robot Simulation Framework for E-waste Disassembly Using Reinforcement Learning

Proposes a simulation framework for training and testing RL on robotic unscrewing during e-waste
disassembly, using ROS as middleware, Gazebo with the ODE solver for physics, and MoveIt as controller.
The architecture explicitly leaves a slot for the user to drop in their own environment, and the authors
fill it with an OpenAI Gym environment to exercise the framework. Classified `infra` because the
scaffold, not any particular task, is the deliverable.

### Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code

Provides an RL environment for training models that give natural-language feedback on buggy code, made
of two parts: Coffee, a dataset of human code-edit traces and human-written feedback, and CoffeeEval, a
reward function that scores feedback by whether the revised code passes unit tests. CoffeeEval gives
more accurate reward than a GPT-4 reward model, and feedback models trained in the gym lift open-source
code LLMs towards closed-source performance. A good example of an executable, test-grounded reward
replacing a learned preference model in the LLM-agentic cell.

### Robust Design for IRS-Assisted MISO-NOMA Systems: A DRL-Based Approach

Reformulates a robust beamforming and phase-shift optimisation problem for intelligent reflecting
surface assisted MISO-NOMA systems into an RL problem so that DRL agents can solve it under channel
state information uncertainty. The paper is explicit about the three features it must specify to turn
the optimisation into an environment (state, action, reward), which is a compact illustration of the
optimisation-to-MDP translation pattern. Otherwise a standard application.

### Comparison of Various Reinforcement Learning Environments in the Context of Continuum Robot Control

Systematically varies the environment design for a three-section planar continuum robot controlled by
DDPG, holding the algorithm fixed and sweeping reward function formulations. The headline finding is
that environment design choices, reward shaping in particular, dominate measured performance. This is a
controlled environment ablation rather than an application, which makes it a useful `design` citation
for the argument that environment design is an experimental variable in its own right.
