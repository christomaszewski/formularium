---
id: perezexposito2017
citation: Pérez-Expósito, Josman P., Fernández-Caramés, Tiago M., Fraga-Lamas, Paula & Castedo, Luis. 2017. VineSens: An Eco-Smart Decision-Support Viticulture System. Sensors 17:465
doi: 10.3390/s17030465
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew, grey mould, black rot, phylloxera, excoriose]
crops: [grapevine]
regions: [Spain, Galicia, Ribeira Sacra, Italy, France, New York (USA)]
processes: [infection, spray timing, primary infection, secondary infection, season severity, leaf wetness, decision support]
records: [rule_3_10, goidanich.incubation]
datasets: []
files: [p17.pdf]
---

# Pérez-Expósito et al. 2017: VineSens wireless sensors with downy mildew alerts

A light read (the deep-research B list).

## What it holds

- VineSens: a wireless sensor and web system on a 0.14 ha vineyard in Ribeira Sacra, Galicia, deployed in 2016 (l. 22, l. 683).
- The paper reviews four downy mildew models (3-10 rule, EPI, DMCast, UCSC) and implements only the 3-10 rule (l. 186-197, l. 332).
- The 3-10 rule needs air at 10 C or more, shoots at least 10 cm and 10 mm of rain in 24 to 48 h (l. 202-203).
- The index follows the Goidanich daily development table (l. 204, l. 336).
- Default alerts fire at 90% (warning) and 100% (urgent) (l. 791).
- The 2016 season used 11 to 13 sprayings across methods (l. 893) and an estimated e14.5 saving on a half-acre farm (l. 898-899).

## Dependence

- verdict: computes; models: Goidanich et al. 1957's incubation table (computed: 'Once the infection starts, its progress is calculated using the Goidanich model (in Table 1)', l. 204; 'the Rule 3-10 index is calculated according to Table 1', l. 336) the 3-10 rule (implemented as the sole infection rule: 'a software algorithm based on the Rule 3-10 was devised and implemented', l. 332); described_not_computed: Rossi et al. 2008's UCSC model (l. 272-279, 'a mechanistic model developed according to the principles of the system analysis'), EPI and DMCast (l. 248-266). These are described and compared, not computed.; shared_authors: none noted

## Bearing (2026-10-10)

- The truth must not share the Goidanich table or the 3-10 rule that this system runs (l. 204, l. 332), and its data are not released, so it offers little to the truth beyond a record of the models the engine would hold out.
