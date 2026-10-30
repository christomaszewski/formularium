# Request: the stamp conventions of DWD's and Météo-France's hourly station data (Agrarium D65)

From Agrarium's session on `agents` (ckt), 2026-10-29, Chris: "do these three first". For an
`ingest` session: providers' documents, read as D40 says.

## Why

Agrarium reads open hourly stations as partners for real downy mildew seasons (Agrarium's
`docs/REAL-OUTCOMES-REPORT.md`, IN18-IN19). Its gate cross-correlates each station-year's
temperature with Open-Meteo's reanalysis. Read as instants at UTC stamps, every recent year runs
about an hour late at both providers, while older years pass:
- DWD 2020-2021, Météo-France 2018-2022: best lag -1 h;
- DWD 1977 (read as UTC+1) and 2000, Météo-France 2000-2001: best lag 0.

Agrarium will not change a convention to admit a year. It needs what the providers say.

## What to find

1. **DWD,** Climate Data Center, `observations_germany/climate/hourly` (air_temperature,
   precipitation):
   - what MESS_DATUM marks (an instant, or the end of an hour);
   - its time zone, and since when (UTC from some date, MEZ before?);
   - whether TT_TU and RF_TU are instantaneous values or means over the hour before;
   - whether R1 is the hour ending at its stamp.

   Their sources are DWD's dataset descriptions (`DESCRIPTION_obsgermany_climate_hourly_*.pdf`
   beside the data) and the CDC's general notes.
2. **Météo-France,** "Données climatologiques de base - horaires" on data.gouv.fr:
   - what AAAAMMJJHH marks, and its zone;
   - whether T and U are instants or hourly means;
   - whether RR1 is the hour ending at its stamp;
   - whether any of this changed between 2000 and 2022.

   The source is the dataset's field description ("descriptif des champs", HOR file), with its
   date.
3. **For both,** any stated change of observing time or convention between 2000 and 2022:
   automation, a new averaging, a change of time base.

## What to deliver

On a branch `ingest/station-stamps-d65`: a short note per provider in `literature/`, each
statement quoted with its document, page and date. Say plainly where a document is silent.
