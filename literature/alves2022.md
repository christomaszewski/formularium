---
id: alves2022
citation: Alves, K.S., Shah, D.A., Dillard, H.R., Del Ponte, E.M. & Pethybridge, S.J. 2022. Safer and Smarter: Leveraging Transfer Learning and Data Fusion of Disease and Environmental Data for Modeling Plant Disease Risk. OSF Preprints (not peer reviewed; supplement dated 2025-01-06)
doi: 10.31219/osf.io/9tgau
read: 2026-10-27, lightly: abstract, introduction, materials and methods, results, discussion and the start of the supplement, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 13 of 13 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [white mold of snap bean (Sclerotinia sclerotiorum)]
crops: [snap bean]
regions: [USA, New York]
processes: [data fusion, reanalysis, kriging downscaling, random forest, SHAP, logistic regression, optimism correction, decision curve, overfitting, forecasting]
records: []
datasets: []
files: [syn1027_alves2022.pdf (the 2026-10-27 drop)]
---

# Alves et al. 2022: reanalysis-filled inputs for a 356-field snap bean white mold survey, random forest against logistic regression (analogue crop, preprint)

Fits a random forest and then a three-variable logistic regression to a three-season field survey of white mold of snap bean, with weather and soil taken from a reanalysis rather than measured. No record: a method, and a preprint.

**Read this first.** Snap bean, not a vine: an analogue for what happens to a small field set whose inputs were never measured. It is a preprint, not peer reviewed. The "transfer learning" of the title is the move of three variables chosen by a random forest into a logistic regression, not pretraining on another data set (l. 4). The random forest scores are apparent (fitted and scored on the same fields), not held-out. The only skill number that is corrected for optimism is the logistic regression's.

## What it holds

- **Real data** (l. 9): 356 commercial snap bean fields in central and western New York in 2006 (88), 2007 (144) and 2008 (124); a field is positive if white mold was seen on at least one of 50 or more plants; 20% positive (73 cases, l. 74). The survey was made earlier (cited from Shah et al. 2019).
- **Labels are observed**, presence or absence, not computed by a model (l. 9).
- **Inputs, weather** (l. 12-13): ERA5-Land hourly reanalysis (air and dew-point temperature at 2 m, surface pressure, soil water and temperature at 0 to 7 cm), used "because the available ground weather station network was sparse relative to the snap bean field locations". Hourly series were made daily means, then downscaled from 0.1 degree (9 km) to 0.02 degree (about 1.57 km) by kriging with elevation as covariate (soil temperature for soil moisture). Humidity and vapour pressure deficit were derived from the 2 m temperatures. Sunshine and rain were taken from ERA5-Land and not downscaled (l. 25).
- **Augmentation of inputs** (l. 34): canopy gap, measured only at the visits, was predicted at 35 days after planting by a random forest (mean squared error 2.52, with bias at the extremes) and used as a feature. Soil properties came from the POLARIS soil database (named in a supplementary figure caption, l. 165). No simulated disease and no generated seasons.
- **Random forest on 16 variables** (l. 34): C-statistic 0.996 (CI 0.993 to 1) and Brier score 0.043 on the data it was fitted to; a 7-variable forest 0.993 (CI 0.988 to 0.998), Brier 0.054. Predicted risks sit near 0 and 1 and are badly calibrated (low risk overpredicted, high risk underpredicted).
- **Logistic regression on three variables** (l. 37, 61-62, Appendix S1 at l. 260): the top three SHAP variables, each as a restricted cubic spline: mean air temperature from planting to 4 days after planting, mean soil water from 40 to 49 days, total rain from 36 to 50 days. C-statistic (AUROC) 0.799 (95% CI 0.748 to 0.861) apparent and 0.780 after bootstrap optimism correction (Table 1; apparent first, as the footnotes at l. 66 say).
- **Sample size** (l. 74): 73 events and 6 parameters, 12 events per parameter.
- **Decision value** (l. 37): up to 40% fewer unnecessary sprays at action thresholds of 10 to 25%; no benefit over spraying every field at 5% or less.
- **Variables** (l. 34, 74): SHAP ranks air temperature near planting and soil moisture among the strongest; the authors "refrain from attempting to attach a causal mechanism".
- **Validation design**: internal only, by bootstrap on the same 356 fields; no year or site held out, so the three seasons are not tested apart. An earlier analysis of the same fields reached random forest accuracy 73% (cited from Shah et al. 2019, l. 8).

## Dependence

- Labels: observed. Inputs: ERA5-Land (a model output), a kriging downscale of it, a soil database and a fitted canopy-gap model. No mechanistic disease model (a Sclerotinia model by Salotti and Rossi 2023 is cited, not used). Shares two authors (Shah, Pethybridge) with the survey's earlier analysis (cited) and Shah with shah2013, shah2014 and shah2023: a flag only.

## Bearing (2026-10-27)

- **D60 (synthetic inputs for real data):** a measured case of filling a survey's missing inputs from a reanalysis plus a downscale plus a fitted gap model, then scoring against observed labels: an optimism-corrected C of 0.78. No run on station weather is printed in the parts read, so the cost of the filled inputs is not measured. One physical source per gap, not several.
- **D58 (variable search):** the variables kept were temperature near planting, soil water and rain over the flowering window, chosen by SHAP on the full 356 fields. Nothing here was tested on a held-out year or site, so none of them is shown to hold. Soil moisture is a variable the project's hourly outbreak records do not hold.
- **Caution for models fitted to few labels:** 0.996 apparent against 0.78 corrected is the gap a random forest on a few hundred labels can show; a simulator-trained model scored in sample would look the same.
