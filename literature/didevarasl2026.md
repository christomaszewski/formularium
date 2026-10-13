---
id: didevarasl2026
citation: Didevarasl, Ali, Deiana, Pierfrancesco, Spano, Donatella, Costa Saura, Jose M., Mercenaro, Luca, Nieddu, Giovanni & Trabucco, Antonio. 2026. Advancing grapevine phenology predictions: a comparison of regression-based statistical learning approach and conventional models in mediterranean environment. International Journal of Biometeorology 70:273
doi: 10.1007/s00484-026-03312-3
read: 2026-10-13, in full, in the publisher's open HTML (no PDF; the text is one line, so the facts cite sections and tables), by a reading agent (claude-haiku-5-5); 60 of 60 quotes found by scripts/verify_quotes.py; Tables 2 and 4 read in the HTML text by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Sardinia]
processes: [phenology, budburst, flowering, veraison, model comparison]
records: [didevarasl2026.monthly_regression]
datasets: [didevarasl2026.sardinia]
files: [didevarasl2026_ijb.html]
---

# Didevarasl et al. 2026: monthly-mean regressions against threshold models on Cannonau

The second non-threshold phenology model in the catalogue: stage dates of Cannonau at
17 Sardinian sites as linear functions of monthly temperatures and rainfall, chosen by
partial least squares and stepwise selection, scored beside degree-day, degree-hour,
chill-day and PhenoFlex models on the same data. From Sassari and the CMCC.

## What it holds

- **Data** (`didevarasl2026.sardinia`): 47 budburst, 42 bloom and 29 veraison dates
  (BBCH 09, 65, 81) of Cannonau within 1991-2020 from the University of Sassari, mean
  day of year 95, 144 and 205; weather from a 2.2 km COSMO-CLM downscaling of ERA5, a
  model product used because stations were few ('Data collection and preparation').
  The site list and the dates are in the supplement, on request.
- **Regressions** (`didevarasl2026.monthly_regression`; Table 4): predictors screened by
  PLS (VIP above 1, repeated), then bidirectional stepwise selection by AIC, from monthly
  means of Tmax, Tmin, Tmean and monthly precipitation over June of the previous year to
  April (budburst), October to June (bloom) and to July (veraison). Budburst DOY =
  12.47 + 1.52·Jun₋₁ Tmax + 2.51·Oct₋₁ Tmin − 0.024·Oct₋₁ P + 0.020·Dec₋₁ P (R² 0.43,
  RMSE 7 d); bloom six terms from 302.07 (R² 0.58, 5.5 d); veraison five terms from
  349.78 (R² 0.55, 4.5 d) (Table 2). No heat sum is a predictor. Table 2's caption says
  five variables a stage; the lines print four and six.
- **Threshold models** (Table 1, Table 3): GDD (base 9.61 °C, 376.6 and 1309.8 °C·d to
  bloom and veraison), GDH (9392 and 27,435 °C·h), CAC chill days, two sequential
  combinations of the authors' own, and PhenoFlex, all fitted by a genetic algorithm on
  RMSE. In-sample RMSE: budburst CH_GDH 7 d, C_GDD 8, PhenoFlex 11.5, CAC 15; bloom GDD
  6, GDH 8, PhenoFlex 12.5; veraison GDD 4, GDH 7, PhenoFlex 23. The regressions' 7, 5.5
  and 4.5 d are "comparable".
- **Validation:** leave-one-out for all, but the regression predictors were screened on
  all observations first, which the authors say may flatter it; the regression's own
  LOOCV figure is in the supplement. The authors call the regressions retrospective, as
  calendar months can end after the event.

## Dependence

- **Fitted to** the same dates and the same reanalysis series as the threshold models;
  the bloom and veraison heat sums start at budburst, observed or modelled unsaid.
  C_GDD and CH_GDH are the authors' combinations; PhenoFlex is Luedeling et al.'s.
- **Form shared** with `fraga2016.monthly_regression` (cited as Fraga 2016a; the
  reference list's year differs); the engine's degree-day pieces are comparators here.

## Bearing (2026-10-13)

- The requested form with printed coefficients, on a Mediterranean cultivar with ERA5
  weather: the one case where Agrarium's gridded inputs match the source's. Its error
  is no better than a fitted degree-day model's on the same data, and its R² (0.43-0.58)
  is low: the honest comparison for a monthly-mean approach.
