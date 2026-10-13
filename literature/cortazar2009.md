---
id: cortazar2009
citation: García de Cortázar-Atauri, Iñaki, Brisson, Nadine & Gaudillere, Jean Pierre. 2009. Performance of several models for predicting budburst date of grapevine (Vitis vinifera L.). International Journal of Biometeorology 53:317-326
doi: 10.1007/s00484-009-0217-4
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 as the source of two catalogue phenology records, read then by Agrarium without a note
status: read
diseases: []
crops: [grapevine]
regions: [France, Angers, Epernay, Montpellier, Bordeaux, Colmar]
processes: [phenology, budburst, dormancy, chilling, degree-days]
records: [cortazar2009.budburst, cortazar2009.brin, bidabe1965.cold_action, richardson1974.forcing_hours]
datasets: [phenoclim]
files: [2009-cortazar-atauri-10-1007-s00484-009-0217-4.pdf]
---

# García de Cortázar-Atauri, Brisson & Gaudillère 2009: budburst models on PHENOCLIM

The source of the catalogue's `cortazar2009.budburst` (degree-days above 5 °C from 1
January) and `cortazar2009.brin` (Bidabé's cold action, then forcing hours), and of the
citations behind `bidabe1965.cold_action` and `richardson1974.forcing_hours`. Held since
2026-10-07; this is its note.

## What it holds

- **Data:** budburst (Baggiolini's stage C, Coombe's stage 4; l. 293-294) of ten cultivars
  at five sites (Angers, Epernay, Montpellier, Bordeaux, Colmar; l. 25-28, 166-190) from
  PHENOCLIM, 1970-2002, observed by trained research-station staff (l. 109-125); 616
  observations (Table 8's column sums, l. 740-749); daily maximum and minimum temperatures
  from station weather (l. 196-204).
- **Models:** GDD with base 10 (GDD10) or 5 (GDD5), summed from 1 January until a
  cultivar sum Gc (eq. 1, l. 326-346, 392-399); RIOU (Riou 1994's development of Pouget),
  a daily action exp(0.07 T) − 1.91 exp(−0.126 T) summed over 24 interpolated hourly
  temperatures (eq. 2, l. 405-431); BRIN, Bidabé's Cold Action for dormancy with chilling
  summed from 1 August to a cultivar threshold Cc (eq. 6, l. 476-490) and then growing
  degree hours above T0B to Gc (eqs 3-5, l. 402-439), with hourly temperatures
  interpolated from Tn and Tx over a 12 h day (l. 409), the upper cardinal temperature 25
  °C (Pouget 1968; l. 438). Q10 is fixed at the cultivar mean 2.17 and T0B at 5 °C,
  chosen "on the basis of other authors' experiments" though base 6 gave the lowest
  cross-validation error (10.96 against 11.02 d; l. 594-598, 658).
- **Parameters** (Table 8, l. 740-749; the text layer, not the page image): GDD10 Gc 33.3
  to 57.0 °C·d; GDD5 Gc 220.1 to 321.3 °C·d; BRIN Cc 94.3 (Ugni Blanc) to 108.2
  (Riesling) chilling units and Gc 6,577 (Chardonnay) to 9,174 (Grenache) degree-hours.
- **Errors (RMSEP, days):** GDD10 9.6-18.9, RIOU 13.8-21.5, BRIN 8.2-14.2 (l. 740-749; the
  text rounds them to 9-18, 9-21 and 8-14, l. 33, 583, 661). GDD5 beats BRIN for Merlot
  (7.4 against 8.2), Grenache (8.2 / 8.8), Riesling (9.2 / 10.8), Syrah (11.0 / 11.1) and
  Ugni Blanc (8.8 / 10.5), so the abstract's claim that BRIN beats every other model for
  all cultivars (l. 36, 660-661) does not hold; the discussion itself calls GDD5 "the best
  model so far" for its fewer parameters (l. 713-717). Starting the sum on 1 February
  lowers quality (data not shown, l. 718).
- **Dormancy did not matter:** in the ANOVA the dormancy factor is never significant (all
  p > 0.05, Table 7, l. 668, 707), though asterisks sit on p = 0.074 and 0.054 (l.
  703-704); base temperature, daily or hourly step and variety all matter (p < 0.001).
  Model-dated dormancy break always falls before 1 January (l. 666).
- **Cited sources as printed** (l. 776-780 and after): Bidabé 1965a, C. R. Acad. Agric. Fr.
  49:934-945, and 1965b, 96e Congrès Pomologique, 51-56; Richardson, Seeley & Walker 1974,
  HortScience 9:331-332 (the peach rest model), and Richardson et al. 1975.
- **Garbled:** the CU expression of eq. 6 and RIOU's sinusoid and parabola are not in the
  text layer; whether Table 8's RMSEP is in-sample or cross-validated is not stated
  (l. 480-481, 527-534).

## Dependence

- **Fitted to** PHENOCLIM's budburst dates (`phenoclim`), observed; no model dated them.
- **Borrows** Bidabé 1965's cold action and Richardson et al. 1974's forcing hours (both
  from fruit trees, l. 436-439), as the catalogue records; GDD10's base 10 is credited to
  Winkler 1962 and others (l. 399); RIOU to Riou 1994 and Pouget 1968, 1988 (l. 405).
- **Engine pieces:** `cortazar2009.budburst` is GDD5 here (the thesis's Table 11 holds the
  same values, the catalogue says); `cortazar2009.brin` is BRIN with eqs 3-6 and Table 8.
  Both of the catalogue's structure tags stand (degree-day phenology; chilling dormancy).
- **Authors:** García de Cortázar-Atauri is an author of `cortazar2010`, `parker2011` and
  `parker2013`-type models: flags.

## Bearing (2026-10-12)

- The records stand. For Agrarium's truth, the paper's own result argues for a budburst
  model of a different form than GDD5 or BRIN (both engine pieces); it also shows that a
  chilling stage adds nothing measurable at these French sites, so a truth may use
  chilling only if it wants a structural difference, not a better fit.
- 2026-10-13: the thesis's Table 11 (`cortazar2006`, p. 43) read in the page image: the
  same values as Table 8; the GDD5 sums are now Published on `cortazar2009.budburst`.
