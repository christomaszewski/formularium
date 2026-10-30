---
id: pieri2016
citation: Pieri, P., Zott, K., Gomes, E. & Hilbert, G. 2016. Nested effects of berry half, berry and bunch microclimate on biochemical composition in grape. OENO One 50(3):23-41
doi: 10.20870/oeno-one.2016.50.3.52
read: 2026-10-30, methods, results of modelling and the flavonol and anthocyanin response in full (HAL author manuscript, scanned, read by OCR; Fig. 1 read in the page image); composition tables and PCA not read in detail; by a reading agent and note writer (claude-sonnet-5-5); 14 of 14 quotes found by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Bordeaux, Saint-Émilion]
processes: [berry temperature, bunch microclimate, intercepted radiation, bunch azimuth, leaf removal, flavonols, anthocyanins, energy balance]
records: []
datasets: []
files: [dr1030_pieri2016.pdf (from Chris's Pieri collection, the inbound folder: 2016-pieri-10-20870-oeno-one-2016-50-3-52.pdf)]
---

# Pieri et al. 2016: modelled radiation and temperature of single berries, and flavonols and anthocyanins in skin

Two Merlot vineyards (N-S and E-W rows) with bunches defoliated on one side; radiation and temperature at the berry are modelled for 30 days before harvest and linked to HPLC composition at berry and half-berry scale.

**Read this first.** The radiation and temperature at the berry are model outputs, not measurements; the model equations are not printed (they are in Cola et al. 2009 and Pieri 2010, not held), and no model validation against a berry thermometer is reported. The bunches were artificially defoliated on one side, so the numbers apply to exposed bunches, not to the normal fruit zone. 5 bunches per category, one year.

## What it holds

- **Sites (l. 143-152):** Chateau Figeac (E-W rows) and Chateau Cheval Blanc (N-S rows), Saint-Émilion; 15-year-old Merlot on sandy gravelly soil, 4525 vines per ha, 1.70 x 1.10 m, VSP cane pruned at 8 buds, foliage 1.40 m high and 0.50 m wide. One-sided LAI on 2 August 2004: 1.54 (sd 0.32) N-S, 1.66 (sd 0.41) E-W, from 12 vines each and a calibrated leaf area from main vein length.
- **Treatment:** leaf removal around single bunches (radius about 30 cm, one side only: N, S, E or W) on 19 August 2004 after 100 % veraison (50 % on 14 August); harvest 30 September; 5 replicate bunches per azimuth; exposed (X) and opposite (O) berries sampled, and for south bunches also outer and inner berry halves.
- **Model (l. 207-229):** porous rectangular hedgerow after Smart & Sinclair 1976, Cola et al. 2009 and Pieri 2010 for intercepted radiation, with row azimuth, canopy structure, bunch position and soil albedo set per site. Berry temperature: a simplified Cola et al. 2009 energy balance with convection terms averaged (no wind measured). Run for the 30 days up to the day before sampling and averaged. Inputs: air temperature and global radiation from a station less than 1 km away (Cheval Blanc).
- **Modelled day (Fig. 1, page image, clear day):** global radiation peaks about 740 W per m2; exposed (X) berries intercept up to about 700 W per m2 (south berries around noon; east in the morning, west in the afternoon), opposite (O) berries mostly under 200 W per m2. Berry temperature of exposed S and W berries peaks near 38 to 40 C (about 15 h) against air near 30 C; O berries stay within a few C of air.
- **Berry minus air (text, l. 337):** exposed berries up to 10 C above bunch-zone air on clear days and 5 C on average over the period; less for opposite berries (gap and leaf reflection).
- **Composition:** sugar and acids similar across categories (sugar/acid ratio about 30), so the differences in flavonols and anthocyanins are read as microclimate. Total flavonols rise linearly with intercepted radiation, about 0.31 ug per g dry skin per MJ per m2 per day (units as printed); anthocyanins rise with radiation and fall with berry temperature, bilinear fit r2 = 0.67 (l. 754-765). Effects are stronger at berry scale than at bunch scale. Radiation and temperature were not separable by azimuth alone (E and W bunches differ in temperature at the same radiation, not enough to decouple them).

## Dependence

- Radiation geometry from the Smart & Sinclair and Riou lineage (riou1989, riou1994 are held or read); berry energy balance from Cola et al. 2009 (not held); same group as pieri2003 and Gaudillere. Shares first author with pieri2003 and riou1994.

## Bearing (2026-10-30)

- **Berry temperature:** gives the size of the berry-over-air excess for a sunlit, defoliated berry: up to 10 C, 5 C on average, peaks of 38 to 40 C on a clear day with air at 30 C. For Agrarium's berry temperature (and for heat damage thresholds) these are upper-end values for exposed fruit; a normal canopy-shaded bunch will sit much closer to air temperature (inferred, not measured here).
- **Not shown:** model equations, a validation against measured berry temperature, wind or humidity in the bunch zone.
