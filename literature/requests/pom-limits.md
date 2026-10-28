# Request: how POM's daily rain limits are built, with a worked month, for a test in Cooptera

From Cooptera's session on `agents` (ckt), 2026-10-27, at Chris's word ("send both requests to
ingest"). For an `ingest` session: it needs the papers, and D40 keeps them with you.

## Why

Chris asked Cooptera to score `tranmanhsung1990.pom` (Agrarium's D44) against the observed
oospore maturity at Changins (`literature/leoni2026_changins_primary.csv`). With the limits as
`equations/tranmanhsung1990.py` reads the paper (Hm = RM / n; HM = (RM + SD) / n, n the
month's mean number of rainy days), built from Changins' reanalysis normals, the January index
IJ comes out far outside the paper's range: a median of -581 (rainy days above 1 mm) or -293
(any rain), where the paper's maturity dates, 27 March to 1 May, imply -15 to 152. Ronzon's
9 mm upper limit falls below Changins' Hm (9.4-10.2 mm). So the index is not reproduced as
read. Cooptera kept the attempt on its branch `candidate-pom` and gave no score.

## What to read and settle

From the page images of Tran Manh Sung, Strizyk & Clerjeau 1990 (Plant Disease 74:120-124)
and, if you can reach it, Ronzon's 1987 thesis (its p. 93 and the pages around it):
1. **Hm and HM, exactly**: their formulas with every term defined. In particular, what "the
   average number of rainy days" counts (days with any rain, at least 0.1 mm, at least 1 mm,
   or something else such as days in the month), whether RM is the month's total or a daily
   mean, and how "the standard deviation of RM divided by the number of rainy days" is
   bracketed. Ronzon's "18 / NJM = 9 mm": what NJM is.
2. **Any printed limits or normals**: Hm and HM for September to January at Bordeaux, or the
   monthly normals they come from (RM, SD, rainy days), from either source.
3. **A worked example**: any month's or year's POS, NEG or Im printed in either source, with
   the year, so the rules can be checked against a computation. Table 1 of the 1990 paper
   gives January's indices by year: transcribe it with every column, and say whether it also
   gives the monthly indices.
4. **The rules as printed**: whether a dry day lacks the whole Hm (LAC = Hm - Rd for every
   day under Hm, including days with no rain), and whether the counting starts on
   21 September in every year.

## What to deliver

On a branch `ingest/pom-limits`, following `literature/INGESTING.md`:
- Table 1 (and any other table of indices) as a CSV under `literature/`, with its page;
- `tranmanhsung1990.pom`'s parameters and flags updated with what the limits are, each with
  its page and quotation;
- `equations/tranmanhsung1990.py` corrected if its reading of the limits or the rules was
  wrong, with a test that reproduces a printed index if one is printed;
- a note in `literature/` for what was read.

Cooptera then checks the reading at Bordeaux on the paper's own years (Open-Meteo's ERA5
reaches back to 1940) before it scores POM at Changins.
