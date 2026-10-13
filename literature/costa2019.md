---
id: costa2019
citation: Costa, Ricardo, Fraga, Helder, Fonseca, André, García de Cortázar-Atauri, Iñaki, Val, Maria C., Carlos, Cristina, Reis, Samuel & Santos, João A. 2019. Grapevine phenology of cv. Touriga Franca and Touriga Nacional in the Douro wine region: modelling and climate change projections. Agronomy 9(4):210
doi: 10.3390/agronomy9040210
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Douro, Lisbon, Vinhos Verdes]
processes: [phenology, budburst, flowering, veraison, dormancy, climate projection]
records: []
datasets: []
files: [costa2019_agronomy.pdf]
---

# Costa et al. 2019: eight model forms for the two Tourigas, fitted in PMP

Four forcing forms (degree-days, Richardson, sigmoid, Wang) with and without three
dormancy forms (Bidabe, Smoothed Utah, Chuine), fitted on 73 dates per stage and cultivar
pooled from the Douro, Lisbon and Vinhos Verdes, scored by leave-one-out, and projected
to 2100 under RCP4.5. Threshold models; the UTAD group that wrote `fraga2016`.

## What it holds

- **Data:** 12 Douro quintas, 2014-2017 (48 records), Dois Portos 20 years within
  1990-2014, Vinhos Verdes 2005-2009 (l. 138-155), BBCH 07, 65, 81; Douro temperatures
  from on-site stations, the others from a 1 km gridded product (l. 158-161). Touriga
  Franca budburst days 61-98, veraison 177-222 (l. 474-475).
- **Models** (Table 3; l. 300-389): dormancy from 1 August after `cortazar2009`; GDD
  max(0, T − Tb), Richardson, sigmoid 1/(1 + exp(e(T − d))), Wang & Engel as García de
  Cortázar-Atauri adapted it, with literature defaults; fitted by simulated annealing in
  the Phenological Modelling Platform; RMSEP by leave-one-out (l. 421).
- **Fits** (Tables 5-6, l. 526-587): Touriga Franca budburst Bidabe + Wang RMSEP 6.4 d
  (R² 0.62), flowering GDD with Tb 6.6 °C 5.1 d (R² 0.85), veraison sigmoid (d 0.0, e
  13.0) 4.3 d (R² 0.92); Touriga Nacional flowering GDD Tb 7.0 °C 5.4 d, budburst 7.2-8.0
  d. Some chilling parameters sit at round values (d −40, e 7.5) that may be bounds
  (l. 531). No clear gain from a dormancy phase (l. 1294).
- **Projections** (EURO-CORDEX, bias-corrected): budburst 6 d, flowering 8 d, veraison
  8-12 d earlier by 2100 under RCP4.5; inter-model spread 2-6 d (l. 886-912).

## Dependence

- **Borrows** the forms above and PMP; fitted to the groups' observed dates, the Lisbon
  series the same as `fraga2016.portugal`'s Dois Portos data, no model dated them.

## Bearing (2026-10-13)

- Threshold models; the comparison of eight forms on one dataset gives the spread a
  tool should expect between forms (budburst 6-8 d, veraison 4-6 d), and the finding
  that dormancy sub-models bought nothing here.
