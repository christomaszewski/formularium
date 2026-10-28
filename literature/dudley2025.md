---
id: dudley2025
citation: Dudley, C., Magdaleno, R., Harding, C., Sharma, A., Martin, E. & Eisenberg, M. 2026. Mantis: a foundation model for mechanistic disease forecasting. arXiv:2508.12260v4 [cs.AI], 22 Jan 2026 (preprint; first posted 2025 as the arXiv number shows; v1 title "Mantis: A Simulation-Grounded Foundation Model for Disease Forecasting")
doi: 10.48550/arXiv.2508.12260
read: 2026-10-27, lightly: abstract, the introduction summary, the discussion of limits and the methods summary of the simulation; the per-disease tables were not read; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 11 of 11 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [COVID-19, influenza, dengue, hepatitis B, smallpox, scarlet fever]
crops: []
regions: [none]
processes: [foundation model, synthetic data, zero-shot forecasting, mechanistic simulation, observation model, simulation-trained model]
records: []
datasets: []
files: [syn1027_dudley2025.pdf (the 2026-10-27 drop)]
---

# Dudley et al. 2026: a forecasting model trained only on 400 million simulated days, tested on real series for six diseases (human disease)

Mantis is trained entirely on output of a modular mechanistic simulator passed through an observation model, with no real data in training, and used zero-shot on real series for six human diseases. It is compared with 48 forecasting models. No record: a method. A preprint.

**Read this first.** Human infectious disease, not a plant, and no fine-tuning on real data at all (simulation-only, zero-shot). The headline ranks (lowest MAE on early-pandemic COVID-19 forecasts; top two on the other five diseases) are the authors' own claims (l. 18-20); the per-disease tables and the scores were not read, so no skill number is given here. There is no real-only arm of the same network; the comparators are other models.

## What it holds

- **Simulator** (l. 141-142): the authors' own modular mechanistic simulator (several transmission modes and population structures, per the reading agent), its output passed through an observation model for "underreporting, stochasticity, and reporting delays" (l. 141). It is not stated to be calibrated to the real series; nothing real is in training (l. 14, 18).
- **Synthetic volume** (l. 142): over 400 million simulated days. The authors say it is unknown whether this scale is needed (l. 599).
- **Real data**: used for evaluation only. Six diseases: seasonal influenza, early COVID-19, dengue, hepatitis B, smallpox and scarlet fever (l. 147-149); sources not read.
- **Validation design** (l. 16, 18): real series for six diseases against 48 forecasting models; for COVID-19 a backtest on early-pandemic forecasts the model "had not previously seen" (l. 19), against CDC COVID-19 Forecast Hub submissions, statistical baselines (exponential smoothing and SARIMA), an LSTM and a time-series foundation model (l. 171-173).
- **Claims** (l. 18, 20): lower mean absolute error than all models in the Hub on early-pandemic COVID-19; "consistently ranked in the top two" on the other diseases across metrics (the authors' own claim; numbers not read).
- **A failure** (l. 485): the 2004 dengue surge in Alagoas, Brazil, was forecast 18 weeks too early, with the peak height close; the authors call it a failure of temporal calibration.
- **Authors' limits** (l. 592, 599, 604, 609): when simulation-trained models fail is an open question; generalisation beyond the simulated regimes is shown but depends on the diversity and realism of the simulations; the model inherits the systematic biases of the mechanistic models it was trained on.

## Dependence

- Trained on the authors' own simulator and observation model; nothing computed from a disease model of another group in the lines read. The authors say the biases of the simulator pass to the model (l. 609). The paper is cited by `lemaitre2026` as a related method.

## Bearing (2026-10-27)

- **The extreme case of D60:** no real data in training, a very large and diverse set of simulations, judged on real series. It shows that a simulator-only model can be competitive, by the authors' own report, when the simulated space is broad; the per-disease numbers were not read, so the size of the gain is unknown here.
- **D45 and TRUTH-METHOD:** the model is kin to its simulator by construction and the authors state that it inherits the simulator's biases (l. 609). The caption of a figure notes a chronic, bloodborne disease type absent from the training set, forecast in Florida (l. 487): the closest this paper comes to an out-of-family check, shown as an example, not scored in the lines read.
- **Not shown:** a plant or a vine, any fine-tuning, a real-only arm, or per-disease scores in what was read.
