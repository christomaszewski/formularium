---
id: kallenberg2023
citation: Kallenberg, M.G.J., Maestrini, B., van Bree, R., Ravensbergen, P., Pylianidis, C., van Evert, F. & Athanasiadis, I.N. 2023. Integrating processed-based models and machine learning for crop yield prediction. 1st Workshop on Synergy of Scientific and Machine Learning Modeling (SynS & ML), ICML 2023; arXiv:2307.13466v1
doi: 10.48550/arXiv.2307.13466
read: 2026-10-27, in full (a workshop paper of about five pages), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 35 of 35 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [potato]
regions: [Netherlands, Wageningen]
processes: [pretraining, synthetic data, metamodel, transfer learning, crop growth model, domain shift, leave-one-year-out, CNN]
records: []
datasets: []
files: [syn1027_kallenberg2023.pdf (the 2026-10-27 drop)]
---

# Kallenberg et al. 2023: a CNN pretrained on Tipstar potato simulations, fine-tuned on trial and commercial yields (crops, potato)

A three-stream convolutional network is pretrained on 86,000 runs of the Tipstar potato growth model, then fine-tuned on observations, first in silico (peat soils to sandy soils) and then on two real potato sets. Compared with the same network trained on real data only, with the crop model alone, and with an expert's linear regression. No record: a method, a short workshop paper.

**Read this first.** A workshop paper with two small real sets, one place. The real-data result is mixed and the authors say so: a hand-built linear regression beats the crop model and the pretrained network on both sets (l. 199-201, 224, 228). The in-silico numbers (peat to sandy soil) are simulator against simulator, not sim-to-real.

## What it holds

- **Simulator** (l. 72, 79, 96): Tipstar with default Dutch parameters, "not calibrated" for these data (l. 96); 86,000 entries, from 7 locations x 32 years x 32 soil types = 7,168 combinations with 12 random management simulations each (l. 79). The trial years were excluded from the synthetic set to prevent leakage (l. 130).
- **Real data** (l. 107, 119): field trials, n=303, 1994-2003; commercial fields, n=77, 2015-2020.
- **Validation design** (l. 135, 143-145, 157-159): real data, leave-one-out by weather year (new years), three seeds; in silico, pretrained on peat soils (n=10k), fine-tuned on sandy soils with only the last two layers free, at 50, 200 or 1,000 target examples, scarcity simulated by limiting the target set.
- **In silico, RMSE in t/ha at fine-tuning size 0 / 50 / 200 / 1,000** (Table 1, l. 218, 220): pretrained and fine-tuned 10.3 / 7.6 / 7.4 / 7.2; real-only (data-driven) not available / 11.2 / 11.0 / 7.5. Correlation r (l. 214, 216): 0.884 / 0.899 / 0.905 / 0.908 against not available / 0.767 / 0.790 / 0.902. The authors read it as 50 points matching real-only training on 1,000 (l. 269).
- **Real data, RMSE in t/ha, trials / commercial** (Table 2, l. 219-224): crop model alone 12.98 / 24.90; pretrained and fine-tuned metamodel 9.40 / 14.10; real-only network 15.80 / 14.10; expert linear regression 8.93 / 9.75. Correlation r (l. 212-217): crop model 0.70 / 0.63; metamodel 0.60 / 0.39; real-only 0.02 / 0.35; linear regression 0.64 / 0.72.
- **Read together** (Table 2, l. 212-224): on the trials pretraining beats real-only training (9.40 against 15.80) and the crop model; on the commercial fields it ties real-only training in RMSE (14.10 both) and is close in r (0.39 against 0.35); both lose to the linear regression (l. 201, 228).
- **Bias** (l. 178): the uncalibrated crop model systematically underestimated the commercial-field yield; the fine-tuned metamodel showed no systematic bias but high scatter.
- **Emulation of Tipstar** (l. 154): on held-out synthetic data RMSE 5.1 t/ha, r = 0.95 (in-distribution).
- **Authors' claim** (l. 265): pretraining on crop-model output beat real-only training; the linear regression "may still be preferred in practice" (l. 228).

## Dependence

- Trained on Tipstar output (Jansen 2008, cited); soil schematisation BOFEK2012 and real weather. The authors overlap with `maestrini2022` and `pylianidis2024` (a flag), and the group's earlier simulation-assisted learning is cited, not read.

## Bearing (2026-10-27)

- **The only crop paper in the strand with a real-only arm on real data**, and it shows a gain on one real set and a tie on the other, both behind a simple expert model. A fair reading for Agrarium: pretraining on a simulator is not shown to beat plain feature engineering when real data are small.
- **D45 and D60:** a metamodel fitted on the simulator is kin to it; the real check here was on yield, the variable both give. The in-silico soil shift is a robustness test of the kind D60 permits (synthetic outcomes test robustness) and the real sets are what judged it.
- **Not shown:** a disease, an epidemic simulator, a calibrated simulator arm, or more than one place.
