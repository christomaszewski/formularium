---
id: koyama2022
citation: "Koyama, Kohei & Smith, Duncan D. 2022. Scaling the leaf length-times-width equation to predict total leaf area of shoots. Annals of Botany (volume and pages not printed in the text read)"
doi:
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full; JATS XML text, one paragraph per line, no page numbers
status: read
diseases: []
crops: []
regions: [Hokkaido, Japan]
processes: [leaf area per shoot, leaf size allometry]
records: []
datasets: []
files: [koyama2022.xml]
---

# Koyama and Smith 2022: shoot leaf area from foliage length times width

A geometric model that predicts a shoot's total leaf area from the product of its foliage length and width, fitted in five non-vine species.

## What it holds

- **Species:** Magnolia kobus, Cardiocrinum cordatum, Prunus sargentii, Ulmus davidiana var. japonica and Fallopia sachalinensis, 29 to 43 shoots each (Table 1, l. 81). No grapevine.
- **Main fit:** the foliage length-times-width equation (Eq 4) gives R2 0.994 to 0.997 for shoot leaf area (Table 2, l. 105; text l. 15).
- **Weaker forms:** shoot leaf area against the largest leaf length or width gives R2 0.930 to 0.976 (l. 94).
- **Lopes and Pinto form (Eq 13):** the fitted k runs from 0.758 to 1.221, with R2 0.981 to 0.994 (Table 2, l. 137-138; text l. 153). The wine-grape authors used k = 1 (l. 70).

## Dependence

- Builds on the Montgomery lamina-area equation (Eq 2, l. 38), the Sun et al. shoot model (Eq 8, l. 52), the Heerema-Spann-Teobaldelli allometry (Eqs 11-12, l. 61-64) and Lopes and Pinto 2005 (Eq 13, l. 68). It retests all four. R 4.1.0 with smatr for the SMA fits (l. 92).

## Bearing (2026-10-26)

- Wanted by the 10-14 phenology and growth list (leaf area from shoot measurements). classes.tsv names no search; its reason is a form that cites Lopes and Pinto 2005.
- A vineyard simulator could take the Eq 13 form, mean leaf area from the largest and smallest leaf on a shoot, and test it on vine shoots. The paper has no vine data, so any vine use needs a vine calibration. Not read in full.
