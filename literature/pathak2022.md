---
id: pathak2022
citation: Pathak, P., Pandya, P., Shukla, S., Sane, A. & Sengupta, R. 2023. A Sensor Placement Strategy for Comprehensive Urban Heat Island Monitoring. ISPRS International Journal of Geo-Information 12(1):11
doi: 10.3390/ijgi12010011
read: 2026-10-21, lightly: abstract, introduction, study area and data, the weighting method and sensor-count calculation, and the discussion and limitations (tables partly unrecoverable), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [India, Maharashtra, Pune]
processes: [sensor placement, heuristic allocation, urban heat island, land surface temperature, local climate zones, sensor budget]
records: []
datasets: []
files: [pathak2022.pdf (the 2026-10-21 drop)]
---

# Pathak et al. 2023: a weighted split of a 500-sensor budget over 1 km grid cells by causal-factor variability, for urban heat

Allocates a fixed budget of low-cost sensors over Pune by ranking 1 km cells on the variability of heat-island causal factors and giving high-variability cells more sensors. No record: a method (the id follows the drop key, pathak2022; the article is dated 2023, l. 33-38).

**Read this first.** There is no validation: the placement is not compared with measurements, with another method or with random layouts (l. 57-58, 922). The table values (Tables 3 to 5) are interleaved with the text, so the sensor count per category is not recoverable, and the per-grid formula (l. 537-548) is garbled; it is recorded as unchecked. The USD 50 per sensor is inferred from 500 sensors and USD 25,000 (l. 510, 550). Wind is at 10 m, not the 1.2 m the WMO recommends (l. 958).

## What it holds

- **Method** (Section 2.3, Tables 3 to 5, l. 346, 441-455, 470-475): Pune is cut into 332 grids of 1 km x 1 km (l. 346); each grid's variability of seasonal surface temperature, wind, bareness and local climate zone proportions is rescaled to 0 to 100; five categories carry weights 5 (85 to 100 %) down to 1 (1 to 40 %), and the budget is split in proportion to grids times weight (unnumbered formula, garbled, unchecked). Within a grid, sites are chosen for visibility and a 500 m distance criterion (l. 591-593).
- **Assumption** (l. 452, 979): higher variability in a grid means more sensors there; the conclusion rests on this and no test is given.
- **Inputs** (l. 353, 384, 946, 954-960): MODIS land surface temperature at 1 km, Landsat 8 bareness and WUDAPT local climate zones (accuracy 82 % against Google Earth, l. 384) kept as class proportions per cell, ERA5 and TerraClimate wind limited to two years because of download charges.
- **Budget** (l. 504-510, 550, 754): 500 low-cost LoRaWAN air, surface temperature and humidity sensors, USD 25,000 in all (about USD 50 each); Table 5 total, 332 grids and 500 sensors. No sensors were installed in the study.

## Dependence

- Builds on the WUDAPT local climate zone classification and its accuracy check, MODIS, Landsat 8 and ERA5 data, carpet and reduced-network placement studies (Twin Cities; Almeida et al. on LCZ-based placement) and the WMO sensor-height guideline. None recorded beyond these.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): a heuristic, zone-weighted placement, and a sensor budget in money.

- **Takeable:** the budget-driven split (sensors in proportion to grid count times a variability weight) is the simplest heuristic to include as a comparator, and the 500 sensors at USD 50 each shows a sensor menu priced per node (l. 510, 550).
- **Not shown:** any validation, any random or optimised comparator, run times, a held-out test, measured heat or wetness data. Kind of result: a design recipe for a case study, with no result to score.
- **Vineyard variability:** it ranks cells by the variability of causal factors, not by variability of the target variable, which is a different choice from Agrarium's simulated-season variability.
