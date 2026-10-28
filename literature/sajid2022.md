---
id: sajid2022
citation: Sajid, S.S., Shahhosseini, M., Huber, I., Hu, G. & Archontoulis, S.V. 2022. County-scale crop yield prediction by integrating crop simulation with machine learning models. Frontiers in Plant Science 13:1000224
doi: 10.3389/fpls.2022.1000224
read: 2026-10-27, lightly: abstract, the introduction summary of the earlier result, the section on APSIM calibration, and the caption of the with-and-without-APSIM comparison; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [maize]
regions: [United States, Corn Belt]
processes: [crop model, feature augmentation, ensemble, machine learning, yield prediction, APSIM, held-out years]
records: []
datasets: []
files: [syn1027_sajid2022.pdf (the 2026-10-27 drop)]
---

# Sajid et al. 2022: APSIM output as extra features for county corn yield models, tested on three future years (crops, Corn Belt)

Five machine-learning models and their ensembles predict county corn yield across 12 Corn Belt states, with and without variables simulated by APSIM (a regionally calibrated crop model) as extra inputs; held-out years are the last three. A context paper: the same group and method as `shahhosseini2021`. No record: a method.

**Read this first.** Feature augmentation, not pretraining and not residual learning: APSIM's output is an input, so the simulator is used at run time as well as in training. The with-versus-without-APSIM gain for 12 states is in Figure 8 (l. 730-732), which was not read; the text gives the ensemble score and the simulator-alone score only.

## What it holds

- **Simulator** (l. 194-196): APSIM with cultivar traits from regional-scale calibration; over 1984-2020 it alone captured 67 % of the variability in NASS county yields, RMSE 1.3 Mg/ha, RRMSE 16 % (Figure 2). The same calibrated version supplied the features (l. 196). The count of simulated samples is not printed in the lines read.
- **Real data** (l. 166, 229): USDA NASS county corn yields for the U.S. Corn Belt (1984 to 2020), 12 states, with weather from the Iowa Environmental Mesonet and SSURGO soils.
- **Validation design** (l. 52, 469): models trained on 1984 to 2017 and tested on the future years 2018, 2019 and 2020 (the previous years given as inputs in each prediction). New years; counties are not held out.
- **Score** (l. 49, 52, 196): the ensemble reached RRMSE of about 9 % for the test years, against 16 % for APSIM alone over the whole period (the two numbers are for different periods and procedures, so this is not a paired comparison). The abstract says accuracy increases by coupling crop modelling with machine learning (l. 46), and that errors were largest in counties with a low cropland ratio (l. 54).
- **Real-only baseline**: the models run without the crop-model variables are the baseline; their scores are in Figure 8, not read.
- **Earlier study, cited** (l. 127-128): adding crop-model output cut RMSE by 8 % to 20 % in three Corn Belt states (cited from Shahhosseini et al. 2021).

## Dependence

- Built on `shahhosseini2021` (same group and design; the held note on that paper records 7 to 20 %; this paper's own sentence, quoting the earlier study, says 8 % to 20 %). The simulator is APSIM, calibrated regionally, and its output enters as features. Authors in common with that paper (a flag).

## Bearing (2026-10-27)

- **A different use of a process model from pretraining:** the simulator's output as input at run time. It needs the simulator at prediction time, which Agrarium's engine would have, and it is the arm that did best in `liu2024hess` (process output as input). D58 fits: the simulator supplies candidate variables and real data judge them.
- **Held-out years, real targets, a calibrated teacher:** the check is on the yield the simulator also outputs. It is in the correct direction for D45 (real data judge the model) but gives no number in the text for the gain from the simulated variables alone.
- **Not shown:** a pretraining arm, a disease, or a result for held-out counties.
