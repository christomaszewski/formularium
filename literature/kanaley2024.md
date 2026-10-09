---
id: kanaley2024
citation: Kanaley, Kathleen, Combs, David B., Paul, Angela, Jiang, Yu, Bates, Terry & Gold, Kaitlin M. 2024. Assessing the Capacity of High-Resolution Commercial Satellite Imagery for Grapevine Downy Mildew Detection and Surveillance in New York State. Phytopathology 114 (issue 12):2536-2545
doi: 10.1094/PHYTO-11-23-0432-R
read: 2026-10-08, in full (supplementary tables S5-S8 not held), by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [New York]
processes: [remote sensing, detection, observation]
records: []
datasets: []
files: [10-1094-phyto-11-23-0432-r.pdf]
---

# Kanaley et al. 2024: commercial satellite imagery for downy mildew detection in New York

From Cornell (Geneva).

## What it holds

- Site: one 0.8 ha Chardonnay block in a Cornell fungicide trial at Geneva, New York (l. 76), (l. 85). No other site.
- Labels: trained scouts rated 20 leaves per panel by eye, weekly, June to August 2020, 2021 and 2022 (l. 95), (l. 97). High severity is panel mean above 10 % leaf area (l. 123-124); high incidence is above 25 % of leaves (l. 125). Most panels stayed low (l. 263-264).
- Scenes: PlanetScope 3, 3 and 5 usable of 16, 53 and 47 (l. 130), (l. 131), (l. 132); SkySat 5, 4 and 3 usable of 13, 13 and 14 (l. 138), (l. 139), (l. 140). Usable means cloud-free, co-registered, within 72 h of scouting (l. 82).
- PlanetScope labels are interpolated panel ratings on a 3 x 3 m grid (l. 125).
- Random forests within a year: PlanetScope accuracy 0.80 to 0.92 (l. 386); SkySat 0.50 (2022 severity) to 0.85 (2020 incidence) (l. 421), (l. 435). High-severity recall as low as 0.33 (l. 416).
- Train and test rows are not stated to be split by panel or date, so within-year scores may be optimistic.
- Across years the best SkySat models reached F1 0.56 and 0.28 (l. 393), (l. 398).
- No significant index difference between classes until late July to early August (l. 23); earliest 26 July 2021 (l. 458).
- Observation role only. Shares four authors with Liu 2026.

## Dependence

- Its own scouting and PlanetScope and SkySat images, 2020-2022; random forests on balanced pooled rows. No model dated the data.
- Gadoury is not an author; no author of an engine model.

## Bearing (2026-10-08)

- Clear: the numbers for a satellite operator. **A correction:** the earlier notes' "cross-year F1 as low as 0.28" is the F1 of the best cross-year SkySat severity model (precision 0.17, recall 0.84, l. 398); the worst values are in supplements not held. A 2022 SkySat accuracy of 0.50 on a balanced set is chance.
