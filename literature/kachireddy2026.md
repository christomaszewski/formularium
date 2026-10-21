---
id: kachireddy2026
citation: Kachireddy, M., Gongora-Canul, C. C., Fernandez-Campos, M., Lane, B., Jahanshahi, M. R. & Cruz, C. D. 2026. Satellite-derived and regional weather data as scalable alternatives to on-site stations for forecasting corn tar spot. Research Square preprint (version 1, posted 2026-07-13, not peer reviewed as posted)
doi: 10.21203/rs.3.rs-10206764/v1
read: 2026-10-21, lightly: abstract, introduction, methods (sites, sensors, NASA POWER, Mesonet, statistics), results (Table 3 agreement, Table 4 MLR, Bayesian, Table 5 SARIMAX), limitations; figures by caption only; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [corn tar spot]
crops: [maize]
regions: [USA, Indiana]
processes: [satellite weather, NASA POWER, regional weather network, on-site station, source agreement, multiple linear regression, SARIMAX, leave-one-site-year-out]
records: []
datasets: []
files: [kachireddy2026.pdf (the 2026-10-21 drop)]
---

# Kachireddy et al. 2026: NASA POWER and a regional network against on-site stations for tar spot forecasts (preprint)

A Research Square preprint, not peer reviewed: nine Indiana corn site-years, 2021-2024, with on-site, Purdue Mesonet and NASA POWER weather compared for agreement and as inputs to three tar spot severity models. A later peer-reviewed version may differ, so check before citing. No record.

**Read this first.** Several things in the preprint do not agree and were not resolved, so none of the model skill below is safe to quote. (1) The text claims MLR RMSE differences below 0.25 between NASA-based and on-site-based models (l. 620), but Table 4 as extracted has 2024 rows that differ by more (upper canopy 1.1684 against 0.2958, l. 594, 602). (2) RMSEs of 0.0001 in the tables are implausible and their scale is not stated (l. 685). (3) The Discussion gives a precipitation r of 0.185-0.356 (l. 832) against 0.25 and 0.19 in Table 3. (4) The validation is leave-one-site-year-out (l. 184), yet the Methods also say models were evaluated per canopy, source and site-year (l. 463), so whether Tables 4 and 5 are out-of-sample is unclear. (5) The sampling radius is 3-9 m in the text (l. 261) and 3-6 m in a caption (l. 294). All five are unchecked against the PDF. Equations 1-3 are garbled in the text layer; the standard forms are assumed.

## What it holds

- **Sites and sources** (l. 60, 61, 216, 222, 304, 322, 334): four Purdue sites in Indiana, nine site-years, 2021-2024. Three weather sources: an on-site ATMOS 41 station within 100 m of each plot, the nearest Purdue Mesonet station at a mean distance of 15-30 km, and NASA POWER at 0.5 x 0.625 degrees (about 50 km). Grid cells for severity ratings are 12.2, 42.7, 18.3 and 15 m wide by site (l. 253).
- **Agreement, 2023 only** (Table 3; l. 494, 490, 507): n = 153 days. NASA POWER against on-site temperature has a warm bias of +2.09 degC and an RMSE of 3.94 degC (rho_c 0.74); Mesonet against on-site has r = 0.90, rho_c = 0.89, MBE -0.45 degC and RMSE 2.52 degC, which the authors attribute to proximity.
- **Humidity and rain** (l. 531, 541, 543): NASA POWER relative humidity reads about 18 points lower than on-site (MBE -17.69 %, r = 0.61, rho_c 0.37, RMSE 22.96 %). Precipitation agrees poorly: NASA against on-site r = 0.25, rho_c = 0.21; on-site against Mesonet r = 0.19, rho_c = 0.01, RMSE 0.96 mm. So a station 15-30 km away already differs in rain. NASA POWER has no leaf wetness and was left out of that comparison (l. 327).
- **Severity series** (l. 173): discrete ratings every 7-14 days per grid cell are fitted with logistic growth curves to give a daily severity, the response of all models. The severity unit is not stated.
- **Models** (l. 560, 591, 654): stepwise MLR picks temperature, relative humidity and solar radiation most consistently, all models p < 0.001. A Bayesian temperature coefficient is -0.072 (94 % HDI -0.10 to -0.04). SARIMAX(2,1,2)(1,0,1) with s = 7 is the common specification.
- **Skill as printed** (l. 594, 602, 620, 685): Table 4, 2024 NASA upper canopy R2 0.893 and RMSE 1.1684; 2024 on-site upper canopy R2 0.849 and RMSE 0.2958. SARIMAX RMSE runs from 0.0001 to 0.58. Read the Read-this-first list above before using any of these.
- **Limitation** (l. 985): one region and few site-years; the authors call performance indicative rather than definitive.

## Dependence

- Uses NASA POWER (ref 21), the Purdue Mesonet (ref 25) and Lin's concordance correlation coefficient (ref 45), all as cited; SARIMA models from refs 29-30. Data are the authors' own field trials. A shared author is only a flag.

## Bearing (2026-10-21)

For Agrarium's D48 study: what one station or a gridded or virtual source misses, and the sensor menu.

- **Takeable:** a measured gap between on-site, regional-network and 50 km gridded weather for one season: temperature is close (r = 0.81 for the grid, 0.90 for a station 15-30 km away), humidity is biased low by the grid (-17.69 %), and rain barely agrees even for a station 15-30 km away (rho_c 0.01). This puts rain and leaf wetness, not temperature, as where a distant source misses.
- **Not usable as is:** the claim that satellite data can "substitute" on-site data in disease forecasts, because of the unchecked flags above and a validation design that is unclear. No decision or spray scoring, no placement method, no held-out sites by design beyond the leave-one-site-year-out statement. The kind of result is a source comparison plus model fits, in a preprint.
