---
id: ziehmann2026
citation: Ziehmann, E., Zachmann, L. & Finger, R. 2026. Patterns and clusters of pesticide reduction strategies in Swiss viticulture. Journal of Wine Economics 21:214-243
doi: 10.1017/jwe.2026.10118
read: 2026-10-25, lightly (abstract, Table 1, the data section and the decision support paragraph; about lines 1-240, 350-392 and 1300-1320 of 1787; clusters and regressions not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Switzerland]
processes: [pesticide reduction, decision support tools, adoption, grower survey, sprayer technology]
records: []
datasets: []
files: [dr1025_ziehmann2026.pdf (the 2026-10-25 drop)]
---

# Ziehmann et al. 2026: 54 % of Swiss grape growers use decision support tools for fungicides (yes or no), from a 2022 survey of 436

An economics paper that clusters Swiss growers by the pesticide reduction measures they use, whose Table 1 gives the share using each measure, including decision support tools.

**Read this first.** The adoption figures are binary: the survey records only whether a measure is used, not how much, so 54 % does not say how closely advice is followed or what share of sprays it decides (l. 388). It is Swiss (steep slopes, a different spray fleet) and not Spanish. Table 1's text layer splits row labels across lines (for example "Decision sup-" and "port tools fungicides"), and the percentages were read from the first line of each row as printed. Table 1's participation numbers are taken from the survey data (Zachmann et al. 2023b), so they refer to the full survey, not necessarily to the final 313 observations. Only the abstract, Table 1, the data section and the decision support paragraph were read.

## What it holds

- **Survey:** 436 Swiss grape growers surveyed in spring 2022 in all six wine regions, together covering 14.4 % of the Swiss vineyard area (l. 357); the final analysis dataset has 313 observations after outliers and organic farms were excluded (l. 396).
- **Decision support tools:** 54 % of growers use decision support tools for fungicides, against 39 % for insecticides (l. 213); canopy management is at 91 % (Table 1, l. 177). The use is a yes or no answer (l. 388).
- **Sprayers:** tunnel recycling sprayers are used by 0.3 % of growers; spraying equipment with horizontal assistance 42 %, hand sprayers 35 %, low-drift nozzles 35 %, spraying guns 13 % and drones 11 % (Table 1, l. 227).

## Dependence

- The same 436-grower survey as the held note `zachmann2024` (Zachmann, McCallum and Finger 2023b is the data description cited). Two authors are shared with that note; a shared author is only a flag.

## Bearing (2026-10-25)

- **Compliance with decision support (grower.dss_compliance):** 54 % of Swiss growers use decision support tools for fungicides (l. 177), any use, not depth. Supports an order of magnitude for the share of growers who use a tool at all, in Switzerland, 2022; it does not give the share who follow it on a given day. Kind: grower survey, binary.
- **Sprayer technology (spray.work_rate_ha_h):** the Swiss sprayer mix (l. 227) is for steep-slope vineyards and says nothing about capacity in ha/h.
- **Not shown:** spray counts, intervals, delay, Spain.
