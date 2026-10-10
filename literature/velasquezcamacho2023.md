---
id: velasquezcamacho2023
citation: Velasquez-Camacho, Luisa, Otero, Marta, Basile, Boris, Pijuan, Josep & Corrado, Giandomenico. 2023. Current Trends and Perspectives on Predictive Models for Mildew Diseases in Vineyards. Microorganisms 11:73
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Italy, Quebec, Douro, New York State]
processes: [infection, oospores, spray timing, season severity, leaf wetness, infection forecast]
records: []
datasets: []
files: [p01.pdf]
---

# Velasquez-Camacho et al. 2023: review of predictive models for vineyard mildews

A light read (the deep-research B list).

## What it holds

- Review of predictive models for downy and powdery mildew in vineyards (MDPI, published 27 December 2022, volume dated 2023); 19 pages; a literature screen with bibliometrics (l. 420-750).
- Table 1: DM favoured by rain 6–10 mm, 6–26 °C, RH >90%, wind >9.0 m/s, 7–18 days to infection (l. 175); the table has no source.
- Describes the 3–10 rule (10 °C, 10 cm shoots, 10 mm within 24–48 h; l. 818-822) and the Goidanich incubation table with later derivatives and PLASMO (l. 823-837).
- Describes Rossi et al.'s mechanistic primary-infection models, UCSC model counting from 1 January (l. 905-911), and DMCAST (l. 891).
- Conclusion: models usually trained and tested in one locality, so validation in other regions is needed (l. 1036).

## Dependence

- Describes, does not compute, several of the engine's models: the 3–10 rule (l. 818-822), the Goidanich incubation table and its later derivatives (l. 823-837), and Rossi et al.'s primary-infection models (ref. 10 at l. 905; ref. 77 at l. 907-911). Table 1 (l. 175) gives RH above 90% as a DM condition, which is the RH-based wetness stand-in the truth's rules keep out. Shared authors (Rossi, Caffi) appear in its bibliometrics (l. 739); flags only. It shares no data, calibration or code with the engine's models that the review itself reports.

## Bearing (2026-10-10)

- It gives a map of the models the truth must not share with the engine: the 3–10 rule, Goidanich's table, and Rossi's mechanistic models are all described here, and Table 1's unsourced DM thresholds should not be taken as parameters.
