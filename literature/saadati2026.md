---
id: saadati2026
citation: Saadati, M., Panelo, J., Visentini, G.C., Sarkar, S., Messina, C. & Ganapathysubramanian, B. 2026. Uncertainty-aware neural emulation reveals climate-resilient maize traits at scale. arXiv:2605.22848v2 [cs.CE], 26 Sep 2026 (preprint)
doi: 10.48550/arXiv.2605.22848
read: 2026-10-27, lightly: abstract, introduction, the results on emulator accuracy and calibration, the discussion of limitations and the methods on the dataset and the network; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 15 of 15 quotes found at their lines by scripts/verify_quotes.py; a preprint, not peer reviewed
status: read
diseases: []
crops: [maize]
regions: [United States, Iowa, Illinois]
processes: [emulator, crop model, APSIM, synthetic data, uncertainty, SWAG, generative weather model, climate projections, random split]
records: []
datasets: []
files: [syn1027_saadati2026.pdf (the 2026-10-27 drop)]
---

# Saadati et al. 2026: a neural emulator of APSIM maize with predictive intervals, checked only against APSIM (crops, maize)

A fully connected network trained on two million APSIM maize runs reproduces 13 APSIM outputs (per the reading agent) and carries a predictive-interval layer (stochastic weight averaging, Gaussian). The authors use it to explore maize traits under future climate in Iowa and Illinois. No record: a method, on simulator output only. A preprint.

**Read this first.** A preprint, and no field data anywhere in the parts read: the emulator is judged only on 0.2 million random held-out APSIM runs (in-distribution), so the scores say how well it copies APSIM, not how well it predicts maize. The trait findings in the title were not read.

## What it holds

- **Simulator and synthetic samples** (l. 32, 108-110, 716): two million APSIM simulations from low-discrepancy sampling of 21 independent variables and one derived variable (22 model inputs); weather from a generative weather model trained on 1984-2023 observations and downscaled projections for 2025-2100 (l. 158-159). Calibration of APSIM to field data is not stated in the lines read.
- **Real samples**: none used for the emulator. The weather model uses historical daily weather for Iowa and Illinois counties (l. 672).
- **Validation design** (l. 716): a random partition, 1.8 million training and 0.2 million held-out test samples, scored against APSIM. In-distribution; no new site, new year or new climate split in the lines read.
- **Scores against APSIM** (l. 235, 268-269, 275): global normalised test R2 0.944 with 1.8 million training samples; R2 rises from 0.918 at 0.2 million to 0.944 at 1.8 million, and normalised test RMSE falls from 0.288 to 0.237. With the interval layer, R2 0.934 and RMSE 0.257 (a slight loss of point accuracy).
- **Calibration of the intervals** (l. 285, 287): 95 % intervals cover 95.67 % of held-out APSIM values (92.51 % to 98.07 % by output); the predictive standard deviation correlates only weakly with error (r = 0.473 with mean absolute error).
- **Weather model** (l. 161, 164): reproduces the four weather inputs of APSIM with correlation above 0.96 and R2 above 0.92; rainfall is the hardest (RMSE 2.019 mm per day on wet days).
- **Cost** (l. 638): about two minutes per APSIM run; the full question would need about 5.4 million runs (180,000 CPU-hours).
- **Authors' limits** (l. 589-590, 597): the emulator inherits APSIM's structural assumptions and any systematic bias in them; use beyond Iowa and Illinois needs locally representative training data.

## Dependence

- Emulates APSIM; inputs are a generative weather model and the NEX-GDDP-CMIP6 downscaled projections. Cites Johnston et al. 2023 (`johnston2023`) only as an example of an emulator application, chickpea yield prediction (l. 80), without its unseen-location failure.

## Bearing (2026-10-27)

- **Another in-distribution emulator score.** R2 0.944 on random held-out runs of the same simulator is the same kind of number as `johnston2023`'s in-range scores, which fell to 0.20-0.76 for biomass at unseen locations; this paper has no such unseen-place test. Under D60 it is a development figure, not a validation.
- **D45:** the authors' own statement that APSIM's biases pass to the emulator (l. 589-590) is the kinship point in one sentence.
- **Useful for scale:** 2 million runs for 22 inputs, and the prediction interval layer, are a design Agrarium could copy for screening candidate variables (D58), with real data judging the survivors. Nothing here shows that the interval is right about the real world.
- **Not shown:** field yields, a disease, a held-out region or year.
