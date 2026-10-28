---
id: maestrini2022
citation: Maestrini, B., Mimić, G., van Oort, P.A.J., Jindo, K., Brdar, S., Athanasiadis, I.N. & van Evert, F.K. 2022. Mixing process-based and data-driven approaches in yield prediction. European Journal of Agronomy 139:126569
doi: 10.1016/j.eja.2022.126569
read: 2026-10-27, lightly: abstract, introduction, section 4.7 (mixed approaches, metamodels) and section 4.7.1 (the proposed transfer-learning method and negative transfer); the rest of the review was not read; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 11 of 11 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [none]
processes: [review, metamodel, transfer learning, negative transfer, crop growth model, synthetic data, pretraining, hybrid model]
records: []
datasets: []
files: [syn1027_maestrini2022.pdf (the 2026-10-27 drop)]
---

# Maestrini et al. 2022: a review of mixing crop growth models and machine learning, with a metamodel-plus-transfer-learning proposal (crops)

A review of yield prediction by process-based and data-driven models, sorting the cases where the two are mixed into three kinds and proposing a fourth way: a neural-network metamodel trained on crop-model output, then retrained on few observations. No record: a review, with no data or scores of its own.

**Read this first.** A proposal, not a test: the transfer-learning method of section 4.7.1 is described and not evaluated here (a companion test is `kallenberg2023`, same group). Almost everything below is the authors summarising or advising, so it is cited from other papers or stated as opinion; only the abstract and sections 4.7 and 4.7.1 were read. Residual learning of a crop model's error is not among the three cases the abstract names.

## What it holds

- **Three integration cases** (l. 40, abstract): crop growth models used to engineer features and expand the predictor space; data-driven methods used to estimate missing inputs of process-based models; data-driven metamodels built to reduce the computing load. The authors then propose a method based on metamodels and transfer learning.
- **Proposal** (l. 601-607, 611-615): a metamodel trained on synthetic data from a crop model, then retrained on the few observations. A new input could be added as a new layer and only part of the network retrained; the example is a leaf-moisture sensor, a state variable "normally not simulated in crop growth models" (l. 605-607). It builds on Pylianidis et al. 2022 (cited, not read), who demonstrated machine-learning metamodels on synthetic data for pasture nitrogen response and evaluated in-silico transfer-learning scenarios (l. 613-615).
- **Negative transfer** (l. 611, 614, 626, 633, 637; cited from Weiss et al. 2016 for the term): a transferred model that does no better than a model trained only on the few target data; it often results from a weakly related source domain. The example given is an output-range mismatch: a metamodel trained on wheat (typical yield 2-8 t/ha) and used for potatoes. Advice: take source data from a domain close to the target, and make synthetic data that reflect the target conditions instead of generic metamodels.
- **Obstacle named** (l. 644): the lack of large, standardised field-level observation sets for the transfer step.
- **A cited metamodel** (l. 565): one cited study cut computing time at the expense of precision (metamodel r2 0.93, cited from that study).
- **No real-only baseline, no scores of its own**: the review reports none.

## Dependence

- Builds on Pylianidis et al. 2022 (simulation-assisted learning for digital twins), Tartarini et al. 2021 and Obsie et al. 2020 (named by the reading agent, not read). Authors in common with `kallenberg2023` and `pylianidis2024` (a flag).

## Bearing (2026-10-27)

- **Negative transfer is the named risk for a model pretrained on simulated data.** A simulated source "close to the target" is the advice (l. 633, 637): Agrarium's synthetic seasons should reflect the real site's conditions, which is also what D60 asks of synthetic inputs (several physical models per gap).
- **The leaf-wetness sensor example** (l. 605-607) is the nearest statement in the strand to adding an observation the simulator does not produce, to a pretrained model: D58's real data judge such a variable; the simulator cannot supply it.
- **Not shown:** any test of the proposal here, a plant-disease case, or residual learning of a process model's error.
