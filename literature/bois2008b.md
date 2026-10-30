---
id: bois2008b
citation: Bois, B., Wald, L., Pieri, P., Van Leeuwen, C., Commagnac, L., Chery, P., Christen, M., Gaudillere, J.-P. & Saur, E. 2008. Estimating spatial and temporal variations in solar radiation within Bordeaux winegrowing region using remotely sensed data. Journal International des Sciences de la Vigne et du Vin 42(1):15-25
doi: 10.20870/oeno-one.2008.42.1.829
read: 2026-10-30, in full (HAL manuscript); Eq. 2 read in the page image; by a reading agent and note writer (claude-sonnet-5-5); 21 of 21 quotes found by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Bordeaux, Gironde]
processes: [solar radiation, satellite irradiation, HelioClim-1, kriging, terrain, slope and aspect, r.sun, diffuse fraction, clearness index, zoning]
records: []
datasets: []
files: [dr1030_bois2008b.pdf (from Chris's Pieri collection, the inbound folder: 2008-bois-10-20870-oeno-one-2008-42-1-829.pdf)]
---

# Bois et al. 2008: daily solar radiation maps of Bordeaux from satellite data, with terrain

HelioClim-1 daily irradiation (1986-2005) is kriged to 500 m, then put on the terrain at 50 m with the r.sun model, and used to zone Bordeaux by August-September irradiation.

**Read this first.** Satellite irradiation underestimates the one pyranometer it is checked against (Villenave d'Ornon) by 11 % on the year, with 20 % daily RMSD; the maps' absolute values are low, their spatial pattern is the result. The diffuse-fraction relation of Eq. 2 is "personal communication" (Pieri and Valancogne) with no data printed.

## What it holds

- **Data and method:** HelioClim-1 daily irradiation (Heliosat-2 on Meteosat ISCCP-B2) at 418 points about 20 km apart, 1986-2005 (l. 66-70, 181); RMS difference about 20 % of pyranometer values; Heliosat-2 has no slope or aspect. Ordinary kriging (R gstat, linear covariance models fitted by least squares) to a 500 m grid for the mean irradiation and the monthly clearness index KT = Gdh / Gd0 (Gd0 from astronomical formulae).
- **Terrain model:** r.sun (Hofierka & Suri 2002) in GRASS, beam, diffuse and reflected irradiation on slopes at 15 minute steps with mask effects, standard overcast method. Inputs: 50 m DEM (elevation, slope, aspect), ground albedo 0.2, daily horizontal irradiation, monthly Linke turbidity from SoDa, and the diffuse fraction kdh.
- **Diffuse fraction, Eq. 2-4 (page image):** with K = Gdh / Gd0, kdh = min(1.09 - 2.6896 K^2 + 1.2843 K^3, 1); kdh = 1 when K < 0.2; kbh = 1 - kdh. The relation is an empirical fit at Bordeaux (Pieri and Valancogne, personal communication). The printed form has no linear term.
- **Climate (l. 99-102):** annual rain 930 mm (1976-2005; 700 to 1300), annual mean temperature 13.8 C (22.3 C in August, 7.8 C in December). 57 AOC, 230 000 ha, 120 000 ha planted, between 44.3 and 45.5 N.
- **Climatology (Table 2):** mean daily irradiation 11.67 to 13.34 MJ per m2 over Gironde (mean KT 0.44) and 11.67 to 12.83 over the vineyards (KT 0.433); April-September KT 0.46 to 0.58; irradiation peaks June and July and stays below 10 MJ per m2 per day from October to February; Medoc KT is 4 to 8 % above the easternmost vineyards.
- **Check at Villenave d'Ornon, 2001-2005 (Table 5):** 50 m maps against the pyranometer: year mean 13.4 MJ per m2, bias -1.5 (-11.1 %), RMSD 2.7 (19.8 %), n 1826, daily errors -11.0 to +9.3. July: 22.2, -2.2 (-9.9 %), 3.7 (16.6 %). August-September: 17.5, -1.7 (-9.8 %), 2.9 (16.6 %). Worst relative bias: October -20.9 %, February -18 %.
- **Zoning:** on the mean August-September horizontal irradiation Gmat,h (15.36 to 16.81 MJ per m2, amplitude 8.9 % of the mean): low 66 % of the vineyard, medium 32 %, high 2 %. The terrain effect on the August-September ratio is nearly the same every year 2001-2005 (Fig. 5), so one 5-year ratio rescales 20 years. With terrain, the Entre-Deux-Mers low class falls from 93 % to 63 %, Cotes de Bourg varies -14 % to +13 % of its mean, and south slopes at Saint-Emilion get 1 to 10 % more.
- **Conclusion:** variability within the region comes mainly from terrain slope and aspect in the east; the authors expect south slopes to have higher evaporative demand (not tested).

## Dependence

- Uses HelioClim-1 / Heliosat-2 (Rigollier 2004; Lefevre 2007), r.sun (Hofierka & Suri 2002), SoDa Linke turbidity. Same HelioClim-1 data and first author as bois2008; same group as pieri2003.
- Kinship with Agrarium's own terrain and sun code (M1.1, `world/terrain.py`): both put a beam and diffuse split on a slope; Eq. 2 is a candidate diffuse-fraction check.

## Bearing (2026-10-30)

- **Terrain radiation check:** gives the size of the terrain effect on seasonal irradiation in a gently hilly French region: a slope and aspect change of seasonal radiation of the order of -14 % to +13 % within one appellation, and 1 to 10 % for south slopes against the local mean. These are realistic bounds for a terrain-strength setting.
- **Diffuse fraction:** a Bordeaux daily relation for kdh from KT to compare with the fraction Agrarium uses; it is valid only for daily values, and its source is unpublished.
- **Not shown:** hourly values, canopy interception, temperature or humidity.
