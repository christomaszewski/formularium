---
id: parker2011
citation: PARKER, A.K., DE CORTÁZAR-ATAURI, I.G., VAN LEEUWEN, C. & CHUINE, I. 2011. General phenological model to characterise the timing of flowering and veraison of Vitis vinifera L. Australian Journal of Grape and Wine Research 17:206-216
doi: 10.1111/j.1755-0238.2011.00140.x
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: [grapevine]
regions: [France, Switzerland, Italy, Greece]
processes: [phenology]
records: []
datasets: []
files: [10-1111-j-1755-0238-2011-00140-x.pdf]
---

# Parker et al. 2011: GFV, a general model of flowering and veraison

From INRA Bordeaux and Avignon and CNRS Montpellier.

## What it holds

- Model (GFV): degree-day sum above Tb 0 degC from t0 = day 60 until F* is reached; F* is fitted per variety and stage (l. 413).
- Chosen over UniFORC and UniCHILL by EF, RMSE and AIC (l. 94).
- Unconstrained fit: t0 56.4 d and Tb 2.98 degC on flowering (l. 349); veraison alone gives t0 92 d, Tb 4 degC (l. 311).
- Classical SW (t0 1, Tb 10) veraison RMSE 14.3 d against 7.7 d for GFV (l. 351).
- Data: own database, 1960-2007, 123 locations, 81 varieties, 2278 flowering and 2088 veraison dates (l. 153); mostly France.
- Fit used 1092 flowering and 980 veraison observations (l. 315); validation 440 and 424 later observations for 11 varieties (l. 78).
- Validation data came later but are not stated to be new sites (l. 265).
- Cabernet-Sauvignon F*: 1270 (flowering, l. 746) and 2641 degC d (veraison, l. 770).
- Sources named: PHENOCLIM, INRA, Domaine de Vassal (l. 874); no site mapping.
- Dependence: Winkler GDD form refitted; Chuine forms rejected; no model dated the data.

## Dependence

- Its own assembled database: 2278 flowering and 2088 veraison dates, 1960-2007, 123 sites, 81 varieties. The acknowledgements name PHENOCLIM and INRA stations among the contributors, unmapped to sites. The engine's García de Cortázar-Atauri 2009 models were fitted to PHENOCLIM's **budburst** dates, so a shared observation is possible only if the networks overlap stage by stage: a flag, not a recorded link.
- García de Cortázar-Atauri is an author of the engine's phenology models: a flag.

## Bearing (2026-10-08)

- **Held out by structure** (a degree-day forcing sum, the engine's form), as before; the author is a flag now. GFV's F* for Cabernet Sauvignon: 1270 (flowering) and 2641 °C·days (veraison).
