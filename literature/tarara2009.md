---
id: tarara2009
citation: Tarara, Julie M., Blom, Paul E., Shafii, Bahman, Price, William J. & Olmstead, Mercy A. 2009. Modeling seasonal dynamics of canopy and fruit growth in grapevine for application in trellis tension monitoring. HortScience 44(2):334-340
doi: 10.21273/HORTSCI.44.2.334
read: 2026-10-14, in full, by a reading agent (claude-haiku-5-5), which read Eqs 1-2 on the page image; 57 of 57 quotes found at their lines by scripts/verify_quotes.py; Table 1 (p. 337) read in the page image by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Washington, Prosser]
processes: [vine growth, shoot elongation, leaf number, canopy mass, fruit growth]
records: [tarara2009.canopy_logistic]
datasets: [tarara2009.prosser]
files: [julie_2009.pdf]
---

# Tarara et al. 2009: logistic shoot and fruit growth on degree-days, five Concord seasons

Shoot length, leaves per shoot, and vegetative and fruit mass per shoot of own-rooted
Concord near Prosser, sampled destructively every two to three weeks over 2002-2006 and
fitted as logistic curves of degree-days above 10 °C from 1 January, with standard
errors: the cleanest printed growth curve the search found, on a labruscana vine.

## What it holds

- **Data** (`tarara2009.prosser`): 0.34 ha planted 1981, bilateral cordon at 1.7 m, rows
  3.0 × 2.4 m, deficit-irrigated to 2004 and watered in 2005 (l. 86-123); 10 shoots from
  each of four vines per date (n 1,360 over five seasons), shoot length on 54 vines
  (l. 136-175); thermal time by trapezoidal integration of 15-minute air temperature,
  base 10 °C, no cap (l. 88-97).
- **Curves** (Eq. 1, Table 1, pp. 336-337; `tarara2009.canopy_logistic`): y = A / (1 +
  exp(−B (DD − D_A))); shoot length A 82.0 cm, B 0.009, D_A 301 °C·d; leaves per shoot
  12.0, 0.011, 253; vegetative mass 47.1 g, 0.011, 330; fruit mass 72.3 g, 0.013, 599,
  the fruit fits "not well described" (l. 281); the fruit-to-vegetative ratio fits worse
  (l. 304). Shoot length within 5 % of its maximum at 635 °C·d (8-13 July), leaves at 552
  (27 June to 2 July), vegetative mass at 598 (l. 158-163, 228-229).
- **Allometry:** vegetative mass 0.678 SL − 7.25 g (R² 0.87), 4.431 LN − 8.31 (R² 0.83),
  both together R² 0.92 (l. 201-208); fruit mass tied to cluster count only above 25 g a
  shoot, from about 530-550 °C·d (l. 271-275, 334).
- **Form:** growth on thermal time; the degree-day clock is the engine's, and the day a
  shoot reaches a length is a degree-day threshold on the curve.

## Dependence

- **Fitted to** the authors' own samples; thermal time after Tobin et al. 2001; an earlier
  logistic of leaf area on thermal time is cited (l. 380). **Kin to the engine** (kin
  report 2026-10-14): the same form as the six degree-day pieces; Tarara is an author of
  `ferguson2011.hardiness` (a flag only).

## Bearing (2026-10-14)

- The truth's leaf-area curve (a logistic in days) has a published twin here in
  degree-days, with its half-growth point at 300 °C·d and saturation by early July; but
  on the engine's clock, and for a labruscana vine under deficit irrigation. The
  mass-from-length lines are usable allometry.
