---
id: zabel2023
citation: Zabel, F. & Poschlod, B. 2023. The Teddy tool v1.1: temporal disaggregation of daily climate model data for climate impact analysis. Geoscientific Model Development 16:5383-5399
doi: 10.5194/gmd-16-5383-2023
read: 2026-10-18, LIGHT (abstract, Sect. 1-5, code availability), by a reading agent (claude-haiku-5-5); 19 of 19 quotes found at their lines by scripts/verify_quotes.py; Fig. 3 (PDF page 4) read in the page image by the reading agent
status: read
diseases: []
crops: []
regions: [global]
processes: [disaggregation, hourly weather, wet hours, relative humidity]
records: []
datasets: []
files: [florian_2023.pdf (the 2026-10-18 drop)]
---

# Zabel & Poschlod 2023: Teddy, disaggregating daily climate-model data

A MATLAB tool that turns daily ISIMIP3 climate-model output into hourly series by picking
the most similar day from WFDE5 (bias-adjusted ERA5) within a day-of-year window, then
rescaling so the daily mean (sum for precipitation) is kept (l. 146, 254). No record: it
serves climate-model output, and its code has no stated licence.

## What it holds

- **Variables** (Table 1): tas, hurs, rsds, rlds, sfcwind, ps, pr. Specific humidity is
  turned to relative humidity with Buck's equation (l. 195); RH is limited to 100 % with the
  daily mean preserved (l. 260).
- **Method** (Sect. 3): days classed wet or dry with sequence classes (l. 211); 23 days from
  each of 40 reference years (1980-2019), 920 days (l. 207-208); window of ±1 to 25 days or 0,
  widened to ±50 d if no rain day is found (l. 264); precipitation event duration from a
  regression on amount (l. 264); rain placed at night by default (l. 306); drizzle below
  1 mm/d disaggregated too (l. 311).
- **Tests** (Sect. 4): 30 global samples, 2010: Pearson r above 0.9 for all variables except
  wind (0.7) and precipitation (0.4) (l. 347). Sample 16 (Ethiopia, ten days, window 7):
  hurs R 0.94, NSE 0.88, RMSE 4.5 %, MAE 3.5 % (Fig. 3, l. 126, from the page image). Wet
  hours (above 0.1 mm/h), sample 29, Germany, 40 years: MAE 13.02 h, 7.8 % (l. 381-384);
  windows of 9 d or more count wet hours better (l. 411).
- **Code:** Zenodo 10.5281/zenodo.8124111, v1.1 and parallel v1.1p (l. 498); no licence
  printed. Equations are not printed in the text layer.

## Dependence

- Trained on WFDE5 (Cucchi et al. 2020, 2022), a reanalysis product; consistent with ISIMIP3
  bias adjustment (l. 500). No other disaggregation model is the data.
- Buck 1981 for the humidity conversion.

## Bearing (2026-10-18)

For Agrarium's sweep (thousands of seasons of hourly weather driving a leaf-wetness model
whose engine counterpart is RH ≥ 90 %):

- **Variables and co-variation:** seven hourly variables, including wind speed (no
  direction), taken together from one reference day, so rain, humidity and wind keep that
  day's pattern. Rain falls at night by default.
- **Near saturation or wet hours:** wet hours are validated (MAE 13.02 h a year, 7.8 %, one
  German sample). Not validated on humidity near saturation: only r (above 0.9) and one
  ten-day example.
- **Where fitted and tested:** WFDE5 reference years 1980-2019, 30 global samples (2010) and
  one 40-year German sample.
- **Code and licence:** MATLAB on Zenodo, no licence stated.
- **Can it run:** MATLAB, with a compiled Windows executable; hourly output only at climate-
  model grid scale (0.5°), and it needs daily climate-model input.
