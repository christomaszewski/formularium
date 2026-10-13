---
id: camargoalvarez2018
citation: Camargo Alvarez, Hector, Salazar-Gutiérrez, Melba, Zapata, Diana, Keller, Markus & Hoogenboom, Gerrit. 2018. Time-to-event analysis to evaluate dormancy status of single-bud cuttings: an example for grapevines. Plant Methods 14:94
doi: 10.1186/s13007-018-0361-0
read: 2026-10-13, a light reading of the publisher's XML text (no page layout) by a reading agent (claude-haiku-5-5); 28 of 28 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Washington, Prosser]
processes: [dormancy, budburst, survival analysis, method]
records: []
datasets: []
files: [camargoalvarez2018_pm.xml]
---

# Camargo Alvarez et al. 2018: dating endodormancy with Kaplan-Meier curves of forced buds

Single-node cuttings of Cabernet Sauvignon and Chardonnay taken weekly at Prosser from
August to December 2013-2016 and forced at 24 °C: each sample date's time to green tip
is a survival curve, the log-rank test against the August reference says whether the
buds are endodormant, and the crossing of the chi-squared line with its critical value
dates onset and release. A method paper; chilling is left out by design.

## What it holds

- **Design:** IAREC Prosser (46.3 °N, 355 m); 18 cuttings a sample (30 in 2016), weekly
  (twice weekly in 2014), forced at 24 ± 2 °C under 15 h light, recorded up to 203-238 d
  (l. 2).
- **Method:** Kaplan-Meier survival with right-censoring (Eq. 1); log-rank tests of each
  sample against the first August one, Dunnett-Hsu adjusted at a family-wise 0.05 (Eqs
  2-6, l. 222); onset and release where the interpolated chi-squared crosses the
  critical value (Eqs 7-8, l. 249-294); SAS PROC LIFETEST (l. 231). The reference sample
  reaches 50 % budbreak within 30 d; Cabernet's mean time rose from 23 to 130 d by 4
  September 2013 (l. 303-304).
- **Dates** (Table 1, l. 323): endodormancy onset 26 August to 4 September (Cabernet) and
  31 August to 6 September (Chardonnay); release 27 October to 5 November and 21 October
  to 3 November, 2013-2016; deepest dormancy 7-10 September 2013 and 14 October 2015
  (l. 313). The chilling accumulated by release is not computed (l. 325).

## Dependence

- **None computed;** standard survival statistics. Keller and Hoogenboom's Prosser
  group (`ferguson2014`, `saxena2023`); the Zapata et al. 2017 base temperatures cited in
  `ramos2018` are this group's.

## Bearing (2026-10-13)

- The time-to-event item on Chris's list, used for dormancy status rather than a date
  from weather. Its product is the release dates a chilling model would have to hit:
  late October to early November at Prosser for both cultivars.
