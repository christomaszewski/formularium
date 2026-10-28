---
id: carisse2021dt
citation: Carisse, O. & Fall, M.L. 2021. Decision Trees to Forecast Risks of Strawberry Powdery Mildew Caused by Podosphaera aphanis. Agriculture 11(1):29
doi: 10.3390/agriculture11010029
read: 2026-10-27, lightly: abstract, methods summary, results (Table 2 and the tree paragraphs) and the start of the discussion, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [strawberry powdery mildew (Podosphaera aphanis)]
crops: [strawberry]
regions: [Canada, Quebec]
processes: [forecasting, classification tree, external validation, inoculum, host susceptibility, variable clustering, severity classes]
records: []
datasets: []
files: [syn1027_carisse2021dt.pdf (the 2026-10-27 drop)]
---

# Carisse and Fall 2021: classification trees for strawberry powdery mildew, with later years held out (analogue crop)

Builds classification trees for four severity classes of strawberry powdery mildew from weather, airborne inoculum and the number of susceptible leaves, and tests them on three later seasons at one farm. No record: a method with measured results. Distinct from the Carisse paper held as carisse2021.

**Read this first.** Strawberry, not a vine, though an analogue for the vine's powdery mildew from the same Quebec group (Lu et al. 2020 in this library). The external validation is later years (2015, 2016, 2018) at the same experimental farm as one training site, so seasons are held out but the place is not. Table 2 is flattened in the text layer; the class-by-class order (1 to 4) is read from its header, not its frame.

## What it holds

- **Real data** (l. 4): 681 training cases from 2006, 2007 and 2008 at one experimental farm and six commercial farms in two production areas, and 136 external-validation cases from the same experimental farm in 2015, 2016 and 2018.
- **Labels are observed** (l. 4, 20): percent leaf area diseased (mean over 25 plants, three leaves each), grouped into four classes: 1: 0; 2: above 0 and under 5%; 3: 5 to 15%; 4: above 15%. The cut points were chosen from the yield-loss relation and the distribution of cases.
- **Inputs** (l. 4, 20): 92 candidate weather variables from on-farm automatic stations (readings every 15 min, stored as hourly averages and rain totals; temperature and RH at 1.5 m), reduced to 21 by variable clustering; hours in temperature bands, RH and vapour-pressure bands and rainy hours over the previous six days. Beyond T, RH and rain: airborne conidia concentration from impaction spore samplers every 2 days (twice weekly in 2015 to 2018) and the count of susceptible leaves per metre of row.
- **Synthetic or augmented data:** none.
- **Validation** (l. 20): bootstrap validation of the trees (internal) and the 136 independent cases from 2015, 2016 and 2018 (external). A case is one combination of year, site and sampling day, so cases from one season are not independent.
- **Best tree** (l. 4): inoculum, susceptible leaves, mean RH, hours at 18 to 30 degC and hours at vapour pressure 10 to 25 mmHg over the previous six days; sensitivity 0.70 to 0.90, specificity 0.87 to 0.98 and accuracy 0.82 to 0.97 across training, internal and external sets.
- **Weather-only tree** (l. 104; 15 predictors): internal sensitivity 0.45 to 0.60 and accuracy 0.70 to 0.81 by class; external sensitivity 0.42 to 0.69, specificity 0.81 to 0.93, accuracy 0.76 to 0.88.
- **External, all predictors against weather only** (l. 104): sensitivity 0.68 to 0.90 and accuracy 0.82 to 0.97 with inoculum and susceptible leaves added, i.e. +0.10 to +0.31 in sensitivity and +0.06 to +0.10 in accuracy by class (arithmetic from the two table rows, not printed).
- **Each added variable** (l. 104, 110): weather plus inoculum gives external accuracy 0.81 to 0.94 and weather plus susceptible leaves 0.86 to 0.93, so each recovers part of the gap.

## Dependence

- Labels field-scored; weather measured on the plot; no process model. Inoculum counts come from the authors' own spore traps. Same Quebec group as lu2020 (a flag, not a dependency).

## Bearing (2026-10-27)

- **D58 (variable search):** the clearest case here of variables that held on later years: inoculum concentration and susceptible-leaf count raise sensitivity by 0.10 to 0.31 on held-out years over a weather-only tree whose external sensitivity is 0.42 to 0.69. The weather-only ceiling on hourly-derived T, RH, vapour pressure and rain is accuracy 0.76 to 0.88 for one farm and four classes. Both are one farm's later years, not new sites.
- **D60:** inoculum and host state are what the project's hourly outbreak records lack; a simulator could carry them but only real data can show they help, as this paper does.
- **Not shown:** new sites, a vine, anything synthetic.
