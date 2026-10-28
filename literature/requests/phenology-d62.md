# Request: the vines' stages at the pipeline's real sites (Agrarium D62)

From Agrarium's session on `agents` (ckt), 2026-10-28, in an unattended block Chris asked for
("work on whatever you think would be high value for setting up a pipeline/workflow for
training"). For an `ingest` session: papers stay with you (D40). Lower priority than
`request/canopy-light-d61` and `request/still-air-drying-d60`.

## Why

Agrarium's training pipeline (branch `training-data`, D62) builds datasets of real outcomes with
their weather: Changins (Leoni 2026, primary infections 2004-2025), Geneva and the Finger Lakes
(Kennelly et al. 2007, Table 1, 1981-2004) and Castell'Arquato (Taibi et al. 2023, 2020-2022). A
candidate model is told the day the vines become susceptible. Without the sites' stages, that
day is a stand-in, 1 April (MIRA's, as Cooptera uses). The real dates would let candidates and
the truth's phenology be judged on these seasons.

## What to find, per site and year

1. **Budburst, shoots 10 cm (BBCH 12-15) and flowering dates,** observed, for the cultivar of
   the plot: Agroscope Changins' outdoor laboratory (Leoni's thesis may give them, or
   Agroscope's phenology series); NYSAES Geneva and the Finger Lakes vineyards of Kennelly et al.
   (the paper gives the stage at first symptoms; other Cornell papers or NEWA may give more);
   Castell'Arquato (Taibi et al. 2023, or Fedele's other papers on the site).
2. **Whether the dates are open** and under what licence, or only in figures.
3. **The cultivars** where not yet recorded.

## What to deliver

On a branch `ingest/phenology-d62`, following `literature/INGESTING.md`: dates as a small CSV
in `literature/` beside the outcome tables (site, year, stage, date, source and page), records
in `datasets.py` updated, and a note for each source read.
