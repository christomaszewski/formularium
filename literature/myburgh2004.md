---
id: myburgh2004
citation: Myburgh, P.A. 2004. Determining grapevine canopy effects on effective rainfall in vineyards (Research Note). South African Journal of Enology and Viticulture 25(1):33-35
doi: 10.21548/25-1-2136
read: "2026-10-25, in full (3-page research note, a scan read through OCR) (equations checked in the page image by the main session), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 19 of 19 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [grapevine]
regions: [South Africa, Western Cape, Stellenbosch]
processes: [rain interception, throughfall, rain gauge, trellis, leaf area, day of season]
records: []
datasets: []
files: [dr1025_myburgh2004.pdf (the 2026-10-25 drop)]
---

# Myburgh 2004: rain reaching soil-level gauges under six vine trellises at Stellenbosch, 86 % (slanting) and 80 % (vertical) of open-ground rain on average

A two-season note in which daily gauge readings under and between vine canopies are fitted to open-ground rain and day of season.

**Read this first.** Rain was measured by gauges at the soil surface directly under the canopy (l. 105, 108). So the 14 % and 20 % that did not reach them is rain that missed those gauges (interception, drip elsewhere, stemflow, siting), not water stored on the leaves. No LAI or storage capacity was measured (cane mass per vine is the only vigour measure, l. 119), so this paper cannot by itself set a storage per LAI. Other points: the trellis systems were not replicated spatially (l. 89-90); the daily totals are not events; the equations are garbled in the OCR text (printed "RU," and "D0S?") and were read in the page image (PDF p. 3).

## What it holds

- **Site and design:** Chenin blanc on 99 Richter, 17 years old, planted 3.0 m by 1.5 m in north-south rows (l. 77, 79) at Stellenbosch, a Mediterranean climate, in six trellis systems (l. 13). Slanting: 1.5 m slanting trellis, gable and bush vines (counted as slanting); vertical: 3-wire hedge, 5-wire lengthened Perold and Lyre (l. 82-88). Cane mass per vine 0.9 to 1.2 kg (l. 119).
- **Gauges:** plastic meters level with the soil surface in 150 mm steel sleeves, two in the work-row centre and two between vines in the row, read daily from October to March in 1994/95 and 1995/96 (l. 101-105). Open-ground rain came from meters outside the vineyard at 1.5 m (l. 101-102). "Interception" is defined as open rain minus rain measured directly under the canopies (l. 108).
- **Rain in the data:** 0.3 to 38 mm per day (l. 129). 1994/95 had 18 rain days, all but one below 10 mm per day, and a season total of 74 mm; 1995/96 had 26 rain days and 269 mm (l. 131). The fits use 44 daily observations from both seasons (l. 236).
- **Work-row centre:** rain there equalled open rain, Rowc = 0.151 + 0.979 Ract, R2 = 0.997, SE 0.35 mm, n = 44 (l. 145).
- **Eq. 1, slanting canopies (PDF p. 3, l. 236):** RUs = 0.86 R - 0.026 DOS + 0.00007 DOS^2 (n = 44; SE = 1.4 mm, R2 = 0.9607). **Eq. 2, vertical canopies (l. 238):** RUv = 0.80 R - 0.041 DOS + 0.0001 DOS^2 (n = 44; SE = 2.0 mm, R2 = 0.8923). R is daily open-ground rain in mm and DOS is the day of season, with 1 September as day 1 (l. 230-231). The three slanting and the three vertical systems were pooled because their data did not differ (l. 226-227, 187-189); the two seasons were pooled to 44 observations (l. 231-232). There is no constant term.
- **What the authors read from them:** on average 86 % (slanting) and 80 % (vertical) of rain reached the soil under the canopy (l. 21); the coefficients on R mean that "at least" 14 % and 20 % was intercepted (l. 244).
- **Worked example, 15 December, 20 mm of open rain:** 15.2 mm reach the soil under a slanting canopy (l. 248) and 12.9 mm under a vertical one (l. 253). The paper then weights by the share of ground under canopy (80 % for slanting, 20 % for vertical) and gets 16.2 mm and 18.6 mm of 20 mm over the whole area (l. 250-256).
- **Season shape:** interception "tended to increase and decrease" with vegetative growth (l. 220); values lay near the 1:1 line early in the season (l. 183). Vertical canopies let less through than slanting ones, which the authors put down "probably" to more leaf layers above the meters (l. 180-182).
- **Conclusion:** both canopy types intercepted "surprisingly little" daily rain (l. 263).
- **Arithmetic, not printed:** at DOS 106 (15 December) the two DOS terms add up to -1.97 mm (slanting) and -3.22 mm (vertical). A 20 mm day then loses 4.8 mm (24 %) and 7.1 mm (36 %), from the printed 15.2 and 12.9 mm. A 10 mm day loses about 34 % and 52 %, and a 5 mm day about 53 % and 84 %, from the equations. Most rain days were small (l. 131), so the DOS terms, not the slope, set the loss on most days.

## Dependence

- Own measurements and regressions (Statgraphics, l. 113); trellis names and vigour classes after Zeeman (1981) and other South African sources. No model borrowed. A 1998 PhD dissertation by the same author on vineyard water use is cited; it may treat the rain data more fully and was not obtained.

## Bearing (2026-10-25)

- **micro.interception (0.6, share caught until full):** not measured here. The paper gives the share of daily rain that failed to reach soil-level gauges: 14 % and 20 % on average, 24 % and 36 % on a 20 mm day in mid-season (arithmetic, not printed). That is a loss at the gauges, not a share caught until a store is full, so it does not test 0.6. It does show a loss that grows with leaf area and is small on large rain days.
- **micro.storage_mm_per_lai (0.25) and SWEB (0.2 mm per unit leaf area):** no support either way. There is no LAI and no storage. The direction (loss follows leaf area, l. 183, 220) fits a store that scales with leaf area. With an assumed LAI of 2 to 3 (my assumption, not in the paper), a store of 0.25 mm per unit LAI holds 0.5 to 0.75 mm, far below the 4.8 to 7.1 mm lost on a 20 mm day. The paper cannot tell whether the gap is a larger store, several fill-and-dry cycles in one day, or gauge siting.
- **micro.wet_threshold_mm, micro.evap_mm_h_per_hpa, micro.density_drying_slowdown:** not addressed; daily totals only, no wetness and no drying.
- **Kind of result:** measurement (one vineyard, two seasons, 44 rain days, daily totals) summarised in two regressions. It is the only vineyard rain-partition measurement in this strand; stemflow was not measured.
