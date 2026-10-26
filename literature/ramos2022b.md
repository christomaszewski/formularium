---
id: ramos2022b
citation: Ramos, M. C. & Martínez de Toda, F. 2022. Macabeo (Viura) grape response to climate variability in areas located at different elevations in the Rioja Designation of Origin. Journal of the Science of Food and Agriculture 102(13):5670-5679
doi: 10.1002/jsfa.11914
read: 2026-10-26, a light reading from Europe PMC's JATS XML (no PDF held), by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; tables as rows, no page image
status: read
diseases: []
crops: [grapevine]
regions: [Rioja]
processes: [phenology, stage dates, climate response, grape composition]
records: []
datasets: []
files: [ramos2022.xml (the 2026-10-25 other-sources drop)]
---

# Ramos & Martínez de Toda 2022: Macabeo stages and composition against weather at five elevations

Thirteen seasons (2008-2020) of stage H (the Baggiolini stage) and harvest dates and of
grape composition at five Macabeo plots from 457 to 650 m in Rioja, regressed on
growing-season maximum temperature and on the water balance. The Carignan companion
(`ramos2022`) has records; this one prints slopes without intercepts.

## What it holds

- **Plots** (l. 14, 44): five Macabeo plots at Haro, San Asensio, Cenicero, Alesanco and
  Sotés, 457-650 m, planted 1972-1990; 2008-2020.
- **Climate** (l. 53): growing-season Tmax 23.7-25.6 °C; precipitation below 225 mm on
  average; ETo by Penman-Monteith and ETc with Allen & Pereira 2009 coefficients (l. 46).
- **Stage dates** (l. 58): stage H on average between 24 May ± 6 d and 1 June ± 8 d, no
  significant trend; harvest 21-30 September, advancing significantly only at San Asensio
  and Cenicero (Mann-Kendall, l. 48).
- **Responses** (l. 80-86): stage H advances 1.57-3.95 d per °C of Tmax from budbreak to H;
  harvest advances 5.2-8.7 d per °C of growing-season Tmax, and up to 6.9 d per 100 mm more
  water deficit at the higher plots; probable alcohol +0.69 degrees per °C at Haro; total
  acidity falls 0.7-1.3 g/L per 100 mm of deficit.
- **Composition** (l. 63, Table 2): 199-260 g per 100 berries, total acidity 5.1-6.6 g/L;
  the text's ranges for probable alcohol and malic acid do not match Table 2's means.
- **Not printed:** per-plot stage dates, the intercepts and statistics of the Fig. 4-5
  regressions, the projection values.

## Dependence

- **Fitted to** its own plot records (observed stages and composition, station weather with
  a computed water balance). Mann-Kendall for trends, Ward clustering and a factor analysis.
- Same authors and method as `ramos2022` (Carignan) and the Rueda and Ribera papers: flags,
  and the same monthly-temperature-regression form where coefficients are printed.

## Bearing (2026-10-26)

- For Agrarium's phenology truth (the 10-14 search): the slopes of stage H and harvest on
  temperature for a Catalan-adjacent white variety, 2-4 d per °C for stage H. No record:
  the regressions' intercepts are in figures the XML does not carry; the publisher's PDF
  would let them be read.
