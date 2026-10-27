---
id: mainini2017
citation: Mainini, L. & Willcox, K. E. 2017. Sensor placement strategy to inform decisions. In 18th AIAA/ISSMO Multidisciplinary Analysis and Optimization Conference, AIAA 2017-3820, Denver, Colorado
doi: 10.2514/6.2017-3820
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: []
regions: []
processes: [sensor placement, self-organising maps, reduced-order modelling, structural damage assessment]
records: []
datasets: []
files: [mainini2017.pdf (the 2026-10-25 other-sources drop)]
---

# Mainini & Willcox 2017: self-organising maps to place sensors for a wing-panel decision

A placement method that picks sensor sites with self-organising maps and maps sparse readings to decisions with MultiStep-ROM, tested on a simulated composite wing panel.

## What it holds

- **Method:** unsupervised self-organising maps pick the sensor set (SSL), and MultiStep-ROM
  maps the sparse data to capabilities for real-time decisions (abstract, l. 34-42).
- **Test case:** a simulated 18 by 18 inch composite panel under static load, modelled by finite
  elements with 3921 plate elements, with damage cases (l. 404-410).
- **Sensor sets:** SSL #3 has 9 points and covers 0.23 % of the reference data; SSL #6 has 20
  points and covers 0.51 % (l. 541-543; Table 1, l. 559).
- **Error:** between 0.5 % and 5 % of the grid points, the estimate error stays near 2 to 3 %,
  about two orders of magnitude below random placement (l. 621-623). The noise levels 10 and
  100 microstrain give similar errors (l. 605-608, 624-626).
- **Range:** sensor sets from about 0.10 % to 10 % of the grid points were compared (l. 643-644).

## Dependence

- **Builds on** the Sense-Infer-Plan-Act framework and MultiStep-ROM of the authors' earlier
  work (refs 1-3; l. 55), and on compressive sensing and sensor placement work (refs 4-21;
  l. 81).

## Bearing (2026-10-26)

- classes.tsv names no search for this key. Its subject is sensor placement, the topic of the
  10-21 placement search.
- A vineyard simulator could take the idea of placing a few sensors where the simulated states
  differ most, but the test is a structure, not a canopy. The paper was not read in full.
