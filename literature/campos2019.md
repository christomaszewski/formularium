---
id: campos2019
citation: Campos, J., Llop, J., Gallart, M., García-Ruiz, F., Gras, A., Salcedo, R. & Gil, E. 2019. Development of canopy vigour maps using UAV for site-specific management during vineyard spraying process. Precision Agriculture 20:1136-1156 (volume and pages from campos2021's reference 17; the held copy is the authors' manuscript)
doi: 10.1007/s11119-019-09643-z
read: 2026-10-20, in full (the authors' accepted manuscript), by a reading agent (claude-haiku-5-5); 47 of 47 quotes found at their lines by scripts/verify_quotes.py; Tables 2-3 checked in the text by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Penedès, El Plà del Penedès, Catalonia]
processes: [canopy height, canopy width, leaf wall area, tree row volume, NDVI, variable-rate spraying]
records: []
datasets: []
files: [campos2019.pdf]
---

# Campos et al. 2019: canopy size by stage in a Penedès Cabernet Sauvignon vineyard

UAV NDVI maps turned into three vigour zones to set spray volume, checked against manual
canopy measurements. Read for the canopy dimensions of a vineyard with Agrarium's 2.8 m
rows.

## What it holds

- **Site** (l. 263-269): about 5 ha of Cabernet Sauvignon at El Plà del Penedès, DO
  Penedès; rows 2.8 m, vines 1.2 m, 2,976 vines/ha; double Royat cordon on two wires.
  The year, rootstock, irrigation and soil management are not printed.
- **Sampling** (l. 300-306): 69 random points, each 1 m of row: canopy height and width
  by hand, tree row volume (TRV, m³ of canopy/ha) and leaf wall area (LWA, m² of canopy
  wall/ha, both sides).
- **Canopy by stage** (Table 2, l. 562-564): BBCH 61 (start of flowering) height 0.32 m,
  width 0.29 m, TRV 334 m³/ha, LWA 2,289 m²/ha; BBCH 75 (pea size) 1.02 m, 0.72 m, 2,583
  and 7,185; BBCH 81 (start of ripening) 0.91 m, 0.49 m, 1,580 and 6,471. The fall after
  pea size is printed, not explained (trimming is a likely reason, not stated).
- **Vigour zones** (Table 3, l. 595-597; stage not printed): low 0.84 m high and 0.51 m
  wide, LWA 6,031; medium 0.95 and 0.46, 6,786; high 1.03 and 0.57, 7,388. The zones
  cover 21.5, 63.9 and 14.6 % of 5.05 ha (l. 653).
- **Spray:** 150 (Table 1: 154), 205 and 260 L/ha for the three zones (l. 450, 472).
- **Not printed:** leaf area per vine, LAI, shoots, leaf density, porosity, dates.

## Dependence

- LWA and TRV are geometric (EPPO definitions); the regressions on NDVI are fitted to the
  paper's own points. Spray volumes from DOSAVIÑA (Gil et al.). No model shaped the data.

## Bearing (2026-10-20)

- **Canopy shape for the viewer at 2.8 m rows in Penedès:** a wall about 1.0 m high and
  0.5 to 0.7 m wide from pea size, 0.3 m high at the start of flowering. No leaf area, so
  it sets the drawing, not `host.leaf_area_max_m2`.
