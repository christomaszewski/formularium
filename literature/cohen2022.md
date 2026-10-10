---
id: cohen2022
citation: Cohen, Bar, Edan, Yael, Levi, Asher & Alchanatis, Victor. 2022. Early Detection of Grapevine (Vitis vinifera) Downy Mildew (Peronospora) and Diurnal Variations Using Thermal Imaging. Sensors 22:3585
doi: 10.3390/s22093585
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 22 of 22 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Israel]
processes: [infection, leaf wetness, season severity, fungicide efficacy]
records: []
datasets: []
files: [cohen2022-thermal-early-dm.pdf]
---

# Cohen et al. 2022: thermal imaging for early grapevine downy mildew

A light read (the deep-research B list).

## What it holds

- Thermal imaging of greenhouse Chardonnay vines inoculated with downy mildew; six campaigns, 169 plants, December 2019 to October 2020 (l. 108-109).
- Classification dataset of 1403 records: 599 healthy and 804 infected leaves (l. 206).
- Best SVM: accuracy 81.6%, F1 77.5%, AUC 0.874 (l. 25, 1086).
- Images at 10:40-11:30 a.m.: accuracy 80.7%, AUC 0.895 (l. 26, 1094).
- Day-split test: accuracy 76.5%, AUC 0.827 (l. 718); one whole experiment as test: AUC 0.593 (l. 726).
- Infected leaves about 1 C warmer than healthy on average (l. 234).

## Dependence

- Flag only, not a computation. The introduction states the primary-infection conditions (at least 10 mm of rain or irrigation and at least 10 C over 24 h, l. 81-82) and cites them to Kennelly et al. 2007 (ref 10, l. 1144). This is the engine's Kennelly primary trigger in its stated form; the paper does not compute, fit or test it. The CWSI feature (l. 282-284, cited to Jones, ref 19) is a stress index built on wet and dry reference temperatures, not an engine model. No shared authors flagged.

## Bearing (2026-10-10)

- A thermal-imaging test of early downy mildew with a dataset of observed leaf temperature and severity that a truth could use as a validation check, while its only tie to the engine is the Kennelly trigger it states at l. 81-82.
