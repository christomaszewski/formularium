---
id: mubarak2017
citation: Mubarak, R., Hofmann, M., Riechelmann, S. & Seckmeyer, G. 2017. Comparison of modelled and measured tilted solar irradiance for photovoltaic applications. Energies 10:1688
doi: 10.3390/en10111688
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by the main session; no page image checked (Eqs 3-15 read cleanly in the text layer)
status: read
diseases: []
crops: []
regions: [Hannover, Golden, Colorado]
processes: [transposition models, tilted irradiance, slope and aspect, solar radiation]
records: []
datasets: []
files: [riyad_2017.pdf (the 2026-10-18 drop)]
---

# Mubarak et al. 2017: five transposition models for tilted irradiance

Five models that turn horizontal global and diffuse irradiance into irradiance on a tilted
plane (Liu & Jordan, Klucher, Hay & Davies, Reindl, Perez), against measurements at
Hannover and at NREL's SRRL in Golden, Colorado. No record: the paper prints the equations
of models published by others.

## What it holds

- **Data:** Hannover IMUK, January 2014 to December 2016 (52.23 °N, 9.42 °E, 50 m; silicon
  sensors facing south at 10-70° tilt, six vertical, one horizontal; a 40° south CM11),
  1-min; NREL, March 2015 to December 2016 (LI-200 tilted and vertical sensors, public
  download, licence not printed). Silicon sensors agree within ±3 %.
- **Equations** (Eqs 3-15, l. 402-482): Liu & Jordan is isotropic; Klucher adds horizon and
  circumsolar terms with F = 1 - (Id / Ih)²; Hay & Davies weights a circumsolar term A = Ibn / Ion;
  Reindl adds a horizon term; Perez has three components with clearness bins. Coefficients are
  printed only for Perez (Table 1, eight bins).
- **Errors, 40° south:** rRMSD 6.0 % (Perez), 6.08 (Klucher), 6.18 (Reindl), 6.26 (Hay & Davies),
  7.85 (Liu & Jordan). Vertical south: Perez 8.72 %, others 10.6 to 11.8 %. Vertical north is
  worst: Perez 18.89 %, Liu & Jordan 24.10, Klucher 29.05, Reindl 31.8, Hay & Davies 33.78 %
  (Table 5). At Hannover vertical north Klucher is 28.94 % (Table 4). Constant albedo 0.2
  instead of measured adds 0.2 to 0.8 % rMAD. The abstract's Perez rMAD at NREL (4.2 % and
  8.7 %) disagrees with Table 5 (3.98 and 5.99 %), unresolved.
- **Recommendation:** Hay & Davies or Reindl for south-facing modules in cloudy regions where
  albedo is unknown.
- **Not printed:** coefficients for Klucher, Reindl and Hay & Davies beyond their forms; any
  data licence for Hannover.

## Dependence

- None computed from one another: the five share the beam and ground-reflected parts and
  differ only in the diffuse part. Hay & Davies and Reindl share the anisotropy index. Perez
  coefficients are from its 1990 fit elsewhere.

## Bearing (2026-10-18)

For the sweep's radiation inputs and sensor placement on sloped or walled surfaces:

- **What it offers:** the error of a plane's irradiance by tilt and aspect: small (6-8 %)
  for south planes at moderate tilt and large (19-34 %) for vertical planes facing away
  from the sun. A vine row's shaded side behaves as the vertical north case.
- **Limits:** photovoltaic planes, not canopies; two mid-latitude sites; hourly and minute
  irradiance only; no humidity, wetness or leaf temperature.
- **Take:** none for the leaf-wetness hours; useful only if the sweep adds a radiation term
  to a sloped site.
