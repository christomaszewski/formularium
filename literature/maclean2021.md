---
id: maclean2021
citation: Maclean, Ilya M. D. & Klinges, David H. 2021. Microclimc: a mechanistic model of above, below and within-canopy microclimate. Ecological Modelling, article 109567 (an accepted manuscript printing no journal details; journal and article number from the DOI in the file name, 10.1016/j.ecolmodel.2021.109567)
doi: 10.1016/j.ecolmodel.2021.109567
read: 2026-10-08, in full (appendices not in the text copy), by a reading agent (claude-sonnet-5-5); 31 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: []
regions: [global]
processes: [canopy microclimate, leaf temperature]
records: []
datasets: []
files: [10-1016-j-ecolmodel-2021-109567.pdf]
---

# Maclean & Klinges 2021: Microclimc, a mechanistic canopy microclimate model

From the University of Exeter and the University of Florida. The manuscript; Ecological Modelling by its DOI (not printed in the copy).

## What it holds

- Microclimc is an R model of leaf temperature, air temperature, humidity and wind above, inside and below a canopy, in transient and steady-state modes (l. 43).
- Leaf heat balance, eq. 12 (l. 508), is linearised so leaf and air temperature are solved together (l. 529). The leaf surface is saturated at leaf temperature (l. 497); stomatal conductance depends only on absorbed PAR (l. 487). There is no leaf-wetness, dew or interception term.
- Boundary-layer conductance follows Campbell and Norman, with a turbulence factor of 1.4 (l. 454, l. 467).
- Validation: air temperature only (l. 733), at four forests, 1 to 10 m height (l. 720): Borden 1998 (l. 790), Harvard 2017 (l. 795), Fuji Hokuroku 2019 (l. 802), Hubbard Brook 2013 (l. 807). Forcing was ERA5 (l. 727). Parameters were biome defaults, not fitted to these data.
- Hourly MAE 2.77 C (transient) and 2.79 C (steady-state) (l. 46, l. 740); Table 4 prints 3.3 C for steady-state (l. 877). RMSE 3.48 C (l. 741).
- Modelled variability is too small: SD 5.44 and 4.67 against 5.93 (l. 746). Freezing weather was excluded (l. 732).
- Use for the simulator: a forest-canopy leaf-temperature scheme; errors of 2.8 C are too large for wetness work.

## Dependence

- It computes textbook canopy physics (Campbell & Norman, Goudriaan, Penman-Monteith and others); soil by NicheMapR. Validation forcing from ERA5.
- No author of an engine model.

## Bearing (2026-10-08)

- Clear. Leaf and canopy temperature and humidity within a canopy, but no leaf wetness state: a source for the truth's leaf temperature, not its wetness.
