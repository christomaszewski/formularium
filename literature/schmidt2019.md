---
id: schmidt2019
citation: Schmidt, D., Bahr, C., Friedel, M. & Kahlen, K. 2019. Modelling Approach for Predicting the Impact of Changing Temperature Conditions on Grapevine Canopy Architectures. Agronomy 9(8):426
doi: 10.3390/agronomy9080426
read: 2026-10-14, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; p. 7 (Eqs 3-4, Figures 3-4) read in the page image by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Geisenheim, Rheingau]
processes: [canopy architecture, phyllochron, internode growth, leaf area, budburst]
records: [schmidt2019.virtual_riesling]
datasets: [schmidt2019.geisenheim]
files: [dominik_2019.pdf]
---

# Schmidt et al. 2019: Virtual Riesling, a canopy model on thermal time

A functional-structural model of a Riesling vine (Virtual Riesling, built in GroIMP):
phytomers appear, internodes and leaf veins grow, and laterals break bud, all as functions
of thermal time. It is run for six years of Geisenheim weather to see how temperature moves
the canopy's architecture.

## What it holds

- **Data** (l. 139-216): three Riesling vines (clone 198-30 Gm on SO4, planted 2012,
  0.9 m by 1.8 m) of the VineyardFACE at Geisenheim, digitised in 3D at E-L 12, 15 and 26
  in May-June 2018 (l. 180-182); 50 primary shoots in the bud-position analysis
  (l. 468-470); bud break scored from DOY 109 (l. 331-333). Weather is DWD station 1580,
  about 200 m away, 1927-2018 (l. 209-216).
- **Thermal time** (Eq. 1, l. 343): base 10 °C from daily maximum and minimum, after
  Schultz 1992. Where Tb sits in the sum is not settled by the print (l. 337-340).
- **Budburst:** 2018 predicted at DOY 111 with a posterior SD of 12.38 °Cd (l. 347, 349).
  Other years use Nendel 2010's single-triangle degree-day sum from 1 March: T0 5.9 °C,
  threshold 186.1 °Cd, SD 24.7 °Cd (l. 350-366).
- **Phyllochron** (l. 376-377): 0.0453 phytomers per °Cd, so 22.0892 °Cd per phytomer.
- **Primary internodes** (Eqs 3-4, p. 7; l. 412, 449): IL1 = IL1max(rank) (1 - exp(-exp(k)
  THTage)), k = -3.1812. Eq. 4 prints a1 -0.5562, b1 1.5729, a2 0.7212, b2 9.0909.
- **Lateral internodes** (l. 459): k = -3.9706. **Lateral budburst** (Eqs 8-9, l. 598-601):
  337.0334 - 18.5344 per rank °Cd, floor 66.2676 °Cd (3 phytomers); SD 27.98 °Cd (l. 599).
- **Leaf veins** (l. 662-675): primary k = -4.1819; lateral maximum 11.9418, k = -3.0008.
- **Leaf area** (Eq. 10, l. 649): sqrt(LA) = sLA times the summed secondary vein length,
  sLA = 0.6869294, fitted to 302 leaves (l. 647-648). The text layer prints LA = sLA L; the
  page image shows the square root, which is used.
- **Run** (l. 749-750, 905): 2000 runs a year of three plants; a run ends when 90 % of
  shoots reach 2.3 m. In 2018 it ends at DOY 174, 63 days (l. 1506); 1987 took 94 (l. 1484).
- **Outputs, not fits:** leaf area per shoot 0.5-1.3 m² at the end (l. 1512; Schultz 1992's
  0.27 m² for primary shoots is cited, l. 1514); LAI about 3.8 quoted from Siegfried et al.
  (l. 1572); leaf area density up to 30 m²/m³ above the bunch zone (l. 1612).
- **Not settled:** Eq. 4 as printed (a1 -0.5562, b1 1.5729) gives negative maxima for
  ranks 3-7, while Figure 4 shows 1.0 at rank 1 and 10.4 at rank 7. a1 1.5729 and b1
  -0.5562 reproduce the figure (1.02 and 10.45). The record keeps the print; the swap is
  a reading, confirmed on the page image by the main session. The simulated years are
  listed without 1979 at l. 322 but 1979 is in the tables (l. 228). Table 2's ± values
  for temperature are implausible; Table 3 prints 917 ± 108 leaves for both 1940 and 2018.
- **Not printed:** budburst to 10 cm shoots, flowering, BBCH 53, bunch number, canopy
  porosity, canopy width as numbers.

## Dependence

- **Borrowed:** Eq. 1 after Schultz 1992 (l. 335-336). Budburst in other years is Nendel
  2010's model with his threshold, and the degree-day method is Zalom & Goodell 1983's
  (l. 350-351): a borrowed equation and a borrowed threshold. The leaf-area form is Beslic
  et al. 2010's (l. 642-643); the leaf-density cube method follows Schultz 1995 (l. 924).
- **Shared data:** sLA is fitted to 302 leaves that Döring et al. provided (l. 647-648):
  shared calibration data, not a model.
- **Fitted** to the authors' own digitised shoots and 2018 phenology. No fit uses another
  model's output.

## Bearing (2026-10-14)

- **Growth on thermal time, kin to the engine by form:** phyllochron, internode and leaf
  curves run on degree-days above 10 °C, and budburst is a degree-day threshold. A kin
  report lists it with the engine's degree-day pieces. Said so, not hidden.
- **Usable numbers:** the phyllochron (22 °Cd per leaf, base 10 °C) and the leaf area per
  shoot range. It prints no stage dates beyond budburst and no canopy porosity, and it
  needs its own code (GroIMP or similar) to run. Three vines of one cultivar in one year.
