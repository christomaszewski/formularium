---
id: ramos2023
citation: Ramos, María Concepción & Yuste, Jesús. 2023. Grapevine phenology of white cultivars in Rueda Designation of Origin (Spain) in response to weather conditions and potential shifts under warmer climate. Agronomy 13(1):146
doi: 10.3390/agronomy13010146
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Table 1 (p. 8) and Tables 3-4 (p. 10) read in the page images by the main session; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Rueda, Castilla y León]
processes: [phenology, budburst, flowering, veraison, ripening, water balance, climate projection]
records: [ramos2023.gdd, ramos2023.regression]
datasets: [ramos2023.rueda]
files: [2023-ramos-10-3390-agronomy13010146.pdf]
---

# Ramos & Yuste 2023: Rueda's white cultivars by degree-days and by stepwise regression

Fourteen seasons of Verdejo, Viura and Sauvignon Blanc in Rueda (700-930 m), both as a
degree-day model with a base per stage and variety (validated on separate plots) and as
stepwise regressions of each stage on the previous period's temperature and water, with
Verdejo's slopes printed in the text.

## What it holds

- **Data** (`ramos2023.rueda`): 13 plots 2008-2021, the Consejo Regulador's records
  (l. 142-146, 775); stations Rueda (709 m) and Medina del Campo (726 m) (l. 266);
  110 mm of rain in the growing season (l. 355). Verdejo budbreak 18 April ± 9,
  flowering 11 June ± 9, veraison 15 August ± 6, ripening 20 September ± 6; Viura later,
  Sauvignon Blanc about 10 d earlier (l. 364-371); all earliest in 2017 (l. 373).
- **Degree-days** (`ramos2023.gdd`; Table 3, p. 10): from 20 March (day 80, after the
  chill phase, l. 552), bases by minimising the SD of the sum, Tmax capped at 26 °C
  (l. 298-305): Verdejo 5.4, 5.4, 5.8, 4.9 °C and 127, 660, 1,765, 2,365 °C·d; Viura 5.4,
  5.4, 5.7, 4.4 and 162, 665, 1,882, 2,484; Sauvignon Blanc 6.1, 5.7, 5.4, 3.4 and 104,
  619, 1,593, 2,471, cumulative from day 80. Verdejo fitted on two plots and validated on
  two: RMSE 5.4, 3.7, 6.1, 5.9 d (l. 306-308); the others 2.5-5.9 d.
- **Regressions** (`ramos2023.regression`; Table 1, p. 8): forward stepwise on the
  period's Tm, Tmax, Tmin and P minus ETc; R² 0.51, 0.68, 0.45, 0.67 (Verdejo), 0.67,
  0.56, 0.38, 0.60 (Viura), 0.73, 0.47, 0.41, 0.55 (Sauvignon Blanc), the terms printed
  as sign and share only. Verdejo in the text: budbreak 6.6 d earlier per °C of the
  previous month's mean, flowering about 10, ripening about 4 d per °C, veraison 1.6 d
  per °C of Tmin (0.5-2.7 by plot); ripening 2.6 and veraison 1.9 d later per 10 mm of
  water balance (l. 495-512). Budbreak and flowering follow the pre-budbreak
  temperature, the later stages the period just before (p. 8).
- **Projections** (Table 4): five MarkSim models; by 2050 Verdejo flowering 7, veraison
  13 and ripening 20 d earlier under RCP4.5 and 9, 16, 25 under RCP8.5; Viura's veraison
  19 d; 29 d of ripening by 2070 (l. 603-613); Tmax +3.4 to +4.3 °C by 2050 (l. 520).
  Yield falls 95-132 kg/ha per 10 mm of pre-veraison deficit (l. 691).

## Dependence

- **Computes** Ramos 2017's method (`ramos2017.budburst`) with the Dynamic Model and
  growing degree hours; fitted to the Consejo's observed dates, the water balance a
  FAO-56 model's. Cites `chacon2021`, `ramos2022`, `caffarra2011` (as "Cafarra").
- **Authors:** Ramos and Yuste, as in `ramos2018`.

## Bearing (2026-10-13)

- Both forms on one dataset: the degree-day model validated on held-out plots (4-6 d)
  and the regression form with R² 0.4-0.7 and only a few slopes printed. For a Penedès
  white (Viura is Macabeo), the Rueda Tb and sums are the nearest published set after
  `ramos2017`.
