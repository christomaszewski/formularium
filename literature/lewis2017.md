---
id: lewis2017
citation: Lewis, K. & Tzilivakis, J. 2017. Development of a data set of pesticide dissipation rates in/on various plant matrices for the Pesticide Properties Database (PPDB). Data 2:28
doi: 10.3390/data2030028
read: 2026-10-20, LIGHT, by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [fungicide residue, residue decay, dissipation half-life]
records: []
datasets: []
files: [lewis_2017.pdf (the 2026-10-20 drop)]
---

# Lewis & Tzilivakis 2017: a data set of pesticide half-lives on plants

A data descriptor for the PPDB's plant dissipation rates: over 2,200 records of DT50 in or
on leaves, fruits and other plant matrices from 1,390 studies, CC-BY, as one Excel file.

## What it holds

- Data descriptor for the PPDB: 1390 published studies, 407 active substances, 207 plants,
  over 2200 records (l. 22-23, 194-196).
- One Excel file with 14 fields (l. 124-125). Each record gives min, max and arithmetic mean
  DT50 in days (l. 135, 179-187).
- Matrices: leaves, fruits, seeds, roots, new shoots 'etc.' (l. 194-195). Grape is not
  named. Wine and other processed products are excluded (l. 330-331).
- Where only a concentration series is printed, half-life is from first-order kinetics: Ct =
  C0 e^(-kt), RL50 = ln 2/k (l. 136-142). Where one article reports several experiments, the
  range is given (l. 147-148).
- Worked example, cypermethrin (an insecticide): leaves 2.5 to 13.1 days and fruit 1.9 to
  6.1 days on the surface (Fig. 1, l. 205-206). In and on: leaves 1.8 to 4.8 days, fruit 1.3
  to 11.7 days (Fig. 2, l. 223). The Fig. 2 chart shows a spinach leaf bar near 5.5 days, so
  the text range may be incomplete.
- Literature from January 1980 to June 2017, from four databases (l. 280-281, 291-292). Only
  replicated, empirical values: modelled or inferred values were excluded (l. 294-297).
- Earlier sets: 79 substances (l. 86-87), 65 pesticides (l. 88), 346 pesticides from 811
  studies (l. 88-89).
- Licence CC-BY (l. 30). Supplementary file 'Plant dissipation data August 2017.xlxs' (l.
  27-28).
- Not printed: fungicide medians, grape values, a default for missing data, and per-matrix
  counts.
- The PDF's text layer holds an unrelated passage (a New Zealand coastal-hazard text, l. 207-259)
  not visible on the printed page; not used.

## Dependence

- None: collated empirical values; 'not modelled or inferred in any way' (l. 296-297).
  Concentration series are turned into half-lives by first-order kinetics (l. 136-142).
  Checked against Fantke & Juraske 2013's set (l. 115-117), a comparison, not a shared fit.

## Bearing (2026-10-20)

- For Agrarium's grower and Cooptera's E6: the open source for first-order residue decay
  rates on leaves and fruit by active substance, to be filtered for grape and the fungicides
  a vineyard uses. The spreadsheet itself was not obtained (MDPI refuses this VM); the paper
  prints no fungicide medians or grape values.
