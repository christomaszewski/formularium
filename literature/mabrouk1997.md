---
id: mabrouk1997
citation: Mabrouk, H., Sinoquet, H. & Carbonneau, A. 1997. Canopy structure and radiation regime in grapevine. II. Modeling radiation interception and distribution inside the canopy. Vitis 36(3):125-132
read: 2026-10-18, in full (OCR text layer), by a reading agent (claude-haiku-5-5); 44 of 44 quotes found at their lines by the main session; Eqs 1-4, Table 2 and Fig. 5 read in page images (pp. 2, 5, 6) by the reading agent
status: read
diseases: []
crops: [grapevine]
regions: [Montpellier]
processes: [light interception, canopy radiation, row orientation, turbid medium model, canopy architecture]
records: []
datasets: []
files: [hatem_2015.pdf (the 2026-10-18 drop; the file name does not match the paper, which is Mabrouk et al. 1997)]
---

# Mabrouk, Sinoquet & Carbonneau 1997: radiation interception in two grapevine canopies

Part II of a pair (part I: Mabrouk, Carbonneau & Sinoquet 1997, Vitis 36(3):119-123, not read).
The file key says 2015; the paper says received 27 January 1997. A three-dimensional
turbid-medium light model for two training systems. No record: the paper sets out a model but
no tool here runs it.

## What it holds

- **Model:** a 3-D version of Sinoquet & Bonhomme's (1992) turbid-medium model (cells of leaf
  area density and leaf angle). Eq. 2: P0 = exp[-Σ Gi ui (dz / sin h)]; Eq. 3 partitions the
  interception by cell; G from Ross (1981); multiple scattering by radiosity (Ozisik 1981, cited
  in the text and missing from the reference list); sky as point sources; isotropic scattering by
  soil and leaves. Eq. 1 defines interception, Ei = 1 - Rt / Ri.
- **Canopies:** Open Lyre at low (OLLV) and moderate (OLMV) vigour and Geneva Double Curtain at
  moderate vigour (GDCMV), at the viticulture faculty in Montpellier (no coordinates here).
  Interception on 15 August 1995 at 9, 11, 13 and 15 h (Picqhelios device); PAR profiles on 7, 9
  and 11 July 1995 (sunfleck ceptometer). Leaf reflectance and transmittance by Schultz's
  (1996) field method (Table 1: main leaves 12.2 % and 8.1 % mean; lateral 13.3 % and 10.8 %);
  soil reflectance 16 %.
- **Fit:** interception against measurement r² 0.887, slope 0.957, residual mean -0.018 (SD 0.034).
  The model reproduces the difference between vigour levels but not between training systems
  (GDCMV underestimated by 0.05). Transmitted PAR residuals -0.025, 0.006 and -0.031 (SD 0.071,
  0.113, 0.140). Daily interception efficiency 0.40, 0.54 and 0.56 (calculated). Fruit-zone
  transmission 14, 5 and 7 % of incident PAR.
- **Rows and sun:** interception is least when the sun's rays run parallel to the row; the
  southern sides of both walls are sunlit at noon and the northern sides partly shaded. The
  row azimuth is not printed.
- **Laterals (Table 2):** lateral leaves are 29 to 39 % of leaf area and absorb 16 to 48 % of the
  absorbed PAR; removing them cuts leaf area by 30 to 40 % and doubles to quadruples fruit-zone
  PAR.
- **Geometric approach** (Eq. 4, after Jackson 1983): Eic = EiG [1 - exp(-(c / sin h)(LAI / EiG))],
  with c fitted 0.29, 0.30, 0.33 (the text layer prints e; the image shows c), r² above 0.98
  against the full model. It is not stated whether c was fitted to measurements or to the
  complete model's output.
- **Not printed:** row azimuth, leaf angle distributions, the units of leaf area density (4.73,
  5.31, 4.66), the model time step, a data release.

## Dependence

- **Computes** Sinoquet & Bonhomme 1992 (H. Sinoquet is an author of both). **Borrows** Ross
  1981, Ozisik 1981, Jackson 1983 and Schultz 1996's method.
- **Data:** the canopy structure data of part I, same canopies: shared input data, not a shared
  calibration.

## Bearing (2026-10-18)

For sensor placement and the sweep's light inputs:

- **What it shows:** within a hedgerow, the interior of a wall gets 5 to 14 % of the incident
  light at the fruit zone, and which side of a row is sunlit depends on the sun's angle to the
  row. Trained systems differ more than the model can resolve.
- **Take:** a sensor on the south face at noon sees a lit leaf and one on the north face a
  shaded one; the sweep cannot treat the canopy as one point for light.
- **Limits:** 1995, three canopies at one site, PAR only, no temperature or humidity; row
  orientation as such is not swept.
