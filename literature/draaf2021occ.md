---
id: draaf2021occ
citation: DRAAF Occitanie (SRISET). 2021. Usage des fongicides dans les bassins viticoles d'Occitanie. Résultats des enquêtes pratiques culturales (Agreste Pratiques culturales 2016 and 2013). Agreste Occitanie Études n°1, February 2021 (8 pages)
doi:
read: 2026-10-25, in full (8 pages, French, official statistics bulletin; two-column layout interleaved by the text layer, so quotes are single-line fragments), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 16 of 16 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [France, Occitanie, Pyrénées-Orientales, Languedoc, Gers, Gaillac, Cahors]
processes: [spray count, spray interval, first spray date, spray window, fungicide, treatment frequency, organic, official statistics]
records: []
datasets: []
files: [dr1025_draaf2021occ.pdf (the 2026-10-25 drop)]
---

# DRAAF Occitanie 2021: three downy mildew sprays a year every 22 days in Roussillon, eleven in the wet Atlantic basins

An official statistics bulletin on fungicide use by Occitanie vineyard basin in the 2016 and 2013 French surveys, with downy mildew passes, intervals and first-spray dates.

**Read this first.** Grey literature: a regional statistics bulletin (Agreste), not a study. Four caveats. (1) The figures are farmers' declared passes and dates in the survey year (2016, repeated from 2013), not observed sprays. (2) The two-column text layer runs sentences across non-adjacent lines, so each quote is a fragment and the charts (interval histograms, treatment-frequency bars) are images that were not read. (3) The sentence on 75 % of plots (l. 504) is ambiguous: it may be a 75th percentile, and it is not clear whether it counts downy mildew passes only. (4) The 18 to 22 day gap at l. 538 is in the powdery mildew section (sulfur) and must not be read as a downy mildew interval. The microdata are under statistical secrecy; only tables are published, and the reuse licence is presumed to be the French open licence but is not stated in the document.

## What it holds

- **Passes:** on average six downy mildew passes a season in Occitanie in the 2016 survey (l. 384); the number is limited to three in the Pyrénées-Orientales basin (Roussillon, bordering Catalonia) and reaches 11 in the Gers and Cahors basins (l. 391, 394); 2013 and 2016 results converge, with the same number of passes per basin in both years (l. 391).
- **Interval:** the downy mildew spray frequency converges and ranges between "every 11 days" and "every 15 days" (l. 431, 433), closer in the Atlantic zone and clearly wider in the Mediterranean zone: every 13 days on average in the Gers (l. 439) and every 22 days in the Pyrénées-Orientales (l. 441). The section heading reads "treatments every 14 days" (l. 427).
- **Window and first spray:** the treatment period runs from early May to the end of July, with a wider range in the Atlantic zone because rain washes off contact fungicide (l. 444). The mean date of the first downy mildew spray is the end of April in Atlantic vineyards (19 April earliest, in the Gers) (l. 450) and early May in Mediterranean ones (5 May at the latest, in the Pyrénées-Orientales) (l. 453).
- **Product class and interval:** fosetyl (penetrating) became the most used active substance in 2016 and lets growers space treatments every 12 days against every 8 days for folpet (contact) (l. 546).
- **Organic:** for 75 % of plots the number of passes is 9 in conventional and 12 in organic farming (l. 504); ambiguous, see above.
- **Treatment frequency:** the fungicide TFI of the Atlantic zone is on average 1.6 times that of the same plot group in the Mediterranean zone (l. 239); Occitanie in 2016 used more than 3.5 million approved doses on 252,000 ha, 14 approved doses per ha on average (l. 24).
- **Copper:** the amount of copper applied in 2016 is 6.8 kg/ha in the Languedoc and over 5 kg/ha in the Pyrénées-Orientales (l. 520).
- **Powdery mildew (not downy):** the Pyrénées-Orientales basin stands out with a gap of 18 to 22 days for more than 60 % of plots (l. 538).

## Dependence

- Descriptive survey statistics from Agreste "Pratiques culturales en viticulture" 2013 and 2016 (face-to-face public surveys); no model. The interval figures are declared practice. The leaflet `draaf2019occ` quotes the same 2016 survey.

## Bearing (2026-10-25)

- **Sprays per season and interval (spray.per_season, spray.interval_days):** Pyrénées-Orientales, 2016, vineyards of all types: 3 downy mildew passes a season, a mean gap of 22 days, first spray in early May (5 May at the latest), window early May to end July (l. 391, 441, 444, 453). The wet Atlantic pair is 11 passes and a 13-day gap (l. 391-394, 439). Kind: official survey of declared practice. These are a dry-site anchor and a wet-site anchor for a grower rule; the Penedès is not in the bulletin.
- **How sprays are timed:** the bulletin gives no share of calendar against warning-based spraying. It says the interval depends on the product class (12 days for fosetyl, 8 for folpet, l. 546) and that rain, which washes off contact fungicide, widens the treatment period in the Atlantic zone (l. 444), which looks like a calendar with a product-driven interval rather than a reaction to alerts (reading of the text, not a stated result).
- **Not shown:** delay from a warning to a spray, trafficability, labour, compliance, cost per pass.
