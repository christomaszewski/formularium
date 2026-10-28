---
id: morales2023
citation: Morales, A. & Villalobos, F.J. 2023. Using machine learning for crop yield prediction in the past or the future. Frontiers in Plant Science 14:1128388
doi: 10.3389/fpls.2023.1128388
read: 2026-10-27, lightly: abstract, the design, the results on data partitioning (Figure 3 and the text on Table 8) and the discussion; Table 8 and Supplementary Table S9 were not read; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 14 of 14 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [wheat, sunflower]
regions: [Spain]
processes: [crop model, synthetic data, yield prediction, data partitioning, validation design, random forest, neural network, forecasting, baseline]
records: []
datasets: []
files: [syn1027_morales2023.pdf (the 2026-10-27 drop)]
---

# Morales and Villalobos 2023: how the train-test split changes the score of yield models fitted to simulated farms (crops, wheat and sunflower)

Uses two crop models (CERES-Wheat in DSSAT, and OilcropSun) to make a synthetic set of farm yields in five areas of Spain, then fits regularised linear models, random forests and neural networks and compares random with time-ordered train-test splits. No record: a method on synthetic data.

**Read this first.** All the data are crop-model output; there are no field yields, so this tests validation design, not sim-to-real. It has no pretraining or fine-tuning step and no real-only baseline; the baseline it uses is the farm's own average simulated yield. Table 8 and Supplementary Table S9, where the random-split numbers are, were not read.

## What it holds

- **Simulators** (l. 38-41, 111, 658): CERES-Wheat (DSSAT 4.8) for wheat and OilcropSun for sunflower, 2001-2020, in five areas of Spain, with farms that differ in soil depth, cultivar, sowing date, nitrogen and irrigation. Not calibrated to field yields; the simulated means and variation were compared with provincial statistics for Cordoba and Granada and found close (l. 658; Table 5 not read). Farms per region 15, 12, 12, 12 and 11 (l. 171-173; 62 farms, arithmetic, not printed).
- **Real samples**: none. Provincial statistics were used only to check simulated means.
- **Validation design** (l. 55, 649, 661): time-ordered splits (older years train, newest test) to test forecasting; training periods of 5, 10 and 15 years with the last five years (2016-2020) as test (Figure 3 caption, l. 641; text l. 670); and, for comparison, random splits.
- **Scores** (abstract, l. 58-62): root mean square error as a percent of mean yield, ordered split: random forest 35-38 %, neural networks 37-141 %, regularised linear models 64-65 %. The baseline, the farm's average yield in the training years, scored 42 %. So the best model gained 7 points (arithmetic, not printed) over a sensible baseline, and the authors say real-world skill will be closer to the baseline because seasonal weather forecast error was not included.
- **The split changes the answer** (l. 661, 669): with 75 % of the data in training, a random partition cut the RMSE by up to a factor of 5 against training on the first 15 years; the authors read the gap as interpolation against extrapolation.
- **Authors' advice** (l. 68, 69, 682): do not use random partitioning to test a forecasting model; validated crop models can be used before data collection to establish the potential advantage of a machine-learning approach; the apparent success of machine learning in many yield studies may come from random partitioning (Khaki et al. 2020 is the example, cited, not read).

## Dependence

- Fully dependent on CERES-Wheat (DSSAT 4.8) and OilcropSun output; the fitted models are kin to those simulators by construction. No disease model.

## Bearing (2026-10-27)

- **A split-design lesson for D45 and D60:** the same simulated data gave a factor of up to 5 lower RMSE under a random split than under a time-ordered one. Any Agrarium score from held-out simulated seasons should say which split it used; D60's synthetic outcomes test robustness, and a random split is not even that for a forecasting use.
- **TRUTH-METHOD:** a score on held-out simulated seasons is a development figure, and this paper shows how far the split alone moves it. It also gives a check-before-data idea (l. 69): use the validated simulator to see whether a learner can beat a plain baseline at all, before collecting data. Here 35 % against 42 % is the size of gain.
- **Not shown:** anything on real yields, a pretrained model, or a plant disease.
