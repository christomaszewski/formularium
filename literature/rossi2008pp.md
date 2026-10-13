---
id: rossi2008pp
citation: Rossi, V., Caffi, T., Bugiani, R., Spanna, F. & Della Valle, D. 2008. Estimating the germination dynamics of Plasmopara viticola oospores using hydro-thermal time. Plant Pathology 57:216-226
doi: 10.1111/j.1365-3059.2007.01738.x
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 51 of 51 quotes found at their lines by scripts/verify_quotes.py; the abstract and the equations page (p. 218) read in the page images by the main session; held since 2026-10-07 as the source of the engine's dormancy rule, read then by Agrarium without a note
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Piedmont, Asti]
processes: [oospore germination, oospore dormancy, primary infection, hydro-thermal time]
records: [rossi2008pp.dormancy, rossi2008.primary]
datasets: [rossi2008pp.discs, laviola1986]
files: [2008-rossi-10-1111-j-1365-3059-2007-01738-x.pdf]
---

# Rossi et al. 2008 (Plant Pathology): oospore germination on hydro-thermal time

The source of the engine's oospore moisture rule (`rossi2008pp.dormancy`, borrowed by
`rossi2008.primary`) and of the dataset `rossi2008pp.discs`. Held since 2026-10-07; this is
its note. Not to be confused with the Ecological Modelling paper of the same year
(`rossi2008`), which runs this germination curve inside the primary-infection model.

## What it holds

- **Data** (`rossi2008pp.discs`): oospores from leaves collected at the end of 1998-2002 in
  a 500 m² plot of a Barbera vineyard at Asti, Piedmont (l. 109-121); 10 g leaf-fragment
  samples taken weekly from late March to early July, 1999-2003 (l. 134-135); germination
  measured indirectly as the relative infection incidence (RII) on grape leaf discs
  floated 24 h on the oospore suspension and incubated 14 d at 20 °C, 280 discs a sample
  (l. 75-89); infected discs by year 87, 276, 272, 125 and 91, 124 fitted cases (l.
  240-241, 388). Hourly weather from an automatic station in the vineyard (l. 105).
- **Four physiological times from 1 January** (p. 218, read in the image): degree-days
  above 8 °C (eq. 1, after Gehmann 1987, l. 132), degree-hours above 10 °C (eq. 2,
  l. 136), thermal time TT = Σ 1/(1330.1 − 116.19 T + 2.6256 T²), the hourly rate from
  Laviola et al. 1986's minimum germination time in hours (R² 0.98; eq. 3, l. 187-194;
  `laviola1986`), and hydro-thermal time HT = Σ TT·M with M = 1 when rain > 0 mm or VPD
  ≤ 4.5 hPa and 0 otherwise (eq. 4, l. 170-172), the moisture switch from Rossi & Caffi
  2007, whose water activity 0.56 corresponds to VPD 2.13 hPa with an upper 90 %
  confidence limit of 4.5 hPa (l. 198-209); VPD from Buck 1981, VPD = (1 − RH/100)·6.11·
  exp[17.47 T/(239 + T)] hPa (l. 176-178).
- **The fit:** a Gompertz RII = exp[−a·exp(−b·HT)], R² 0.97-0.99 by year and 0.887
  pooled (against 0.880 for degree-days), with pooled a = 15.9 ± 2.63 and b = 0.653 ±
  0.034 (abstract, l. 30-33, 334); cross-estimation of each year from the other four: r
  0.93-0.99 (l. 375-383, 309); 26 of 124 points outside the confidence bands for HT
  against 43 for degree-days (l. 337). The between-year coefficient of variation of the
  time to 5 % germination falls from 90 to 41 % across the four methods (l. 261).
- **Against Gehmann's 160 degree-days:** 18 of 124 cases germinated below it, the lowest at
  about 71 degree-days (l. 509-511).
- **Field check:** probable infection periods "determined following Rossi et al. 2002"
  (the method not printed, l. 111-113): in 1999 first symptoms on 27 May after infections
  on 15 May (7.7 mm, 13 h wet, 15.3 °C) and 17 May (14.6 mm, 30 h, 12.7 °C), at HT about
  2.1-2.3 budbreak held under 3 % of the season's oospores (l. 319-327); 2001 infection
  6-7 May (9 mm, 16 h); 2002 infections 23 and 25 May at HT 4.1-4.2; no downy mildew in
  2003 (l. 338-406).
- **Garbled or inconsistent:** "HD" for HT in the 2002 paragraph (l. 396); Table 1's
  degree-hours /1000 against Table 2's /100 (l. 277, 373); per-year Gompertz parameters
  not printed; the results of the logistic and monomolecular fits "not shown" (l. 164).

## Dependence

- **Fitted to** the Asti leaf-disc assays (observed); the x-axis is computed from the
  vineyard's weather. The field infection dates are dated by Rossi et al. 2002's method
  (`rossi2002`), a model's, and serve only as a check.
- **Borrows** Laviola et al. 1986's temperature polynomial (`laviola1986`, data read there
  as inferred), Rossi & Caffi 2007's moisture threshold, Gehmann 1987's degree-day base
  and Buck 1981's vapour pressure.
- **Engine pieces:** `rossi2008pp.dormancy` is the M rule with VPD ≤ 4.5 hPa; the Gompertz
  (a 15.9, b 0.653) is what `rossi2008` runs for germination. `rossi2009` credits other
  Gompertz values (173.6, 0.119) to this paper, which does not print them.
- **Authors:** Rossi, Caffi, Bugiani (`caffi2009`), Spanna (`sanna2017`): flags.

## Bearing (2026-10-12)

- The record and dataset are read: the dataset now names Asti, Barbera, the weekly
  samples and the 280 discs, and the record carries the printed thresholds and
  coefficients. For a truth, the paper's own numbers mark the engine's germination
  curve's error (26 of 124 points outside its bands), and its degree-day comparison shows
  Gehmann's 160 is not a floor.
