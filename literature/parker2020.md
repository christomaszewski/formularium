---
id: parker2020
citation: Parker, Amber K., García de Cortázar-Atauri, Iñaki, Trought, Michael C. T., Destrac, Agnès, Agnew, Rob, Sturman, Andrew & van Leeuwen, Cornelis. 2020. Adaptation to climate change by determining grapevine cultivar differences using temperature-based phenology models. OENO One 54(4):955-974
doi: 10.20870/oeno-one.2020.54.4.3861
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5), which read Table 4 on the page image; 29 of 29 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Bordeaux, Champagne, Marlborough]
processes: [phenology, flowering, veraison, ripening, climate projection]
records: []
datasets: []
files: [2020-parker-10-20870-oeno-one-2020-54-4-3861.pdf]
---

# Parker et al. 2020: GFV and GSR tested on Bordeaux, Champagne and Marlborough

The flowering-veraison model (`parker2013.gfv`) and the sugar-target model GSR (thermal
time from 1 April, base 0 °C, to 170-220 g/L for 65 cultivars; Parker et al. 2020, not
held) applied with their published F* to three new series, and Champagne's Chardonnay
projected under ALADIN-Climat. Threshold models; a validation paper.

## What it holds

- **Series:** VitAdapt, Bordeaux, 31 of 52 cultivars, 2012-2017 (l. 252-262); Oyster Bay,
  Marlborough, Sauvignon blanc 2004/05-2019/20 (from 2011/12 the 8 °Brix date comes from
  a softness correlation, l. 241-248); Champagne Chardonnay, 58 regional years 1961-2019
  (flowering averages and harvest dates, no veraison; Table 4 note, l. 533-546).
- **Scores** (Table 4, p. 8): VitAdapt flowering RMSE 4.70 d (EF 0.55), veraison 5.07,
  sugar target 6.52; Oyster Bay 6.67, 4.67 and 9.67 d (negative EF for flowering and
  target); Champagne flowering 6.83 d (bias −4.05) and the 170 g/L target 7.12 d, which
  the text calls a week or less (l. 515-537, 727). 94 % of VitAdapt cultivars within a
  week at flowering, 87 % at veraison, 70 % at 190 g/L (l. 562-565).
- **F* used:** Chardonnay flowering 1,217 and 170 g/L 2,723 °C·d; Sauvignon blanc 1,282,
  2,528 and 200 g/L 2,820 (l. 267-290).
- **Champagne projections:** flowering −0.098 d/yr (RCP4.5) and −0.221 (RCP8.5), the
  sugar target −0.214 and −0.490 d/yr (l. 714-725); the abstract's veraison projection
  and the discussion's 5 and 10 d by 2100 do not match the results (l. 46, 698, 883).

## Dependence

- **Computes** `parker2013.gfv` and GSR as published, nothing refitted; the same authors.

## Bearing (2026-10-13)

- The transfer error of GFV with fixed F*: 5-7 d at new sites, worse in Marlborough.
