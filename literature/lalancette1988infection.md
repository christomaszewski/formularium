---
id: lalancette1988infection
citation: Lalancette, N., Ellis, M. A. & Madden, L. V. 1988. Development of an infection efficiency model for Plasmopara viticola on American grape based on temperature and duration of leaf wetness. Phytopathology 78(6):794-800
read: 2026-10-08, in full (OCR text and page images) by a reading agent (claude-sonnet-5-5); 60 quotes checked at their lines by scripts/verify_quotes.py, the model and dependence by the main session
status: read
diseases: [downy mildew]
crops: [grapevine, Vitis labrusca]
regions: [Ohio]
processes: [infection]
records: []
datasets: [lalancette1988a]
files: [Phyto78n06_794.PDF]
---

# Lalancette, Ellis & Madden 1988: infection efficiency by temperature and wetness

From the Ohio State University (OARDC, Wooster). The first of the two 1988 Ohio papers; the
sporulation model is [lalancette1988sporulation](lalancette1988sporulation.md).

## What it holds

- **Data:** infection efficiency (lesions per zoospore) on potted *V. labrusca* 'Catawba' in
  growth chambers at Wooster: 6 temperatures from 5 to 30 °C, wetness up to about 15 h, 33
  combinations, 3 replicates of 5 plants each (l. 139-142). Inoculum 100 sporangia/ml,
  about 1.5 sporangia/cm²; lesions counted 8 days after inoculation (l. 106, 111, 155).
- **Form:** a linearised Richards function (Richards 1959) in wetness, with m = 1.2 and W
  the wetness hours minus 1 (l. 184, 189, 357).
- **Model (eq. 5, averaged data):** IE = k(1 + e^-ρ)^(1/(1-m)), with
  k = -0.071 + 0.018T - 0.0005T² + 0.01 and ρ = -0.24W + 0.070WT - 0.0021WT² (l. 517, 519).
  The added 0.01 keeps a logarithm defined and biases IE upward (l. 218, 737). It explains
  84% of the variation (l. 511).
- **Behaviour:** the asymptote k peaks at 0.083 lesions per zoospore at 17.5 °C and is zero
  at 4.6 and 30.4 °C (l. 260, 345); the rate peaks at 16.9 °C (l. 368). The authors warn
  against use outside 5-30 °C (l. 735).
- **Replicates differ:** replicate 1 (February-April) is lowest (l. 383, 394). Its b1
  prints -0.91 (l. 470, and on the page image); -0.091 reproduces the text's rate maximum
  of 0.17, so -0.91 is probably a misprint (the agent's inference, checked by the main
  session only in arithmetic).
- **Garbled in the text copy:** minus signs in Tables 1-3 (for example replicate 3's b1 is
  -0.40 on the page image); equation 4 prints without the minus sign that equations 2 and
  5 carry. Equation 5 is the usable form.

## Dependence

- It computes only Richards's growth function. Three constants (0.016 ml/cm², 7 zoospores
  per sporangium) come from the authors' own 1987 paper (l. 159, 161). No model dated or
  selected its data: wetness was set in the chamber and lesions counted after 8 days.
- Its data are the ones Magarey et al. 2005 fitted their P. viticola row to (their
  ref. 43; dataset `lalancette1988a`). The engine runs Magarey's model with Brischetto
  et al. 2021's parameters, fitted to other data, so nothing the engine runs shares them.
- Authors: Ellis and Madden are authors of the engine's `lalancette1988.sporulation_bounds`
  (the companion paper), and Madden of the policy's sampling bound: flags (D27).

## Bearing (2026-10-08)

- **No longer kin to the engine** under D27: its only links are shared authors. D20 (the
  Ohio lineage is kin) called it kin for those authors; Agrarium's PLAN 15 now recommends
  narrowing D20 to the substantive links.
- A candidate infection formulation for a truth family, with three caveats: an American
  grape (*V. labrusca*), chamber data from one place, and Magarey 2005's P. viticola row
  fitted to the same data (a truth using both would not be two witnesses).
