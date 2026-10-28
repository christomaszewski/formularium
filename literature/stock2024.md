---
id: stock2024
citation: Stock, M., Pieters, O., De Swaef, T. & wyffels, F. 2024. Plant science in the age of simulation intelligence. Frontiers in Plant Science 14:1299208
doi: 10.3389/fpls.2023.1299208
read: 2026-10-27, lightly: abstract, introduction and the sections on surrogate modelling and simulation-based inference (Europe PMC full-text XML, converted to text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [various]
regions: [none]
processes: [surrogate model, simulation-based inference, approximate Bayesian computation, digital twin, mechanistic-ML coupling, synthetic data, perspective]
records: []
datasets: []
files: [syn1027_stock2024.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Stock et al. 2024: perspective on surrogate models and simulation-based inference for plant science (review)

A perspective on nine "simulation intelligence" motifs for plant and crop science, of which surrogate models and simulation-based inference bear on training from a simulator. No record: a review, with no measured result of its own and no plant-disease example in the parts read.

**Read this first.** A perspective, not a test. It states what surrogates and approximate Bayesian computation are and claims speed, not fidelity to field data. The only disease example it names for simulation-based inference (Cavanagh et al. 2021, Asian soybean rust) was not read.

## What it holds

- **Surrogate** (l. 14): "A surrogate data-driven model is trained to mimic the mechanistic model's output accurately", and, "when properly trained", can be "several magnitudes faster" while behaving nearly identically (cited from Gherman et al. 2023). The claimed gain is speed; agreement with the field is not claimed.
- **Couplings** (l. 14, cited from Zhang et al. 2023): crop-model output as input to a machine-learning model (in series), data assimilation in a crop model (in parallel), or replacement of part of a crop model by a learned module.
- **Simulation-based inference** (l. 47): in approximate Bayesian computation "the simulator generates synthetic data by sampling parameters" from a prior; synthetic data are summarised (for example total biomass) and compared with observations, and the parameter values whose summaries come close are kept. The real data judge the simulator.
- **Motivation** (l. 10): process models "remain highly species-specific, complex, and difficult to calibrate due to many interlinked parameters" (cited from Wallach et al. 2021).
- **Disease example** (l. 47): approximate Bayesian computation used "to characterize the morphodynamic progression of Asian soybean rust" (Cavanagh et al. 2021), cited only.

## Dependence

- Secondary source. None recorded.

## Bearing (2026-10-27)

- **D45 and D58:** the "train on the simulator" route is the surrogate: a learned model that mimics the simulator, so it inherits the simulator's formulations and its speed gain does not make it truer. That supports the rule that only real data show a variable is real.
- **D60 and TRUTH-METHOD:** simulation-based inference is the form in which synthetic data are compared with real summaries; it fits the calibrated twin-experiment idea but the review has no measured case for a plant disease.
- **Not shown:** any score on real data for a model trained on simulated seasons; Cavanagh et al. 2021 is a lead.
