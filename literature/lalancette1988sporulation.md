---
id: lalancette1988sporulation
citation: Lalancette, N., Madden, L. V. & Ellis, M. A. 1988. A quantitative model for describing the sporulation of Plasmopara viticola on grape leaves. Phytopathology 78(10):1316-1321
read: 2026-10-08, in full (text extraction; no page images) by a reading agent (claude-sonnet-5-5); 57 quotes checked by scripts/verify_quotes.py, the model and dependence by the main session
status: read
diseases: [downy mildew]
crops: [grapevine, Vitis labrusca]
regions: [Ohio]
processes: [sporulation]
records: [lalancette1988.sporulation_bounds]
datasets: []
files: [Phyto78n10_1316.pdf]
---

# Lalancette, Madden & Ellis 1988: sporulation by temperature and humid hours

From the Ohio State University (OARDC, Wooster). The engine computes this model's 10-30 °C
bound (`lalancette1988.sporulation_bounds`, through Cooptera's port of Brischetto et al.
2021).

## What it holds

- **Data:** sporangia per cm² of lesion on potted *V. labrusca* 'Catawba' leaves infected 7
  days earlier, in a dark mist chamber above 95% RH: 10, 15, 20, 25 and 30 °C by 6 to
  12 h, 25 combinations, 3 replicates (l. 22, 63, 65, 109); 15 disks of 0.95 cm² per
  treatment (l. 77).
- About 300,000 sporangia/cm² after 12 h at 20 °C; none at 10 or 30 °C (l. 25, 27).
- **Model (eq. 6):** S = k(1 - e^(B+ρ))², a Richards form with m = 0.5 (l. 109, 183), where
  k = -873,164 + 114,369T - 2,828T² + a constant, B = -8.96 + 1.16T - 0.029T², and
  ρ = 1.51H - 0.20HT + 0.0049HT² (l. 201, 242, 243). R² 0.90 (l. 21).
- **Two conflicts in print:** ρ's HT term prints -0.020 in eq. 6 but -0.20 in Table 2
  (l. 243, 315); the constant on k prints 5,000 in eq. 6 and 50,000 in the methods (l. 201,
  136). The rounded coefficients do not reproduce Table 3 at short durations (the earlier
  session found this; the reading agent confirmed it at 7.5 h and in the field row).
- **The bound:** the authors call 10 and 30 °C "arbitrarily chosen temperature extremes",
  and say true limits of 11 and 28 °C would give narrower, taller curves (l. 470-471).
- **Validation:** new chamber runs and a 1987 field test in a Catawba vineyard, using hours
  of RH above 90% (l. 85, 91, 104).
- **Garbled in the text copy:** superscripts in eqs. 2, 5 and 6; lost minus signs in
  Table 1 (replicate 1 b2) and Table 2 (replicate 2 b0).

## Dependence

- Only Richards's form is computed; all parameters were fitted to the authors' own chamber
  data, and no model dated or selected them. The infection paper is cited for its optimum
  only (l. 359).
- It is the source of an engine piece, so a truth that ran this model is the engine's
  model (`part_of` in Agrarium's candidates).

## Bearing (2026-10-08)

- **Kin, and rightly so,** under D27 too: the engine computes a piece of it. The
  authors' own words that 10 and 30 °C were arbitrary is worth telling Cooptera, whose
  bound rests on them.
- As data, its chamber counts could check a truth's sporulation; as a formulation it is the
  engine's.
