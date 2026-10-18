---
id: shahhosseini2021
citation: Shahhosseini, M., Hu, G., Huber, I. & Archontoulis, S. V. 2021. Coupling machine learning and crop modeling improves crop yield prediction in the US Corn Belt. Scientific Reports 11:1606
doi: 10.1038/s41598-020-80820-1
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: [maize]
regions: [US Corn Belt]
processes: [hybrid crop model and machine learning, yield prediction, APSIM, feature importance]
records: []
datasets: []
files: [shahhosseini_2021.pdf (the 2026-10-18 drop)]
---

# Shahhosseini et al. 2021: APSIM outputs as machine-learning features for corn yield

Five machine-learning models and six ensembles for corn yield, with and without APSIM simulated variables as input features (l. 11-17). Yield, not disease. No record.

## What it holds

- **Result:** adding APSIM variables lowers yield RMSE by 7 to 20 % (l. 17-19).
- **Importance:** soil moisture variables matter most, then crop and phenology variables; simulated drought stress and water table depth are the top APSIM inputs (l. 19-23).
- **Finding:** weather alone is not enough, and ML needs hydrological inputs (l. 23-25).

## Dependence

- Builds on APSIM crop model outputs, NASS yield data, and weather, soil and management data.

## Bearing (2026-10-18)

- **Strand s6 (methods):** a case that simulator outputs make good features for a statistical model, an arrangement a vineyard simulator could use with sensors. County-scale corn yield; no disease.
- Triage-grade: not read in full.
