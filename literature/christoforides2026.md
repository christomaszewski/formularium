---
id: christoforides2026
citation: Christoforides, Elias, Chronopoulos, Kostas, Kamoutsis, Athanassios & Panagiotou, Ioulia. 2026. A Geospatial Model for Identifying High-Risk Locations for Downy Mildew (Plasmopara viticola) Infestation in Vineyards of Greece. Agriculture 16:511 (article number)
doi: 10.3390/agriculture16050511
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Greece]
processes: [oospore maturation, primary infection, incubation, interpolation]
records: [puelles2024.ur]
datasets: []
files: [10-3390-agriculture16050511.pdf]
---

# Christoforides et al. 2026: MeteoGrape, a geospatial downy mildew risk model

From the Agricultural University of Athens. Run for the 2024 season around Kavala, Greece, on one reference station and eight sensors.

## What it holds

- Spatial downy mildew risk model for Kavala, Greece, 85 km2, one reference station plus eight sensors (l. 19). It is run for 2024.
- Builds upon VitiMeteo (l. 196) and follows the structure of Puelles et al. 2024 (l. 254); most thresholds are transferred from Puelles (Table 4).
- Oospore maturation: degree-days above 8 deg C from 1 January until 140 deg C (l. 268).
- Germination: rain over 5.0 mm in 24-48 h, Tm above 8 deg C (l. 270). Dispersal: 2.0-3.0 mm/h 6 h later (l. 273). These two differ slightly from VitiMeteo's.
- Infection: degree-hours at RH > 90% reach 50 deg C (l. 289).
- Incubation: daily coefficient from 4 (5-6 deg C) to 25 (23-26 deg C), summed to 100 (Table 2, l. 298); source Bagis 2012.
- Not Magarey or Yin: wetness is an RH > 90% stand-in.
- Validation: one bulletin, 23 May 2024; model showed oil spots on 16 May (l. 538). No hit rates (l. 620).
- Germination and dispersal are marked locally calibrated, with no data shown (l. 340).

## Dependence

- **It computes the engine's Puelles et al. 2024 rules** (its phases B and C, l. 254; Table 4's sources), a borrowed equation, and shares four of the engine's forms: a 140 °C·day oospore sum, wet degree-hours, a daily incubation table and an RH > 90% wetness stand-in.
- By its own account the lineage runs Goidanich, VitiMeteo, Puelles, MeteoGrape (l. 588).
- No data fitted; two bulletins as a check.

## Bearing (2026-10-08)

- **Kin**, for borrowed equations and four shared forms (Agrarium's candidates). Its interpolation of a station to a sensor grid (regression plus radial basis functions) is a method a virtual-station operator could use.
