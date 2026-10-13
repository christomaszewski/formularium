---
id: fraga2016
citation: Fraga, H., Santos, J. A., Moutinho-Pereira, J., Carlos, C., Silvestre, J., Eiras-Dias, J., Mota, T. & Malheiro, A. C. 2016. Statistical modelling of grapevine phenology in Portuguese wine regions: observed trends and climate change projections. Journal of Agricultural Science 154(5):795-811
doi: 10.1017/S0021859615000933
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Eqs 1-6 (p. 802), Table 1 (p. 798), Table 4 (p. 803) and Tables 5-7 (pp. 804-805) read in the page images by the main session; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Portugal, Lisbon, Vinhos Verdes, Douro]
processes: [phenology, budburst, flowering, veraison, climate projection]
records: [fraga2016.monthly_regression]
datasets: [fraga2016.portugal]
files: [2015-fraga-10-1017-s0021859615000933.pdf]
---

# Fraga et al. 2016: stage dates as linear functions of monthly temperature

The first phenology model in the catalogue that sums no heat: each stage's day of year
is a straight line in one or two monthly temperature means, fitted per variety on
Portuguese series of 11 to 22 years, with coefficients printed for 14 varieties. From
UTAD (Vila Real) and the Portuguese wine institutes.

## What it holds

- **Data** (`fraga2016.portugal`; Table 1, p. 798): field-observed budburst, flowering
  and veraison (OIV descriptors, l. 185) of 14 varieties at Dois Portos, Lisbon (series
  within 1990-2011, 11 to 22 years each), Loureiro at Arcos de Valdevez, Vinhos Verdes
  (2003-2012, l. 128) and Touriga-Franca at Ervedosa do Douro (2001-2011, l. 175), with
  monthly means of daily Tmin, Tmax and Tmean from each site's station (l. 181); the
  Douro station is about 20 km from the vineyard (l. 668).
- **Form** (Eqs 1-6, p. 802; l. 380-397): DOY = k + α·x1 (+ β·x2), the predictors chosen
  by forward (P < 0.05) and backward (P < 0.10) stepwise selection on the two longest
  series, Fernão-Pires (white) and Castelão (red) (l. 176, 189), from candidates that are
  monthly and multi-month means (Table 2). White: budburst on Tmin February-March,
  flowering on Tmax March-April, veraison on Tmin March-July and Tmax March-April. Red:
  Tmin January-March, Tmax March-April, Tmax June-July and Tmean March-April
  (l. 315-316, 366-369). The abstract names other veraison windows (l. 33).
- **Coefficients** (Tables 5-7, pp. 804-805; `fraga2016.monthly_regression`): k, α and β
  for six white and six red Lisbon varieties and the two other regions' varieties, each
  with leave-one-out R²cv and RMSE. Budburst slopes −3.6 to −9.5 d/°C, flowering −5.3
  to −9.1 d/°C. The calibration varieties' own coefficients are not printed; their
  scores are R²cv 0.63 and 0.69 (budburst, RMSE 4.5 and 4.6 d), 0.79 (flowering, 3.9 d),
  0.77 and 0.88 (veraison, 5.0 and 2.9 d) (Fig. 4, Table 4).
- **Scores:** 16-variety mean R²cv 0.71 (budburst), 0.83 (flowering), 0.78 (veraison)
  (l. 34-35, 596); the lowest 0.32 and 0.38 for budburst of Loureiro and Touriga-Franca
  (l. 397-398), where the model was transferred. The printed white means (flowering
  0.87, veraison 0.86) do not reproduce from Table 5 (0.86, 0.80, l. 387-390).
- **Against degree-days** (Table 4, p. 803): a 10 °C GDD model on the two calibration
  varieties gave budburst R²cv 0.40 and 0.48 (RMSE 5.7 and 6.0 d) and veraison 0.31 and
  0.53; a base fitted by minimising the SD (9.2 and 8.9 °C, l. 270) did no better.
- **Projections:** four EURO-CORDEX pairs, RCP4.5 and RCP8.5, 2040-2070 against
  1991-2011 (l. 284-297, 511): budburst 1-5 d earlier (red) and 1-3 (white), flowering
  2-6 d, veraison 6-14 d (l. 521-524); flowering-veraison 4-8 d shorter (l. 512).

## Dependence

- **Fitted to** the authors' own observed series; no model dated them. The GDD
  comparator borrows the 10 °C base (Winkler et al. 1974) and the SD-minimising base
  (Zapata et al. 2015).
- **Form shared** with `didevarasl2026.monthly_regression` (the same sum, different
  windows); unrelated to the engine's degree-day and chilling pieces.
- **Authors:** none on an engine model.

## Bearing (2026-10-13)

- For Agrarium: the requested form, printed in full for 14 varieties (Merlot, Pinot,
  Grenache and Riesling among them), with its errors beside a degree-day model on the
  same data. It is retrospective (the veraison windows close in July) and the authors
  say it needs local calibration: a Penedès use means refitting k and α on the
  region's own series, keeping the windows.
- The slopes themselves are the useful prior: about 4-10 d of budburst per °C of the
  late-winter minima.
