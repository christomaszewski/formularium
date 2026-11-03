---
id: merlone2019
citation: Merlone, A., Al-Dashti, H., Faisal, N., Cerveny, R. S., Alsarmi, S., Bessemoulin, P., Brunet, M., Driouech, F., Khalatyan, Y., Peterson, T. C., Rahimzadeh, F., Trewin, B., Wahab, M. M. A., Yagan, S., Coppa, G., Smorgon, D., Musacchio, C. & Krahenbuhl, D. 2019. Temperature extreme records: WMO metrological and meteorological evaluation of the 54.0 °C observations in Mitribah, Kuwait and Turbat, Pakistan. Int. J. Climatol. 39(13):5154-5169 (the author-submitted version, INRiM repository)
doi: 10.1002/joc.6132
read: 2026-11-03, the sections on uncertainty components (shield ageing, self-heating, logger; not the climatology), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Kuwait, Pakistan, Italy (laboratory calibration)]
processes: [air temperature, shield ageing, self-heating, uncertainty budget, calibration]
records: []
datasets: []
files: [dr1103_merlone2019.pdf (the 2026-11-03 drop)]
---

# Merlone et al. 2019: WMO evaluation of the 54.0 °C records, with its uncertainty components

A WMO evaluation of two extreme-temperature records, including the uncertainty of shield ageing and sensor self-heating.

**Read this first.** The file is the author-submitted version; the author list is from its cover page (l. 11-14). The site of the one- versus three-year screen comparison is not in the facts held. The temperature extreme itself was not read.

## What it holds

- **Shield ageing, field (l. 479):** differences between one-year and three-year old screens were distributed around 0 °C, with a thermal noise of about 0.06 °C in 3.5 to 5 m/s wind.
- **Ageing term (l. 498):** solar shield ageing uncertainty ±0.04 °C (k=2); the correction applied is 0 °C.
- **Paint (l. 476):** the shield paint degrades with field use (five-year and three-year old Vaisala screens).
- **Self-heating (cited, l. 559):** heating of HMP155 sensors was evaluated in a climatic chamber and a wind tunnel (Izquierdo et al. 2018): significant, and wind-dependent. No number in the facts held.

## Dependence

- Own calibration of a Vaisala HMP155 and of a Vaisala radiation screen at INRiM. Cites Lopardo et al. 2014 (screen ageing) and Izquierdo et al. 2018 (self-heating).

## Bearing (2026-11-03)

- **sense.station_temperature_bias_c (assumed 0):** a ±0.04 °C (k=2) shield-ageing term with a correction of 0 °C. That is small against the assumed range of ±1 °C. There is no field value here for air-temperature drift over years; self-heating is wind-dependent and unquantified in the held text. Kind of evidence: own calibration budget.
- **sense.station_shield_error (assumed 0):** one- and three-year-old screens agree to about 0 °C, so shield ageing alone is not a large error.
