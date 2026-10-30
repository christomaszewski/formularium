# Answer to station-stamps-d65.md

2026-10-29, by an `ingest` session, from the providers' own documents (notes `dwd2024hourly`
and `meteofrance2026hourly`; the documents are in the drop `2026-10-29-requests/d65stamps`).

## DWD (hourly air_temperature, precipitation)

| Question | What DWD says | Where |
|---|---|---|
| What MESS_DATUM marks | "reference date", YYYYMMDDHH24; instant or end of hour not stated | dataset descriptions v24.03 (2024-03-29), csv content table |
| Time zone, and since when | per station and period, in the archive's metadata. Geisenheim: "Stundenwerte in MEZ" to 1996-10-01, "Stundenwerte in UTC" after | `Metadaten_Parameter_tu_stunde_01580.txt` (generated 2026-04-22) |
| TT_TU, RF_TU instant or mean | not stated. The source is named: thermohygrograph to 1996, first-generation automatic stations 1996-2006, "generiert aus SYNOP-Meldungen (nach dem 01.04.2001)" from 2006-12 at Geisenheim | the same file |
| R1, the hour ending at its stamp | not stated. R1 is "stdl. Niederschlagshoehe" from SYNOP reports, "in UTC"; WRTR has "UTC=1h Bezugszeitraum" at listed hours | `Metadaten_Parameter_rr_stunde_01580.txt` |

## Météo-France ("Données climatologiques de base - horaires")

| Question | What Météo-France says | Where |
|---|---|---|
| What AAAAMMJJHH marks, and its zone | "date de la mesure (année mois jour heure)"; "Les heures sont exprimées en UTC pour la métropole" | descriptif PDF (2026-06-03) and field list (2026-03-24); the dataset's page |
| T, U instant or mean | T: "température sous abri instantanée"; U: not stated | descriptif PDF |
| RR1, the hour ending at its stamp | not stated: "quantité de précipitation tombée en 1 heure" | descriptif PDF |
| Change between 2000 and 2022 | not stated | the same documents and the open-data wiki |

## Changes of observing time or convention, 2000-2022

- **DWD:**
  - many stations were automated "between the end of the nineties and 2009";
  - the zone changed from MEZ to UTC per station; at Geisenheim on 1996-10-01;
  - the hourly source became SYNOP reports (FM 12 from 2001-04-01; at Geisenheim from
    2006-12-01).

  None of these is said to shift a stamp by an hour, and the sampling of SYNOP-derived hourly
  values is not described.
- **Météo-France:** none stated.

## What this means for Agrarium's lags

- DWD 1977 read as UTC+1 is what the metadata say (MEZ to 1996).
- DWD 2000 and 2020-2021 are documented as UTC.
- Météo-France 2000-2022 are documented as UTC, with T an instant.

The documents give no reason for recent years to run an hour late at either provider.
Agrarium's own checks would have to settle it, for example DWD's 10-minute data for the same
station and hours. Read each DWD station's own metadata file: the change date differs by station.
