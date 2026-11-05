# Answer to leoni-dates-d70.md

2026-11-05, by an `ingest` session. The main session read the passages below in the thesis, the
paper, the two Dubuis papers and the raw Agrometeo notices. A reading agent went through Agroscope's
reports, reviews and notices for the first-spot series; its 128 quotes were found at their lines by
script. Thesis pp. 66, 96, 100 and 183, Dubuis 2012 p. 196 and Dubuis 2019's Table 1 were also read in
the page images. The series is `literature/changins_first_spots_2026-11-05.csv`.

## Short answer

**Infections dated back, not symptoms seen.** Leoni's "observed primary infection" is the day of the
infection judged to have caused the first oil spots at the outdoor laboratory. No sentence defines the
column. But in five years a source names that infection, and the day is Leoni's to the day. Over 18
years the first spots come 7 to 16 days later, median 10. So Agrarium's scores at Changins read about
10 days too late, as the request feared. 2020 does not fit, and 2019 has no laboratory spot to check.

## 1. What the term means

Table 3.3 (thesis p. 183) and Table S1 (the paper's supplement) head the column "Observed day" under
"Primary infection". Neither text defines it. Where a source gives both dates, the column holds the
infection, not the spot:

| Year | First oil spot | Infection named for it | Leoni | Where |
|---|---|---|---|---|
| 2009 | 25 May | "vraisemblablement" (probably) the rain of 14-15 May | 15 May | Dubuis 2012 p. 196 |
| 2021 | 25 or 26 May | 16 May | 16 May | thesis p. 66; Agrometeo notice 423 |
| 2023 | 11 May | 1 May | 1 May | thesis p. 96; Agrometeo notice 507 |
| 2024 | 16 May | 6 May | 6 May | thesis p. 100 |
| 2025 | 20 May | 12 May | 12 May | Agrometeo notice 575 |

- **In Agroscope's words:** "Cela correspond à l'infection primaire du 01 mai 2023" (this corresponds
  to the primary infection of 1 May). Notices 338, 423, 507 and 575 all say so, signed by Anne-Lise
  Fabre, a co-author of the paper.
- **The method, in the thesis's words** (2024, the PIN and CHA plots, p. 100): "the first oil spots were
  observed on 11 June, implying a primary infection occurring around 25 May, according to
  VM-Plasmopara".
- **Not simply the model's output.** Notice 507: the 1 May 2023 infection "n'est pas visible sur
  Agrometeo", since the 140 °C·day sum was not reached and the vine in its usual setting was not
  receptive. In 2009 the model computed no infection for the rain chosen (Dubuis 2012 p. 196). So the day
  is picked by people, reasoning back from the spot with the model's incubation.
- **Days between spot and infection, as named:** 2021 9-10, 2023 10, 2024 10, 2025 8, and 2020 11-12. No
  fixed number is stated.

## 2. Which plot

The outdoor laboratory (LEX): rows of Pinot noir, Gamay and Chasselas with a cane of each vine bent to
the ground over oospore-rich leaves, never sprayed (paper p. 3; thesis p. 61). From May to June, to
detect the first symptoms, "all leaves from these vines were counted and assessed for downy and
powdery mildew on a weekly basis" (thesis p. 61, l. 3025-3026). A weekly round fixes a spot to about a
week, as I read it, which is part of the spread in the gaps.

**It is built to be early.** Leaves are held near concentrated inoculum, and in 2023 it was infected
when vines "dans son environnement classique" (in their usual setting) were not yet receptive. So even
its true first spots mark the earliest possible, not a vineyard's first spots.

## 3. Whether the two Changins series are the same observations

**Viret's and Dubuis's are, in most years; Leoni's is a different quantity derived from them.**

- Viret 2014's Table 12 "témoin" sits under the heading "Changins, laboratoire extérieur", and equals
  Dubuis 2019's "field laboratory" in 10 of 11 years, 2003-2013. Only 2012 differs, 14 against 10 May.
  Notice 238 writes "laboratoire extérieur à Changins (témoin non traité)" in 2017. So the request's
  control and the laboratory are one series, under two labels.
- From 2018 the notices do list the laboratory and "nos témoins non-traités" apart: those controls are
  a separate plot, first spots 7 June 2018 and 15 August 2019.
- Leoni's dates fall before the laboratory's spots in all 18 years compared. The series file has every
  year, with the gap. Median 10 days, range 7-16.

## What does not fit, or is not settled

- **2020:** the laboratory's first 2 spots came on 25 May, from the infections of 13-14 May (notice
  338). Leoni's 7 June is 13 days after them. It cannot be their infection. No source explains it.
- **2019:** no laboratory spot found: none by 29 May, none in Changins's controls by 20 June. Leoni's 20
  June is the day first spots appeared at Aigle and Marcelin, not Changins (Viret 2019, Table 2). That
  may be how it got there, or chance; no source says.
- **2011:** the paper leaves the year out because "no symptom was observed at the experimental site"
  (p. 11), yet Dubuis 2019 and Viret 2014 print 16 May. Agroscope's own 2011 report prints 16 May too and
  calls the disease nearly absent to mid-August. Oospore germination was "non atteinte", so the year
  also lacks the maturity day Table S1 needs, which may be the real reason.
- **2022:** the paper's reason is right: no spot in any Changins plot.
- **Dates that differ:** 2017's 24 May and 2021's 31 May are probably notice dates; notice 238 gives 23
  May and notice 423 gives 26 May. 2018's 7 June is the controls, and Dubuis's 29 May for the laboratory
  has no second source. 2012 is unsettled. 2013 is 17 May in Table 12 and "début juin" in the review.
  2016's 9 May is uncorroborated.
- **The notices begin in 2016 here,** and ids 1-171 and 343-419 were not probed. Agrometeo's observation
  tables, which need a browser, may hold more. The 2022 review could not be fetched.

## What follows

- **For Agrarium (recommended once, Chris decides):** score first symptoms at Changins against
  `changins_first_spots_2026-11-05.csv`, and keep Leoni's column only as an infection date. Leave out
  2019, and read the plot as an early bound, not a vineyard.
- **For Cooptera and `leoni2026.oospores`:** the paper's gain, 80 % to 95 % of years and a median error
  of 8 to 4.5 days, is scored against days set by reasoning with the same model's incubation. In 6 of 20
  years Table 3.3's day equals its VitiMeteo column exactly (2004, 2008, 2010, 2012, 2014, 2021). The MTG
  < 1.5 d threshold was also chosen against these dates (paper p. 13).
- **Not done, for Chris:** `calibrated_with` on `leoni2026.oospores`. It would change kinship for both
  tools, and the catalogue has no VitiMeteo incubation record to point at. I recommend adding one and
  the link, as for `rossi2002.onset`. For now this is a flag on both records.

## What changed here

- New: `changins_first_spots_2026-11-05.csv` (dates only, no quotes: Agrometeo states no reuse licence);
  notes `agrometeo2025`, `viret2012`, `viret2013`, `viret2025`.
- `leoni2026thesis.md`, `leoni2026.md`, `dubuis2012.md`, `dubuis2019.md`, `viret2014.md`: the findings.
- `leoni2026_changins_primary.csv`: a flag in the header line. Columns and values are unchanged, so
  nothing that reads them breaks.
- `datasets.py` (`leoni2026.changins_primary`, new `agroscope.changins_first_spots`) and `catalogue.py`
  (`leoni2026.oospores`, `vitimeteo.oospores`): flags in text. No equation, number or dependency changed.
