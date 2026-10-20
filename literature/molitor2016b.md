---
id: molitor2016b
citation: Molitor, D., Baus, O., Hoffmann, L. & Beyer, M. 2016. Meteorological conditions determine the thermal-temporal position of the annual Botrytis bunch rot epidemic on Vitis vinifera L. cv. Riesling grapes. OENO One 50(4):231-244
doi: 10.20870/oeno-one.2016.50.4.36
read: 2026-10-20, in full, by a reading agent (claude-haiku-5-5); 56 of 56 quotes found at their lines (within one line, ignoring the text layer's 0x0F word separators) by the main session's check; eq. 2 read in the page image (p. 234) by the main session
status: read
diseases: [grey mould]
crops: [grapevine]
regions: [Geisenheim, Rheingau]
processes: [epidemic progress, thermal time, bunch rot severity, window-pane analysis]
records: [kim2007.bacchus]
datasets: []
files: [molitor_2016.pdf (the 2026-10-20 drop)]
---

# Molitor et al. 2016: when the Riesling bunch rot epidemic comes, in degree-days

Ten seasons of untreated Botrytis bunch rot progress on Riesling at Geisenheim (fitted
2007-2013), each a logistic curve in days or in degree-days (thresholds 7, 18, 24 °C) after
flowering, with window-pane correlations against temperature, rain, leaf wetness and the
Bacchus index.

## What it holds

- One site, Geisenheim (Riesling Gm 239, planted 1982), disease scored in 2004-2013; fitted
  2007-2013 (l. 118-121, 133-134, 174-176).
- Scoring: 100 clusters per plot, four plots, seven severity classes (l. 180-189).
- No fungicide with B. cinerea activity was applied (l. 145).
- Sigmoid y = 100/(1+exp(-((x-x0)/a))) (eq. 1, l. 203-214); r2 > 0.97 (l. 295, 598-599).
- Slope factor CV 0.28 (days) and 0.18 (CDD) (l. 304-305, 598-601); CDD slope 26.6 (2013) to
  48.8 (2012) (l. 318).
- 5% severity reached at 781 (2010) to 1105 CDD (2009) (l. 330-335, Table 3).
- Thermal time base 7 C, thresholds 7, 18 and 24 C from 32 datasets (l. 146-159).
- Window-pane analysis: the thermal time of 5% correlates with temperature at veraison (days
  75-84, positive), with bloom wetness and Bacchus index (positive), with bloom temperature
  and veraison rain (negative) (l. 503-519, 588-589).
- Best r: temperature 0.9006 (50 days, day 96); leaf wetness 0.9337 (5 days, day -17);
  Bacchus 0.9727 or 0.9444 (30 days, day 79); precipitation -0.9500 (20 days, day 97) (Table
  4, l. 637-641; text l. 593-603).
- Early epidemic: 35.9 days between 2010 and 2009 at 16 C (l. 748-750); SD 12.7 days (l.
  752-753).
- Cited delays of cultural and chemical measures: 0.3 to 7.3 days (l. 725-734).
- Vintage rating vs CDD: r2 = 0.45, p = 0.03 (l. 856-857); heliothermic index: no effect (l.
  815).

## Dependence

- Its own scoring; no fungicide active against B. cinerea was applied (l. 145). Degree-days
  follow the 7-18-24 °C triplet chosen from 32 datasets (l. 146-159). It computes the
  Bacchus index of Kim et al. 2007 (eq. 2, l. 292-293) as a summary variable, not to produce
  the data. Molitor is an author of the engine's Molitor 2014 phenology
  (`molitor2014.shoots`): a flag.

## Bearing (2026-10-20)

- For a Botrytis truth's timing check: 5 % severity came at 781-1105 degree-days after BBCH
  65 and the curve's slope is steadier in degree-days than in days (CV 0.18 against 0.28);
  warm veraisons and wet flowering bring it forward. The paper prints doi 10.20870/oeno-one.2016.50.4.36 (l. 49); OpenAlex lists 10.20870/oeno-one.2016.50.3.36.
- Its eq. 2 is a third printed form of the Bacchus index, added to `kim2007.bacchus`'s flags
  (Kim's coefficients with a reciprocal).
