---
id: dwd2024hourly
citation: Deutscher Wetterdienst, Climate Data Center. 2024. Hourly station observations of 2 m air temperature and humidity for Germany, and Hourly station observations of precipitation for Germany: dataset descriptions, version v24.03 (published 2024-03-29), with the station archives' metadata files
doi:
read: 2026-10-29, in full (the two English and two German descriptions; the CDC readme searched; Geisenheim's (station 01580) Metadaten_Parameter and Metadaten_Geraete files for temperature and precipitation, generated 2026-04-22 and 2026-04-23; the 10-minute air temperature description searched); by the main ingest session
status: read
diseases: []
crops: []
regions: [Germany]
processes: [weather data, time stamps, station metadata]
records: []
datasets: []
files: [dr1029_dwd2024hourly.pdf (the 2026-10-29 requests drop; with the German descriptions and the station metadata files beside it)]
---

# DWD's hourly station data: what the stamps say, and where the documents are silent

What DWD's own documents say about MESS_DATUM, the time zone, and the hourly temperature,
humidity and rain, for Agrarium's D65 (`literature/requests/station-stamps-d65.md`).

**Read this first.** The dataset descriptions never give the time zone. Each station's archive
gives it per period, in `Metadaten_Parameter_*.txt`, and it changes from MEZ to UTC. No DWD
document read says whether TT_TU and RF_TU are instants or hourly means, or which hour R1 covers.

## What it holds

- **MESS_DATUM** is "reference date", format "YYYYMMDDHH24" (temperature description, l. 115;
  precipitation, l. 96; German "Referenzdatum"). Nothing more is said of it.
- **Time zone, by station and period.** Geisenheim's (01580) temperature and humidity metadata:
  - 1946-01-01 to 1996-10-01: "Stundenwerte in MEZ", from "analogen Registrierungen
    (Thermohygrograph)";
  - 1996-10-01 to 2006-10-01: "Stundenwerte in UTC", from "automatischen Stationen der 1.
    Generation (MIRIAM/AFMS2, ESAU-Daten)";
  - 2006-12-01 to 2026-04-18: "Stundenwerte in UTC", "generiert aus SYNOP-Meldungen (nach dem
    01.04.2001)".

  MEZ is Central European Time, UTC+1, with no summer time ("GZ = Gesetzliche Zeit" is defined in
  the file's legend but not used in Geisenheim's rows).
- **Precipitation,** Geisenheim, from 2006-12-01: R1 "stdl. Niederschlagshoehe", "Daten aus
  SYNOP-Meldungen (FM 12 ab 01.04.2001 mit neuen nationalen Schlüsselgruppen)", "in UTC".
  WRTR (precipitation form) carries "01,02,04,05,07,08,10,11,13,14,16,17,19,20,22,23 UTC=1h
  Bezugszeitraum": a one-hour reference period at those hours, not said for R1.
- **Statistical processing:** temperature "time series, hourly value" (German "Stundenwert");
  precipitation "time series, hourly sum" ("Stundensumme").
- **Instruments, Geisenheim:** thermograph at 2 m to 2006-11-30; PT 100 electrical from
  2006-12-01 (Metadaten_Geraete_Lufttemperatur).
- **Automation:** "Between the end of the nineties and 2009 many stations were changed from
  manual to automated" (temperature description, l. 166). The descriptions say station metadata
  record "reference time changes" (l. 36; German "Wechsel der Bezugszeit").
- **The 10-minute product** (a different dataset): "Die Messungen sind vor dem Jahr 2000 einem
  Zeitstempel in MEZ und ab dem Jahr 2000 einem Zeitstempel in UTC zugeordnet" (its description,
  l. 78-79).

## Silent

- Whether MESS_DATUM marks an instant or the end of an hour.
- Whether TT_TU and RF_TU are instantaneous values or means over the hour before. For SYNOP-
  derived values the documents name the source but not the sampling.
- Whether R1 is the hour ending at its stamp.
- A general rule for the MEZ-to-UTC change: it is per station, in each archive's metadata.

## Dependence

- None: a provider's documentation.

## Bearing (2026-10-29)

- Agrarium should read each station's `Metadaten_Parameter` file for its zone by period, not
  assume one. At Geisenheim, 1977 is MEZ (UTC+1), and 2000 and 2020-2021 are UTC.
- The documents give no reason for a one-hour lag in recent years. The source changed to SYNOP
  reports (from 2001, at Geisenheim from 2006-12), but how a SYNOP-derived hourly value is
  sampled is not stated.
