---
id: bindi1997b
citation: Bindi, M., Miglietta, F., Gozzini, B., Orlandini, S. & Seghi, L. 1997. A simple model for simulation of growth and development in grapevine (Vitis vinifera L.). II. Model validation. Vitis 36(2):73-76
doi: 10.5073/vitis.1997.36.73-76
read: 2026-10-14, in full, by a reading agent (claude-haiku-5-5), which read Tables 1-3 on page images; 56 of 56 quotes found at their lines by scripts/verify_quotes.py; Table 1 (p. 73) read in the page image by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Chianti, Tuscany]
processes: [vine growth, biomass, model validation]
records: [bindi1997.growth]
datasets: [bindi1997.mondeggi]
files: [bindi_1997b.pdf]
---

# Bindi et al. 1997 (II): the whole-vine model on two more seasons and a second cultivar

The part I model (`bindi1997.growth`) run unchanged on Sangiovese in 1993 and 1994 and,
with three constants refitted on a 1992 Santa Cristina trial, on Cabernet Sauvignon: dry
matter per vine within 10-12 % on average, leaf area only shown in a figure, and a
sensitivity test of temperature and radiation.

## What it holds

- **Data:** Sangiovese, 20-year-old vines at Mondeggi-Lappeggi (clay loam) and Cabernet
  Sauvignon, 25-year-old vines at Santa Cristina (clay), both Chianti; validation years
  1993 and 1994, independent of the 1992 calibration, parameters held constant (l. 40-58).
- **Cabernet set** (Table 1, p. 73): leaf-area exponent f 2.06 (Sangiovese 2.13), radiation
  use efficiency 0.691 g/MJ (1.001), fruit-share slope 0.00328 a day (0.00443), from the
  1992 Santa Cristina experiment (l. 28-45); the phenology constants are not restated.
- **Fit** (Table 2): fruit dry matter MBE 1.93 g a vine (Sangiovese) and MAE 40.8
  (Cabernet); total dry matter MBE 58.2 and 38.9; modelling efficiency 0.945-0.978; mean
  absolute error 9.9-11.8 %, bias −0.7 to 2.7 %; paired t-tests not significant
  (l. 143-164). Total biomass over-predicted late in the warm, dry 1994 (l. 220-225).
- **Leaf area** (Fig. 4, read off the axes): about 16.5 m² a vine observed for Sangiovese
  by day 242 against 22 simulated; Cabernet 14 against 18; no error statistic printed.
- **Sensitivity** (Table 3): radiation ±20 % moves fruit and biomass by about ±20 %;
  temperature by −11 to +15 %, with rows that are not monotonic (l. 277-294).

## Dependence

- **Computes** `bindi1997.growth` on the authors' own observations; the fruit-priority
  assumption cited to Ho et al. 1989.

## Bearing (2026-10-14)

- The transfer test of the one printed whole-vine model: a second cultivar needed three
  constants refitted and one season over-predicted; leaf area is the weakest output,
  which is the one the truth needs.
