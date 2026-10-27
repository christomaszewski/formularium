---
id: ramos2025
citation: Ramos, M. C. 2025. Effect of climate extremes and elevation on the Tempranillo grapevine response: case study in Ribera del Duero DO (Spain). International Journal of Biometeorology (s00484-025-02970-z)
doi: 10.1007/s00484-025-02970-z
read: 2026-10-22, lightly: the methods and the results on phenology and elevation (Europe PMC full text PMC12479616, an XML flattened to one paragraph per line, so line numbers refer to that flattened text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, Castilla y León, Ribera del Duero DO]
processes: [phenology, budburst, flowering, veraison, elevation, climate extremes, grape composition]
records: []
datasets: []
files: [PMC12479616.xml (the 2026-10-22 drop)]
---

# Ramos 2025: Tempranillo phenology at three elevations in Ribera del Duero, 2004 to 2023

A 20-year comparison of budbreak, flowering and veraison of Tempranillo in zones at 725 to 915 m, finding no significant date difference between the lowest and highest zones.

**Read this first.** Tempranillo, not a Penedès variety, and an elevation contrast on a plateau, not a cold hollow. The mean dates and standard deviations are only in Fig. 3, not in the text. The middle zone is given as 830 to 845 m in the methods (l. 14) and as 841 to 864 m in the Fig. 3 caption (l. 24).

## What it holds

- **Zones:** three zones of the Ribera del Duero DO at 725 to 765, 830 to 845 and 880 to 915 m a.s.l., 2004 to 2023 (l. 14); weather from four ITACyL stations at 740, 790, 811 and 852 m (l. 15); four plots a zone for grape composition (l. 115). Mostly rainfed, goblet and trellis, DO minimum 2,000 plants ha-1 and maximum 7,000 kg ha-1 (l. 16).
- **Phenology:** dates of budbreak, flowering and veraison (the paper's stages C, I and M, after Baggiolini 1952) as the dominant stage, more than 50 % of the plants in a plot, supplied by the DO's Regulatory Council (l. 16).
- **Temperature contrast:** April to September mean Tmax 25.2 to 25.6 °C across the zones, mean Tmin 7.2 to 9.0 °C, so the zones differ more in Tmin than in Tmax (l. 18); years differ by up to 3.8 and 4 °C in Tmax (l. 18).
- **Elevation result:** "No significant differences in phenological dates were observed between the higher and lower elevation zones" (l. 23). The medium zone had later average budbreak, flowering and veraison than both the low and the high zone (l. 23).
- **Seasons:** the earliest budbreak was in 2011, 2014, 2017, 2020 and 2023 and the latest in 2009, in all locations (l. 23). Over the 20 years the mean trend is an advance of 8.2 d for budbreak, 6.9 d for flowering, 2.6 d for veraison and 6.3 d for maturity (l. 23).

## Dependence

Own records from the DO's Regulatory Council (l. 16); no model is computed. Shares its author with `ramos2017`: a flag, not a dependency.

## Bearing (2026-10-22)

- **host.hollow_delay_days_per_m:** the elevation evidence for budbreak in this batch points to about zero: no significant difference in budbreak, flowering or veraison across 725 to 915 m in one DO, while the middle zone is later than both ends, so site, soil or aspect outweigh an elevation trend. It does not support the assumed 0.5 d per m. What is not shown: a value in days per m (the dates are in Fig. 3), or any cold-hollow or frost-pocket effect; elevation here is height across a plateau.
- **host.budburst_sd_days:** the same years are earliest and latest for budbreak in all three zones, so the season effect dominates the location effect. No standard deviation is printed in the text, and the 20-year budbreak trend (8.2 d earlier) would inflate a raw SD of yearly dates.
- **host.budburst_doy and the other host parameters, cultivar susceptibility:** nothing; no budbreak date is printed and no disease is studied.
