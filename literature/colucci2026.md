---
id: colucci2026
citation: Colucci, G. P., Filipescu, E., Scatozza, F. & Trinchero, D. 2026. Machine learning methods for leaf wetness prediction using agrometeorological data. IEEE Transactions on AgriFood Electronics (accepted version, early access), pp. 1-9
doi: 10.1109/TAFE.2026.3711283
read: 2026-10-18, LIGHT, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py; Tables I-VI read from the page images; the appendix grid-search tables VII-XI not transcribed; accepted version (repository cover page)
status: read
diseases: []
crops: [grapevine]
regions: [Italy, Sardinia, Tuscany, Marche, Piedmont]
processes: [leaf wetness, wetness classification, machine learning, capacitive sensor, soil moisture, edge inference]
records: []
datasets: []
files: [r_10_1109_tafe_2026_3711283.pdf (the 2026-10-18 drop, second pass)]
---

# Colucci et al. 2026: machine-learning wet/dry classifiers for leaf wetness, with an open vineyard dataset

Six classifiers (LDA, decision tree, random forest, k-NN, linear and RBF SVM) predict whether a leaf side is wet from eight hourly weather and soil features, against a capacitive sensor, at seven Italian sites. No record: a comparison of fitted classifiers, not a formulation.

**Open dataset, non-commercial.** The data are on Mendeley Data, doi 10.17632/sd4b8vpvyb.1, under **CC BY-NC 4.0** (l. 77, 494-497). It is the one open vineyard leaf-wetness dataset this search found. The non-commercial licence is why it is not copied into this public MIT repository: a record may say where it is held. Not printed: the file format, the period of record, the time range per site, whether all seven sites are in the release.

## What it holds

- **Ground truth** (l. 163-173, 230-235): iXemWine stations (running across Italy since 2018) with the group's double-sided capacitive sensor (`filipescu2024`), tilted down 30 degrees; soil sensor buried 30 cm and rotated 45 degrees. Wet is a sensor reading above a 20 % label, taken from Detka et al. 2025 as "a threshold associated with visual inspection"; the 20 % is about the 65th percentile (top side) and 68th (bottom) of the sensor values. Sensor height and period are not printed.
- **Sites** (Table I, l. 132): seven, elevation 33 to 434 m; 1, 125 m valley by the sea; 2, 33 m sea side; 3, 242 m medium hilly; 4, 258 m high hilly; 5, 187 m medium hilly; 6, 434 m medium mountain; 7, 418 m mountain valley (Sardinia, Tuscany and Marche, Piedmont).
- **Data** (l. 219-254): 54 706 hourly samples, 54 643 kept after screening; all variables hourly means except rain (hourly intensity) and gust (hourly maximum). Inputs: air temperature and RH, rainfall, soil temperature and volumetric water content, wind speed and gust, day of year, hour. 80 % / 20 % split; training set 36 % wet (top) and 32 % wet (bottom), balanced by random undersampling; fivefold cross-validated grid search.
- **Table III, top side, 20 % label, test balanced accuracy** (l. 376): LDA 0.8139, DT 0.9136, RF 0.9290, k-NN 0.9215, linear SVM 0.8191, SVM 0.9067. **Table IV, bottom** (l. 382): LDA 0.7445, DT 0.9340, RF 0.9471, k-NN 0.9283, linear SVM 0.7455, SVM 0.8931. RF top: precision wet 0.8652, recall wet 0.9378, F1 wet 0.9001; RF bottom 0.8853, 0.9504, 0.9167.
- **Label sensitivity** (Table V, l. 436), balanced accuracy at 20 / 30 / 40 %: RF top 0.9290 / 0.9135 / 0.9118; RF bottom 0.9471 / 0.9445 / 0.9450; LDA top 0.8139 / 0.8062 / 0.7990.
- **Soil features** (Table VI, l. 410, 442): nonlinear models gain up to 6 % (top) and 13 % (bottom) balanced accuracy; RF top 0.9290 with all features, 0.8732 with no soil; RF bottom 0.9471 against 0.8359. Linear models are flat.
- **Parameters** (l. 311, 316): decision tree minimum samples split 20; k-NN k = 3. Wet samples are rare below 60 % RH and above 25 degC (l. 287).
- **Edge** (l. 449-451): the tree on an STM32L072 via emlearn, 15.4 KiB, 14 microseconds per prediction.
- **Literature models, not scored** (l. 82, 89): RH above 90 % (Gleason et al. 1994) and dew-point depression (Gillespie et al. 1993) are described in the introduction only.

## Dependence

- The label threshold is Detka et al. 2025's; the sensor is `filipescu2024`'s, with three authors in common (shared-author flag, shared sensor). No formulation is computed from another model's equations. The classifiers are textbook algorithms.

## Bearing (2026-10-18)

Strand 2 (weather) and strand 5 (the wetness label as a sensor reading).

- **Comparison with the RH >= 90 % stand-in: none.** No RH-threshold model is scored on these data, so no accuracy for the engine's stand-in comes from this paper. The dataset has RH, temperature and the sensor, so the stand-in could be scored on it, but only if the file is obtained and its licence respected.
- **What it does show:** a learned classifier from eight hourly features reaches balanced accuracy 0.93 (top) and 0.95 (bottom), and RH and temperature alone are not enough: removing soil features costs up to 6 to 13 points for the nonlinear models. Soil moisture is not a variable the engine has.
- **The label is a cut:** the 20 % cut is the 65th to 68th percentile; moving it to 40 % costs the forest 0.2 (bottom) to 1.7 (top) points of balanced accuracy and LDA 1.5 (top) to 2.2 (bottom). Top and bottom leaf sides differ: linear models lose about 7 points on the bottom side.
- **Kind of result:** a test-set score at seven sites, an 80/20 split of hourly samples; the parts read do not say it was made by site or by date, so serial correlation between train and test is not excluded.
