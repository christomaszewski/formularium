---
id: helbig2009
citation: Helbig, N., Loewe, H. & Lehning, M. 2009. Radiosity approach for the shortwave surface radiation balance in complex terrain. Journal of the Atmospheric Sciences 66:2900-2912 (end page not read)
doi: 10.1175/2009JAS2940.1
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [Davos, Switzerland (one real-topography check)]
processes: [terrain reflection, shortwave radiation, sky view factor, effective albedo]
records: []
datasets: []
files: [nora_2009.pdf (the 2026-10-18 drop)]
---

# Helbig et al. 2009: radiosity for shortwave radiation in complex terrain

A radiosity equation for anisotropic terrain reflection, solved by progressive refinement (l. 19-22) on Gaussian random-field topographies (l. 22-26). No vineyard and no field measurement.

## What it holds

- **Method:** topography described by a variance and a correlation length (l. 23-25); grid resolution and finite domain size are treated explicitly (l. 25-27, 533-547).
- **Comparison:** against an isotropic sky-view-factor parameterisation, mean reflected radiation is similar while spatial distributions differ (l. 27-28).
- **Real terrain:** reflected radiation in real topography is reasonably well described by the Gaussian approximation (l. 28-29); the example uses the Weissfluhjoch area, mean slope 25 deg (l. 469-471).
- **Albedo:** the effective albedo varies with sun elevation, with differences up to 0.025 (l. 30-31).

## Dependence

- Radiosity from computer graphics (Cohen and Wallace 1993, l. 263); Gaussian random fields; sky view factor as the simple baseline.

## Bearing (2026-10-18)

- **s3 terrain and canopy physics:** a way to add reflected terrain radiation beyond a sky-view factor; the size of the effect (mean similar) suggests it matters little for mean values. Not read in full.
