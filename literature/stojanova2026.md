---
id: stojanova2026
citation: Stojanova, Simona, Volk, Mojca, Superina, Argene, Kos, Andrej & Stojmenova Duh, Emilija. 2026. Framework Proposal for Assessing the Sustainability Impacts of IoT-Enabled Disease Management in Viticulture. Agriculture 16:2117
doi: 10.3390/agriculture16192117
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Slovenia, Podravska region]
processes: [spray timing, season severity, leaf wetness, infection, spraying operations, decision support]
records: []
datasets: []
files: [q180.pdf]
---

# Stojanova et al. 2026: sustainability framework for IoT disease management

A light read (the deep-research B list).

## What it holds

- A framework that links IoT monitoring, a proposed disease-risk DSS and SROI sustainability value, applied to one 8 ha Slovenian vineyard (l. 18, 464, 807).
- The DSS is proposed, not built or validated; the paper says so (l. 339, 1112).
- The proposed DSS uses the UC Davis powdery mildew risk index: a rain, leaf-wetness and temperature gate, then a 0 to 100 index (l. 537, 553-554, 558).
- Spraying counts are the only operational data: 17 operations in the reference year, 14 in the digitalized year (l. 810-811).
- Savings per operation are 16 h labour, 16 kg copper, 24 kg sulphur and 2400 L water (l. 815).
- The base SROI ratio is 0.60, and the optimistic end of the sensitivity range is 0.99 (l. 954, 994).

## Dependence

- model: UC Davis powdery mildew risk index (Gubler et al. 1999); relation: computes (proposed, not run): the DSS would run the index's two-stage calculation; the index is for grape powdery mildew, so this is a disease other than downy mildew; line: 537; quote: Risk Index (Gubler–Thomas model) is one of the most validated and widely adopted model: UC Davis powdery mildew risk index (Gubler et al. 1999); relation: the gate and index steps the DSS is to implement; line: 553; quote: estimates the risk of initial infection based on environmental conditions, including rainfall, model: Magarey et al. 2005 infection model (ref 64); relation: cited only in a list of forecasting approaches; not computed or borrowed; line: 535; quote: based on environmental conditions [63–65].

## Bearing (2026-10-10)

- The paper offers only an operational spray count from one vineyard and an unvalidated proposal to run a powdery mildew index; the truth could use the counts as an operational record, not as disease data, and the engine gains nothing from it.
