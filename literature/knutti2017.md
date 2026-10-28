---
id: knutti2017
citation: Knutti, R., Sedláček, J., Sanderson, B.M., Lorenz, R., Fischer, E.M. & Eyring, V. 2017. A climate model projection weighting scheme accounting for performance and interdependence. Geophysical Research Letters 44(4):1909-1918
doi: 10.1002/2016GL072012
read: 2026-10-27, lightly: abstract, the perfect-model passages and the conclusions in full; the weighting equations and the Arctic results skimmed, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 19 of 19 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [model weighting, perfect-model test, pseudoreality, model interdependence, climate projection, overconfidence]
records: []
datasets: []
files: [syn1027_knutti2017.pdf (the 2026-10-27 drop)]
---

# Knutti et al. 2017: weighting climate models by skill and independence, with a perfect-model reliability test

Weights CMIP5 models by agreement with observations and by how alike they are, applies it to Arctic September sea ice and temperature, and tests whether the weighted ranges are reliable by letting each model in turn be the truth. No record: a method with a measured reliability test on one variable.

**Read this first.** The test is for one variable (Arctic September sea ice extent) in one study, not a general measure of how over-confident model-as-truth tests are. Two-column layout; quotes are single-column fragments. This is the weighting-scheme paper, not Knutti et al. 2013 and not Masson and Knutti 2011.

## What it holds

- **The design** (l. 22, 299-301): "we test reliability in a perfect model setup"; the setup is also called cross validation or pseudoreality, and "each model is sequentially treated as 'truth' and the" others are weighted to predict its future response (cited to Karpechko et al. 2013 and Wenzel et al. 2016a for the setup).
- **Correlation is not enough** (l. 306): it says nothing about constant bias or about projection uncertainty.
- **The reliability metric** (l. 308-311): the fraction of cases in which the "true" model's outcome falls inside the 5-95 % range predicted by weighting the others should be "around 90%". This fixes a minimum width parameter sigma_D of about 0.37; "Any value lower than that leads to overcon-fident results", and overly narrow projections even if agreement in the observed period is good. Fig. 3 plots both against sigma_D (l. 400).
- **Duplicates flatter the test** (l. 312-314): part of the high perfect-model correlation "may result from" multiple initial-condition members or duplicate models matching each other unrealistically well; using one model per institution suggests sigma_D = 0.57 and future ranges "about 20% wider". The authors add that this may be overly conservative.
- **Uses** (l. 339, 442): perfect-model tests can test skill, flag overfitting to natural variability, guide the choice of sigma_D, and check whether the choice of metric leads to overconfident results.
- **Limits** (l. 354-360): inference from perfect-model tests "is limited if the emergent constraint is artificially high due to common structural model biases, large amounts of replication, or too few models"; such tests "are a necessary test to pass", and give more confidence with them than without. Necessary, not sufficient.

## What TRUTH-METHOD says of it

TRUTH-METHOD part 4: "Climate science tests a projection method by letting each model in turn play the truth while the rest predict it: the perfect-model or model-as-truth test (Knutti et al. 2017)." Table: "perfect-model tests" (status snippet).

Verdict: **confirmed, with the paper identified.** It is the weighting-scheme paper (GRL 44:1909). The sentence at l. 299-300 is the design. The paper adds three things TRUTH-METHOD can use:
- a measured over-confidence criterion for the setup (coverage near 90 % of the 5-95 % range; sigma_D at least about 0.37; l. 308-311);
- the warning that replicates and shared structure flatter the test (l. 312-314, 354-357), which supports the kinship rule;
- the statement that the test is necessary, not sufficient (l. 359-360).

## Dependence

- CMIP5 models, some of which share code and institutions; the scheme explicitly down-weights similar models. Knutti and Sanderson are co-authors of `herger2018`: a shared-author flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 4:** keep the coverage check (truth inside the stated range about as often as the range says) as a pass criterion for the matrix, and keep replicates and kin out of the predictors when the test is run.
- **D45:** a model fitted on the truth family is a replicate of it; its good score in the matrix is the flattered kind (l. 312-314).
- **Not shown:** how far coverage falls in a disease setting, or what width a disease engine's ranges need.
