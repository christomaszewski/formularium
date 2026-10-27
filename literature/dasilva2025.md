---
id: dasilva2025
citation: "Silva, Thaís Rayane Gomes da. 2025. Influência climática no desenvolvimento e produtividade de videira (Vitis vinifera L.) descrito por modelos de aprendizagem de máquina [Climatic influence on the development and yield of grapevine (Vitis vinifera L.) described by machine learning models]. PhD thesis, UNESP, Jaboticabal; pages not printed in the text read"
doi:
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full; Portuguese thesis, read through the English abstract, the results and the table list
status: read
diseases: []
crops: [grapevine]
regions: [southern Brazil]
processes: [phenology, yield, climate-yield relation, machine learning]
records: []
datasets: []
files: [dasilva2024.pdf]
---

# da Silva 2025: climate, development and yield of grapevines in southern Brazil

A Brazilian PhD thesis that links NASA-POWER weather to yield in seven southern Brazil grape regions, 1982 to 2021, with four machine-learning models and a Holliday yield curve.

## What it holds

- **Data:** seven southern Brazil regions, 1982 to 2021; climate from NASA-POWER, yield from Sidra/IBGE (English abstract, l. 269-279).
- **Models:** multiple linear regression, Random Forest, SVM and CatBoost, with cross-validation. CatBoost gave the best accuracy (English abstract, l. 280-287).
- **Headline fit:** Random Forest R2adj 0.89 and RMSE 1543.22 kg/ha without variable selection (Results, l. 1963-1964).
- **Yield curve:** the Holliday (1960) model with fitted a, b and g for each region (Eq 4, l. 3071; Table 6, l. 3295).
- **Climate signs:** relative humidity correlates positively with yield, and reference evapotranspiration negatively (English abstract, l. 287-290).

## Dependence

- Builds on the NASA-POWER and Sidra/IBGE data (l. 1029-1033), the Holliday (1960) model (Eq 4, l. 3071), and the scikit-learn and CatBoost 1.2 implementations (l. 1278). Spearman correlation for the climate-yield links (English abstract).

## Bearing (2026-10-26)

- classes.tsv's reason: the non-threshold form that the 10-14 search asked about. Its outcome is yield, not stage timing, leaf area or disease, so it is indirect data for those questions.
- A growers' decision engine could take the finding that climate effects on yield differ by region. The thesis gives no stage model. Not read in full.
