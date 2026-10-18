---
id: segoviacardozo2021
citation: Segovia-Cardozo, Daniel A., Rodriguez-Sinobas, Leonor, Diez-Herrero, Andres, Zubelzu, Sergio & Canales-Ide, Freddy. 2021. Understanding the mechanical biases of tipping-bucket rain gauges: a semi-analytical calibration approach. Water 13(16):2285
doi: 10.3390/w13162285
read: 2026-10-18, LIGHT (abstract, methods, site and selected results and discussion), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py; Eqs 3-10 (pp. 5-6), Figs 9-10 and Tables 1-3 (pp. 11-12) read in the page images by the reading agent, since the text layer is overprinted in places
status: read
diseases: []
crops: []
regions: [Spain, Sierra de Gredos]
processes: [rainfall, tipping-bucket rain gauge, undercatch, sensor error, calibration]
records: []
datasets: []
files: [daniel_2021.pdf (the 2026-10-18 drop)]
---

# Segovia-Cardozo et al. 2021: mechanical bias of tipping-bucket rain gauges

Two Davis gauges (Rain Collector II, RC1; Rain Collector 7852M, RC2) calibrated in the
laboratory at rain intensities of 32 to 900 mm h-1, and the method applied to 13 years of 10
gauges in the Venero Claro basin (15.53 km², eastern Sierra de Gredos).

## What it holds

- **Gauges** (l. 144-150): manufacturer 0.2 mm per tip, ±4 % up to 50 mm h-1 and ±5 % from
  50 to 100 mm h-1; bucket volume 4.245 mL (RC1) and 4.28 mL (RC2); funnel orifice 0.1963 cm² (l. 147; the collecting area is 212.27 and 214 cm², l. 149)
  as printed.
- **Mechanism** (l. 909-912, Eqs 3-10): the bucket's tipping time falls with intensity
  (linear fit R² 0.74 and 0.644; a 40 % cut at 480 mm h-1 for RC1 and 43 % at 470 mm h-1 for
  RC2), so water that arrives during the tip is lost or credited to the next bucket. Three
  calibrations are compared: static (water dropped slowly to fix 0.2 mm per tip), dynamic
  (33 and 45 tests of 10-20 min, l. 185-187) and a semi-analytical one (tip movement plus a
  drop-size surplus, Eqs 4-9) with a simplified one (Eq 10).
- **Error by intensity** (Table 1, p. 11, l. 1366): static RMSE 4.8 % (RC1) and 9.4 % (RC2) up
  to 100 mm h-1; 10.9 % and 28.0 % up to 900 mm h-1; dynamic RC1 2.9 % to 900 mm h-1. Total
  error of the methods 2 % to 28 % by intensity (l. 1619). Dynamic and semi-analytical errors
  below 100 mm h-1 (about 2 % RC1, 5 % RC2) are under half the manufacturer's 5 % (l. 1626).
- **In the field** (Tables 2-3, l. 1425-1436): 64.6-67.2 % of the rain falls below 10 mm h-1;
  above 200 mm h-1 the share is 15.7-24.4 % at three gauges. The static calibration is out
  by more than 6 % at Collado Morales (55-60 mm per year of 701 mm) and by about 1 % at La
  Dehesa; over the basin 2.05-2.48 % between methods.
- **Cited** (l. 1622-1623): other tipping-bucket studies 5.2-37.7 % by intensity (Sypka), 5-29 %
  (Humphrey et al.), 2-16 % (Niemczynowicz), 10 % under-reading between 25 and 400 mm h-1
  (Marsalek).
- **Not printed:** the fitted regression coefficients as numbers (R² and slopes only); the
  slope units; the rain series as data; the second site's labels beyond the table.

## Dependence

- The semi-analytical equations are the authors' own; the test follows UNE-EN 17277:2021 and
  the static calibration follows the manufacturer and Humphrey et al.; one calibration per
  gauge model is applied to all basin gauges, which the authors call an uncertainty (l. 623).

## Bearing (2026-10-18)

For strand 5 (sensor error): what an observation model in Agrarium could take.

- **Bias:** a rain-gauge undercatch that rises with intensity: a static error of up to 28 %
  by 900 mm h-1 for one model against 2.9 % after a dynamic calibration; at the usual
  intensities (two thirds of the rain below 10 mm h-1) a few percent. So a daily total is
  biased little, but an hourly peak is read low. Davis datasheet ±4-5 %.
- **Noise:** the 0.2 mm resolution (the tip). Nothing on repeatability beyond RMSE.
- **Threshold:** the 0.2 mm tip is itself a detection threshold: lighter or intermittent
  rain, drizzle or dew below it is not counted until a bucket fills. Not tested here.
- **Drift, failure:** not studied (no blockage, no leaf litter, no freezing).
- **Kind of result:** a laboratory calibration with a field application on 13 years
  of a mountain basin. Wind undercatch (a separate and larger error) is not in the paper.
- **Can it run:** the form is printed (Eq 10) but coefficients are per gauge and not
  printed.
