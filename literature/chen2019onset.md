---
id: chen2019onset
citation: Chen, Mathilde, Brun, François, Raynal, Marc & Makowski, David. 2019. Timing of grape downy mildew onset in Bordeaux vineyards. Phytopathology 109(5):787-795
doi: 10.1094/PHYTO-12-17-0412-R
read: 2026-10-08, in full by a reading agent (claude-sonnet-5-5); 60 quotes checked by scripts/verify_quotes.py, provenance and dependence by the main session. Earlier read on 2026-10-07 (Agrarium's read-primary.md)
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Bordeaux]
processes: [season onset]
records: []
datasets: []
files: [10-1094-phyto-12-17-0412-r.pdf]
---

# Chen, Brun, Raynal & Makowski 2019: when downy mildew appears in Bordeaux

From ACTA and INRA (Chen, Brun, Makowski) and the IFV, Bordeaux (Raynal). The journal paper
of the chapter on onset in Chen's thesis ([chen2019](chen2019.md)).

## What it holds

- **Data:** untreated rows observed weekly by eye by the IFV and partners, weeks 12 to 33,
  2010-2017 (l. 118, 125); a row held 53.1 stocks on average (l. 124); 266 untreated plots
  (l. 130), also called sites and site-years. Observation stopped when infection neared
  100% (l. 129). The paper names no network or rule for choosing sites, and thanks the IFV
  for access to its data and to the EPIcure platform (l. 540).
- **Event:** the week when 1% of vines, or of bunches, show symptoms, counted from the
  first week of the year (l. 114). For vines, 40.6% of plots are right-censored and 16.9%
  left-censored (l. 151).
- **Weather:** SAFRAN daily rain and temperature (Météo-France), not plot sensors (l. 102).
- **Model:** log-normal survival, ln(T) = b0 + X·b + s·Z, years against 2010 (l. 256).
  Vines: b0 = 3.228 (25.2 weeks), log scale -1.658; bunches: b0 = 3.329 (27.9 weeks), log
  scale -1.976 (l. 374, 382). Year effects for vines from -0.277 (2014) to -0.010 (2011)
  (l. 375, 378).
- **Pooled:** 90, 50 and 10% of plots symptomless on vines at weeks 19.1, 25.3 and 33.6
  (l. 212), on bunches at 22.6, 27.8 and 34.4 (l. 229); 29.3% of plots never show symptoms
  on vines, 42.1% on bunches (l. 204, 226).
- **Weather effect:** only spring rain (March to June) is significant; wet springs bring
  onset earlier (l. 313, 348). Its coefficient is not printed.
- The paper calls the same curve log-normal and log-logistic in different places (l. 175,
  206, 258).

## Dependence

- No model computed or dated its data: onsets are seen, not inferred.
- Whether EPIcure, the IFV's risk platform, helped choose sites or time visits is not said:
  a question to settle before matching a truth to these data.
- No author of an engine model.

## Bearing (2026-10-08)

- A history-matching pattern made outside the engine's lineage: the distribution of onset
  weeks and the share of plots never infected. The "Disease models" session records the
  IFV data behind it (Formularium `chen2019.ifv`, on its branch) and holds the thesis note.
