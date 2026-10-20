---
id: oriolani2015
citation: Oriolani, E. J. A., Moschini, R. C., Salas, S., Martinez, M. I. & Banchero, S. 2015. Predicción de epidemias del oídio de la vid (Uncinula necator (Schwein) Burrill) mediante modelos basados en factores meteorológicos (Weather-based models for predicting grape powdery mildew epidemics). Revista de la Facultad de Ciencias Agrarias, Universidad Nacional de Cuyo 47(2):197-211
doi: 
read: 2026-10-20, in full (Spanish), by a reading agent (claude-haiku-5-5); 51 of 51 quotes found at their lines by scripts/verify_quotes.py; Table 3 and its definitions read in the page image (p. 204) by the main session
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [Mendoza]
processes: [epidemic rate, cluster incidence, forecasting]
records: [oriolani2015.powdery_rate]
datasets: [oriolani2015.mendoza]
files: [oriolani_2015.pdf (the 2026-10-20 drop)]
---

# Oriolani et al. 2015: daily powdery mildew increase on Mendoza clusters from hourly weather

Six seasons of weekly cluster incidence in one untreated Chenin plot at INTA Mendoza, and
ordinal logistic models that class each date's daily increase as severe, moderate or nil
from the 15 days of hourly weather before it.

## What it holds

- Six seasons (2001/02, 2002/03, 2005/06, 2007/08, 2008/09, 2009/10) at one untreated Chenin
  plot, EEA INTA Mendoza (l. 26-27, 177-180). Incidence on clusters from flowering to
  veraison, observed weekly (l. 184-193).
- Response: daily incidence increment TI% (l. 158-162). Categories from the 25th and 50th
  percentiles of 40 values: 0 and 0.795% (l. 186-192). Severe if TI > 0.795%, moderate if 0
  < TI <= 0.795%, nil if TI = 0.
- Predictors: hourly temperature, rain, RH and wetness from a canopy station, summed over
  the 15 days before each observation (l. 194-201, 253-255). The 15-day window beat 10-14
  days on Kendall correlation (l. 308-314).
- Best single predictor: Dif2 = NPp2 - NPn2 (day-pair counts of warm humid versus cool or
  dry periods), Kendall rk 0.73 (l. 315-319; Table 2).
- Rain and wetness alone were weak: FPr1 0.20, Prt1 0.19, Mojt 0.05, HRt 0.01 (l. 372-374;
  Table 2).
- Model I: 87.5%. Model II (adds FPr1): 90% (36 of 40). Model III (adds FPr2): 92.5% (3 of
  40 wrong) (l. 386-394, 419-430).
- Without humidity in NPp2, model III accuracy fell to 80% (l. 574-577).
- 2000/01 validation (N = 11): PrS exceeded the other classes on only 1, 4 and 19 January
  (l. 317-319, 517-519). No accuracy printed.
- Not printed: standard errors, class counts, the thresholds tested (l. 313), the
  2003/04-2006/07 gap, and whether the software is released (l. 776-778).

## Dependence

- Its own observations; no model dated them. The UC Davis index (Gubler et al. 1999; Thomas
  et al. 1994) and Snyder et al. 1983 are discussed, not used (l. 605-612, 759-766); its
  positive-day band (21.0-29.4 °C) is nearly the UC index's (21.1-29.4 °C), a shared form,
  not a stated borrowing. No engine author.

## Bearing (2026-10-20)

- Recorded as `oriolani2015.powdery_rate` with the dataset `oriolani2015.mendoza`; Table 3
  read in the page image. Kin report against the engine's list (cooptera@6f8d0a2): same form
  as `gubler1999.powdery_index` (temperature-hours-mildew-index), as expected.
- For Cooptera: a published, runnable powdery mildew rate model for an arid region, fitted
  in-sample on 40 dates; for Agrarium, development families only while it shares the UC
  index's form.
