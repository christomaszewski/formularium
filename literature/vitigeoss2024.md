---
id: vitigeoss2024
citation: VitiGEOSS project (deliverable by LINKS Foundation; Oldani, F., Monopoli, T., Blanco, G., Salza, D., Cartenì, F., Otero, M., Pujol, A., Pérez-Zanón, N., Snoek, J., Basile, B. as listed in the document history). 2024. D4.7 Validation and Evaluation, Final Report. Horizon 2020 grant 869565. Zenodo
doi: 10.5281/zenodo.10804377
read: "2026-11-04, section 5 (disease forecast service) and the site list, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 3 of 3 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Penedès, Spain]
processes: [disease forecast, risk class, incidence, machine learning regression, validation]
records: []
datasets: []
files: [dr1104_vitigeoss2024.pdf (the 2026-11-04 drop)]
---

# VitiGEOSS 2024: final validation report; Torres plots in the Penedès, downy and powdery mildew incidence 2021-2023

A public EU project deliverable (63 pages) on the 2023 season, validating the project's vineyard services against end users' data, among them Torres plots in the Penedès.

**Read this first.**
- The report releases no observation data: only figures and tables of mean absolute error (reading agent). The incidence series are not here. The authors listed are the document-history contributors, not a printed author line.
- The document is dated 2024-02-29; the Zenodo record is dated 2024-03-11.

## What it holds

- **Sites (l. 421):** "Spain (Torres): Aranyó and Sant Martí Sarroca", the Penedès-area pilot plots for the 2022-23 season.
- **Calibration (l. 1722):** the downy and powdery mildew risk models "were calibrated with all incidence percentage data obtained during the years" on end-user parcels (2021 and 2022), and tested on 2023 (reading agent).
- **Risk classes (l. 1745):** predicted leaf incidence of at most 0.5 % is low, 0.5 to 10 % medium, 10 % or more high (the quoted line shows the first class and "medium risk"; the other limits are from the reading agent's claim).
- **Data (reading agent):** BSC forecasts are on Zenodo (10.5281/zenodo.10889568 and 10.5281/zenodo.10889656, CC BY-NC-ND), already recorded.

## Dependence

- The models are machine-learning regressions fitted to the end users' 2021 and 2022 incidence; not mechanistic. No borrowed equations recorded.

## Bearing (2026-11-04)

- **Cooptera hindcasts:** the Torres plots (Aranyó, Sant Martí Sarroca) had downy mildew incidence recorded in 2021 to 2023 and used to train a model. A hindcast on these plots needs the series, which is not released. Lead: ask BSC and Torres whether it can be shared.
- Kind of evidence: a project deliverable, observations only as summary errors; no data released.
