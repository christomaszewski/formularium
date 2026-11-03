---
id: meteocat2021
citation: Servei Meteorològic de Catalunya. 2013-2021. Press notes on new automatic stations of the XEMA (Palafrugell 2021, Terrassa 2019, Massoteres and others). Generalitat de Catalunya (a series of notes), with the open-data metadata of datasets nzvn-apee and 4fb2-n3yi, retrieved 2026-11-03
doi:
read: 2026-11-03, the seven press notes in full (one page each) and the full open-data metadata, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes (press notes) and 9 of 9 quotes (open-data metadata) found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Spain (Catalonia)]
processes: [XEMA stations, sampling, recording interval, transmission latency, timestamp convention, validation code, data resolution]
records: []
datasets: []
files: [dr1103_meteocat2021_gov1.pdf (the 2026-11-03 drop), dr1103_meteocat2021_gov2.pdf (the 2026-11-03 drop), dr1103_meteocat2021_gov3.pdf (the 2026-11-03 drop), dr1103_meteocat2021_gov4.pdf (the 2026-11-03 drop), dr1103_meteocat2021_gov5.pdf (the 2026-11-03 drop), dr1103_meteocat2021_gov6.pdf (the 2026-11-03 drop), dr1103_meteocat2021_gov7.pdf (the 2026-11-03 drop)]
---

# Meteocat 2013-2021: press notes on new XEMA stations, and the open data's own metadata

Seven one-page press notes (Palafrugell 2021, Terrassa 2019, Massoteres 2017, Canyelles 2013-2014, Tivissa 2015, Granollers 2019, Fígols i Alinya 2014) and the Socrata metadata of the XEMA half-hourly data.

**Read this first.**
- Press notes are a public body's descriptions, not a technical specification. No sensor model, height, averaging, shield or quality-control delay is stated in any of them.
- The latency snapshot below is the reading agent's observation on 2026-11-03: one sample, at one hour of day, not a distribution.

## What it holds

- **Sampling (Palafrugell, l. 29):** sensors measure every second.
- **Recording and sending (l. 294):** data are recorded every 30 minutes and sent to the central office every half hour by GPRS.
- **Wind (l. 140):** wind speed and direction at 10 m on the new stations.
- **Small stations (Granollers, l. 487):** temperature, relative humidity and precipitation sensors only.

## The open data's own metadata

- **Stamp (l. 12):** `data_lectura` is the start of the reading interval ("labelled ahead"), in UTC (l. 12).
- **Interval (l. 2):** the dataset holds variables measured at a frequency below daily, generally half-hourly. `codi_base` is HO (hourly) or SH (semi-hourly), per variable and station, so not every value is half-hourly (l. 16).
- **Validation (l. 15):** `codi_estat` is blank (validation not started), T (started, not finished) or V (valid); invalid values are not shown. The latest records may be unvalidated.
- **Resolution:** temperature (variable 32) to 0.1 °C (l. 33); relative humidity (variable 33) in whole % (l. 34); precipitation (variable 35) to 0.1 mm (l. 36).
- **Rain maximum (l. 53):** a precipitation variable "maximum in 1 minute" exists (variable 72).
- **Leaf wetness:** none among the 68 variables (reading agent's count of the variable list).
- **Latency snapshot, 2026-11-03 (reading agent's observation, nzvn-apee, variable 32):** at 06:05 UTC the newest stamp was 05:00 (182 stations), so it was out within 65 minutes of its start. At 06:16 UTC the 05:30 stamp was still absent after 46 minutes. The 05:30 stamp first appeared in the 06:17 UTC poll (about 180 of 182 stations): 47 min from its start, 17 min from its end. One sample; a V code may come later than first appearance.

## Dependence

- None recorded. Own descriptions by the data's publisher; the latency figures are the reading agent's own polling.

## Bearing (2026-11-03)

- **sense.station_latency_min (assumed 60, range 30 to 180):** the half-hour is recorded and sent every 30 minutes, and the feed showed the first readings 47 to 65 min after the interval start in one snapshot. The 60 min default sits inside that bracket; 30 min is too short for this feed. Kind of evidence: publisher's text plus one observation.
- **Stamp convention:** the start-of-interval, UTC stamp is stated by the publisher, so an engine must treat a stamp as the half-hour that begins at it.
- **Missing and unvalidated data:** invalid values are absent, not flagged, and recent values may carry a blank or T code; relevant to what the engine sees live.
- **Variables:** humidity is whole %, temperature 0.1 °C, rain 0.1 mm; no leaf wetness is published, and some stations carry only temperature, humidity and rain.
