---
id: cosseboom2023
citation: Cosseboom, Scott D. & Hu, Mengjun. 2023. Predicting ripe rot of grape, caused by Colletotrichum fioriniae, with leaf wetness, temperature, and the crop growth stage. PhytoFrontiers 3(3):303-313
doi: 10.1094/PHYTOFR-05-22-0060-R
read: 2026-10-13, in full (the accepted manuscript, 39 pages, from the publisher's open copy), by a reading agent (claude-haiku-5-5); 47 of 47 quotes found at their lines by scripts/verify_quotes.py; the Gompertz parameters (manuscript p. 17) and Table 2 (p. 30) read in the page images by the main session; journal, volume, pages and DOI from Crossref, since the manuscript prints none
status: read
diseases: [ripe rot]
crops: [grapevine]
regions: [Maryland]
processes: [infection, crop-stage susceptibility, forecasting, spray timing]
records: []
datasets: []
files: [cosseboom2022_phytofr.pdf]
---

# Cosseboom & Hu 2023: ripe rot risk from wetness, temperature and crop stage

The source of the two models `cosseboom2024` runs: six classifiers of infection from
wetness and temperature, times a Gompertz curve of cluster susceptibility by stage, scored
against 45 Maryland epidemics. From the University of Maryland.

## What it holds

- **Infection trials:** detached Merlot and Cabernet Sauvignon berries (1259 and 1249,
  l. 444) at 12-30 °C with 0-24 h of wetness in 4 h steps (l. 290), and 132 and 157
  potted-vine clusters inoculated before harvest at 12, 17, 22, 27 and 32 °C (l. 398,
  448) for 0-24 h (l. 404); a cluster counts as diseased at 3 % severity or more
  (l. 418). The abstract says 27 °C with 24 h gave 100 % in both greenhouse trials
  (l. 64); the Results give 100 % at every temperature but 12 °C in the first trial and
  only at 27 °C in the second (l. 734).
- **Environmental models:** a decision tree, ridge and LASSO logistic regressions (on
  wetness, temperature and their squares and cubes, l. 466-468), a neural network, a
  random forest and a support vector machine, fitted in JMP to each trial and to the
  pairs (l. 42, 430); no coefficient or tree is printed (they are in the authors'
  repository, l. 776-780). Tested on the other trial of the pair (Table 2, p. 30):
  accuracy 0.58-0.70, recall 0.03-0.34 on berries and 0.56-0.91 on clusters.
- **Crop-stage susceptibility:** a four-parameter Gompertz on the stage code 1-6 (bloom
  to harvest, BBCH 66-89, l. 610): LA 0.043, UA 0.974, GR 2.567, IP 4.331, R² 0.971
  (p. 17; l. 792-806), giving 0.043 to berry touch, 0.133 to veraison, 0.821 to
  pre-harvest and 0.961 to harvest (l. 810). Fitted to five bagging trials of Cosseboom
  & Hu 2022 (Phytopathology 112:1956-1964, not held), severities rescaled 0-1 per trial
  (l. 572, 606). Standard errors are not printed.
- **Risk** is the environmental probability times the susceptibility (p. 17, l. 622); a
  day is an infection event above a threshold chosen per model from 0.3 to 0.75
  (l. 662); wetness is RH above 90 % where no sensor was present (l. 648, after Beruski
  et al. 2019).
- **Validation:** 45 epidemics, two sites, 2019-2021, in unsprayed, bagged or exposed
  clusters (l. 628-636; Table 1); the count of events regressed on mean severity.
  Table 2 (p. 30): the GH2 decision tree R² 0.85 at threshold 0.65 (y = 3.18x + 7.77,
  2.5 sprays a season), the pooled-greenhouse tree 0.85 at 0.60, the GH2 network 0.84
  at 0.70, the DF2 network 0.81 at 0.45 (y = 3.72x + 7.53, 3.0 sprays); the pooled-berry
  random forest also 0.81, not discussed. Sprays no closer than 10 days (l. 678).
- **2021 field test:** the DF2 network at 0.45 against a 12-day captan programme: two
  fewer sprays at one trial, the same at the other (l. 1094).

## Dependence

- **Fitted to** the authors' own trials. The susceptibility curve's data and the test
  epidemics come from the same bagging trials (Table 1's treatment numbers are Cosseboom
  & Hu 2022's, l. 1444), and the thresholds were chosen by R² on the 45 epidemics they
  are scored on (l. 828): the fit and the test are not independent, which the paper does
  not discuss.
- **Cites** Ji et al. 2021 (Plants 10:2288, with Rossi) as the existing mechanistic ripe
  rot model, faulted for lacking stage susceptibility (l. 154, 882); not computed here.
  A shared author with engine models (Rossi) is a flag only.
- **Downstream:** `cosseboom2024` runs the DF2 network and the GH2 tree at these
  thresholds.

## Bearing (2026-10-13)

- For Cooptera, if it adds ripe rot: the Gompertz stage curve is the printed, usable
  piece; the infection classifiers are not reproducible from the paper.
- The 45-epidemic R² is an in-sample score (thresholds tuned on it, fit data shared);
  the 2024 field trials are the independent test.
