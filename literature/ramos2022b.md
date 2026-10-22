---
id: ramos2022b
citation: Ramos, M. C. & Martínez de Toda, F. 2022. Macabeo (Viura) grape response to climate variability in areas located at different elevations in the Rioja Designation of Origin. Journal of the Science of Food and Agriculture 102(13):5670-5679
doi: 10.1002/jsfa.11914
read: 2026-10-22, lightly: the phenology and discussion text (Europe PMC full text PMC9544767, an XML flattened to one paragraph per line, so line numbers refer to that flattened text; tables lose their layout), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, La Rioja, Rioja DOCa]
processes: [phenology, budburst, flowering, harvest, elevation, grape composition]
records: []
datasets: []
files: [PMC9544767.xml (the 2026-10-22 drop)]
---

# Ramos & Martínez de Toda 2022: Macabeo (Viura) in five Rioja plots at 457 to 650 m, 2008 to 2020

The only Macabeo phenology in this batch from outside the Penedès: five unirrigated Rioja plots, with a mean budbreak date and the spread of the flowering stage between extreme years.

**Read this first.** This is a different paper from `ramos2022` (Carignan). Rioja is a cooler, higher, inland region, so its dates are a contrast to the Penedès, not a value for it. The budbreak date is "an average of what was available", not recorded for all plots and years, and the paper gives no flowering date in its text (the stage H dates are in a figure).

## What it holds

- **Plots:** five Macabeo plots in Rioja DOCa at 457 to 650 m a.s.l. (lowest SA 457 m, highest S 650 m; l. 148-149), 2008 to 2020, vines averaging 2.8 m × 1.1 m and not irrigated (l. 134). Phenology is the date when 50 % of the plants in the plots reached the stage (l. 136).
- **Budbreak and veraison:** stage C, budbreak, on 15 April on average (day of year 105) and stage M, veraison, on 15 August; the other stage dates "were not available for all plots and years" (l. 136). The paper's introduction says Macabeo "has a late budbreak and late harvest" (l. 79).
- **Stage H:** the flowering stage scored is Baillod-Baggiolini's H, "flowers separated" (l. 134, 148); the paper prints no BBCH number for it.
- **Year-to-year range:** between the coolest and the hottest year (maximum temperature 3.1 to 3.4 °C apart, by location) stage H differed by 13 and 23 d in the two zones, and harvest by 19 to 24 d (l. 245).
- **Cited elsewhere:** Macabeo flowered in La Mancha on 2 June ± 6 d, which the authors call "similar dates" to Rioja's, and was harvested on 3 September ± 5 d (l. 241); at Raïmat (Costers del Segre) harvest was on 5 September ± 8 d, an 11-year average given as a personal communication (l. 243). In the Penedès, 9° potential alcohol was reached on 28 August on average (cited to Ramos 2017, reference 35), against 8 September in the earliest Rioja plots (31 August to 23 September) (l. 239-241).

## Dependence

Own data; the grape parameters were supplied by the Consejo Regulador of Rioja DOCa (l. 136), and the sentence does not name a source for the phenology dates. The Penedès, La Mancha and Raïmat figures are cited. Shares its first author with `ramos2017` and both authors with `martinezdetoda2019`: flags, not dependencies.

## Bearing (2026-10-22)

- **host.budburst_doy:** Macabeo budbreak 15 April (day 105) in Rioja against 6 April (day 96) for Macabeo in `ramos2017`'s Penedès vineyard: about 9 d later in the cooler, higher region. It supports a Macabeo budbreak in the first half of April for the Penedès (as `ramos2017` measured) and not a Penedès value of its own; Xarel·lo, Parellada and Chardonnay are not covered.
- **host.budburst_sd_days:** no value. The 13 to 23 d range is for the flowering stage between the two most extreme years, not for budbreak and not a standard deviation.
- **host.flowering_after_budburst_days:** no Rioja flowering date is printed in the text. Taking La Mancha's 2 June (a proxy the authors call similar) against the 15 April budbreak would give an interval near 48 d (my arithmetic, through another region); treat it as a loose cross-check only.
- **host.vine_sd_days and cultivar susceptibility:** nothing; no vine-to-vine spread is given and no disease is studied.
