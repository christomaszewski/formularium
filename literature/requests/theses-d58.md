# Request: three theses with downy mildew and weather records (D58 follow-up)

From Cooptera's session on `agents` (ckt), 2026-10-27, at Chris's word ("send the theses to an
ingest session"). For an `ingest` session: these are papers, and D40 keeps them with you.

## Why

`ingest/datasets-d58` (Formularium #54) found twelve records of downy mildew outcomes with
weather for Agrarium's D58. Cooptera, which scores D58's candidates (Chris's decision of
2026-10-27), downloaded the one open dataset, `taibi2023.castellarquato`. Three more are theses
with an open PDF, which that work read only from their landing pages or abstracts:

| Record | Thesis | Where | Licence (as recorded) |
|---|---|---|---|
| `margaritis2019.spata` | Margaritis E. 2019, MSc, Agricultural University of Athens | kalligeneia.aua.gr/handle/10329/6933, `Margaritis_E.pdf`, 9.35 MB | not stated |
| `leoni2026.geneva_thesis` | Université de Genève, 2026 (author not read) | archive-ouverte.unige.ch/unige:193385 | not stated; check the landing page |
| `kleb2026.hohenheim_thesis` | Kleb M. 2026, PhD, Universität Hohenheim | hohpublica handle 123456789/19105, `Dissertation_MelissaKleb_2026.pdf` | CC BY-NC-SA 4.0 |

## What to read and settle

For each thesis, fetched and filed as `literature/INGESTING.md` says (leave it if its host
refuses the script; Chris pulls those):
1. **The disease record.** Which organism, and what is recorded: first-symptom dates,
   incidence or severity, spore catches. At what unit (plot, vine, leaf) and interval;
   untreated or sprayed; which years, how many sites, which varieties; growth stages and
   their dates.
2. **The weather with it.** Which variables (temperature, humidity, rain, leaf wetness,
   radiation), at what step (hourly or finer is what Cooptera's models need), from where
   (in the canopy, a station in the vineyard, a regional station and how far).
3. **Whether the numbers can be had**, not only the figures: a table in an appendix, a
   supplement, a repository (DOI), or "on request"; and the licence of each.
4. **Anything Cooptera could not use**: weather in figures only, outcomes without dates, an
   inoculated or potted experiment rather than a natural epidemic.

Kleb 2026 combines Kleb et al. 2022 and a 2026 paper on canopy microclimate against station
weather: what it measured inside the canopy against the station, and how much leaf wetness
differs, is also wanted (Cooptera stands in for wetness with humidity of 90 % or rain).

## What to deliver

On a branch `ingest/theses-d58`, following `literature/INGESTING.md`:
- each of the three `datasets.py` records brought up to what was read (its `how checked`
  raised from snippet or landing page to read, with pages);
- a new `datasets.py` record for any further dataset a thesis describes;
- any formulation a thesis fits, in `catalogue.py` as usual;
- a note in `literature/` for each thesis.

No code is needed. Cooptera downloads any data you find to be open, at Chris's word.
