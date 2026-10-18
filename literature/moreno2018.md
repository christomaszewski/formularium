---
id: moreno2018
citation: Moreno, H. A., Ogden, F. L. & Alvarez, L. V. 2018. Unstructured-Mesh Terrain Analysis and Incident Solar Radiation for Continuous Hydrologic Modeling in Mountain Watersheds. Water 10(4):398
doi: 10.3390/w10040398
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [upper Green River basin, Wyoming]
processes: [terrain analysis, slope and aspect, sky view fraction, cast shadows, incident solar radiation, remote albedo]
records: []
datasets: []
files: [h__2018.pdf (the 2026-10-18 drop)]
---

# Moreno et al. 2018: incident solar radiation on triangular terrain meshes

A vector method on triangular irregular network (TIN) meshes for slope, aspect, self-shading, cast shadows, sky view fraction and remote albedo, giving total incoming solar radiation (l. 19-31). No record.

## What it holds

- **Method:** a normal vector per element gives slope and aspect; spherical trigonometry gives the sun vector each hour; sky view is computed at prescribed azimuth steps (l. 24-28); shading by comparing sun zenith with the steepest gradient (l. 28-30).
- **Test:** sensitivity of radiative components to seasonal atmospheric transmissivity and surrounding albedo in a Wyoming watershed (l. 31-33, 115-116).
- **Use:** terrain features can be pre-computed and stored for later time-stepping runs (l. 34-36). No error statistics against observations were located.

## Dependence

- Builds on TIN terrain meshes and remote-albedo from sky-view fractions.

## Bearing (2026-10-18)

- **Strand s3:** a pre-computable way to get slope, aspect, shading and sky view for each terrain element. A simulator could take the pre-computation idea for a vineyard slope; it is a method with sensitivity runs, not a validated tool.
- Triage-grade: not read in full.
