---
id: lebon2004
citation: Lebon, E., Pellegrino, A., Tardieu, F. & Lecoeur, J. 2004. Shoot development in grapevine (Vitis vinifera) is affected by the modular branching pattern of the stem and intra- and inter-shoot trophic competition. Annals of Botany 93(3):263-274
doi: 10.1093/aob/mch038
read: 2026-10-15, in full, by a reading agent (claude-haiku-5-5); 58 of 58 quotes found at their lines by scripts/verify_quotes.py; printed pp. 266 and 268 (Eqs 1-3, the 93-leaf allometry, Eqs 5-8 and Tb) read in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Montpellier]
processes: [leaf appearance, base temperature, leaf expansion, shoot architecture]
records: [lebon2004.leaf_development]
datasets: [lebon2004.montpellier]
files: [mch038.pdf]
---

# Lebon et al. 2004: leaf development of Grenache N on thermal time

Four experiments on Grenache N at Montpellier, two in pots and two in a vineyard, all with no
water deficit. The main stem makes leaves as a straight line in degree-days above a base; the
branches do not. This is the paper the later Montpellier shoot models take their base
temperature and leaf-appearance rule from.

## What it holds

- **Experiments** (l. 95-101, 217-249): Grenache N clone 226 on Fercal in pots (0.30 m
  across, 0.70 m high; expt 1 in a glasshouse, expt 2 moved outside), and clone 70 on 110
  Richter in a vineyard planted 1987 (0.432 plants/m², rows 2.35 m, short-pruned espalier;
  expts 3 and 4, 1999 and 2000). The years of the pot runs conflict: the text says 1999 and
  2000 (l. 100), Tables 1-2 and the figure captions say 2000 and 2001 (l. 436-437). Both are
  kept.
- **Counts** (l. 332-346, 401): leaves counted every 3-4 d on six shoots (expt 1) and 12
  shoots (expt 2), weekly on nine shoots (expts 3 and 4); leaf lengths on six shoots every
  2-4 d; 93 extra leaves from expt 3 for the area fit (l. 393).
- **Thermal time** (Eq. 3, l. 419-426): the daily integral of the mean temperature above Tb,
  from budbreak; Tb is 10 °C in the analysis (l. 421, 552), the method after Bonhomme 2000.
- **Leaf appearance rate on temperature** (Eq. 5, l. 545): LAR = 0.0430 Tm - 0.3946 leaves
  per day (r² 0.837, n 376), fitted over periods of 9-15 d at 13.0-23.8 °C (l. 527). One
  line fits all four experiments (F 1.22, not significant, l. 537). Rates ran from 0.097 to
  0.770 leaves per day (l. 541).
- **Base temperature** (l. 547, 552): Tb = -b/a = 9.2 ± 0.5 °C (the print does not say SD or
  SE). It is "slightly lower" than 10 °C, and 10 °C was kept as the standard value.
- **Leaves on the main stem against CDD from budbreak** (Eqs 6-8, l. 548-551):
  initiated 0.050 CDD + 7.85 (r² 0.993); unfolded 0.046 CDD + 0.36 (r² 0.986, n 186, l. 567);
  expanded 0.038 CDD - 5.27 (r² 0.991, n 42). So about 22 °Cd a leaf unfolded. The same
  lines hold in the glasshouse and the field.
- **Leaf expansion** (l. 579, 598-599): the duration is 366 and 425 °Cd at phytomers 10 and
  20; it grows by about 25 °Cd a phytomer up to the tenth, then by about 5.
- **Leaf area** (l. 394): LA = 0.0075 L² + 0.07505 L - 29.151 (r² 0.901, n 93), the quadratic
  form of Schultz 1992. The units of L and LA are not printed.
- **Per-leaf logistic** (Eq. 1, page image): area = a / (1 + exp(4c (b - CDD)/a)) from leaf
  initiation. The values of a, b and c are not printed, only plotted (Fig. 5).
- **Internodes** (l. 587): length rises to phytomer 12, then stays near 100 mm.
- **Branches** (l. 606-643, 726): branches from P0 phytomers (R0) make more leaves, for
  longer, than R1 and R2. Their rate against thermal time is not linear and no relation is
  fitted. About 15 % of branches stopped completely (l. 629); in expt 4 up to 25 % of R0 and
  50 % of R1 and R2 (l. 642). Branches stop 200-300 CDD after their own budbreak (l. 726).
- **Totals at harvest** (Table 3, l. 454-456): 29.7, 28.3 and 30.3 main-stem leaves at 618,
  603 and 685 degree-days (expts 1, 3, 4); branch leaves 107.0, 53.5 and 65.7. The origin of
  the harvest time is not stated.
- **Not printed:** budburst or other stage dates, fitted branch relations, the values of
  Eq. 1.

## Dependence

- **Borrowed:** the framework of three linear thermal-time stages from annual crops
  (Rickman and Klepper 1995, l. 27, 133-135); the leaf-area quadratic from Schultz 1992
  (l. 391); the CDD method from Bonhomme 2000 (l. 421); 10 °C from Winkler et al. 1974 and
  Jackson and Cherry 1988 (l. 549).
- **Fitted** to the authors' own four experiments; no other model's output.
- **Borrowed from here:** Pallas 2008 (pallas2008.shoot_development) and Louarn 2007
  (louarn2007.shoot_architecture) take the base and the leaf-appearance rule from this paper
  and compute the same rule. Schmidt 2019 uses 10 °C after Schultz 1992. Shared authors
  (Lebon, Lecoeur) with those papers are a flag only.

## Bearing (2026-10-14)

- **The base and the rule:** 9.2 °C fitted and 10 °C used; 0.046 unfolded leaves per °Cd,
  about 22 °Cd a leaf. This is what Pallas 2008, Louarn 2007 and Schmidt 2019 build on.
- **Usable as a rate on temperature:** 0.043 leaves per day per °C above 9.2 °C is the one
  printed rate-temperature response for leaf appearance. A truth could use it without a heat
  sum as such, though it is the same rule written per day.
- **Kin to the engine by form** (growth on thermal time). Said so, not hidden. No stage
  dates, and no branch relation to run.
