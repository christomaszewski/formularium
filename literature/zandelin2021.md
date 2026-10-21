---
id: zandelin2021
citation: Zandelin, P. 2021. Virtual weather data for apple scab monitoring and management (Swedish title Virtuell väderdata för bevakning och behandling av äppleskorv). Degree project (30 credits, course EX0857), Swedish University of Agricultural Sciences (SLU), Department of Plant Protection Biology, Alnarp (not peer reviewed)
doi:
read: 2026-10-21, lightly: abstract, introduction (apple scab, RIMpro, grid data, stations, leaf wetness), methods, results (Tables 2-4, Figures 2-4), discussion, conclusion; background sections skimmed; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [apple scab]
crops: [apple]
regions: [Sweden, Scania]
processes: [virtual weather, gridded weather, weather station, RIMpro, infection category agreement, leaf wetness proxy, rain threshold]
records: []
datasets: []
files: [zandelin2021.pdf (the 2021 SLU degree project, 2026-10-21 drop)]
---

# Zandelin 2021: apple scab infection categories from an orchard station against two virtual weather sources (SLU degree project)

Ten Scanian apple orchards, 2019 and 2020: RIMpro apple scab infection categories computed from an in-orchard station, the LantMet grid and Meteoblue virtual stations, and compared by source. A degree project, not peer reviewed. No record.

**Read this first.** There is no check against observed scab: the thesis says accuracy against real infections cannot be evaluated, because no scab assessments were made (l. 1122), so the in-orchard station stands as the reference only by assumption. Rain caused 69 % of the larger category differences in Results (l. 919) but 65 % in Discussion (l. 1044); unchecked which is right. The LantMet comparison has no leaf wetness sensor behind it, only a proxy.

## What it holds

- **Design** (l. 689, 822, 835): ten commercial orchards in Scania, each with a physical station and two virtual stations (LantMet and Meteoblue). Primary infection periods of 2019 (130 predicted events) and 2020 (100 events).
- **Grid** (l. 130, 472, 958): the Swedish virtual weather station is on a 2.5 x 2.5 km grid; LantMet keeps only grid points with at least 37 % open ground. Each in-orchard station lies 0.4-4.1 km from its LantMet grid point. Distance against percentage of differing infections: r = 0.151, not significant (l. 960). The Swedish Board of Agriculture uses in-orchard stations at 35 locations for RIMpro (l. 451).
- **Agreement, RIM category** (Table 2; l. 825, 831, 835, 844, 845, 849): 2019, station against LantMet, the same category in 62 % of events, 33 % one apart, 5 % two apart, none more. 2019, station against Meteoblue, the same in 29 %, 52 % one apart, 13 % two, 3 % three, 3 % four. 2020, station against LantMet 53 % the same; station against Meteoblue 39 % the same (Delta 0-4: 39, 48, 11, 3, 0 %). LantMet and Meteoblue agreed in 37 % in 2019 (l. 829).
- **Counts** (Table 3; l. 898, 906): mean events per orchard per year differ by 0 to 1 between station and LantMet, and by 0 to 2.7 between station and Meteoblue. Example, 2019 Northeast: 12.0, 12.0 and 9.3 for station, LantMet and Meteoblue.
- **Causes** (l. 919, 922, 1044): of the 87 events where two sources differed by more than one category (eight of them station against LantMet, l. 915-917), rain caused 69 % (65 % in Discussion), mature spores and leaf wetness 15 % each; temperature caused none. Rain cut-offs differ: stations 0.2 mm, LantMet 0.1 mm, and RIMpro needs 0.2 mm for ascospore discharge (l. 1052).
- **Leaf wetness** (l. 680): LantMet has none; the trees are treated as wet when rain is above 0.0 mm or VPD below 2.5 hPa.
- **One virtual source, one rain record** (l. 1032): Meteoblue reported the same rain data at three Northeast orchards 12 km apart in 2020, so two rain events appeared at the three Meteoblue sites and at none of the physical or LantMet stations.
- **Abstract** (l. 99): virtual data predicted the number and severity of infections similar to physical stations, with more error for low-category infections.

## Dependence

- Computes the RIMpro apple scab model (Trapman 2013; RIMpro 2020), whose RIM value uses a revised Mills curve as cited (MacHardy & Gadoury 1989; Stensvand et al. 1997). Weather: LantMet (SLU, Fältforsk, Swedish Board of Agriculture), built on SMHI's MESAN analysis of AROME forecasts, and Meteoblue. Ehlert et al. (2019) is cited on leaf wetness sensors (l. 507-509). None recorded in the catalogue.

## Bearing (2026-10-21)

For Agrarium's D48 study: vineyard and orchard variability, and what one station or a gridded or virtual source misses.

- **Takeable:** a worked size of the loss when a disease model is driven by a gridded or virtual source instead of an in-orchard station: the infection category agrees in 62 % (2019) and 53 % (2020) of events with a 2.5 km grid source, and 29 % and 39 % with a virtual source, with rain as the main cause. It is a measured agreement of decision-relevant outputs, not of weather variables.
- **Takeable:** a grid point 0.4-4.1 km from the orchard showed no significant distance effect (r = 0.151), and a virtual source can return the same rain at orchards 12 km apart. These are cautions for any scoring of a "virtual station" arm.
- **Not shown:** agreement with observed disease (none), placement of stations, held-out sites, a random baseline, or a cost of wrong sprays. The kind of result is a comparison of sources on one model in one region over two seasons.
