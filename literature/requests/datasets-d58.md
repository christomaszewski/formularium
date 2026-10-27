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

## Already known (Cooptera's session, 2026-10-27, from its docs/test-datasets.md)

Not to search for again, but to check and record in `datasets.py` where missing:
- **MIRA** (Del Cavallo, Bregaglio et al. 2026, Zenodo doi:10.5281/zenodo.21534581, CC BY 4.0):
  77 vineyards in 9 Italian regions, 2020-2025; BBCH, disease by visit with incidence and
  severity, 101 downy mildew first-symptom dates, treatments for 62 of 186 vineyard-years; no
  weather (Cooptera pairs it with Open-Meteo's reanalysis). Cooptera already holds and scores it.
- Italian weekly downy mildew risk, 2012-2017 (Mendeley doi:10.17632/3jsh4y2bw4.1, CC BY):
  experts' readings of bulletins, no weather.
- French yearly intensity grades, 1941-2023, Bordeaux, Champagne and Vaucluse (Recherche Data
  Gouv doi:10.57745/HM3HBE, CC BY).
- BASF fungicide trials with untreated plots, 2012-2019, 36 trials (Zenodo
  doi:10.5281/zenodo.6353533): files restricted.
- In papers: Kennelly et al. 2007, Table 1 (29 dated site-years, New York); Chen et al. 2020,
  S1 Data (156 untreated plot-years near Bordeaux, monthly weather, no places); Barrios & Reyes
  2004 (Vilafranca del Penedès, 1984-2004, one class a year).

The gap they leave: dated first symptoms or incidence with daily or hourly weather measured at
the plots, outside Italy and Catalonia.

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
