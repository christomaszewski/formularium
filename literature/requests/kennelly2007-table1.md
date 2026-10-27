# Request: Kennelly et al. 2007's Table 1, transcribed, for a test in Cooptera

From Cooptera's session on `agents` (ckt), 2026-10-27, at Chris's word ("lets do that as
well"). For an `ingest` session: it needs the paper, and D40 keeps it with you.

## Why

Cooptera scores downy mildew models against dated outcomes (MIRA, and D58's candidates at
Chris's decision of 2026-10-27). `kennelly2007.geneva` (Formularium #54) records Table 1 of
Kennelly, Gadoury, Wilcox, Magarey & Seem 2007 (Phytopathology 97:512-522): 29 site-years in
New York, 1981-2004, of the first symptoms in unsprayed Chancellor vines, each with the
infection event the authors judged responsible. That is the best-dated set either project
knows of, but only its description is recorded: no row of it is. Cooptera will run its models
on reanalysis weather at each site and year and set the infections they predict beside the
attributed event and the first symptoms. It needs the rows, read from the page.

## What to read and transcribe

From the page image of Table 1 (and its footnotes, and Materials and methods for the sites):
1. **Every row, as printed**: site, year, the date of first symptoms, the date of the
   attributed infection event, its rain (mm) and temperature (which: the mean, over what
   window), the incubation (days), the degree-days, the growth stage, and any other column.
   Keep "No disease" (Dundee 2003) as a row. Never guess a value: a cell you cannot read
   is marked so.
2. **Where each site is**: Geneva (NYSAES) and Watkins Glen, Wayne, Ovid and Dundee, with
   coordinates if the paper gives them, else the place as named; the weather station each
   used and its distance (the record says 2 to 20 km), if printed.
3. **How the dates were taken**: how often the clusters were examined (the record says
   every 1-5 days from three weeks before bloom), whether "first symptoms" is the day seen
   or a window, and how the infection event was attributed (by back-counting an incubation
   model, which one).
4. **Which rows the trigger was fitted on.** `kennelly2007.trigger` is `calibrated_on`
   `kennelly2006.chancellor`, the Geneva Chancellor data: say which Table 1 rows are those
   data (Cooptera would score the trigger on the others only, as the paper evaluates it on
   the Finger Lakes vineyards of 2001-2003).

## What to deliver

On a branch `ingest/kennelly2007-table1`, following `literature/INGESTING.md`:
- the table as a CSV under `literature/` (one row per site-year, the columns as printed,
  with units in the header), and its page;
- `kennelly2007.geneva` updated to point at it, with what was read and how;
- a flag on `kennelly2007.trigger` saying which rows it was fitted on, if the paper says.

No code is needed. Cooptera builds the test, and fetches the reanalysis weather at Chris's word.
