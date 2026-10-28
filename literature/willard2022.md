---
id: willard2022
citation: Willard, J., Jia, X., Xu, S., Steinbach, M. & Kumar, V. 2022. Integrating scientific knowledge with machine learning for engineering and environmental systems. ACM Computing Surveys 55(4):Article 66
doi: 10.1145/3514228
read: 2026-10-27, lightly, for leads: section 3.2 (physics-guided initialization), sections 3.4.1-3.4.2 (residual modelling and physics output as input) and the methods summary near l. 1076; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 12 of 12 quotes found at their lines by scripts/verify_quotes.py; the file is the arXiv version 2003.04919v6, 14 Mar 2022
status: read
diseases: []
crops: []
regions: [none]
processes: [review, physics-guided machine learning, pretraining, residual modelling, hybrid model, process model as input, synthetic data]
records: []
datasets: []
files: [syn1027_willard2022.pdf (the 2026-10-27 drop)]
---

# Willard et al. 2022: a survey of ways to combine scientific models with machine learning (review, mostly lakes and physics)

A survey of how scientific knowledge is combined with machine learning in engineering and environmental systems: physics-guided loss, initialisation (pretraining on a process model's simulated data), architecture, residual modelling, and hybrid models that take process output as input. No record: a review, with no measurement of its own.

**Read this first.** A review read only for leads (three sections). Everything in it is cited from other papers: the examples are the group's own lake work and a robotics case. It is not about plants or crops.

## What it holds

- **Physics-guided initialisation** (l. 686, 691-695, 1092): pretraining on a physics-based model's simulated data is one way to give an informed starting state. The review's example is the lake temperature work of Jia et al., which it summarises as showing that pretraining even on data from a physical model with an incorrect parameter set cuts the training data needed (l. 693), and that Read et al. found initialisation plus a physics loss generalise better to unseen scenarios (l. 695) (`jia2021`, `read2019`). With initialisation, domain expertise can pick the most relevant synthetic data and the machine-learning model can remain process-agnostic (l. 1092).
- **A robotics case, cited** (l. 701): simulation pretraining reduced the real data needed by a factor of 50 for object grasping (cited by the review from another paper; not checked here).
- **Residual modelling** (l. 949-954, 1082): the oldest and most common hybrid; a machine-learning model, "usually linear regression", learns the errors of the physics-based model against observations. Its limitation: it cannot enforce physical constraints, because it models the errors and not the physical quantity. It needs no process knowledge beyond an operational mechanistic model run at prediction time.
- **Process output as an input** (l. 991-993): feeding the physics model's output to the machine-learning model as one feature along with the driving inputs; cited from Karpatne et al. 2017 as improving lake temperature predictions.
- **No scores, no real-only baseline** of its own: the review reports none in the sections read.

## Dependence

- Cites Jia et al. 2019 and 2021 (lakes), Read et al. 2019, Jia et al. 2020 (river graph), Karpatne et al. 2017 and robotics simulators. The review's authors are also authors of `jia2021`, `jia2020` and `read2019` (a flag).

## Bearing (2026-10-27)

- **Names the three hybrid designs that the strand's measured papers realise:** pretraining (`jia2021`, `read2019`, `liu2024`), process output as input (`sajid2022`, the LSTM-q arm of `liu2024hess`) and residual learning (`liu2024hess`). For Agrarium's plan (D45, D58, D60) this is the vocabulary for stating which design a pilot tests.
- **Residual learning has the clearest limit for a simulator-trained model:** it needs the process model at run time and cannot enforce physical constraints (l. 954). No crop or disease example is in the sections read.
- **Not shown:** any plant disease use, or any measured score here.
