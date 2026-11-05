# Request: what Leoni 2026's "observed primary infection" date marks (Agrarium D70)

From Agrarium's session on `agents` (ckt), 2026-11-04, Chris: "Sure" (to D70's recommendation
after CB10). For an `ingest` session: papers stay with you (D40).

## Why

Agrarium's pool reads Leoni 2026's Table 3.3 column "observed primary infection"
(`literature/leoni2026_changins_primary.csv`, `primary_infection_observed_date`) as the day first
symptoms were seen at Changins, 2004-2025 (recipe `leoni2026`). The truth's first symptoms are
scored against it. Two things make that reading doubtful:
- `leoni2026thesis.md` already notes that the term is not defined in the oospore chapter; the
  outdoor laboratory's leaves were assessed weekly from May to June for first symptoms (p. 61).
- Agroscope's untreated control at Changins (Viret et al. 2014's Table 12, as
  `real_outcomes_2026-11-03.csv` has it) saw its first oil spots later than Leoni's dates in all
  nine years the two share (2004-2010, 2012, 2013), by 8 to 16 days, median 10 (Agrarium's
  `scripts/diagnostics/changins_control_dates.py`). That is about one incubation period.

If Leoni's dates are infections dated back from the symptoms (or VitiMeteo's infection day
matched to them), every Agrarium score at Changins is about an incubation too late; CB10's
Switzerland result (docs/TRUTH-CALIBRATION-REPORT.md) turns on it.

## What to find

1. **How the thesis and the published paper define "observed primary infection":** a first lesion
   seen, the infection day dated back from it (by which incubation model), or the VitiMeteo-flagged
   infection that the first lesions confirmed. Quote it with the page.
2. **Which plot:** the outdoor laboratory (LEX) with concentrated inoculum, the untreated control
   of Viret et al., or another; and how often it was inspected.
3. **Whether the two Changins series are the same observations:** Leoni's 2004-2013 dates against
   Viret et al. 2014's Table 12 first spots and the Agroscope annual reviews (viret2017 to
   viret2021) for later years.

## What to deliver

On a branch `ingest/leoni-dates-d70`, following `literature/INGESTING.md`:
- the findings added to `leoni2026thesis.md` (and the paper's note, if read), each quoted with
  its page;
- a short answer note, `literature/requests/leoni-dates-d70-answer.md`, saying which reading the
  sources support: symptoms seen, or infections dated back, and by how many days if stated;
- if the dates are infections, a flag on the dataset record for `leoni2026_changins_primary.csv`.
