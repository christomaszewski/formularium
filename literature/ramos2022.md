---
id: ramos2022
citation: Ramos, M. C. & Martínez de Toda, F. 2022. Influence of weather conditions and projected climate change scenarios on the suitability of Vitis vinifera cv. Carignan in Rioja DOCa, Spain. International Journal of Biometeorology 66(5):1067-1078
doi: 10.1007/s00484-022-02258-6
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 53 of 53 quotes found at their lines by scripts/verify_quotes.py; the Results page (p. 1071) read in the page image by the main session; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Rioja]
processes: [phenology, flowering, veraison, harvest, climate projection, grape composition]
records: [ramos2022.gdd]
datasets: [ramos2022.rioja]
files: [2022-ramos-10-1007-s00484-022-02258-6.pdf]
---

# Ramos & Martínez de Toda 2022: Carignan's stages and composition in Rioja

Thirteen seasons of Carignan at two Rioja plots, fitted by Ramos 2017's degree-day method
after a 100-chill-unit start, with per-degree slopes stated in the text, and composition
and dates projected to 2050 and 2070. A threshold model, from Lleida and La Rioja.

## What it holds

- **Data** (`ramos2022.rioja`): plots at 428 and 460 m, not irrigated, 2008-2020, stages
  at 50 % of surveyed plants (l. 115-127); Logroño stations at 408 and 456 m (l. 128);
  flowers separated 25 May ± 5 (17 May to 5 June), veraison 19 August ± 6, harvest 30
  September ± 9 (1 September to 12 October) (p. 1071). Soil water from the VSIM model
  (l. 176-180).
- **Model** (`ramos2022.gdd`; p. 1071): 100 chill units reached 15-25 March; degree-days
  from 15 March above 7.4, 6.3 and 5.2 °C to 1,350, 1,690 and 2,480 °C·d for flowers
  separated, veraison and maturity, Tmax capped at 26 °C (l. 182); RMSE 6.82, 5.16, 8.71
  d, Willmott d 0.57, 0.87, 0.68, on the fitting seasons.
- **Slopes in the text:** veraison about 2.7 d earlier per °C of the bloom-to-veraison
  mean, maturity 3.65 d per °C of the veraison-to-maturity mean (l. 283-289); no
  equation or R² (Table SM1). Trends 0.93 and 0.83 d/yr earlier for veraison and harvest
  over 2008-2020 (l. 273); Tmax +0.13 and Tmin +0.15 °C/yr (l. 435).
- **Projections** (Table 3): the same 17-model ensemble as `chacon2021`; by 2050 under
  RCP4.5 flowers separated 4, veraison 6 and maturity 11 d earlier (the abstract says 5,
  8, 11), maturity 17 d under RCP8.5 and 26 d by 2070; berry weight −26 to −33 g per 100,
  acidity −0.26 to −0.34 g/L (l. 390-413).
- **Composition:** four varimax factors hold 85 % of the variance; stepwise models explain
  13, 29 and 11 % of total and malic acidity and anthocyanins (l. 328, 376).

## Dependence

- **Computes** Ramos 2017's method (`ramos2017.budburst`, `chacon2021.gdd`) with the
  Dynamic Model and growing degree hours; fitted to the authors' observed dates; the
  water variable is VSIM's, a model's.
- **Authors:** Ramos, as in `ramos2010`, `ramos2017`, `ramos2018`, `ramos2023`.

## Bearing (2026-10-13)

- A threshold model; its per-degree slopes (2.7 and 3.65 d/°C for the later stages) are
  the Rioja counterpart of Ruml's and Fraga's, stated without equations.
