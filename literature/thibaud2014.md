---
id: thibaud2014
citation: Thibaud, E., Petitpierre, B., Broennimann, O., Davison, A.C. & Guisan, A. 2014. Measuring the relative effect of factors affecting species distribution model predictions. Methods in Ecology and Evolution 5:947-955
doi: 10.1111/2041-210X.12203
read: 2026-10-27, lightly: abstract, introduction, the virtual-species simulation and sampling, the modelling techniques, the results on technique and sample size and the discussion; the mixed-model algebra not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Switzerland (Vaud)]
processes: [virtual ecologist, virtual species, species distribution model, synthetic data, sample size, model comparison, spatial autocorrelation]
records: []
datasets: []
files: [syn1027_thibaud2014.pdf (the 2026-10-27 drop)]
---

# Thibaud et al. 2014: a factorial virtual-ecologist experiment, in which the best method is the one that made the data

Ten virtual plant species with response parameters fitted to ten real species, placed on a real Alpine landscape; presences are simulated with or without spatial autocorrelation, sampled at two sizes and two designs, and modelled with four techniques (GLM, GAM, MaxEnt, random forest) scored against the known presence probabilities. No record: a method on synthetic data with real predictors.

**Read this first.** Species distribution models, not plant disease. The result is conditional on the simulated settings (l. 27), and the study does not vary the class of generator, so it cannot say by how much the generator decides the winner.

## What it holds

- **Design** (l. 22, 85, 121-122, 201): a "virtual ecologist" factorial experiment; ten virtual species from parameters estimated by fitting a probit model to ten real species in the study area; a real Alpine landscape of about 700 km2 in the canton of Vaud (l. 121-122); training samples of n = 100 and n = 500 presence and absence points.
- **Scoring** (l. 191): the error is the RMSE of estimated against true presence probabilities, possible only because the simulation knows the truth.
- **Overall result** (l. 27): for the parameter values considered, most variation in prediction accuracy is due to sample size and modelling technique.
- **The same-model case** (l. 229): the GLM (probit with quadratic terms, no interactions) used as one technique "is the true model that generates our" species when no covariate is missing.
- **Ranking changes with n** (l. 425): at n = 500 GLMs "are generally the best models, but for n = 100, they tend" to predict worse than MaxEnt. A winner that changes with the sample size the experiment sets.
- **The authors' own caveat** (l. 515-516): that GLMs were generally best "is not surprising as our virtual species were generated using a GLM", and MaxEnt and random forest, which model interactions, gave poorer predictions.
- **Against real-data comparisons** (l. 518, cited from Elith et al. 2006 and Wisz et al. 2008): machine-learning methods such as MaxEnt generally outperform GLMs and GAMs in small samples; the virtual study agreed only for small samples.

## What TRUTH-METHOD says of it

Not cited in TRUTH-METHOD. Verdict: **not in TRUTH-METHOD; a direct small example of its worry that the truth's form decides the winner.** The authors state the effect themselves (l. 515-516), and the ranking depends on a setting of the experiment (l. 425). It is the measured companion to the generator effect that `meynard2013` asserts; `meynard2019` lists it only under dispersal.

## Dependence

- The GLM technique is the data-generating model when no covariate is missing (l. 229): the same-model case. The virtual-ecologist framework is Zurell et al. 2010 (see `zurell2010`).

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 1:** supports the kinship rule with a measured case: the model class that made the data was the best model (l. 515-516), and the methods that win in real-data comparisons did worse except in small samples (l. 518).
- **D45:** a plant model fitted on a simulator's output is the "GLM on GLM-made data": its good score on the simulator's held-out seasons is the same-model case, and only real data separate it from the generator.
- **Not shown:** how much of the ranking is due to the generator, since only one generator class was used.
