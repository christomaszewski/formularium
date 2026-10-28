---
id: johnston2023
citation: Johnston, D.B., Pembleton, K.G., Huth, N.I. & Deo, R.C. 2023. Comparison of machine learning methods emulating process driven crop models. Environmental Modelling & Software 162:105634
doi: 10.1016/j.envsoft.2023.105634
read: 2026-10-27, lightly: abstract, the design (section 2), the training-location and unseen-location results (tables) and the discussion of covariate shift, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 18 of 18 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [chickpea]
regions: [Australia]
processes: [emulator, crop model, APSIM, synthetic data, covariate shift, out-of-range test, random forest, MARS, neural network]
records: []
datasets: []
files: [syn1027_johnston2023.pdf (the 2026-10-27 drop)]
---

# Johnston et al. 2023: three machine-learning emulators of APSIM-NextGen chickpea, good in range and wrong at unseen locations (crops, chickpea)

An artificial neural network (ANN), multivariate adaptive regression splines (MARS) and a random forest (RF) are trained to reproduce APSIM-NextGen chickpea outputs at seven Australian locations, then tested on a held-out 20 % of those locations and on two unseen locations. No record: a method, on simulator output only.

**Read this first.** Synthetic data only: the emulators are never judged against field data (no real samples; no real-only baseline). The result that matters is the failure at the unseen locations, which is measured once on two locations pooled. The abstract says seven outputs (l. 37); the reading agent counted six in the tables.

## What it holds

- **Simulator** (l. 37, 235-239): APSIM-NextGen chickpea at seven locations, 120 years (1900-2019), 26 sowing dates and six cultivars; whether it was calibrated to field data is not stated in the lines read.
- **Synthetic samples** (l. 521-523, 552): 130,928 data points in all; the emulators trained on 80 % and were validated on the unused 20 %, 26,185 points per target (l. 100-102, 412, 521). No real samples.
- **Validation design** (l. 214-215, 596): random 20 % of the training locations; and two extra locations (Goondiwindi, Queensland, and Mildura, Victoria; l. 207-209) outside the original seven, for further assessment.
- **In range** (l. 38, 395, 408, 422): R2 above 0.95 for the outputs at the training locations. Held-out biomass: ANN R2 0.923, RMSE 102 kg/ha; MARS 0.902, 115 kg/ha; random forest 0.995, 27 kg/ha.
- **Unseen locations, R2 / COELM** (Table 6, l. 610, 613-614, 623-624, 633-634): flowering date held for all three (ANN R2 0.98, COELM 0.88). Biomass: ANN 0.76 / 0.35 (RMSE 260 kg/ha), MARS 0.62 / -7.25 (mean bias +1315.6 kg/ha), RF 0.20 / 0.02. Grain weight: ANN 0.79, MARS 0.48 / -6.28 (RMSE 932 kg/ha), RF 0.10 / -0.09. A negative COELM means worse than predicting the mean.
- **Cause** (l. 642, 649, 789, 799-803): all three failed on biomass and yield at the unseen locations while phenology timing held; the unseen locations fell outside the training ranges. Mildura's soil was the only sandy loam and had the lowest water holding capacity of any soil; the authors call it covariate shift and warn that all patterns of input factors must be in the training data.

## Dependence

- Emulates APSIM-NextGen chickpea (configuration from CSIRO, acknowledged in the paper); R packages for the three methods. Nothing computed from a disease model.

## Bearing (2026-10-27)

- **A measured failure outside the range of the simulated training set.** A random held-out split gave R2 0.90 to 0.995 for biomass; two unseen sites gave 0.20 to 0.76. If an Agrarium emulator or pretrained model is checked only on random held-out simulated seasons, it will look this good and mean this little (TRUTH-METHOD asks for an evaluation family that shares no substantive dependency with what the engine runs; held-out seasons of the same simulator are not that).
- **D60:** synthetic outcomes test robustness, never establish a feature. This paper is the robustness test, run on the emulator; it also shows that one unfamiliar soil is enough to break biomass and yield while timing survives.
- **Not shown:** any comparison with field data, a pretraining or fine-tuning step, a plant disease, or more than two unseen places.
