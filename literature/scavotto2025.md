---
id: scavotto2025
citation: "Scavotto, N., Siegert, C.M., Alexander, H.D. & Varner, J.M. 2025. Leaf water storage capacity among eight US hardwood tree species: differences in seasonality and methodology. Hydrology 12:40"
doi: 10.3390/hydrology12020040
read: "2026-10-25, lightly: the abstract, the methods and the results (leaf water storage numbers; the discussion not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [oak and other hardwood trees (not a crop)]
regions: [United States, Mississippi]
processes: [canopy storage capacity, leaf water storage, rain interception, rainfall simulator, water displacement, seasonality]
records: []
datasets: []
files: [dr1025_scavotto2025.pdf (the 2026-10-25 drop)]
---

# Scavotto et al. 2025: eight Mississippi hardwoods held about 0.07 to 0.32 mm of water per unit leaf area by displacement, and up to 0.77 mm under a rainfall simulator (not vines)

Single-leaf water storage of three oaks and five other hardwoods, by submersion and by a heavy rainfall simulator, early and late in the season.

**Read this first.** ANALOGUE: broadleaf forest trees, not a vine, and a flat single leaf, not a canopy; a bound on what a broad leaf holds. The units are inconsistent in print: Eq. 2 and the figure captions say mL per cm2 (l. 220-221), the results text says mL/m2. The text figures are used here as mL/m2 (1 mL/m2 = 0.001 mm of water; arithmetic, not printed), since 72.5 mL per cm2 would be 725 mm of water on a leaf, which cannot be right (arithmetic, not printed). It is not stated whether the leaf area is one-sided; an area meter measured each fresh leaf (l. 166-167). The rainfall-simulator numbers below were found in the text by the note writer, not among the JSON quotes; the reading JSON listed 322 mL/m2 as the highest value, which only holds for the displacement method.

## What it holds

- **Setting:** eight species in northern Mississippi (white, southern red and post oak; red maple, winged elm, mockernut hickory, sweetgum, black gum), three leaves per species from the overstory and midstory, early growing season (June) and late (October) (l. 150-165).
- **Water displacement, calm (l. 238-247):** overstory early season, white and southern red oak 72.5 +/- 5.9 mL/m2 against 145.0 +/- 6.4 for the other three (0.07 and 0.145 mm, arithmetic); late season 80.6 +/- 24.4 against 194.2 +/- 46.6 (post oak); midstory winged elm early season 321.9 +/- 58.9 against 93.3 +/- 9.7 for the others (0.32 and 0.09 mm). The lowest calm value quoted is 66.9 +/- 3.9 mL/m2 (white oak, early; l. 244). Simulated windy displacement was generally lower early in the season but not late (l. 259-262).
- **Rainfall simulator, "prolonged wetting" (l. 337-345):** overstory early season sweetgum 502.5 +/- 102.0 against 157.2 +/- 16.5 mL/m2 for the others; late season 135.7 +/- 6.4 (post oak) against 101.8 +/- 6.2; midstory early season winged elm 772.1 +/- 127.0 against 183.3 +/- 24.8; late season sweetgum 151.4 +/- 42.7 against 75.8 +/- 6.5. In mm (arithmetic, not printed), typical values are 0.08 to 0.18 mm, with two outliers at 0.50 and 0.77 mm.
- **Simulator against displacement:** the abstract says simulator storage was up to two times that of displacement, particularly early in the season (l. 35).
- **Simulator:** a hose nozzle 1.5 m above the leaf, intensity 0.029 +/- 0.001 cm per s (l. 200-201), about 1,000 mm per hour (arithmetic, not printed), so the capacities are for very heavy, fully wetting rain.
- **Season and layer:** the ranking of species changed between early and late season and between methods (abstract; l. 244-257). Most species held more water late in the season in calm displacement (l. 250-258), but more early in the season in the simulator (l. 347-352).

## Dependence

- Own measurements; method after earlier leaf-storage work (Holder 2012 and others, per the reading JSON). Eastern US hardwoods; no vine.

## Bearing (2026-10-25)

- **micro.storage_mm_per_lai (0.25, range 0.1 to 0.5) and the SWEB store (0.2 mm per unit leaf area):** per unit leaf area, a hardwood leaf holds 0.07 to 0.32 mm by displacement and mostly 0.08 to 0.18 mm in the simulator, up to 0.77 mm for two species. The registry's 0.25 and the SWEB 0.2 sit inside this spread, and the registry range 0.1 to 0.5 covers nearly all the typical values. This does not show the value for a vine leaf, which is not measured here, and a canopy of overlapping leaves is not a sum of single leaves.
- **micro.interception, micro.wet_threshold_mm, drying parameters:** not addressed. A single leaf's storage is not a canopy catch rate.
- **Kind of result:** ANALOGUE measurement (single leaves of non-vine trees, two methods, two dates, one site); useful as a bound on the order of magnitude of a leaf's water store.
