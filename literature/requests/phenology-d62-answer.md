# Answer to phenology-d62.md

2026-10-28, by an `ingest` session; a reading agent searched and the main session checked each
date against its text. Dates are in `literature/pipeline_stage_dates.csv` (site, year, cultivar,
stage, BBCH, date, source, where).

## Per site

- **Changins (Chasselas): 2021-2024 only.**
  - Leoni's thesis, Table 1.1 (p. 24), "Agroscope observations": BBCH 09, 11, 53, 61, 71 and
    81. Budburst was 20, 19, 18 and 8 April; flowering began 18 June, 30 May, 10 June and
    12 June.
  - No dates for 2004-2020, 2025, or BBCH 12-15.
  - Agroscope Pully holds the Changins series from 1958. An Int. J. Biometeorol. 2018 study
    (PMC5966476) used budburst for 1958-2012 "provided by Agroscope", without printing it.
    No open release or licence was found. Ask Agroscope for 2004-2025.
- **Vaud, Chasselas, 2011-2021, site not named** (`proconseil2021`): budburst and full
  flowering. It is not Changins: 2021's budburst is 7 April against 20 April. A regional check
  only.
- **Geneva and the Finger Lakes (Chancellor, 1981-2004): none.**
  - Kennelly et al. 2007 print only the stages at symptoms and infection.
  - No year-by-year Cornell series was found. The records are the authors'.
  - Cornell newsletters give recent budbreak and bloom for other cultivars. They were not read.
- **Castell'Arquato (Barbera, 2020-2022): figure only.**
  - Taibi et al. 2023 show the stages as bars in Fig. 1 (p. 5); no dates are printed.
  - The nearest printed dates are Fedele et al. 2026's Merlot at the Piacenza campus, about
    25 km away: budburst 22 April 2020 and 20 April 2022, flowering from 11 May 2020. They
    are in the CSV, labelled.

## Cultivars

Changins Chasselas, Geneva and the Finger Lakes Chancellor, Castell'Arquato Barbera. The
Barbera is now on `taibi2023.castellarquato`. Chancellor was already on `kennelly2007.geneva`.

## Records

- `leoni2026.changins_stages` and `proconseil2021.vaud_phenology`, new.
- `taibi2023.castellarquato`: cultivar and stage-date note added.
- Notes: `proconseil2021`, new; sections added to `leoni2026thesis` and `kennelly2007`.

Not obtained: Spring, Viret & Bloesch 2009, Revue suisse Vitic. Arboric. Hortic. 41(3):151-155
(Chasselas stages at Pully since 1925; the journal's link now opens its home page; no Wayback
capture).
