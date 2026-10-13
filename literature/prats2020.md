---
id: prats2020
citation: Prats-Llinàs, Maria Teresa, Nieto, Héctor, DeJong, Theodore M., Girona, Joan & Marsal, Jordi. 2020. Using forced regrowth to manipulate Chardonnay grapevine (Vitis vinifera L.) development to evaluate phenological stage responses to temperature. Scientia Horticulturae 262:109065
doi: 10.1016/j.scienta.2019.109065
read: 2026-10-13, a light reading of the accepted manuscript by a reading agent (claude-haiku-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Lleida, Raïmat]
processes: [phenology, flowering, fruit set, veraison, maturity, pruning date]
records: []
datasets: []
files: [2020-prats-llinas-10-1016-j-scienta-2019-109065.pdf]
---

# Prats-Llinàs et al. 2020: Chardonnay regrown at later dates to find upper temperature limits

Chardonnay vines at Raïmat forced to regrow 60 to 230 days after budbreak, so that each
stage ran under different temperatures, and degree-day forms with an upper threshold
fitted to the spread. From IRTA Lleida and Davis; the project's own province.

## What it holds

- **Design:** field vines regrown 60 and 98 d after budbreak in 2015 and 105 d in 2016,
  container vines (on 1103 Paulsen) at 174-230 d in 2016, shoots cut to six nodes after
  Gu et al. 2012 (l. 312-357); calibration on 9-10 dates a stage, validation on
  Californian and Badajoz data (27-33 dates) (l. 381-399); two Raïmat stations (l. 436).
- **Forms:** UniForc (base only), Zalom et al. 1983's single triangle and single sine with
  a base TB (5 °C fitted best) and an upper TU, and a modified triangle summing (DD1 −
  DD2) (l. 474-558); a high threshold after veraison after Molitor et al. 2013 (l. 574);
  a cubic correction of Tmax from radiation-use efficiency (Eq. 10, l. 785).
- **Fits:** budbreak to bloom UniForc, 491.2 °C·d, RMSE 4.3 d (validation 6.7 d); bloom
  to fruit set TU 25.4 °C, 47.6 °C·d, RMSE 1.6 d; fruit set to veraison TU 20.9 °C,
  744.4 °C·d, RMSE 4.8 d (7.1 d when predicted in sequence); sparkling-base maturity
  (16.5 °Brix) TU 25.7 °C, 286 °C·d, cross-validation 8.3 d; wine maturity TU 29.4 °C,
  8.5 d (l. 742-810). The abstract's 29.8 °C at bloom appears nowhere in the results
  (l. 67-69).

## Dependence

- **Borrows** Chuine 2000, Zalom et al. 1983, Molitor et al. 2013 (`molitor2014` kin)
  and Nendel 2010; fitted to the authors' trial, validated on others' dates.

## Bearing (2026-10-13)

- Chris's pruning-date item: regrowth date is used as a tool to spread temperatures, not
  modelled as a driver; the stage dates per treatment are in a figure. The upper limits
  (20.9 °C for fruit set to veraison) are the finding for a Lleida Chardonnay.
