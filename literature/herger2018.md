---
id: herger2018
citation: Herger, N., Abramowitz, G., Knutti, R., Angélil, O., Lehmann, K. & Sanderson, B.M. 2018. Selecting a climate model subset to optimise key ensemble properties. Earth System Dynamics 9:135-151
doi: 10.5194/esd-9-135-2018
read: 2026-10-27, lightly: abstract, the model-as-truth part of the results (skill and spread) and the conclusions; the optimisation method (cost function, solver) and the precipitation results not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 15 of 15 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [model subset selection, model-as-truth, perfect-model test, ensemble spread, model dependence, climate model]
records: []
datasets: []
files: [syn1027_herger2018.pdf (the 2026-10-27 drop)]
---

# Herger et al. 2018: choosing a subset of climate models, tested by letting each model in turn be the truth

Picks a subset of CMIP5 simulations that keeps skill and spread, and tests whether the subset keeps them outside the period it was chosen on by treating each of 21 simulations as the truth. No record: a method with measured model-as-truth results on climate output.

**Read this first.** Climate model output, not plant or disease data. The truth in the test is another model; the main application uses real observation products, which were not read. The authors expect the approach to carry over to hydrological and ecological models but do not test that. Two-column layout; quotes are single-column fragments.

## What it holds

- **Dependence problem** (l. 30, cited as the starting point): climate model simulations "cannot necessarily be regarded as independent" estimates because of shared code and development history.
- **Design** (l. 497-498): one simulation per institute is treated as the truth "as though it were observations"; the optimal subset is chosen from the remaining 20 in an in-sample period (1956-2013) and tested out of sample (2071-2100 for climatological metrics, 2006-2100 for the trend metric); results are collated over all 21 truths (l. 499-523, 542-543).
- **Near relatives are removed from the truth set** (l. 505-506): "because members from the same" model "are likely to be much closer to each other than to the" real observational product. The authors say this is consistent with Leduc et al. 2016 (l. 508, cited) and with Sanderson et al. 2017, who removed the truth model's neighbours.
- **Reliability criterion** (l. 597): the truth should fall in the 10th-90th percentile range of the ensemble "at least 80 % of the time" to avoid overconfidence.
- **Spread result** (l. 604, 609): ensembles chosen on climatology and space-plus-time metrics were slightly over-dispersive in and out of sample; for the trend metric the subset was overconfident, at least at smaller ensemble sizes.
- **Skill result** (l. 578): "the magnitude and nature of trends within individual models do not persist into the future", so a subset chosen by trend skill has no improved out-of-sample skill.
- **Conclusions** (l. 695, 700): the model-as-truth runs examined overconfidence, ensemble spread and emergent constraints; present-day absolute values constrain future absolute values through a persistent bias but not projected changes, and the skill of the optimal subset against the unweighted mean falls the further out of sample it is tested.

## What TRUTH-METHOD says of it

Not cited in TRUTH-METHOD. It bears on part 4 (the perfect-model matrix) and on part 1 (the kinship rule). Verdict: **not in TRUTH-METHOD; new, and it supports both parts.** Its practice of excluding near relatives from the truth set (l. 505-506) is the kinship rule applied to the test set itself. Its 80 % rule in the 10-90 % range (l. 597) is a stated reliability target for a model-as-truth test.

## Dependence

- CMIP5 simulations that share code and institutions (the dependence the paper is about); builds on Abramowitz and Bishop 2015 and Leduc et al. 2016 (both cited, not read). Knutti is a co-author of `knutti2017` and of Masson and Knutti 2011: a shared-author flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 4:** a model-as-truth test needs near relatives out of the truth set; here that is stated and used. Skill chosen in sample on a feature that does not persist (trends) is lost out of sample (l. 578): the same warning applies to a model fitted on a simulator's season and judged on the same simulator.
- **D45, D58:** a constraint that holds inside the family of truths may not hold for the quantity we care about (l. 700); real data must judge.
- **Not shown:** anything for crops or disease; how the reliability target would be set for a disease engine.
