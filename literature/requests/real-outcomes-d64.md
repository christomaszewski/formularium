# Request: real downy mildew seasons outside Switzerland and New York, with their weather (Agrarium D64)

From Agrarium's session on `agents` (ckt), 2026-10-28, after Chris decided to end the screening
series ("go ahead with your recommendation"). For an `ingest` session: papers stay with you (D40).

## Why

Agrarium's screening (`docs/SCREENING-REPORT.md`, D64) fitted weather-only primary-infection rules
on one of the truth's disease lineages and judged them on the other. In four rounds none carried
across. Within the simulator, a 10 mm rain day or a calendar date is as good as any of the six
shapes tried. Whether real vineyards share such a rule only real seasons can say.

Agrarium holds real outcomes from two regions only:
- Changins, Switzerland: Leoni 2026, primary infections 2004-2025;
- Geneva and the Finger Lakes, New York: Kennelly et al. 2007, Table 1, 1981-2004;
- Castell'Arquato, Italy: Taibi et al. 2023, 2020-2022, incidence;
- Colucci's seven Italian sites: leaf wetness, no disease.

MIRA (77 Italian vineyards, 2020-2025) is Cooptera's and scored there. More regions would let
Agrarium judge transfer between real places, as it judged it between lineages, and Cooptera is
meant for the whole globe.

## What to find

Seasons of grapevine downy mildew (*Plasmopara viticola*), each a site and year, with:
1. **A dated outcome:**
   - the first primary infection (observed, or inferred and said how);
   - or the first symptoms (first oil spots);
   - or, failing those, an onset in incidence with its sampling dates.

   Say whether the plot was untreated, and its cultivar.
2. **The site's position,** and the weather it was read against: a named station (its owner,
   distance, and whether its hourly temperature, humidity and rain are open, and under what
   licence), or the paper's own logger.
3. **Licence and access,** for the outcomes and for the weather.

Places, most wanted first:
- the southern hemisphere: Australia, New Zealand, South Africa, Brazil, Uruguay, Chile,
  Argentina;
- central and eastern Europe: Germany, Austria, Hungary, the Czech Republic, Romania, Moldova,
  Georgia;
- France outside published model papers already held;
- China, Japan, India;
- North America outside New York.

Search the old and local names too: *Peronospora*, Rebenperonospora, mildiou, peronospora della
vite, mildiu, míldio. Theses, extension bulletins and forecasting-service reports often hold
dated first infections that journal papers summarise.

Not wanted:
- Catalonia's Meteocat weather: never in Agrarium. Name the station, and Agrarium will say whether
  it can be used.
- Data from MIRA's vineyards, already Cooptera's.

## What to deliver

On a branch `ingest/real-outcomes-d64`, following `literature/INGESTING.md`:
- **The seasons:** a small CSV in `literature/`, `real_outcomes_d64.csv`, with columns site,
  country, latitude, longitude, how the position is known, year, cultivar, treated (yes, no or
  unknown), outcome kind, date (or dates), how the date was determined, weather source, its
  distance in km, its licence, the outcome's licence, and source and page.
- **The sources:** records in `datasets.py` where a source is a dataset, and a note for each
  source read.
- **A short list** of the weather sources found, each with how to reach it and its terms, so
  Agrarium can write recipes (`sources/*.yaml`).

Even a dozen seasons from one new region is worth the branch.
