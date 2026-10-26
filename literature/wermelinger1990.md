---
id: wermelinger1990
citation: Wermelinger, B. & Koblet, W. 1990. Seasonal growth and nitrogen distribution in grapevine leaves, shoots and grapes. Vitis 29:15-26
doi: 10.5073/vitis.1990.29.15-26
read: 2026-10-26, in full, by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py; the Fig. 2, 3 and 5 regressions (printed pp. 18, 19, 21) read in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Wädenswil]
processes: [leaf growth, leaf area, specific leaf area, shoot growth, nitrogen, degree-days]
records: [wermelinger1990.leaf_growth]
datasets: [wermelinger1990.waedenswil]
files: [wermelinger1990.pdf (the 2026-10-25 other-sources drop)]
---

# Wermelinger & Koblet 1990: one season of Pinot noir organ growth on degree-days

Destructive samples through 1988 at Wädenswil give leaf area, dry mass, water and nitrogen
of primary leaves, laterals, shoots and grapes against degree-days above 10 °C: the data
behind the closed Wermelinger et al. 1991 demographic model.

## What it holds

- **Site** (l. 56-70): FAW Wädenswil, 1988; 18-year-old Blauburgunder (Pinot noir) clone
  Mariafeld on 5 C, 2.2 m × 1.1 m; budburst 21 April, harvest 17 October (l. 67-68); six
  shoots per date, weekly to mid June and then every 3-5 weeks.
- **Clock** (l. 83-97): degree-days above 10 °C by sine integration of daily maximum and
  minimum (credited to Frazer & Gilbert 1976, an insect paper); 1155.3 dd in 1988 against
  1121 ± 5.4 on average; budburst at 35.8 dd, bloom 335, harvest 1135 (l. 95-101).
- **Primary leaves** (l. 108-121, 166): about 200 cm² and 1.5 g dry mass at full size;
  dry mass grows 0.0043 g per dd below 250 dd and 0.0006 g per dd after; specific leaf area
  peaks at 0.022 m²/g near 150 dd; longevity about 900 dd (120 d).
- **Fits on leaf age x in dd** (page images; n not printed): water content % y = 79.56 -
  4.04e-2 x + 6.73e-5 x² - 3.89e-8 x³, r² 0.71 (Fig. 2 B); N % y = 6.45 - 1.69e-2 x +
  2.48e-5 x² - 128e-8 x³ as printed (1.28e-8 by the curve), r² 0.95 (Fig. 3 A); N per leaf
  (mg) y = -15.17 + 0.33 x - 8.56e-4 x² + 9.19e-7 x³ - 3.59e-10 x⁴, r² 0.75 (Fig. 3 B).
  Figs 1 and 2 A are Lowess curves (l. 153, 208).
- **Shoot against leaf dry mass per vine** (Fig. 5, l. 360): y = -20.29 + 1.64 x, r² 0.98,
  before leaf fall; shoot mass rises 1.6 times as fast as leaf mass.
- **Totals** (l. 329, 368, 437, 495-497): 14.2 shoots and 1.8 clusters a shoot per vine; leaf
  mass per shoot peaks at 29 g; grapes 63 g a shoot, berries 273 mg at 0.4 mg per dd; per
  vine 6.40 m² of leaf area and 8.9 g of leaf N at 845 dd, 797 g of grapes.
- **Not printed:** n for any fit, how per-vine totals were scaled from six shoots, the sine
  formula.

## Dependence

- **Fitted to** its own samples (`wermelinger1990.waedenswil`): observed, no model in them.
- **Feeds** Wermelinger, Baumgärtner & Gutierrez 1991 (Ecol. Model. 53:1-26), "submitted"
  (l. 610) and not held; Gutierrez et al. 1985 is cited for the earlier grape model.

## Bearing (2026-10-26)

- For Agrarium's vine growth truth (the 10-14 search): a whole season of leaf area and mass
  per shoot and per vine on a 10 °C degree-day clock, Pinot noir, one year. The 6.40 m² per
  vine at 845 dd is a direct value for `host.leaf_area_max_m2` in a cool climate. The record
  holds the printed fits, tagged growth on thermal time like `lebon2004.leaf_development`;
  the engine's shoot models carry the degree-day-phenology tag instead, so stemma lists no
  engine kin (kin report 2026-10-26): whether those records should also carry this tag is
  a question for Agrarium's PLAN section 15.
