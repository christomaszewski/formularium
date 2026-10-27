---
id: taibi2022
citation: Taibi, O., Furiosi, M., Caffi, T. & Rossi, V. 2022. Characterization of the Folpet fungicidal activity against Plasmopara viticola. BIO Web of Conferences 50:03002 (GDPM 2022)
doi: 10.1051/bioconf/20225003002
read: 2026-10-25, in full (3 pages; Figures 1 to 3 read by eye from the page image), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 14 of 14 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Italy, Piacenza]
processes: [fungicide, folpet, protection period, wash-off, rain simulator, curative activity, persistence]
records: []
datasets: []
files: [dr1025_taibi2022.pdf (the 2026-10-25 drop)]
---

# Taibi et al. 2022: how long folpet protects potted Merlot, and after how much simulated rain it fails

A three-page conference paper with a preventive period (to 9 days), a curative test, and a rain-wash test (to 80 mm) on leaves of potted vines, scored as efficacy against Plasmopara viticola, not as residue.

**Read this first.**
- The rain result is an efficacy, not a residue, and most of it is in a figure. The text prints only ">70 %", "40 %", "33 %", the control severities 39 % and 23 % and R² = 0.8971. The rain-curve values below (about 90 %, 77 %, 66 %, 7 %) were read by eye from Figure 3 by the reading agent. The regression equation is not printed.
- The simulator's intensity is not printed. The nozzle data give about 2.7 mm/h (arithmetic, not printed: 13 nozzles x 1.9 L/h over 9 m²), a very light rain. The drying interval between spray and rain is not stated.
- Sampled leaves were washed repeatedly under tap water and dried before discs were cut (l. 68), so the preventive efficacy is that of the residue that survived a rinse. The rain test says it followed "the same protocol", so the rinse probably applies there too (an inference).
- The dose is printed "1,875 kg/ha"; read as 1.875 (decimal comma), which gives 1.5 kg a.i./ha at 80 % (arithmetic, not printed). Outdoor pots: no rain record is printed for the 11 days.

## What it holds

- **Design (l. 46, 60):** Merlot vines in outdoor pots at Piacenza, 2020 and 2021 (l. 46). Folpet (Vinifol 80 WDG, 80 % folpet) at 1.875 kg product/ha by shoulder sprayer to full coverage on plants at BBCH 65 (l. 60).
- **Preventive period (l. 64, 69, 81, 125):** leaves 3 and 4 from the apex sampled 1, 3, 5, 7, 9 and 11 d after spraying, then inoculated as leaf discs (l. 64). Infection was cut by more than 70 % from day 1 to day 9 on leaves and bunches (l. 69). Efficacy is long-lasting to 9 d and had collapsed at 11 d (Figure 1, bar "b") (l. 125). Untreated control severity 39 % on leaf discs and 23 % on bunch parts (l. 81).
- **Rain-wash test (l. 36, 39):** 10, 20, 40, 60 and 80 mm of artificial rain after spraying, then the leaves were challenged with the pathogen (l. 36). The rain came from an irrigation pipe at 2 m with 13 nozzles of 1.9 L/h over 9 m² (l. 39).
- **Rain result (l. 138, 140, 113):** protection remained high after 60 mm (l. 138) and dropped sharply to a non-significant level at 80 mm (l. 140). Read by eye from Figure 3: relative efficacy about 90 % at 0 to 10 mm, about 77 % at 20 mm, about 66 % at 40 and 60 mm, about 7 % at 80 mm. A dotted regression curve was drawn through the points, R² = 0.8971 (l. 113).
- **Curative test (l. 110):** high efficacy at 1 h after inoculation, 40 % at 3 h, 33 % at 12 h, and unreliable at 6, 24 and 96 h.
- **Use (l. 56):** the rain curve was fed into the persistence model of Caffi & Rossi 2018 inside the decision system vite.net.

## Dependence

- **Own experiments** (2020 and 2021). Feeds the persistence model of `caffi2018`. Same research group as the engine's Rossi-family models (Rossi, Caffi, Furiosi): a flag only.

## Bearing (2026-10-25)

- **Wash-off per mm of rain (E6; M4):** folpet only, on potted Merlot leaves, as efficacy. Protection stays near its plateau to 60 mm and falls to about 7 % at 80 mm (by eye), a threshold-like response, unlike copper's early loss in `molot2004`. The rain was very light (about 2.7 mm/h, arithmetic) and the drying time before rain is unknown, so it is not a per-mm rate for field rain.
- **Decay with time:** efficacy above 70 % to 9 d after spraying, then collapse at 11 d, on leaves 3 and 4 from the apex after a tap-water rinse; weather in the 11 days is not reported. This supports a protective period of about 9 d for folpet at full coverage, at BBCH 65 (not early season).
- **Dilution by growth and dose-efficacy:** not tested (one dose; leaves 3 and 4 from the apex are young leaves, but their age at spraying is not given). Kind of result: a measurement on potted vines, with efficacy read from figures.
