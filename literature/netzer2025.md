---
id: netzer2025
citation: Netzer, Y. & Ohana-Levi, N. 2025. Interactions Between Leaf Area Dynamics and Vineyard Performance, Environment, and Viticultural Practices. Agriculture 15(6):618
doi: 10.3390/agriculture15060618
read: 2026-10-20, LIGHT with the leaf-area content in full (methods, Tables 1-4, results 3.1, thresholds, discussion), by a reading agent (claude-haiku-5-5); 42 of 42 quotes found at their lines by scripts/verify_quotes.py; Tables 1-2 checked in the text by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Gilboa, Israel]
processes: [leaf area index, deficit irrigation, crop coefficient, LAI dynamics, yield]
records: []
datasets: []
files: [netzer2025.pdf]
---

# Netzer & Ohana-Levi 2025: seven seasons of weekly LAI in deficit-irrigated VSP Sauvignon blanc

An original field study (not a review), 2017-2023: five deficit-irrigation regimes, LAI
measured weekly, analysed against yield and weather with GAMs and XGBoost. Read for the
course of LAI over the season.

## What it holds

- **Site** (l. 125-153): Sauvignon blanc on 1103 Paulsen planted 2009, Gilboa Mountain,
  430 m; vines 1.5 m, rows 3 m (4.5 m² a vine), VSP; Mediterranean, 450 mm of rain a year;
  drip at 30, 45 or 60 % of ETc, or two regulated regimes; irrigation set by Kc = 0.54 LAI
  + 0.16 (Munitz et al. 2019, l. 141-142).
- **LAI method** (l. 328-337): SunScan, three vines a replicate, weekly; validated against a
  LI-COR area meter, R² 0.922 (cited ref 32).
- **Stages** (Table 1, l. 318-324): stage 0 BBCH 07-69 from a mean 19 March, 48 days;
  stage 1 BBCH 69-79 from 6 May, 29 days; stage 2 BBCH 79-85 from 4 June, 25 days; stage 3
  BBCH 85-89 from 29 June, 41 days; post-harvest from 9 August.
- **Mean LAI by stage** (Table 2, l. 414-420; minimum, maximum, median, mean ± SD, all
  seasons and treatments): stage 0 0.31-0.78, mean 0.52 ± 0.10; stage 1 0.77-1.92, 1.22 ±
  0.24; stage 2 0.70-2.48, 1.39 ± 0.36; stage 3 0.78-2.56, 1.41 ± 0.38; post-harvest 0.60-
  2.00, 1.22 ± 0.27.
- **By treatment and year** (Tables 3-4, l. 645-666; the unit is printed mm²/mm²): 1.02
  (30 % ETc) to 1.28 (60 %; 1.26 in the text, l. 628); season means rising from 0.93 (2017)
  to 1.34 (2023).
- **Pruning** (Table 2, l. 409-411): 16 to 48 canes a vine (median 32); pruning weight 0.19
  to 2.54 kg (median 1.16).
- **Threshold** (l. 21, 890): LAI above about 1.6-1.7 lowered yield.
- **Not printed:** the weekly series, leaf area per vine, canopy size.

## Dependence

- Irrigation is set from LAI by Munitz et al. 2019's Kc relation, so the water given
  depended on the measured LAI: a feedback, not a borrowed growth model. Details in
  Ohana-Levi et al. 2022, 2024 (l. 147).

## Bearing (2026-10-20)

- **A Mediterranean deficit-irrigated VSP at about LAI 1.4:** 6.3 m² a vine over 4.5 m²
  (my calculation), with about 32 shoots. Leaf area per vine scales with the vine's ground
  and shoots; the LAI near 1.2-1.4 is the transferable figure.
- **Timing:** relative to stage 3's 1.41, the mean over budbreak to end of flowering is
  0.37, over end of flowering to bunch closure 0.87, to veraison 0.99. A day-based logistic
  fits these interval means with t50 about 26 d and tau about 16 d; if SunScan reads about
  0.3 at budbreak from wood, as the stage-0 minimum suggests (not stated), the fit moves to
  t50 about 40-45 d and tau about 10 d (my calculations). Budbreak here is mid-March.
