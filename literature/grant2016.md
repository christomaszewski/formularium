---
id: grant2016
citation: Grant, E. R., Ross, A. N. & Gardiner, B. A. 2016. Modelling canopy flows over complex terrain. Boundary-Layer Meteorology 161:417-437
doi: 10.1007/s10546-016-0176-3
read: 2026-10-18, targeted (abstract, sections 2, 4, 5 and 6, and a search of the whole text for numbers and correction factors), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py; an author manuscript from White Rose (accepted version, draft dated 31 July 2015); figures not viewed
status: read
diseases: []
crops: []
regions: [Scotland, Isle of Arran]
processes: [canopy flow, complex terrain, flow separation, lee slope, wind, canopy drag]
records: []
datasets: []
files: [r_10_1007_s10546_016_0176_3.pdf (the 2026-10-18 drop, second pass)]
---

# Grant, Ross & Gardiner 2016: a canopy flow model over a forested ridge

A three-dimensional mixing-length model with an explicit canopy (BLASIUS) run over a forested ridge on Arran, against 12 weather stations and three towers. No record: a flow model for a 15 m forest, not a formulation of a crop or disease.

## What it holds

- **Observations** (l. 259-269): 12 automatic stations (cup anemometers and vanes at 2 m) and three towers of 15 to 23 m with four sonic anemometers each, on the Leac Gharbh ridge, spring 2007; 15-minute averages. The north-easterly subset is about 15 hours (l. 937). Cup anemometers stall at about 0.7 m/s and read low in canopy flow (l. 919, 1470).
- **Model** (l. 289, 352, 384-388, 459-469): neutral flow only, geostrophic wind 10 m/s (20 m/s for the south-westerly run, l. 1174); closure Gamma0 = 0.357; domain 6 km by 6 km, 120 x 120 points, 50 m horizontal grid; 5 km high, 80 levels from 0.5 m at the surface to about 180 m; canopy 15 m, uniform leaf-area density 0.5 m2 m-3, drag coefficient 0.25 (from field measurements near the site), roughness length 0.05 m on open land and the forest floor.
- **Comparison** (Table 1, l. 1443-1455): reference wind speed, observed median (interquartile) against model: north-easterly, tower T3, 4.3 m/s (2.8 to 5.9) against 5.4 m/s; south-westerly, tower T1, 10.0 m/s (7.9 to 12.5) against 3.7 m/s. The south-westerly gap is not explained in the parts read. Tower T2 is overpredicted in north-easterly cases; T1 and T3 agree reasonably (l. 1482). No error figure is printed.
- **Separation** (l. 1789-1867): in the easterly case flow separates on the forested lee slope and needs the canopy; in the westerly case it separates on the steep eastern lee slope even without a canopy (l. 1850). With a roughness-length treatment there is no separation in the easterly case (l. 1857), and it is moved further down the lee slope inside the canopy (l. 1867); the paper concludes the canopy must be explicit for near-surface flow.
- **Forest edge** (l. 2003-2033): adjustment length Lc = 1/(Cd a) = 4 m, adjustment over about 24 m, half the grid spacing; the largest mismatch is at forest edges and agreement is much better away from them.
- **Not printed in the parts read:** RMSE or bias of wind, wetness, humidity, the momentum equations, a simple correction factor or parametrisation, data access. Terrain and land cover are Ordnance Survey 50 m via EDINA (l. 382-384).

## Dependence

- BLASIUS (Wood & Mason 1993); the closure is Ross & Vosper 2005's, with canopy dissipation after Wilson et al. 1998; canopy height and drag come from Grant et al. 2015's field data. No tool's list shares a formulation with it.

## Bearing (2026-10-18)

Strand 3 (terrain and canopy physics).

- **Nothing takeable as a factor:** the paper offers no correction for wind in a sweep; its message is that a roughness-length treatment misses lee-slope separation where a canopy sits on a lee slope, and the explicit canopy is needed.
- **Mismatch with the vineyard:** a 15 m forest on a ridge, near-neutral flow at 50 m grid spacing; a vine row is under 2 m and well below the grid. At best it says where lee-side flow separation can be expected, not what temperature or wetness there is.
- **Wetness:** none; no comparison with the engine's RH >= 90 % stand-in.
- **Kind of result:** a model run against a few hours of field data, with a large unexplained gap in one case (3.7 against 10.0 m/s).
