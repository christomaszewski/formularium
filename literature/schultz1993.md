---
id: schultz1993
citation: Schultz, H. R. 1993. Photosynthesis of sun and shade leaves of field-grown grapevine (Vitis vinifera L.) in relation to leaf age. Suitability of the plastochron concept for the expression of physiological age. Vitis 32:197-205
doi: 10.5073/vitis.1993.32.197
read: 2026-10-26, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Eq. 3 and the Fig. 1 caption (printed pp. 199-200) read in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Geisenheim]
processes: [leaf appearance, plastochron, base temperature, photosynthesis, leaf age]
records: [schultz1993.plastochron]
datasets: [schultz1993.geisenheim]
files: [schultz1993.pdf (the 2026-10-25 other-sources drop)]
---

# Schultz 1993: plastochron duration of Riesling against thermal time, and leaf age for photosynthesis

The time a Riesling shoot takes to make one leaf, the plastochron duration (PD), falls
exponentially with the thermal time per day to a floor, with a base near 10 °C early in the
season and a base that rises as the season goes on. The paper's point is that leaf age in
plastochrons, not days, orders the photosynthesis of sun and shade leaves. It is the nearest
held thing to the closed Schultz 1992 leaf model, which it cites but does not print.

## What it holds

- **Site and material** (l. 99-101): a 9-year-old White Riesling, clone 198 Gm on 5 C, at
  Geisenheim (50° N, 8° E), 1987 and 1988.
- **Clock** (l. 112-115): thermal time (TT, °C d per day) from daily maximum and minimum
  with a 10 °C base, from stage 05 (or bud break in Fig. 3 B, l. 414); the alternative uses
  mean daily temperature (MDT) with no threshold (l. 149).
- **Plastochron index** (Eqs 1-2, l. 126-137; Erickson & Michelini 1957): PI from the leaves
  longer than a 30 mm reference lamina, LPI = PI - i.
- **Eq. 3** (l. 143): PD = PD(max) exp(-k TT) + PD(min), PD in days; fitted by PROC NLIN to the
  PI and LPI of 5-10 sun and shade shoots recorded every 1-3 d in 1988 (l. 150-151). The unit
  of k and the number of points per fit are not printed (l. 148).
- **Fits** (Fig. 1 caption, page image): TT 100-240 °C d (May-June) PD(max) 14.4, PD(min)
  2.2 d, k 0.33, R² 0.91; TT 240-670 (B) 65.7, 3.3, 0.74, 0.95; TT 670-980 (August-September)
  107.6, 4.0, 0.58, 0.87. MDT form: (A) 415.8, 1.8, 0.33, R² 0.88; (B) 15350.9, 3.2, 0.63,
  0.95; (C) 2104.4, 3.4, 0.39, 0.83.
- **What the fits say** (l. 187-202): PD nears its minimum at about 8 °C d per day of TT, or
  17 °C MDT; the lower threshold is close to 10 °C MDT in the rapid-growth phase, then the
  responsiveness falls: at TT 4 and 12 °C d per day a plastochron took 14 and 4 d in August
  against 6 and 2 d in May-June. No upper threshold was reached. PD did not depend on canopy
  light (data not shown, l. 262-263).
- **Photosynthesis** (l. 330-343): Amax came 15-20 d later in 1987 than 1988; shade leaves
  older than LPI 5 had lower rates; the A-LPI slope stayed constant until TT about 1000.
  Fig. 5 recalculates Kriedemann et al. 1970 and Alleweldt et al. 1982 with this paper's PD
  of 2.2 d and LPI -1 at unfolding (l. 548-554), an assumption.
- **Not printed:** the TT formula, k's unit, points per fit, residuals, whether sun and shade
  shoots were pooled (l. 150-153).

## Dependence

- **Fitted to** its own 1988 Geisenheim shoots (`schultz1993.geisenheim`); the temperatures
  are observed, nothing model-dated.
- **Cites** Schultz 1992 only for plastochrons varying with decreasing leaf appearance (l. 81)
  and for the approach used on shoot growth and leaf area (l. 259): no 1992 number is printed
  here. Winkler & Williams 1939 and Gutierrez et al. 1985 for the 10 °C base (l. 191-193).
- Shares the author with Weyand & Schultz 2006 and the closed Schultz 1992: a flag only.

## Bearing (2026-10-26)

- For Agrarium's vine growth truth (the 10-14 search's leaf-appearance question): a printed
  leaf-appearance rate against temperature for Riesling, piecewise by season, with the base
  rising from 10 °C. It is kin to `lebon2004.leaf_development` by form (a rate-temperature
  response); no engine record carries that tag, so stemma lists it as independent of the
  engine (kin report 2026-10-26). The Schultz 1992 model that VitiMeteo runs stays
  unobtained.
