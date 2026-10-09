---
id: orlandini2003
citation: Orlandini, S., Dalla Marta, A., D'Angelo, I. & Genesio, R. 2003. Application of fuzzy logic for the simulation of Plasmopara viticola using agrometeorological variables. Bulletin OEPP/EPPO Bulletin 33:415-420
doi: 10.1111/j.1365-2338.2003.00666.x
read: 2026-10-09, in full by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Tuscany]
processes: [infection, incubation, sporulation, disease severity, model evaluation]
records: []
datasets: []
files: [EPPO Bulletin - 2004 - Orlandini - Application of fuzzy logic for the simulation of Plasmopara viticola using.pdf]
---

# Orlandini et al. 2003: a fuzzy-logic PLASMO against the mechanistic one

Presented at the EPPO conference on computer aids for plant protection, York, October 2002.

## What it holds

- **The mechanistic model** is "a developed form" of PLASMO (Rosa et al. 1993, 1995): leaf
  area growth, primary infection, sporulation, spore survival, inoculation and incubation,
  hourly, from budbreak; Visual Basic. No equations or parameters are printed; they "were
  chosen according to the results obtained during previous experiments performed in the
  same area on cv. Sangiovese (Orlandini et al., 2003a,b)".
- **The fuzzy model** keeps the same cycle; fuzzy rules for "devitalization" and
  "advancement" in sporulation, germination, inoculation and incubation; inoculation stays
  mechanistic (a wetness threshold for zoospore penetration). Matlab. Two parameters (the
  rate of infected leaf area increase during sporulation, and the rate of oil-spot
  devitalization) were calibrated by minimising MAE each year (Fig. 4).
- **Data:** Mondeggi-Lappeggi (Firenze), Paretaio vineyard, cv. Sangiovese, 1995-2001
  except 2000; Delta-T station beside the vineyard with leaf wetness sensor; disease every
  10 days from budbreak to harvest, about 15 observations, 800 leaves and 400 clusters on
  200 plants in untreated plots sheltered by two rows.
- **Errors (Table 1, degree of attack):** mechanistic MBE 0.887, 0.636, -0.427, -0.413, 2.558,
  2.072 and MAE 0.936, 0.791, 0.538, 0.874, 2.558, 2.072 for 1995-1999 and 2001; fuzzy MAE
  1.094, 0.526, 0.217, 0.924, 1.08, 2.107. 1999: only the fuzzy model followed the observed
  trend; 2001: both failed (they suggest underestimated primary infection, a spring frost,
  or simultaneous primary infections).

## Dependence

- The mechanistic version is PLASMO (literature/orlandini1993), refitted to Sangiovese in the
  same area; the fuzzy version was calibrated on the same plots it was scored on.
- Orlandini and Dalla Marta are authors of Sentelhas et al. 2008 (the engine's wetness
  thresholds): a flag only.

## Bearing (2026-10-09)

- Prints none of PLASMO's equations, so it neither gives Franche 2012's bounds nor the
  survival parameters. Rosa et al. 1995 (Comput. Electron. Agric. 12:311-322) and Orlandini
  et al. 2003a,b (Vitic. Enol. Sci.) are the papers to seek for the later version.
- **Followed up (2026-10-09):** Rosa 1995 ([rosa1995](rosa1995.md)) and Orlandini et al.
  2008 ([orlandini2008](orlandini2008.md)) read. Orlandini 2008 prints the bounds but no
  survival parameters. Orlandini et al. 2003a,b are cited to *Vitic. Enol. Sci.*, which ended
  with vol. 55 in 2000 by the German National Library's record (as a search reported it,
  not checked here): probably miscited, and unfound.
- Seven seasons of severity in untreated Sangiovese plots near Florence are a pattern a
  truth could be compared with, if the data could be had.
