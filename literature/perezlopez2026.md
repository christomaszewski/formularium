---
id: perezlopez2026
citation: Pérez López, J. 2026. Análisis de rentabilidad de una explotación vitivinícola de la DOCa Rioja, subzona de Rioja Oriental. Trabajo Fin de Grado (supervisor Martínez Martínez, Y.), Facultad de Economía y Empresa, Universidad de Zaragoza
doi:
read: 2026-10-25, lightly (the sections on the farm's cultivation calendar and labour costing, about lines 480-545 and 770-815 of 1650), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, La Rioja, Rioja Oriental]
processes: [spray calendar, spray interval, labour cost, work rate, farm economics]
records: []
datasets: []
files: [dr1025_perezlopez2026.pdf (the 2026-10-25 drop)]
---

# Pérez López 2026: one Rioja Oriental farm's spray calendar and labour costing, from an undergraduate profitability thesis

A bachelor's thesis analysing the profitability of one real vineyard farm of about 8 ha in Rioja Oriental for the 2023-24 campaign, whose calendar and labour costing show the farm's declared spray practice.

**Read this first.** Weak evidence: an undergraduate final-year thesis (Trabajo Fin de Grado) on one farm, with costs taken from a local cellar and supplier documents per the thesis, and no measurement. It is internally inconsistent: it says phytosanitary treatments "must be every 18 days" (l. 502), the calendar lists five treatments over April to July (l. 524-536), which are about 3 to 4 weeks apart on average (the strand agent's reading, not printed), and the labour costing counts six passes (l. 808). The treatments are all phytosanitary treatments (fungicide and insecticide), not downy mildew only. Only the calendar and labour sections were read.

## What it holds

- **The farm:** 7.81 ha (l. 76); the text also gives 8 ha in the municipality of Alfaro, divided into three parcels of 34,000, 37,000 and 7,100 m2 (young, adult and old bush-trained vines, l. 374-376). Campaign 2023-24.
- **Stated rule:** phytosanitary treatments "must be every 18 days", with the dates varying with the start of the programme; a calendar rule, not a reaction to disease (l. 502).
- **Calendar 2023-24:** the first phytosanitary treatment is in April, together with foliar fertiliser (l. 524). The calendar lists five phytosanitary treatments: April 1, May 1, June 2 and July 1 (l. 536).
- **Labour costing:** phytosanitary application counted as 6 passes at 1 hour per ha each, 75 EUR/ha of hired labour at 12.5 EUR/h, which is a field capacity of about 1 ha/h including loading; the six passes are one more than the five in the calendar, possibly a herbicide pass (the strand agent's guess, l. 808).

## Dependence

- A student's description of one commercial farm; costs are from local cellar and supplier documents per the thesis. No model and no data borrowed that bear on sprays.

## Bearing (2026-10-25)

- **Interval and count (spray.interval_days, spray.per_season):** one small Rioja Oriental farm declares an 18-day calendar rule and lists five treatments in 2023-24 (l. 502, 536). Weak support for a calendar-driven small-farm grower with spacing near 18 days or longer; one farm, one year, all pesticides, and the two figures disagree.
- **Work rate and labour cost (spray.work_rate_ha_h, spray.cost_per_pass):** about 1 ha/h per sprayer pass including loading, and 12.5 EUR/ha of hired labour per pass (75 EUR/ha for 6 passes at 12.5 EUR/h, l. 808). It matches the 1.0 ha/h of the French simple-kit case in `coc2023`; kind: a student's costing, not a measurement.
- **Not shown:** delay, compliance with any warning, wind or trafficability limits.
