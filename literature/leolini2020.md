---
id: leolini2020
citation: Leolini, Luisa, Costafreda-Aumedes, Sergi, Santos, João A., Menz, Christoph, Fraga, Helder, Molitor, Daniel, Merante, Paolo, Junk, Jürgen, Kartschall, Thomas, Destrac-Irvine, Agnès, van Leeuwen, Cornelis, Malheiro, Aureliano C., Eiras-Dias, José, Fonseca, Antonio, Bindi, Marco & Moriondo, Marco. 2020. Phenological model intercomparison for estimating grapevine budbreak date (Vitis vinifera L.) in Europe. Applied Sciences 10(11):3800
doi: 10.3390/app10113800
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5), which read the equations (p. 5) and Tables 1-2 on page images; 30 of 30 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [France, Luxembourg, Portugal]
processes: [phenology, budburst, dormancy, model comparison]
records: []
datasets: []
files: [2020-leolini-10-3390-app10113800.pdf]
---

# Leolini et al. 2020: six budbreak models for eight varieties across Europe

GDD, Wang-Engel and UniForc (forcing only) against BRIN, UniChill and Unified
(chilling-forcing), fitted per variety on 15 vineyards in France, Luxembourg and
Portugal and applied to independent series. Threshold models; the parameter tables are
the resource.

## What it holds

- **Data:** budbreak (BBCH 09; three Bordeaux varieties BBCH 07 plus two days after
  Nendel 2010) of Cabernet Sauvignon, Chardonnay, Gewürztraminer, Grenache, Pinot
  Noir, Riesling, Touriga Franca and Touriga Nacional, observed by institutions and
  growers (l. 147, 280-284); outliers removed against a preliminary fit, 1.5-10 % by
  variety (l. 419-432); 60 % of years to fit, 40 % to validate, ten random splits
  (l. 467); fitted in PMP 5.5 (l. 470).
- **Models** (Eqs 1-7, p. 5): GDD with Tb fitted in 0-10 °C; WANG with 0 and 45 °C
  fixed and Topt within ±30 % of Fila et al.; UniForc's sigmoid; BRIN with its 25 °C
  upper limit; UniChill and Unified (l. 438-461). Forcing-only models start 1 January
  or 1 March, chilling-forcing 1 September or 1 August (l. 460-461, 948-955).
- **Scores** (l. 593-603): Unified best, fit R² 0.77 and RMSE 3.96 d, validation 0.64 and
  5.42 d; WANG the poorest fit (R² 0.61), GDD the poorest validation (RMSE 6.25 d);
  Chardonnay best fitted (R² 0.90), Touriga Nacional poorest (0.42). On independent
  series RMSE 8.4 (BRIN hourly) to 9.7 d (GDD), 4-19 d over all cases (l. 940-955,
  1118).
- **Start dates and latitude:** chilling-forcing models release endodormancy on average
  on day 54 for northern varieties and day 13 for southern ones, so a 1 March start
  suits the north and 1 January the south (l. 1032-1037).
- **Parameters** for every model, variety and start date are in Tables 2-3 (pp. 11-13),
  not transcribed in this reading.

## Dependence

- **Borrows** all six forms (Amerine & Winkler, Wang & Engel 1998, Chuine 2000,
  `cortazar2009.brin`); fitted to observed dates after a model-based outlier screen.
  `costafreda2025` reuses these calibrations; `fraga2016`'s authors are co-authors.

## Bearing (2026-10-13)

- The yardstick for threshold budbreak models in Europe (4-6 d in validation, 8-10 d
  transferred) and a parameter table for Chardonnay, Grenache and Cabernet Sauvignon
  that could be recorded when a tool wants them.
