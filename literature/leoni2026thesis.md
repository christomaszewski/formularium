---
id: leoni2026thesis
citation: Leoni, S. 2026. Integrating spore monitoring and molecular aerobiology to investigate grapevine pathogens dynamics and airborne fungal ecology in vineyards. PhD thesis (Sc. 5993), Université de Genève
doi: 10.13097/archive-ouverte/unige:193385
read: 2026-10-27, in full for downy mildew and weather records and the oospore chapter, by a reading agent (claude-sonnet-5-5); 54 of 54 quotes found at their lines by scripts/verify_quotes.py; Table 3.1 and the paper's Table 1 read in the page images by the main session; for Agrarium and Cooptera D58
status: read
diseases: [downy mildew, powdery mildew, grey mould]
crops: [grapevine]
regions: [Switzerland, Vaud, Changins]
processes: [oospores, oospore maturation, spore trapping, primary infection, first symptoms, aerobiology]
records: [leoni2026.oospores]
datasets: [leoni2026.geneva_thesis, leoni2026.changins_primary, leoni2026.changins]
files: [2026-leoni-10-13097-archive-ouverte-unige-193385.pdf (supplied by Chris, the 2026-10-27 theses-d58 drop)]
---

# Leoni 2026: the thesis behind the Changins oospore model, with a different fit of it

A Geneva thesis on spore monitoring at Agroscope Changins; its oospore chapter is the
manuscript of `leoni2026`, but its coefficients are not the paper's.

**Read this first.** The oospore GLM appears twice with different numbers. The paper's Table 1
(p. 11) counts rainy days "since 1 January": intercept 2.36, precipitation +0.00076, rainy days
−0.034, degree-days −0.0046, residual deviance 40.44, AIC 307.68. The thesis's Table 3.1
(p. 170), on the same 96 observations, counts rainy days in "the last 30 days": 2.23,
−0.00092, −0.056, −0.0068, residual deviance 34.68, AIC 301.91. The paper's own methods define
the variable as rain days "in the 30 days prior to sampling". Both tables were read in the page
images. The engine runs the paper's (`leoni2026.oospores`; flagged there).

## What it holds

- **Site:** everything at Agroscope Changins: a never-sprayed outdoor laboratory with oospore-rich
  litter laid each autumn since 2003, and Pinot noir and Chasselas plots 70 m away.
- **First oil spots** in the outdoor laboratory: 25 May 2021, 11 May 2023, 16 May 2024.
- **Primary infections, 2004-2025:** the observed day and the laboratory-observed oospore
  maturity for 20 years (Tables 3.2-3.3, pp. 182-183; no 2011 or 2022).
- **2024 incidence and severity** per block, about 7 dates (Tables 2.7-2.8); only the untreated
  control is unsprayed.
- **Weather:** the Agrometeo station beside the plots, daily (temperature, humidity, rain, leaf
  wetness, dew point, radiation); no hourly or in-canopy series printed.
- **Spore catches** (SporeStick, qPCR; holographic detector) in figures only.
- **Rainwater fungi,** monthly 2018-2022 (Chris's two spreadsheets; also Zenodo
  10.5281/zenodo.18745101): taxa by sample, no Plasmopara, no disease or weather.

## Dependence

The oospore chapter shares data, authors and form with `leoni2026` (the engine's model).

## Bearing (2026-10-27)

- For Cooptera: which rainy-day window the published coefficients belong to is unsettled; the
  thesis's 30-day fit is the better one by deviance. Worth asking the authors before E-anything
  depends on it.
- For D58: the 20-year primary-infection days (Table 3.3) with the Agrometeo station's daily
  weather are the thesis's best record, at one plot with concentrated inoculum. The data are
  not deposited; the thesis is "protected by copyright".

## Tables 3.2-3.3 transcribed (2026-10-27)

For Cooptera (literature/requests/leoni2026-changins.md): both tables, read in the page images
of pp. 182-183, are in `leoni2026_changins_primary.csv`, one row per year 2004-2025.
- 2011 and 2022 are not printed; the published paper (p. 11) says no symptom was seen then.
- Table 3.2's columns "GLM-based − TDD > 140" and "VM based on GLM − VM based on TDD > 140"
  carry the opposite sign in every row: they are TDD minus GLM. Three cells of the second
  (2004, 2005, 2006) also disagree with Table 3.3's days, by 1, 5 and 2 days. Left as printed.
- "Observed primary infection" is not defined in the oospore chapter; the outdoor laboratory's
  leaves were assessed weekly from May to June for the first symptoms (p. 61).
- The plot is at 46°23'47.7"N 6°13'54.0"E (p. 158); the Agrometeo station at 46°23'53.4"N
  6°13'50.4"E (p. 160), about 190 m away (arithmetic).
- The GLM was fitted on germination observations of 2004-2024, so only 2025 lies outside its
  fitting years. Confirmed 2026-10-27: Table 3.1's n = 96 is "the complete dataset (n = 96)"
  before BBCH 13, against "recent observations (n = 24)" (p. 166); the full set is 175
  observations (p. 162). Which year each of the 96 is from is not printed.
- Table 3.3's observed oospore maturity is "the laboratory-observed maturity date" (p. 172):
  the same germination tests, by the same method, in the years they share. That is how the
  thesis names it; the rule that turns a year's tests into one date (the first MTG at 1, or
  below 1.5) is not stated in the passages read. Through the threshold, which was chosen to
  fit these dates (p. 172), 2025 also bears on the model.

