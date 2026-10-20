---
id: velez2023
citation: Vélez, S., Ariza-Sentís, M. & Valente, J. 2023. Mapping the spatial variability of Botrytis bunch rot risk in vineyards using UAV multispectral imagery. European Journal of Agronomy 142:126691
doi: 10.1016/j.eja.2022.126691
read: 2026-10-20, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [Botrytis bunch rot]
crops: [grapevine]
regions: [Spain]
processes: [spatial risk mapping, UAV multispectral imagery, canopy structure, NDVI, Random Forest]
records: []
datasets: []
files: [velez_2022.pdf (the 2026-10-20 drop)]
---

# Vélez et al. 2023: Botrytis bunch-rot risk maps from UAV canopy layers

A Random Forest turns UAV canopy layers into a within-field map of Botrytis risk. It is fitted and tested on one Spanish vineyard in one season.

## What it holds

- One 1.06 ha commercial vineyard with an 8.1 % slope in Spain, 2021 campaign, with georeferenced infected clusters (l. 151-152).
- Inputs are the DTM, NDVI, CHM and LAI from UAV imagery. The classifier is a Random Forest with 500 trees (l. 391-397).
- Fit: R² of 0.68 to 0.72 for the risk maps against observed infected clusters (l. 372-375).

## Dependence

- Builds on the Random Forest classifier and the NDVI index (Rouse et al. 1973, l. 96).
- Cites bunch-compactness and vigour links (Keller et al. 2001) and weather models (Hill et al. 2019) as context. No other model is recorded.

## Bearing (2026-10-20)

- Strand t1 (fungicide protection, through spatial timing) and t4 (Botrytis). A simulator could take the canopy-based link between vigour, bunch compactness and risk. The map is one season and one site with no weather term, so it gives no rate.
- Not read in full.
