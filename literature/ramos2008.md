---
id: ramos2008
citation: Ramos, M. C., Jones, G. V. & Martínez-Casasnovas, J. A. 2008. Structure and trends in climate parameters affecting winegrape production in northeast Spain. Climate Research 38:1-15
doi: 10.3354/cr00759
read: 2026-10-22, lightly: the phenology, yield and variety passages (the climate-trend sections were not read line by line), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, Catalonia, Alt Penedès, Priorat, Segrià]
processes: [phenology, climate trends, yield, veraison]
records: []
datasets: []
files: [2008-ramos-10-3354-cr00759.pdf]
---

# Ramos, Jones & Martínez-Casasnovas 2008: climate trends at three Catalan stations, with a short Penedès phenology series

A climate analysis for the Alt Penedès, Priorat and Segrià (1952 to 2006) that tests relations to vine and wine data; the Penedès growers' phenology it uses is not tabulated.

**Read this first.** The paper prints no Penedès budbreak dates. Its "Stage I: budbreak to bloom" is a fixed climate window set by the authors (a definition), not an observed interval. No disease appears in it.

## What it holds

- **Climate:** three stations, Vilafranca del Penedès (1952 to 2006), Cabacès (1967 to 2005) and Lleida (l. 19, 332); growing-season warming of 1.0 to 2.2 °C (l. 23); Vilafranca's growing-season mean temperature 18.8 °C (l. 316).
- **Phenology source:** Penedès bud break, bloom, véraison and harvest dates for 1996 to 2007 "from numerous growers", for Macabeo, Xarello, Parellada, Chardonnay and Pinot Noir (l. 317-319); in the discussion, "limited data from 1996-2007 provided by 5 producers" (l. 846). Only véraison and harvest regressions are printed; the yearly budbreak and bloom dates are not.
- **Stage I definition:** budbreak to bloom is 1 April to 10 May in the paper's stage table (l. 238). It is a window for averaging rain, not a measured interval.
- **Cited, not measured here:** phenology responds 3 to 6 d per 1 °C of warming in Europe, with a weaker response for early-season events such as bud break (Jones et al. 2005b; l. 841).
- **Own regression:** Parellada véraison, Penedès 1996 to 2006, earlier by 4.1 d per 1 °C of warmer growing-season minimum temperature, R2 0.55 (l. 654-657).
- **Yield:** Penedès production 1994 to 2006 fell with heat: 915 (Macabeo, R2 0.40), 1,420 (Parellada, R2 0.50) and 729 (Xarello, R2 0.36) kg ha-1 per 100 Winkler units (l. 692-694); not significant for Chardonnay, "not shown" (l. 695-697). The yield level itself is not printed.

## Dependence

None recorded beyond the paper's own climate analysis; the growers' phenology is the authors' own collection and is not published in the paper. Shares its first author with `ramos2017` (a flag, not a dependency).

## Bearing (2026-10-22)

- **host.budburst_doy, host.budburst_sd_days:** no value. The yearly Penedès budbreak dates are not printed, so neither a mean nor a spread comes from this paper. The 3 to 6 d per °C figure is a cited temperature response, weaker for budbreak, not a between-season spread.
- **host.flowering_after_budburst_days, host.inflorescence_after_budburst_days:** no value. The 1 April to 10 May "Stage I" is the authors' averaging window; it must not be read as an observed budbreak-to-bloom interval.
- **host.bunches_per_vine:** nothing; yields are given only as slopes per Winkler unit, with no level and no bunch count.
- **Cultivar susceptibility:** none, as no disease is studied. The yield-against-heat slopes for Macabeo, Parellada and Xarello (and none for Chardonnay) are a heat response of production, not a susceptibility.
