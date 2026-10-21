---
id: gilmoya2019
citation: Gil, E., Campos, J., Ortega, P., Llop, J., Gras, A., Armengol, E., Salcedo, R. & Gallart, M. 2019. DOSAVIÑA: Tool to calculate the optimal volume rate and pesticide amount in vineyard spray applications based on a modified leaf wall area method. Computers and Electronics in Agriculture 160:117-130 (journal from OpenAlex and the DOI, snippet; volume and pages not checked; the held copy is the authors' manuscript)
doi: 10.1016/j.compag.2019.03.018
read: 2026-10-20, in full (the authors' manuscript from UPCommons), by a reading agent (claude-haiku-5-5) with Eqs 1-2, Figure 1 and Tables 1-3 and 6 in the page images; 36 of 36 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Torrelavit, Penedès, Catalonia]
processes: [leaf wall area, leaf density, spray volume, decision support]
records: []
datasets: []
files: [gilmoya2019.pdf]
---

# Gil et al. 2019: DOSAVIÑA, spray volume from leaf wall area

A spray-volume tool built on the EPPO leaf wall area (LWA) method, with factors for leaf
density and canopy width, tested on four Penedès parcels in 2018. Read for canopy data.

## What it holds

- **LWA** (Eq. 1, l. 176): 2 × 10⁴ × canopy height / row distance, m² a hectare; geometric,
  not leaf area. Unit rate 0.037 L per m² LWA (l. 176-179).
- **Leaf density against canopy height** (Figure 1, l. 923, page image): y = 2.7341 x +
  0.4909, R² 0.6515; the data are cited to Da Silva et al. 2002 (l. 240).
- **Density classes** (Table 1, l. 1013-1016): leaf density 0.083, 0.125, 0.143, 0.196 at
  canopy heights 0.719, 0.833, 0.881 and 1.038 m. The unit is m²/m² in the table and m²/m³
  in the text (l. 241); neither fits Figure 1's line (2.7341 × 0.88 + 0.49 = 2.9): unsettled.
- **Width classes** (Table 2, l. 1029-1031): 0.45, 0.70 and 0.82 m, heights 0.65, 1.01, 1.17 m.
- **Parcels** (Table 6, l. 1118-1125): Merlot, Chardonnay and two Cabernet Sauvignon at
  Torrelavit, double Royat, rows 2.20 m (the Figure 7 caption says Jean Leon winery,
  Vilafranca del Penedès). Their canopy sizes are not printed.
- **Not printed:** LAI, leaf area, measured canopy size per parcel.

## Dependence

- EPPO LWA dose method; Gil et al. 2011's unit rate; class factors from the authors'
  unpublished field database. `campos2020` applies its rates. No model shaped canopy data.

## Bearing (2026-10-20)

- **No leaf area;** the class tables say a Penedès VSP wall is about 0.7 to 1.0 m tall and
  0.45 to 0.8 m wide, the authors' assigned classes, not measurements.
