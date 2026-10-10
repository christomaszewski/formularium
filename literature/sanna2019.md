---
id: sanna2019
citation: Sanna, F., Deboli, R., Calvo, A. & Merlone, A. 2019. Influence of sensor calibration on forecasting models for vineyard disease detection. IOP Conference Series: Earth and Environmental Science 275:012020
doi: 10.1088/1755-1315/275/1/012020
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Monferrato Piedmont North Italy]
processes: [primary infection, secondary infection, incubation, germination, sporangia, infection risk forecast, leaf wetness, sensor calibration, measurement uncertainty, spray timing, epi index]
records: [epi1983.corrected]
datasets: []
files: [sanna2019-sensor-calibration-forecast.pdf]
---

# Sanna et al. 2019: sensor calibration in vineyard disease forecasting models

A light read (the deep-research B list).

## What it holds

- Two calibrated AWS in a Monferrato vineyard, one sun-exposed (VA), one near trees (VB) (l. 172, 345-347).
- Calibration uncertainty: expanded 0.11 C (k=2) for temperature and 2.5 per cent RH (l. 218, 227).
- The EPI index (Stryzik 1983) flags risk above -10; uncalibrated inputs predicted germination 4 to 5 days early (l. 237, 243, 356).
- First season: germination 6 to 7 April; infection 1 May; symptoms 9 to 10 May (l. 259, 273).
- Calibrated data cut secondary-infection risk by 20 per cent (VA) and 14 per cent (VB); position alone about 11 per cent (l. 407-408).
- Primary infection is printed as 10 C or higher with 10 mm rain in 24 h; the back-calculated incubation curve (Figure 2b) has no cited source (l. 155-156, 257).

## Dependence

- Possible, not established. (a) The primary infection rule as printed (10 C or higher and 10 mm of rain in 24 h, l. 155-156) has the form of the 3-10 rule. (b) The secondary infection condition uses RH above 90 per cent with a night temperature above 14 C (l. 158): the RH-90 wetness stand-in form. (c) The primary infection period is back-calculated from observed symptom dates with a T- and RH-dependent incubation curve (Figure 2b, l. 255-257). The source of that curve is not cited; if it is Goidanich (1957) or Rossi et al. (2008) incubation regressions, the back-calculated dates depend on that model. The EPI model (Stryzik 1983) is not on the engine list. Shared author of the list: none noted.

## Bearing (2026-10-10)

- Gives the truth an observation design for sensor calibration and station siting, and a 5-day sensitivity of forecasts to input error, but its incubation curve must be traced to its source before the truth could use or cite it.
