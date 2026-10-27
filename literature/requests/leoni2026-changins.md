# Request: Leoni 2026's Changins primary infections, transcribed, for a test in Cooptera

From Cooptera's session on `agents` (ckt), 2026-10-27, at Chris's word. For an `ingest`
session: it needs the thesis, and D40 keeps it with you.

## Why

`leoni2026.changins_primary` (Formularium #57) records Tables 3.2-3.3 of Leoni's 2026 thesis
(pp. 182-183): the day of the observed primary infection in Agroscope Changins' never-sprayed
plot, 2004-2025, beside laboratory-observed oospore maturity. Cooptera will run its oospore
gate and infection models on reanalysis weather at Changins and set their dates beside these,
as it is doing for Kennelly et al. 2007's Table 1 (`literature/kennelly2007_table1.csv`). It
needs the rows.

## What to read and transcribe

1. **Every row of Tables 3.2 and 3.3, as printed**: year, the Julian day (and the date) of the
   observed primary infection, of laboratory oospore maturity, the differences, and any other
   column. Keep 2011 and 2022 (no symptoms) as rows. A cell you cannot read is marked so.
2. **What "observed primary infection" means** if the thesis says anywhere (the day the first
   oil spot was seen, or the infection date counted back from it, and how).
3. **Where the plot is**: coordinates if printed, else as named, and the Agrometeo station's
   name and distance.
4. **Which years fitted which model.** Leoni's GLM (paper Table 1; thesis Table 3.1) was
   fitted on germination observations from some of these years: say which, so Cooptera can
   score that model on the others only. Likewise VitiMeteo's 140 °C·day rule if the thesis
   says where it was set.

## What to deliver

On a branch `ingest/leoni2026-changins`, following `literature/INGESTING.md`:
- the tables as a CSV under `literature/` (one row per year, the columns as printed, units in
  the header), with their pages;
- `leoni2026.changins_primary` updated to point at it;
- flags on `leoni2026.oospores` and `vitimeteo.oospores` naming the years they were fitted on,
  if the thesis says.

No code is needed. Cooptera builds the test and fetches the weather at Chris's word.
