---
id: bernard2019
citation: Bernard, J., Kéravec, P., Morille, B., Bocher, E., Musy, M. & Calmet, I. 2019. Outdoor Air Temperature Measurement: A Semi-Empirical Model to Characterize Shelter Performance. Climate 7:26
doi: 10.3390/cli7020026
read: 2026-11-03, abstract, sections 1.2, 2.2 (data) and 3 up to the findings on wind (not the model fit tables), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Algeria (Ghardaïa)]
processes: [air temperature, radiation shield, shelter response time, low wind, WMO intercomparison]
records: []
datasets: []
files: [dr1103_bernard2019.pdf (the 2026-11-03 drop)]
---

# Bernard et al. 2019: a semi-empirical model of the radiative error of air-temperature shelters

A model of shelter error fitted to the WMO 2009 Ghardaïa intercomparison, in which error depends on the shelter's response time and radiation sensitivity.

**Read this first.**
- The reading agent did not copy Table 2 or the model-coefficient tables, so no fitted coefficient is held here.
- The 2 to 4 times and 130 to 180 s figures are cited from Lin et al., not this paper's own.
- The primary data (Lacombe et al. 2011, WMO IOM Report 106) were not fetched.

## What it holds

- **Campaign (cited, l. 339):** in 2009 the WMO ran a campaign in Algeria: air temperature in 18 shelter types, recorded for one year in desert conditions, seven of them artificially ventilated.
- **Model (l. 27):** coefficients are regressed on that campaign; the error depends on the shelter's response time and its radiation sensitivity.
- **Skill (l. 33):** for low-response-time shelters the model cuts the root mean square error by about 15 % (0.07 K) against other schemes (Cheng, Nakamura).
- **Shield airflow (cited from Lin et al., l. 97):** air speed inside a shield is 2 to 4 times weaker than outside.
- **Time constant (cited from Lin et al., l. 100):** for wind below 2 m/s two shields had time constants of 130 to 180 s.
- **Low wind (l. 531):** below 1 m/s, whatever the radiation, the Davis reference shield is neither the warmest at night nor the coolest by day; shield differences are not simply ordered at calm.
- **Agreement of twin shields (l. 521):** two Davis 7714 shelters agree within ±0.3 °C for 90 % of values (best type 0.2 °C).
- **Davis 7714 (l. 146):** it is the multiplate shield that Nakamura & Mahrt modelled.

## Dependence

- Uses the 2009 WMO shelter intercomparison at Ghardaïa (Lacombe et al.; 18 shelters, one year). Its model is compared with Nakamura & Mahrt 2005 and Cheng et al.

## Bearing (2026-11-03)

- **sense.station_shield_error (assumed 0):** measured, from a desert site: shield error is a function of response time and radiation, and twin Davis shields differ by ±0.3 °C for 90 % of values. It shows the error is not zero and is shield-specific; it gives no value for a XEMA shield (type not found).
- **sense.station_shield_min_wind_ms (assumed 0.5 m/s):** below 1 m/s the behaviour of shields changes (l. 531), and the airflow inside is 2 to 4 times weaker (cited). It supports a floor of the order of 0.5 to 1 m/s; no floor formula is printed. Kind of evidence: own measurement plus cited figures.
