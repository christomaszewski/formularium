# Request: open records of downy mildew against weather, outside Catalonia (Agrarium D58)

From Agrarium's session on `agents` (ckt), 2026-10-27, at Chris's word ("send both
requests"). For an `ingest` session: it needs papers, theses and data pages, and D40 keeps
them with you.

Agrarium's variable search (PLAN 15, D58) screens candidate predictors in the simulator, but
only real data may judge them. Apart from Cooptera's MIRA and Gelida, which are in the Penedès,
nothing on hand pairs disease outcomes with weather; Chris's rule is that models are judged
by how they transfer, on data from outside their region. Please find what can be obtained.
Work on a branch `ingest/datasets-d58`, following `literature/INGESTING.md`.

## What counts

A record of *Plasmopara viticola* outcomes (first symptoms, incidence or severity, ideally in
untreated or calendar-sprayed plots, with dates) together with the weather at or near the
plots (at least daily temperature, rain and humidity; hourly and leaf wetness better), for one
or more seasons, anywhere outside Catalonia. Several regions and climates are worth more than
many seasons of one.

## 1. Start from Formularium's own list

`src/formularium/datasets.py` holds 142 records. For each that describes disease outcomes with
weather (`haasbroek2006.westerncape` at Nietvoorbij first; also `puelles2024.rioja`,
`istvanffi1913.hungary` and any others you find), say:
- what it records, where, which years, at what interval;
- whether the raw numbers can be had (a data repository, a thesis appendix, a table in the
  paper, the authors on request) and under what licence or terms;
- how you checked (`read`, `trail`, `snippet`).

## 2. Then search further

Open data repositories (Zenodo, Dryad, Mendeley Data, Recherche Data Gouv, national
agricultural services), theses with appendices, and papers whose tables print season-by-season
disease and weather. Downy mildew is also searched under its old and local names
(Peronospora, Rebenperonospora, mildiou, peronospora della vite).

## What to deliver

- A record in `datasets.py` for each new dataset, with what was checked.
- A note in `literature/` for each source read, as INGESTING.md says.
- A short summary on the branch: a table of datasets, with region, years, what each records,
  how to obtain it, licence, and whether it can be downloaded now.

Do not download data whose terms forbid it, and nothing from Meteocat. Downloading is for
Chris's sessions to do, from the summary.
