---
id: vanleeuwen2023
citation: van Leeuwen, C., Destrac-Irvine, A., Gowdy, M., Farris, L., Pieri, P., Marolleau, L. & Gambetta, G.A. 2023. An operational model for capturing grape ripening dynamics to support harvest decisions. OENO One 57(2):505-524
doi: 10.20870/oeno-one.2023.57.2.7399
read: 2026-10-27, in full in reading order; Figures 2-7 are plots and were not read in images; by a reading agent and note writer (claude-sonnet-5-5); 16 of 16 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Bordeaux, Pessac-Leognan, Saint-Emilion]
processes: [berry ripening, sugar to total acidity ratio, degree days, mid-veraison, harvest date, vine water status]
records: []
datasets: []
files: [dr1027_vanleeuwen2023.pdf (2026-10-27, from Chris)]
---

# van Leeuwen et al. 2023: ripening speed as the slope of sugar to acid ratio against degree days, 53 varieties in Bordeaux

A two-parameter linear model of the sugar to total acidity ratio (S/TA) against thermal summation in the first four weeks after mid-veraison, fitted per variety, year and soil on two Bordeaux data sets.

**Read this first.** The model is a straight line fitted to weekly berry samples after veraison, so it needs observed sugar and acid to give its slope (alpha); it does not predict ripening from weather alone. There is no sugar or acid equation of time or heat that runs forward from veraison without those samples. The fitted slopes by variety and year are only in box plots (Figs. 3A, 3B, 4A), not read here.

## What it holds

- **Model (l. 159):** y = alpha x + beta, y = S/TA, x = thermal summation; alpha is the ripening speed and -beta/alpha is a proxy for the thermal summation at mid-veraison, where S/TA is near zero (l. 162-164). Taken from Duteau 1990 (l. 162).
- **S/TA:** reducing sugar (g/L) over total acidity as tartaric acid (g/L), times 100 so that alpha exceeds 1 (l. 268). It uses the first four weekly samples after mid-veraison; a five-sample fit changed mean R2 by +0.002 (l. 275-278, grep).
- **Heat sum (l. 286, l. 295):** sum of average daily temperature (degC) from 1 July (DOY 182) to the day before sampling; base temperature 0 degC after Parker et al. 2011; no upper cap (the paper notes the model is linear and not capped at high temperature, l. 516-517, grep). Duteau used 1 August; 1 July avoids negative x for early veraison. Because no sample precedes mid-veraison, the start date does not change the slope (l. 304-306, grep).
- **Fit:** R2 0.98 to 1.00 for the linear approximation (l. 359).
- **Data 1 (l. 269):** VitAdapt common garden at the ISVV campus, Villenave d'Ornon (Pessac-Leognan); 53 varieties (21 white, 32 red) with five replicates, planted 2009, data 2012-2022 with 2012 discarded for young-vine water deficit (l. 272-276, grep). Mean temperature in the 28 days after veraison ranged 19.8 degC (2013) to 25.0 degC (2022) (l. 515).
- **Data 2 (l. 246):** dry-farmed Saint-Emilion, Merlot (clone 181) and Cabernet franc (clone 326) on 3309C, grafted 1994, three soils (gravel, clay, sand with a water table), data 2004-2016.
- **Drivers of alpha (l. 358):** year 41.2 % of variance and variety 25.5 % in Data 1; year 45.0 %, soil 14.5 % and variety 5.5 % in Data 2 (ANOVA). Alpha is 29 % smaller on sand with a water table than on clay for Merlot in 2005 (l. 365).
- **Berry weight (l. 395):** the only significant term in a stepwise regression on Data 2 (11.6 % of variance, larger berries slower; R2 0.323 Merlot, 0.095 Cabernet franc). Veraison date, delta13C, leaf area to fruit weight and yield were not significant.
- **Water status (l. 459):** with the season's lowest pre-dawn leaf water potential, alpha rises with deficit down to about -0.8 MPa and then falls (LOESS, Fig. 5 not read in image); few severe-stress points, two varieties.
- **Mid-veraison from -beta/alpha (l. 449):** correlation 0.85 (Data 1) and 0.95 (Data 2) with observed dates; RMSE 9.44 and 2.77, printed without a unit (the text speaks of days). Early bias of three to seven days in Data 1 and two to three days in Data 2 (l. 598, grep).
- **Varieties (l. 580-584, grep):** Grenache fastest, Colombard slowest with alpha about half of Grenache's (Fig. 3B ranking not read in image).

## Dependence

- Builds on Duteau 1990 (not held) for the linear S/TA form, and on Parker et al. 2011 (parker2011) for the base temperature of 0 degC. The GFV phenology model (Parker et al. 2011, 2013: parker2011, parker2013) is named for estimating mid-veraison (l. 573); this paper gives its own -beta/alpha estimate instead.
- Fitted to the authors' two data sets only. Compared with Sadras and Petrie 2011 (sugar only, not held) and Suter et al. 2021 (not held) in the discussion.
- Authors: Pieri is an author here, of gowdy2022 and of Pieri 2010; a flag only, not held. Shares no equation with the wetness pieces of the engine.

## Bearing (2026-10-27)

- **Host ripening for the truth:** a post-veraison ripening clock in degree days at base 0 degC from 1 July, with a speed that depends on year, variety (about a factor of two between varieties) and soil. It gives no veraison date from weather (only -beta/alpha back-estimated from samples), so Agrarium would still need a phenology model such as GFV for the start. Kind of result: an empirical linear fit on two Bordeaux data sets, validated against the same data.
- **For berry susceptibility:** S/TA is a ripeness index, not a berry-age or berry-size measure; it says nothing about when berries stop being susceptible to downy mildew. Not shown: any sugar or acid in g per berry, any disease link, any temperature response above 25 degC.
- **Water status:** alpha is not driven by delta13C here; a possible rise then fall with pre-dawn potential near -0.8 MPa rests on one plot of two varieties. Not usable as a response function without the figure.
- **Place:** Bordeaux, Merlot, Cabernet franc and 51 other varieties; nothing from Catalonia or other climates.
