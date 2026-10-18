---
id: hughes2017b
citation: Hughes, G. & Burnett, F. J. 2017. Evaluation of Probabilistic Disease Forecasts. Phytopathology 107:1136-1143
doi: 10.1094/PHYTO-01-17-0023-FI
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 45 of 45 quotes found at their lines by scripts/verify_quotes.py; equations 1-15 in the text layer checked against page images 3-5; the reader recomputed BS 0.230, DS 0.650, PSEP 0.454 and REL 0.144 from Table 1's counts and they match
status: read
diseases: []
crops: []
regions: [not applicable]
processes: [forecast evaluation, Brier score, divergence score, index of separation]
records: []
datasets: []
files: [hughes_2017.pdf (the 2026-10-18 drop)]
---

# Hughes & Burnett 2017: evaluating probabilistic disease forecasts with scoring rules

A method for evaluating probabilistic disease forecasts with predictive values, the Brier and divergence scoring rules and an index of separation, split into uncertainty, resolution and reliability (l. 18-25). A different paper from hughes2017 (Hughes, McRoberts & Burnett, 107:158). No record.

## What it holds

- **Scores** (eq. 1-9, l. 152-274): Brier score (eq. 1), divergence score as the mean Kullback-Leibler divergence in nits (eq. 2), Bregman divergence (eq. 3-4), PSEP = Pr(o2|f worst) - Pr(o2|f best) (eq. 5, l. 208-210; after Altman & Royston 2000), and the split BS or DS = UNC - RES + REL (eq. 6, l. 274). Expected mutual information, entropies H(o), H(o|f) and normalised IM (eq. 10-15, l. 311-353); G2 = 2 N IM (l. 365). Only Brier and divergence scores are used. Eq. 3, 7, 10 and 12-15 are garbled in the text layer; the page images give the forms.
- **Table 1** (l. 128-133), counts only: Scenario A, Stewart's disease of corn (Esker et al. 2006, Table 5): Pr(o2|f1) = 56/139 = 0.403, Pr(o2|f2) = 12/14 = 0.857, prior 68/153 = 0.444. Scenario B, white mold of dry bean in North Dakota (Harikrishnan & del Rio 2008, Table 2): 7/71 = 0.099, 27/29 = 0.931, prior 34/100, N = 100. Scenarios C1 (training, N = 150) and C2 (validation, N = 29), Fusarium head blight and deoxynivalenol in spring malting barley (Bondalapati et al. 2012, Table 4, Model 3): Pr(o2|f1) = 6/104 = 0.058 and 3/12 = 0.250; Pr(o2|f2) = 28/46 = 0.609 and 14/17 = 0.824; C2 prior 17/29 = 0.586.
- **Worked results, Scenario A** (l. 189-288): BS 0.230, DS 0.650 nits, PSEP 0.454, RES 0.037 nits. The reader recomputed BS (35.14 / 153 = 0.2297), DS (99.49 / 153 = 0.650) and PSEP (0.857 - 0.403) from Table 1's counts and they match.
- **Scenario C, calibration** (l. 244-246, 341-344, 405-411): C1 forecasts applied to C2: REL 0.144 nits (recomputed (12 x 0.194 + 17 x 0.109) / 29 = 0.144; matches), Bregman terms 0.108 and 0.195 nits. C2 DS is 0.506 with reliability taken as zero (UNC 0.678 - RES 0.172) and 0.650 with it included. PSEP C1 0.551, C2 0.574; IM 0.177 and 0.172 nits.
- **Scenario B** (l. 323-392): H(o) 0.641, H(o|f) 0.301, IM 0.340 nits, normalised IM 0.530, G2 67.931 (= 2 x 100 x IM); logistic fit intercept -2.213, slope 4.816 on the 0/1 forecast indicator; McFadden R2 0.530 equals the normalised IM.
- **Recommendation** (l. 432-435): when reliability is implicitly zero (the forecast probabilities are assumed right), say so clearly.
- **Context** (l. 28-40, 124-131): a forecast used to trigger management cannot be scored simply, because action changes the outcome; Madden's (2006) example: a positive forecast with sensitivity 0.833 and specificity 0.844 gives posterior 0.22, 0.75 and 0.97 at prevalences 0.05, 0.36 and 0.85.
- **Not printed:** dates and sites of the source studies in Table 1; the underlying data; any licence. No vineyard, wetness, sensor or spore values.

## Dependence

- No equation of another model is computed and no code is shared. The scenario counts come from three published models (Esker 2006's Stevens model, Harikrishnan & del Rio 2008's logistic model, Bondalapati 2012's Model 3). Whether those models shaped the data they were validated on is not stated, so no dependency is recorded. The logistic fit to Scenario B is the paper's own calculation. Hughes et al. 2015 and 2017 are self-citations (l. 513-515): a flag only.

## Bearing (2026-10-18)

Strand 6 (methods):

- **What Agrarium can take:** a scoring step for a probabilistic risk output, with the decomposition into uncertainty, resolution and reliability. Brier and divergence scores, PSEP and the reliability term are all computable from a 2 x 2 count table, and the printed numbers (BS 0.230, DS 0.650, PSEP 0.454, REL 0.144) are a test for an implementation. Reliability separates a forecast that discriminates well (resolution) from one whose probabilities can be believed.
- **For the sweep and sensor placement:** compare sensor layouts or gap-filled series by the score of the risk forecast they feed, not by temperature error alone; report reliability whenever the forecast is a probability.
- **Limits:** tiny samples (29 to 153); counts only; the intervention problem (l. 28-40) is not solved.
