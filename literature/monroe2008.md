---
id: monroe2008
citation: Monroe, J. W., Ritsche, M. T., Franklin, M. & Kehoe, K. E. 2008. Comparison of Meteorological Measurements from Sparse and Dense Surface Observation Networks in the U.S. Southern Great Plains. DOE/SC-ARM/TR-084 (US Department of Energy technical report, February 2008)
doi:
read: "2026-11-04, abstract and results text (Tables 3 and 4 are images and were not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 3 of 3 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: []
regions: [Oklahoma, Kansas, USA]
processes: [weather network, station representativeness, temperature, relative humidity, spatial error]
records: []
datasets: []
files: [dr1104_monroe2008.pdf (the 2026-11-04 drop)]
---

# Monroe et al. 2008: temperature and humidity differences between station pairs in the Southern Great Plains

A DOE/ARM technical report comparing sparse and dense surface networks (Kansas and Oklahoma) by correlation, bias and RMSD against distance.

**Read this first.**
- It is a technical report, not peer reviewed. The values are for 30-minute data, not daily, and temperature is corrected to sea level with a lapse rate of 6.5 degC/km.
- Tables 3 and 4 (slope and intercept) are images and were not read (garbled/absent). Humidity is given as relative humidity, not dew point.
- Page 1 prints four authors: Monroe, Ritsche, Franklin, Kehoe. The reading agent's JSON listed three and "et al."

## What it holds

- **Temperature (l. 253):** RMSD between two dense northern Oklahoma stations 16.34 km apart is 1.05 degC; a pair 423.61 km apart is 4.67 degC.
- **Relative humidity (l. 255):** RMSD 6.45 % at 16.34 km and 18.9 % at 423.61 km. The humidity differences are far larger relative to distance than those of temperature.
- **Shape (l. 153):** correlation and RMSD are roughly linear in distance from a central station; the slopes are in Tables 3 and 4 (images, not read).
- **Method:** scatter plots per station pair, then correlation, mean difference (bias) and RMSD.
- **Data:** Oklahoma Mesonet and ARM SMOS 30-minute data, 1999-2006.
- **Lead:** Brotzge & Richardson 2003, J. Appl. Meteorol. 42:5-19, on daily averaged T and RH in the Oklahoma Mesonet.

## Dependence

- None recorded. Own analysis of Mesonet and ARM data.

## Bearing (2026-11-04)

- **weather.site_dewpoint_offset_sd_c (Agrarium):** an RH RMSD of 6.45 % at 16 km is a measure of humidity difference between stations; it is not a dew point and not a daily value, so it needs conversion before use. Evidence: a measured technical report.
- **weather.site_t_offset_sd_c:** 1.05 degC at 16 km for 30-minute temperature, an upper bound for a daily mean.
