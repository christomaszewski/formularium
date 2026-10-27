---
id: weyand2006
citation: Weyand, K. M. & Schultz, H. R. 2006. Light interception, gas exchange and carbon balance of different canopy zones of minimally and cane-pruned field-grown Riesling grapevines. Vitis 45(3):105-114
doi: 10.5073/vitis.2006.45.105-114
read: 2026-10-26, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Eq. 1 and the leaf-area methods (printed p. 107) read in the page image by the agent
status: read
diseases: []
crops: [grapevine]
regions: [Geisenheim]
processes: [leaf area per vine, light interception, carbon balance, respiration, training system]
records: []
datasets: [weyand2006.geisenheim]
files: [weyand2006.pdf (the 2026-10-25 other-sources drop)]
---

# Weyand & Schultz 2006: leaf area, light and carbon of minimally and cane-pruned Riesling

Two seasons at Geisenheim compare a minimal-pruned (MP) Riesling canopy with a cane-pruned
VSP one: three times the leaf area, more light caught, and a daily carbon gain per vine
three to six times higher, on a canopy cut into eight zones. The paper runs the Schultz
1991 respiration and Schultz 1992 shoot models, printing neither's coefficients.

## What it holds

- **Site** (l. 17, 106-123): Riesling Gm 198 on 5C planted 1977 at Geisenheim (50° N, 8° E),
  2002 and 2003; VSP with a cordon at 1.1 m and 3-4 canes of 5-6 buds, MP on a catch wire
  at 1.8 m.
- **Vines** (l. 84-89, 421): buds per vine MP 171.8, VSP 14.2; shoots 136.8 and 13.4; bud
  break 78.8 and 95.6 %; yield 26.4 and 11.7 t/ha (6.3 and 2.8 kg a vine, MP 225 % of VSP).
- **Leaf area** (l. 208-215, 181-182): maximum near veraison 2002 of 15.2 m² a vine for MP
  and 5.2 for VSP, MP about three times VSP through the season; leaf area from leaf weight
  with R² 0.69-0.86; LAI by date is in Fig. 2 only.
- **Light** (l. 146-147, 214): ceptometer grids on 8 May, 18 June, 15 August and 1 October
  2002; interception at season end 76 % (MP) and 63 % (VSP).
- **Carbon** (l. 504-521, 474, 548): gain on 28 May 2002 (BBCH 17) 18.5 g C a vine a day for
  MP and 3.29 for VSP; 15 August 2003 22.43 and 10.28; respiration 4-7 % of the gain; sugar
  at harvest VSP 21.8-23.2 °Brix, MP 20.8.
- **Models run** (l. 131-134, 149, 169-175): canopy segments from Zimmer 1998 and the
  Schultz 1992 shoot model; night respiration DR = a exp(k T) (Eq. 1) by Schultz 1991 in six
  phases, a, k and Q10 not printed (l. 437); A against time as polynomials per zone and a
  third-order polynomial for leaf area between sampling dates, coefficients not printed.
- **Lead check:** no 0.27 m² a shoot and no 1987 value appear; Schultz 1992 is cited for
  leaf area from lamina length and for the shoot model (l. 139, 149, 174); Riou et al. 1989
  is named for comparison only (l. 325-326), not run. The summary's "17 times" is not what
  the table gives (buds 12.1 against shoots 10.2 per vine).

## Dependence

- **Computes** Schultz 1991's respiration and Schultz 1992's shoot and leaf-area models,
  neither held nor printed here; Lebon & Schultz 1996's canopy segmentation.
- **Fitted to** nothing new: a measurement paper (`weyand2006.geisenheim`). Observed, no
  model-dated values. Schultz again (a flag beside schultz1993).

## Bearing (2026-10-26)

- For Agrarium's `host.leaf_area_max_m2` and the 10-14 growth search: 5.2 m² a vine for a
  cane-pruned Riesling VSP and 15.2 m² for minimal pruning, 2002, with interception 63 and
  76 %. No formulation to record; the carbon gains are a yardstick for a canopy model.
