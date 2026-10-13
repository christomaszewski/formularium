---
id: ramos2018
citation: Ramos, M. Concepción, Jones, Gregory V. & Yuste, Jesús. 2018. Phenology of Tempranillo and Cabernet-Sauvignon varieties cultivated in the Ribera del Duero DO: observed variability and predictions under climate change scenarios. OENO One 52(1):31-44
doi: 10.20870/oeno-one.2018.52.1.2119
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py; the base temperatures and thresholds (pp. 36, 38) and Table 3 (p. 38) read in the page images by the main session; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Ribera del Duero, Aranda de Duero, Castilla y León]
processes: [phenology, budburst, flowering, veraison, maturity, water balance, climate projection]
records: [ramos2018.gdd]
datasets: [ramos2018.ribera]
files: [2018-ramos-10-20870-oeno-one-2018-52-1-2119.pdf]
---

# Ramos, Jones & Yuste 2018: Ribera del Duero stages by degree-days and water

Twelve seasons of Tempranillo and Cabernet Sauvignon stage dates in four plots, fitted
with degree-days from 20 March (the start found by partial least squares) and a base
per stage, then a water term, and projected under CMIP5. A threshold model with a
non-thermal water correction; from Lleida, Linfield College and ITACyL.

## What it holds

- **Data** (`ramos2018.ribera`): budbreak, bloom, véraison and maturity (Baggiolini C, I,
  M, N) 2004-2015 in plots A (802-808 m, deficit-irrigated) and B (820-840 m, dry) from
  the Consejo Regulador, a stage dated when it is the most frequent in the area
  (l. 219-227; Table 1, p. 36: budbreak 24-30 April, bloom 15-18 June, véraison 12-19
  August, maturity 30 August to 4 September on average); Aranda de Duero station, 798 m,
  5.6 and 13.1 km away (l. 175-177). Warming 2004-2015: Tmax 0.17 and Tmin 0.09 °C/yr
  (l. 364).
- **Windows:** chill portions (Dynamic Model) and growing degree hours (base 4 °C,
  optimum 26 °C) in 10-day means from 15 September to 10 May, regressed on budbreak by
  PLS (l. 209-214): chilling counts from mid-October to 20 March, heat from 20 March on
  (l. 367-382); 118-121 chill portions a season (l. 364).
- **Degree-days** (`ramos2018.gdd`; p. 36, 38): base per stage by minimising the SD of
  the sum (Excel Solver, after Zapata et al. 2017, l. 275): budbreak 3.8 and 4.7 °C,
  bloom 6.4 and 7.2, véraison 13.4, maturity 9.2 and 10.5 (Tempranillo, Cabernet);
  thresholds 250 ± 45, 425 ± 51, 398 ± 53, 410 ± 76 °C·d and 205 ± 43, 395 ± 73,
  386 ± 42, 372 ± 88 (l. 486-490). In-sample RMSE 5.2-7.3, 3.8-7.6, 5.1-7.0 and
  8.9-12.2 d (l. 461-465); the worst years (2009, 2015, 2014) up to 20 d early, 2005 and
  2006 up to 19 d late (l. 470).
- **Water** (Table 3, p. 38): bloom and véraison dates regressed on P minus ETc over 15
  April to 30 May, slopes 0.14-0.18 and 0.09-0.16 d/mm by plot (R² 0.46-0.84), about
  1-2 d earlier per 10 mm of deficit (l. 471); maturity on April-June water, 0.095-0.097
  d/mm (R² 0.34-0.35); budbreak not significant.
- **Projections** (Table 4, p. 39): eight CMIP5 models, RCP4.5 and RCP8.5, 2030, 2050,
  2070 against 1960-2000 (l. 285-303): véraison 6-19 d earlier (RCP4.5) and 10-28 d
  (RCP8.5), maturity up to 23 and 35 d (l. 34-38); bloom-véraison 10-11 d shorter
  (l. 651). The abstract's bloom range (3-8 d) stops short of Table 4's 9.4 d.

## Dependence

- **Borrows** the Dynamic Model (Fishman et al. 1987), growing degree hours (Anderson et
  al. 1986), the 26 °C cap (Parker et al. 2011), the SD-minimising base (Zapata et al.
  2017) and FAO-56 ET (Allen et al. 1998); fitted to the Consejo's observed dates, no
  model dated them. Base, threshold and RMSE come from the same twelve seasons.
- **Kin** to `ramos2017.budburst` (the same author's Penedès fits, the same method) and
  the engine's degree-day pieces by form; cites `fraga2016` for comparison.

## Bearing (2026-10-13)

- Not the requested form: a degree-day sum to a threshold, with the start day and base
  fitted. Its added piece is the water term (1-2 d per 10 mm of spring deficit), a
  non-thermal driver Agrarium's phenology does not carry.
- The in-sample errors (4-12 d, up to 20 d in hot or dry years) are the yardstick for
  any Penedès-like dry-farmed site.
