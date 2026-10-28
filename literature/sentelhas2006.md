---
id: sentelhas2006
citation: Sentelhas, P.C., Gillespie, T.J., Gleason, M.L., Monteiro, J.E.B.M., Pezzopane, J.R.M. & Pedro, M.J. Jr. 2006. Evaluation of a Penman-Monteith approach to provide 'reference' and crop canopy leaf wetness duration estimates. Agricultural and Forest Meteorology 141:105-117
doi: 10.1016/j.agrformet.2006.09.010
read: 2026-10-28, Section 2.3 (Eqs 1-6) and the overestimation passage; results tables and crop sections not read; by a reading agent and note writer (claude-sonnet-5-5); 3 of 3 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [turfgrass, maize, cotton, coffee, grape]
regions: [Canada, Brazil, United States]
processes: [leaf wetness duration, Penman-Monteith, boundary layer resistance, dew]
records: []
datasets: []
files: [dr1028_sentelhas2006.pdf (the 2026-10-28 requests drop)]
---

# Sentelhas et al. 2006: a Penman-Monteith wetness model whose boundary layer resistance is forced convection only, and the stalled anemometer it blames for early dew

The journal version of the thesis model in `sentelhas2004`.

**Read this first.** Read only for how wind enters and for the authors' remark on anemometers. Skill figures are not taken here.

## What it holds

- **Form:** LE from Penman-Monteith with gamma* 0.64 for dew and 1.28 after rain; rb = D/(k Nu), D the sensor's 0.07 m (l. 190-210).
- **Nu = 0.68 Pr^(1/3) Re^(1/2)** for Re < 20 000 (l. 197): forced flow over a plate only. With average temperatures rb = 307 (D/u)^0.5 s/m, halved for two sides (l. 213-222). rb is infinite at u = 0, so drying and dew both vanish in still air, as in SWEB.
- **The authors' own diagnosis (l. 396-403):** the model overestimates wetness duration; this "might be associated with the difficulty of measuring low wind speeds at night"; when "the anemometer may stall, average recorded wind speed may be too small. This makes ra and rb too big, and modeled dew starts early." They call it a data problem fixable "with an empirical correction", not a model error.

## Dependence

Form and parameters from the thesis `sentelhas2004`, Monteith & Unsworth 1990, Rao et al. 1998, Pedro & Gillespie 1982. No free-convection term.

## Bearing (2026-10-28)

- **Request still-air-drying-d60:** the one wetness paper read that names the stalled anemometer as the cause of an error of SWEB's kind (overlong wetness at low recorded wind). It offers no floor.
