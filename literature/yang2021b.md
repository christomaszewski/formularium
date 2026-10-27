---
id: yang2021b
citation: "Yang, Chenyao, Menz, Christoph, Fraga, Helder, Costafreda-Aumedes, Sergi, Leolini, Luisa, Ramos, Maria Concepción, Molitor, Daniel, van Leeuwen, Cornelis & Santos, João A. 2022 (online 2021). Assessing the grapevine crop water stress indicator over the flowering-veraison phase and the potential yield lose rate in important European wine regions. Agricultural Water Management 261:107349"
doi: 10.1016/j.agwat.2021.107349
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full; PDF text, two columns with soft hyphens
status: read
diseases: []
crops: [grapevine]
regions: [France, Germany, Luxembourg, Italy, Portugal, Spain]
processes: [water stress index, yield loss rate, STICS grapevine model, phenology]
records: []
datasets: []
files: [yang2021.pdf]
---

# Yang et al. 2021: a water stress index and yield loss over European vineyards

A STICS-grapevine grid run for 38 sites in six countries, 1986 to 2015, giving a flowering-to-veraison water stress index and a potential yield loss rate.

## What it holds

- **Sites and period:** 38 sites in six countries, 10 varieties, 1986 to 2015 (l. 85, 193, 236). Four phenology parameters are calibrated per site over DD 40-205, PD 6000-11500, FL 230-560 and VR 600-1700 (l. 293-296).
- **Two indices:** CWSI = 1 - ET/ETmax over the flowering-veraison phase (eq. 1, l. 304-307); potential yield loss rate = 1 - stressed over unstressed cluster weight at harvest (eq. 2, l. 320-324).
- **Drought classes:** CWSI 0-0.25 slight, 0.25-0.5 moderate, 0.5-0.75 severe, 0.75-1 extreme, after Wu et al. 2019 (l. 310-313).
- **Median yield loss:** Italy 20-45 %, Portugal 10-40 %, Spain 30-50 %, France 20-40 %, Germany 10-30 %, Luxembourg below 5 % (l. 456-458).
- **Calibration errors:** MBE, MAE, RMSE and r are given only in the supplement (Figs S2-S6, l. 315-320).

## Dependence

- Builds on STICS and its GDD and phenology routines (Brisson et al. 2009; l. 241-254), the CWSI and yield loss definitions of Zhu et al. 2021 (l. 304-305, 320-321), the drought classes of Wu et al. 2019 (l. 312-313), EU-SoilHydroGrids soils (l. 285), E-OBS v22.0e climate (l. 334), and PEP725 and IPHEN phenology (l. 199-200).

## Bearing (2026-10-26)

- classes.tsv names no search for this row; its reason is the grid run with the water stress index and yield loss rate. By the triage question list it falls under the 10-14 whole-vine model item, but the loss here is from water stress, not disease.
- A vineyard simulator could use the CWSI and yield loss definitions, and the regional medians as a check. The calibration statistics are not in the text read. Not read in full.
