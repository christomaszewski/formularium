---
id: chacon2021
citation: Chacón-Vozmediano, Juan Luis, Martínez-Gascueña, Jesús & Ramos, María Concepción. 2021. Projected effects of climate change on Tempranillo and Chardonnay varieties in La Mancha Designation of Origin. Agronomy for Sustainable Development 41:24
doi: 10.1007/s13593-021-00672-5
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; the base temperatures and thresholds (p. 6) read in the page image by the main session; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [La Mancha, Castilla-La Mancha]
processes: [phenology, budburst, flowering, veraison, maturity, climate projection, grape composition]
records: [chacon2021.gdd]
datasets: [chacon2021.lamancha]
files: [2021-chacon-vozmediano-10-1007-s13593-021-00672-5.pdf]
---

# Chacón-Vozmediano, Martínez-Gascueña & Ramos 2021: La Mancha stages by degree-days

Twenty years of Tempranillo and Chardonnay stage dates at 663 m in La Mancha, fitted by
Ramos 2017's degree-day method and projected to 2050 and 2070, with stepwise regressions
of grape composition on the period's weather. A threshold model, not the requested form.

## What it holds

- **Data** (`chacon2021.lamancha`): two series per variety 2000-2019 plus two or three
  plots in half the years (l. 140-142), stages at 50 % of lots of four vines (l. 180);
  Argamasilla de Alba station with Tomelloso filling gaps (l. 103-106); 350 mm a year
  (l. 95). Mean bud break 16 April (Tempranillo) and 5 April (Chardonnay), flowering 31
  May, veraison 26 July, maturity 23 August (l. 237, 386).
- **Model** (`chacon2021.gdd`; p. 6): PLS on 10-day chill portions and growing degree
  hours from 1 October to 30 April fixes the start, 26 February (Tempranillo) and 11
  March (Chardonnay) (l. 153-167, 312); the base per stage by minimising the SD of the
  sum (l. 180-182): 6.6, 6.4, 3.2, 12.5 °C and 0.0, 5.5, 1.1, 10.5 °C; sums with Tmax
  capped at 22 °C: 180 ± 40, 431 ± 38, 1,020 ± 55, 259 ± 68 and 276 ± 52, 479 ± 33,
  1,207 ± 49, 262 ± 72 °C·d (l. 266-271). RMSE in-sample, Tempranillo bud break 5.5 d
  (Table 1, l. 372).
- **Projections** (Table 2): a 17-model MarkSim ensemble, RCP4.5 and RCP8.5 (l. 133-145);
  by 2050 under RCP4.5, Tempranillo 6, 11, 9, 8 d earlier and Chardonnay 4, 9, 9, 10
  (l. 24-25); by 2070 under RCP8.5 up to 11 and 7 d for bud break, 19 d for Tempranillo's
  flowering (l. 315-317). Temperature only; rain left out (l. 344-347).
- **Composition** (Table 4): acidity −0.28 g/L and total anthocyanins −164 mg/L per °C
  of Tmax between flowering and veraison (Tempranillo, R² 0.63; l. 423, 494-498); the
  text credits GDD with the most variance though Table 4 keeps none (l. 413).

## Dependence

- **Computes** Ramos 2017's method (`ramos2017.budburst`) with the Dynamic Model,
  growing degree hours (Parker et al. 2011's 26 °C optimum) and FAO-56 ET; fitted to
  IRIAF's own observations, no model dated them. Base, thresholds and RMSE from the same
  years.
- **Authors:** Ramos, as in `ramos2017`, `ramos2018` and `ramos2010`.

## Bearing (2026-10-13)

- Not the requested form. Its use is a Spanish inland Chardonnay parameter set beside
  `ramos2017`'s Penedès one: the base temperatures driven to 0 °C show the limit of the
  SD-minimising fit.
