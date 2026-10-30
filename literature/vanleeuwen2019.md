---
id: vanleeuwen2019
citation: van Leeuwen, C., Pieri, P., Gowdy, M., Ollat, N. & Roby, J.-P. 2019. Reduced density is an environmental friendly and cost effective solution to increase resilience to drought in vineyards in a context of climate change. OENO One 53(2):129-146
doi: 10.20870/oeno-one.2019.53.2.2420
read: 2026-10-30, in full; Eq. 1 read in the page image (p. 98); Tables 2a-2c (cost tables) and Figures 1-6 not used; by a reading agent and note writer (claude-sonnet-5-5); 32 of 32 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Bordeaux, Avignon]
processes: [water balance, fraction of transpirable soil water, planting density, row spacing, canopy geometry, yield, production cost, climate change]
records: []
datasets: []
files: [dr1030_vanleeuwen2019.pdf (from Chris's Pieri collection, library/inbound/pieri-2026-10-27/2019-leeuwen-10-20870-oeno-one-2019-53-2-2420.pdf)]
---

# van Leeuwen, Pieri, Gowdy, Ollat and Roby 2019: wide rows and the vine water balance, Bordeaux and Avignon, now and 2041-2070

A water balance (Lebon et al. 2003) run on conceptual vineyards with three row spacings and three soils for two sites and two climates; yield and cost are layered on top. It is a modelling study with no measurements of its own.

**Read this first.** The water balance model itself is not printed (only its reference). The canopy dimensions are assumptions of the conceptual vineyard. Eq. 1 prints its exponent as "e-000116x" with the decimal point lost; read in the page image as e^(-.000116 x), and Table 1 reproduces from it (arithmetic, not printed: 9000 x 0.667 x e^(+0.1934) = 7280 at 3333 vines/ha).

## What it holds

- **Vineyard (l. 272-290):** vine spacing 1.0 m; rows 2.0, 3.0, 4.0 m (5000, 3333, 2500 vines/ha); trunk 0.7 m, row (trellis) height 2.0 m, canopy height 1.3 m, canopy width 0.45 m; porosity 15 % at 2.0 m rows and 10 % at 3 and 4 m; soil albedo 0.18, consistent with Pieri and Gaudillère 2003 (pieri2003). Dry-farmed. Soils: total transpirable soil water TTSW 100, 200, 300 mm.
- **Phenology (l. 233, 241, 290, 351-356):** budbreak at 90 GDD (base 10 C from day 1; de Cortázar-Atauri 2009); flowering and veraison by GFV (Parker 2013); harvest = veraison + 40 days. Recent past (1981-2010), Avignon grenache: budbreak DOY 102, flowering 153, veraison 218, harvest 258; Bordeaux Cabernet-Sauvignon: DOY 98, 157, 223, 263 (l. 356; the last two on the next lines). Near future 2041-2070: dates 13 days earlier (l. 474).
- **Climate (l. 251, 264):** measured Grande Ferrade (Bordeaux) and INRA Avignon stations 1981-2010; 2041-2070 from Pieri et al. 2010 (CLIMATOR), a scenario close to RCP 6.0.
- **Water status:** FTSW, no deficit between 1.0 and 0.4 (Lebon 2003; l. 251). FTSW around flowering 0.93 to 0.46 (l. 376); in the 30 days before harvest 0.54 to 0.02 (l. 367). Bordeaux, TTSW 300 mm: pre-harvest FTSW 0.31 at 2 m rows to 0.54 at 4 m (l. 374). ANOVA of pre-harvest FTSW: site 46.4 %, soil 24.1 %, density 9.6 %, period 8.2 % of variance (Table 3, l. 545).
- **Yield and leaf area (l. 273-282, 332, 428-430):** Eq. 1 y = 7.50 e^(-0.000116 x), kg per vine, x vines/ha, from Hunter 1998b; unstressed 9000 kg/ha at 5000 vines/ha; yield falls linearly from FTSW 0.4 to 0, to 50 % at FTSW 0. Table 1: exposed leaf area 12963, 9149, 6863 m2/ha and yield 9000, 7280, 6014 kg/ha at 5000, 3333, 2500 vines/ha (leaf area after Murisier 1996). Lowest leaf area per fruit weight 1.14 m2/kg (l. 402).
- **Cost:** 7,046, 4,572 and 3,608 EUR/ha at the three densities (l. 410; the tables are scrambled).
- **Background cited (l. 201):** in a dry-farmed Cape vineyard, closely spaced vines had higher LAI but less dense canopies and a better microclimate (Archer and Strauss, second hand).

## Dependence

- Lebon et al. 2003 (water balance, cited by gowdy2022) and Hunter 1998b (yield and density) are not held. Phenology models are held as parker2013. Authors Pieri and Gowdy are shared with pieri2003, gowdy2022 and vanleeuwen2023.

## Bearing (2026-10-30)

- **For Agrarium's vine and water side:** a printed set of canopy dimensions and soil water classes for a VSP vineyard (canopy 1.3 m by 0.45 m, porosity 10 to 15 %, TTSW 100 to 300 mm) and the FTSW thresholds 0.4 and 0 with yield loss to 50 %. All are modelled, not measured.
- **Not shown:** measured canopy microclimate, leaf wetness or disease; the water balance equations; any validation of FTSW against vine water potential.
