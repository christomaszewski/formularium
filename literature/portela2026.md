---
id: portela2026
citation: Portela, F., Pádua, L., Sousa, J. J., Rodríguez-Pérez, J. R., Mendes, S., Valín, M. I., Morais, R. & Paredes, C. A. 2026. Detection of downy mildew infection in grapevine leaves using field spectroscopy and machine learning. Precision Agriculture 27:79
doi: 10.1007/s11119-026-10372-3
read: 2026-10-20, LIGHT, by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Portugal]
processes: [image detection, spectroscopy, machine learning]
records: []
datasets: []
files: [portela_2026.pdf (the 2026-10-20 drop)]
---

# Portela et al. 2026: field spectroscopy separates downy-mildewed Loureiro leaves

A portable spectroradiometer on 600 attached Loureiro leaves in one 2.2 ha vineyard over ten
dates in 2023-2024, with PLS-LDA and random forests separating leaves visually classed as
symptomatic or not.

## What it holds

- Field spectroscopy (portable spectroradiometer) on attached leaves of Vitis vinifera cv.
  Loureiro, a 2.2 ha vineyard, 2023 and 2024 (l. 24, 181).
- 600 leaves: 30 symptomatic and 30 asymptomatic per block and campaign, classed by visual
  inspection; leaves not marked (l. 277, 287).
- Campaign dates 2023: 20 and 27 July, 3, 8, 21 August; 2024: 28 June, 12 and 29 July, 12
  and 26 August (l. 274, 275).
- PLS-LDA and RF overall accuracy 95.1% (l. 32); infected-class recall 0.923 (PLS-LDA) and
  0.912 (RF) (l. 586, 589).
- Best band sets 96.7% (VIS_RE_NIR and RE_NIR, PLS-LDA) (l. 596).
- Cross-year transfer: 2024 to 2023 PLS-LDA 86.7% (VIS_RE) (l. 731); RF 2023 to 2024 VIS_RE
  95.7% (l. 738).
- No accuracy by infection stage or days after inoculation; presymptomatic detection not
  tested (l. 285).
- One cultivar in one vineyard (l. 1081).
- Data on Zenodo (DOI 10.5281/zenodo.17339255 as read from split text).

## Dependence

- Its own measurements; the classes come from visual inspection, so the method is scored
  against a scout, not against infection.

## Bearing (2026-10-20)

- For Agrarium's proximal-sensing operators: 95 % accuracy separating visibly diseased
  leaves, 87-96 % across years, but no test before symptoms ('asymptomatic' means no visible
  signs), so like cameras it sees symptoms. Data on Zenodo (doi as read from the split text:
  10.5281/zenodo.17339255, not checked).
