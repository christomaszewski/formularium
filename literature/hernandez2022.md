---
id: hernandez2022
citation: Hernández, Inés, Gutiérrez, Salvador, Ceballos, Sara, Palacios, Fernando, Toffolatti, Silvia L., Maddalena, Giuliana, Diago, María P. & Tardaguila, Javier. 2022. Assessment of downy mildew in grapevine using computer vision and fuzzy logic. Development and validation of a new method. OENO One 56(3):41-53
doi: 10.20870/oeno-one.2022.56.3.5359
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [La Rioja (Spain), Milan (Italy)]
processes: [sporulation, severity assessment, leaf disc bioassay, image analysis, fuzzy logic, expert rating, classification]
records: []
datasets: []
files: [assessment-of-downy-mildew-in-2022.pdf]
---

# Hernández et al. 2022: fuzzy logic and images to score downy mildew

A light read (the deep-research B list).

## What it holds

- Image method for downy mildew severity on grapevine leaf discs, lab only; validated against the mean of 11 raters (l. 29-44).
- Set-1 Cabernet-Sauvignon, Milan: 14 dishes, 109 discs, 4 MP (l. 139-140, l. 177); Set-2 Tempranillo, La Rioja: 29 dishes, 261 discs, 24 MP (l. 164, l. 169).
- Discs held 9 days at 23 C in a humid chamber; no infection model (l. 162).
- Raters trained on 36 discs and retrained above a 15 % difference; 370 discs each (l. 310-320).
- Best regression: R2 0.87, RMSE 7.61 % (l. 476-477; Table 2, l. 430).
- Three classes: accuracy 86 %, F1 0.78 to 0.79 (l. 44, l. 483).
- The authors name field conditions and other crops as next steps (l. 618).

## Dependence

- none. The paper inoculates leaf discs (Plasmopara sporangia, 23 C, 9 days in a humid chamber) and scores sporulation on images. It computes no infection, incubation, sporulation, wetness, phenology or oospore model, and cites no engine-list model. Shared authors with engine-list papers: none found in the author list.

## Bearing (2026-10-10)

- A severity-reading method for sporulation on leaf discs: a possible observation operator for the truth's lab or bioassay data, with rater protocol and error figures; it carries no infection model.
