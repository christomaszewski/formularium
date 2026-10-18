---
id: multsch2015
citation: Multsch, S., Exbrayat, J.-F., Kirby, M., Viney, N. R., Frede, H.-G. & Breuer, L. 2015. Reduction of predictive uncertainty in estimating irrigation water requirement through multi-model ensembles and ensemble averaging. Geoscientific Model Development 8:1233-1244
doi: 10.5194/gmd-8-1233-2015
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: [wheat]
regions: [Murray-Darling Basin, Australia]
processes: [reference evapotranspiration, crop coefficient, multi-model ensemble, reliability ensemble averaging]
records: []
datasets: []
files: [multsch_2015.pdf (the 2026-10-18 drop)]
---

# Multsch et al. 2015: multi-model ensembles for irrigation water requirement

Six reference evapotranspiration equations and five crop-coefficient sets for wheat in the Murray-Darling Basin, run in the SPARE:WATER system and combined by reliability ensemble averaging (l. 34-45). No record.

## What it holds

- **Setup:** six ETo equations (Table 2, l. 255) and five Kc sets (Table 1, l. 245), with the single crop coefficient approach.
- **Result:** structural uncertainty among the ETo equations is far more important than parametric uncertainty from the crop coefficients (l. 40-43).
- **Averaging:** reliability ensemble averaging cuts overall predictive uncertainty by more than 10 % (l. 46-47); an irrigation limit of 400 mm is exceeded with probability 45 % under the REA average against 66 % under the equal-weight average (l. 47-52).

## Dependence

- Builds on FAO-56 (Allen et al. 1998), Penman-Monteith, Priestley-Taylor and Hargreaves-Samani ETo equations and SPARE:WATER.

## Bearing (2026-10-18)

- **Strand s6 (methods):** an example that the choice of model form can matter more than parameter values, and of weighting models by reliability. A simulator could take the ETo equation spread as a measure of how much weather-to-evaporation structure counts for leaf drying. Wheat, not vines.
- Triage-grade: not read in full.
