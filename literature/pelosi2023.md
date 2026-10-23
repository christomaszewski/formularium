---
id: pelosi2023
citation: Pelosi, A. 2023. Performance of the Copernicus European Regional Reanalysis (CERRA) dataset as proxy of ground-based agrometeorological data. Agricultural Water Management 289:108556
doi: 10.1016/j.agwat.2023.108556
read: 2026-10-22, in full (two columns interleaved in the text; Figures 4 to 8 are boxplots whose values were taken from the text and Table 4, not from the images), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 34 of 34 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Italy, Sicily]
processes: [reanalysis, CERRA, downscaling, bias correction, air temperature, wind speed, vapour pressure, solar radiation, reference evapotranspiration]
records: []
datasets: []
files: [gd1021_pelosi2023.pdf (the 2026-10-22 drop)]
---

# Pelosi 2023: CERRA reanalysis against 38 Sicilian ground stations

Daily errors of the 5.5 km CERRA reanalysis for temperature, humidity-derived vapour pressure, wind and radiation, after a bias correction fitted on station data, over 2009 to 2022.

**Read this first.** All 38 stations are in Sicily; none in Spain or Catalonia. The errors are on daily aggregates only: there is no hourly evaluation, no rain evaluation and no direct relative humidity score (humidity enters as vapour pressure from RHmax and RHmin). The temperature and humidity scores are after a regional monthly bias correction computed from station data of 2003 to 2008, so CERRA does not replace the station here without that correction. The abstract's mean PBIAS 5.6 % for ETo belongs to the interpolated ground data (IGD); CERRA's is -2.7 % (l. 45, 653). Table 4's "ea before BC" PBIAS prints "16." with its digits lost (l. 606).

## What it holds

- **Scope:** CERRA at 38 automatic SIAS stations in Sicily, 10 to 1470 m a.s.l., irrigation seasons 2003 to 2022 (l. 36, 199); Tmax and Tmin at 2 m, wind at 10 m (l. 199); variables are those that feed FAO-56 ETo: air temperature, actual vapour pressure, wind and solar radiation (l. 37).
- **CERRA:** a 5.5 km regional reanalysis released in August 2022 by ECMWF, forced by ERA5, from 1984 (l. 33); forecast-mode data hourly, analysis products 3-hourly (l. 340); analysis products used where available (radiation from the hourly forecast), then aggregated to daily values (l. 348, 181).
- **Downscaling and correction:** triangle-based bilinear interpolation of the three nearest grid points (l. 322); Tmax and Tmin corrected with monthly lapse rates from 96 sites, -0.0046 to -0.0064 (Tmax) and -0.0027 to -0.0045 (Tmin) per metre, in place of -0.0065 (l. 356; the unit is degC per m). Bias correction adds the monthly regional mean ground-minus-CERRA difference, computed on 2003 to 2008; none for wind (l. 405). All statistics use 2009 to 2022, 14 years (l. 412).
- **Tmax:** mean PBIAS 1.2 % (l. 491), NRMSE 5.8 % with two mountain outliers at 12 % and 11 % (l. 495), R2 always above 0.90 (l. 499), NSE above 0.80 for CERRA and 0.40 for interpolated ground data (l. 506).
- **Tmin:** PBIAS 0.93 % and NRMSE 13 % for CERRA, against -0.35 % and 11 % for IGD (l. 542); R2 above 0.84 for CERRA; NSE positive and above 0.40 for CERRA, 0.62 for IGD; one NRMSE of 32 % at an inland hill station; interpolating the stations is slightly better than CERRA (l. 547-548).
- **Wind (10 m daily mean, no correction):** the worst variable: PBIAS -18 % and NRMSE 37 % for CERRA (IGD -17 % and 33 %) (l. 605); R2 from 0.16 to 0.89; NRMSE above 80 % at one windy coastal station (l. 611); NSE negative at about half the stations, where the observed mean beats both estimates (l. 612).
- **Vapour pressure from RH:** CERRA PBIAS -3.5 % and NRMSE 15 % (IGD 1.7 % and 14 %) (l. 620); R2 above 0.56, NSE always positive (l. 623). **Solar radiation:** PBIAS -2.5 %, NRMSE 12 % (IGD 10 %), R2 0.66 to 0.94, NSE above 0.65 (l. 632).
- **Table 4** (PDF p. 9, l. 602-606), mean PBIAS %, NRMSE %, R2 before then after correction: Tmax -4.8, 8.1, 0.94 then 1.2, 5.8, 0.94; Tmin 10.2, 15.8, 0.91 then 0.93, 13.5, 0.91; ea (PBIAS garbled), 21.3, 0.76 then -3.5, 15.4, 0.73; RS 3.2, 12.5, 0.79 then -2.5, 12.3, 0.79.
- **ETo with CERRA inputs:** PBIAS -2.7 % (CERRA) and 5.6 % (IGD), NRMSE 13 % for both (l. 653), like ERA5-Land at the same stations (PBIAS 2.8 %, NRMSE 14 %, R2 0.76, NSE 0.67; Pelosi and Chirico 2021, cited; l. 650, 690).
- **Limits and access:** the conclusion that CERRA can replace stations rests on 6 calibration years of station data and on Sicily alone (l. 738). CERRA is free on the Copernicus Climate Data Store; the station data come from the Sicilian service SIAS and are available on request (l. 738).

## Dependence

- **Same design and station set** as Pelosi and Chirico (2021, ERA5-Land, Sicily) and Pelosi et al. (2020a, UERRA MESCAN-SURFEX). FAO-56 Penman-Monteith (Allen et al. 1998); statistics PBIAS, NRMSE, R2 and Nash-Sutcliffe efficiency.
- **The reanalysis itself** is an ECMWF model product forced by ERA5. A single author.

## Bearing (2026-10-22)

- **What it answers:** whether a reanalysis can stand in for a missing station. For daily temperature in Sicily, yes after local correction: Tmax NRMSE 5.8 %, Tmin 13 %, radiation 12 %. Not for wind (NRMSE 37 %, NSE negative at half the stations). Humidity only as vapour pressure (NRMSE 15 %).
- **What it does not answer:** rain, hourly values and leaf wetness, which are what the disease models take. Daily Tmax and Tmin errors cannot be turned into hourly temperature or wet-hour errors. Nothing here covers Catalonia, and the correction needs a station's own data, so it is not a stand-in where no station ever existed.
- **Use:** a daily error band for temperature in Agrarium's weather and Cooptera's inputs, if a station gap is filled from CERRA with a correction from neighbouring stations. Kind of result: a validation of a gridded product against ground stations on one Mediterranean island, with calibration years (2003 to 2008) split from validation years (2009 to 2022).
