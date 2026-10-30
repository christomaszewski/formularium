---
id: brisson2010
citation: Brisson, N. & Levrault, F. (eds) 2010. Changement climatique, agriculture et forêt en France: simulations d'impacts sur les principales espèces. Le Livre Vert du projet CLIMATOR 2007-2010. ADEME, Angers, 336 p.
doi: 
read: 2026-10-30, a 338-page book; the vine chapter (book p. 213-222), the health chapter (p. 113-126), the model table (p. 41-43) and the timing chapter's vine figures (p. 35, 69-70) only; by a reading agent and note writer (claude-sonnet-5-5); 28 of 28 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [Botrytis]
crops: [grapevine, wheat]
regions: [France]
processes: [climate change, phenology, water balance, leaf wetness, Botrytis, fungicide sprays, downscaling]
records: []
datasets: []
files: [dr1030_brisson2010.pdf (from Chris's Pieri collection, library/inbound/pieri-2026-10-27/2010-brisson-url-pieri-climator-book.pdf)]
---

# Brisson and Levrault (eds) 2010: the CLIMATOR green book, French edition

The French project that ran crop and disease models for 12 sites under one climate scenario to 2100. Pieri wrote the vine chapter (with Lebon's runs) and part of the health chapter.

**Read this first.** No downy mildew model was run: the only vine disease is Botrytis (BOTRYTIS, Fermaud, Pieri, Mimiague 2003, daily step; l. 1871), on merlot. A grep for "mildew" and "mildiou" finds no hit in the book text. Wetness comes from HUMECTATION, a model of a wheat-type leaf (l. 1908), not a vine canopy. The English edition of the health chapter is gouache2011; a two-page summary is gouache2010.

## What it holds

- **Vine protocol (book p. 214, l. 10033-10047):** 12 French sites, rainfed or irrigated (30 % of needs), densities 0.3 and 0.9 plants m-2, three soils (available water 226, 73 and 150 mm; the proceedings print 193 mm for soil 1, gouache2010), three cultivars (Chardonnay, Merlot, Grenache). Models BHV, STICS-Vigne, BOTRYTIS. Climate ARPEGE, SRES A1B, regionalisation TT, QQ, ANO; periods 1970-99, 2020-49, 2070-99.
- **Models (table, p. 41-43):** BHV is daily and cites Pieri and Gaudillère 2003 (l. 1867, held as pieri2003); it draws the foliage as architectural leaf layers and computes interception by radiation balance (table 3, l. 1958-1961). HUMECTATION is hourly (Lhomme and Jimenez 1992); BOTRYTIS, SEPTORIOSE and CERES-ROUILLE give damage and sprays (l. 1909).
- **Phenology:** vine base temperature 10 C (l. 2923). BHV harvest is a degree-day sum, base 10 C, from flowering; STICS uses berry sugar (l. 3130). Flowering advances 8.6 days per degree of annual warming with BHV (l. 3155). Harvest advance over all sites: vine -19.1 days (2020-49) and -32.2 days (2070-99); Bordeaux -12.6 and -25.4; Avignon -12.9 and -22.9 (Table 1, l. 3035-3047).
- **Botrytis (p. 117-121):** risk days follow rain from veraison to maturity, slope about 0.2 risk days per mm (l. 5444); simulated sprays near the current 0 to 2 (l. 5628); fewer at Bordeaux, many at newly feasible sites (feasibility above 80 %, l. 5423); low to moderate risk at the new Centre-North sites (l. 12194).
- **Vine chapter results (p. 216-222):** the whole cycle is 20 to 40 days earlier at current vine sites (proceedings, gouache2010); ripening temperature rises by at least 5 C at traditional sites by 2100 (l. 10426); water comfort ETR/ETM falls clearly only at Toulouse and Saint-Étienne (l. 10201) and follows annual P - ET0 below -200 mm (l. 10217); irrigation need is computed to hold ETR/ETM at 0.3 or more (l. 10369). The quality index QUAL is the mean minimum temperature from veraison to maturity (l. 10257).

## Dependence

- Wetness is an own hourly micrometeorological model after Lhomme and Jimenez 1992 (not held); Botrytis is Fermaud et al. 2003 (not held, IOBC bulletin). Neither shares an equation with the engine's downy mildew models. Authors: Pieri, Fermaud and Lebon appear in other held notes (a flag, not a dependency).
- BHV rests on pieri2003 (radiation) and on Lebon et al. 2003 (water; cited in gowdy2022).

## Bearing (2026-10-30)

- **For the truth's disease:** nothing. CLIMATOR ran Botrytis, not Plasmopara; its figures cannot score or calibrate a downy mildew model. It does show the scale of climate effects on a wetness-driven risk: fewer wet hours (8.19 to 7.84 h in spring, gouache2010) but more wet degree-days.
- **For the vine and weather side:** a documented set of French site climates for 1970-2099 and a degree-day harvest model with base 10 C. Figures are plots; the numbers in text and Table 1 are all that is held.
- **Not shown:** any microclimate, canopy temperature or leaf wetness measured in a vineyard.
