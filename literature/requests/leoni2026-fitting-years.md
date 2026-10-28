# Request: which years Leoni's GLM was fitted on, for a test in Cooptera

From Cooptera's session on `agents` (ckt), 2026-10-27, at Chris's word ("send both requests to
ingest"). For an `ingest` session: it needs the paper and the thesis, and D40 keeps them with
you.

## Why

Cooptera scores `leoni2026.oospores` (the GLM) against the Changins seasons of Leoni's thesis
(`literature/leoni2026_changins_primary.csv`) only outside the years it was fitted on. Two
records disagree on those years:
- the flag added to `leoni2026.oospores` in #60 says the GLM was fitted on germination
  observations of **2004-2024**, so only 2025 lies outside them (Cooptera now scores 2025
  alone);
- Cooptera's `engine/origins.py`, written from an earlier reading of the paper (2026-10-03),
  gives the GLM's 96 germination observations as from **2022-2024**.
If the second is right, the GLM can be scored on about 17 seasons, not one.

## What to read and settle

From the page images of Leoni et al. 2026 (OENO One 60(3), doi:10.20870/oeno-one.2026.60.3.9963)
and Leoni's 2026 thesis (the oospore chapter and its methods):
1. **The 96 observations**: in which years the germination observations behind Table 1 (the
   paper) and Table 3.1 (the thesis) were made, with the page and the quotation.
2. **What 2004-2025 was used for**: whether those years enter the fit at all, or only the
   check of VitiMeteo's dates against the observed primary infections (the "95% of primary
   infections" figure).
3. **The laboratory maturity dates** in Table 3.3 (`maturity_observed_doy`): whether they are
   the same observations the GLM was fitted on, in the years they share.

## What to deliver

On a branch `ingest/leoni2026-fitting-years`, following `literature/INGESTING.md`:
- the flag on `leoni2026.oospores` corrected or confirmed, with the page and quotation;
- `leoni2026.oospores`'s `calibrated_on` (or a dataset record) naming the fitting years;
- a line in `literature/leoni2026thesis.md` and the paper's note for what was read.

No code is needed. Cooptera changes which years its test scores the GLM on, at Chris's word.
