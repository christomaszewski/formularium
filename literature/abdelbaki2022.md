---
id: abdelbaki2022
citation: Abdelbaki, A. & Udelhoven, T. 2022. A Review of Hybrid Approaches for Quantitative Assessment of Crop Traits Using Optical Remote Sensing: Research Trends and Future Directions. Remote Sensing 14(15):3515
doi: 10.3390/rs14153515
read: 2026-10-27, lightly: abstract, the terminology discussion, the benefit statement and the accuracy-range summary of the results discussion (not read in full), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [review, hybrid retrieval, radiative transfer, synthetic training data, leaf area index, chlorophyll, machine learning, regression]
records: []
datasets: []
files: [syn1027_abdelbaki2022.pdf (the 2026-10-27 drop)]
---

# Abdelbaki & Udelhoven 2022: review of hybrid (radiative-transfer plus data-driven) retrieval of crop traits

A review of retrieval schemes that train a data-driven model on spectra simulated by a radiative-transfer model (RTM) and apply it to satellite or airborne images. No record: a review, and not a vineyard one.

**Read this first.** A review, read only in part. The accuracy ranges are pooled across studies, crops and sensors, and are not paired comparisons of hybrid and empirical methods. No vine-specific finding was found in the parts read.

## What it holds

- **Claim** (l. 15): hybrid approaches "have been found to provide outstanding accuracy" for leaf area index (LAI), fractional cover, and leaf and canopy chlorophyll. The generator is an RTM (PROSAIL type) whose simulations train an ANN, a Gaussian process regression (GPR) or another regressor, per the reading agent's summary of the review.
- **Stated benefit** (l. 205, 208): simulations can number in the hundreds of thousands, far more than a field campaign gives, and only a few in-situ samples are needed to validate.
- **Terminology** (l. 145): "there is no consensus" on what a hybrid retrieval is; the term covers RTM plus machine learning and RTM extended with geometry alike.
- **Surveyed accuracy, empirical group** (l. 1151, 1159): parametric (index) regressions for LAI, R2 0.2 to 0.93 and RMSE 0.05 to 0.94 m2/m2, across the studies reviewed.
- **Surveyed accuracy, hybrid group** (l. 1166): ANN or GPR hybrids for LAI, R2 0.63 to 0.83 and RMSE 0.32 to 3.89 m2/m2. The two ranges overlap; the text read gives no paired comparison.
- **Caution** (l. 209): a hybrid method "does not mitigate the nature of the ill-posed problem", so results can be unstable.
- **Test:** none of its own; the numbers are cited from the reviewed studies.

## Dependence

None recorded. It summarises PROSAIL-type RTMs with ANN, GPR and other regressors; the ranges come from the reviewed studies.

## Bearing (2026-10-27)

- **D60 (synthetic inputs, several physical models per gap):** a review-level statement that RTM-trained regressors work for canopy traits, with ranges that overlap the empirical ones, so it supports trying RTM training but does not show it beats an index. The three vineyard studies in this strand (`sandonis2026`, `brown2024`, `zarcotejada2013`) are the vine evidence.
- **Terms:** "hybrid" means three things across the strand (RTM plus ML, RTM with geometry, RTM-derived indices); a D60 note must say which.
- **Not shown:** a paired hybrid against empirical comparison, a vineyard result, a water-status retrieval, or a test on shifted conditions.
