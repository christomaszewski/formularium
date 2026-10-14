---
id: bindi1997
citation: Bindi, M., Miglietta, F., Gozzini, B., Orlandini, S. & Seghi, L. 1997. A simple model for simulation of growth and development in grapevine (Vitis vinifera L.). I. Model description. Vitis 36(2):67-71
doi: 10.5073/vitis.1997.36.67-71
read: 2026-10-14, in full, by a reading agent (claude-haiku-5-5), which read Fig. 1 and the tables on page images; 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Table 1 and Fig. 1 (p. 68) read in the page image by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Chianti, Tuscany]
processes: [vine growth, leaf appearance, leaf area, phenology, biomass]
records: [bindi1997.growth]
datasets: [bindi1997.mondeggi]
files: [bindi_1997a.pdf]
---

# Bindi et al. 1997 (I): a whole-vine model from one Sangiovese season

The simplest published whole-vine model: leaves appear at a rate linear in the day's mean
temperature, bloom comes at 17 leaves, shoot leaf area follows leaf number, biomass is
radiation times an efficiency, and fruit growth runs between two degree-day marks. Every
constant from one 1992 season at Mondeggi (Chianti); the validation is part II
(`bindi1997b`).

## What it holds

- **Data** (`bindi1997.mondeggi`): 20-year-old Sangiovese on 420 A, 3 × 1 m, 11 buds a
  vine; shoots sampled every three weeks May-September 1992 for leaf number, leaf area,
  clusters and dry weights; sensors 10 m away (l. 29-63). Phenology indicators were
  tested on Conegliano's 1965-1970 records of 123 cultivars (l. 64, 111-118).
- **Model** (Table 1 and Fig. 1, p. 68; `bindi1997.growth`): budburst is an input
  (l. 180); leaf number rate RLF = (a + b Tmd)(1 + c SLN) with a −0.28, b 0.04, c −0.015
  (l. 88-92, after Miglietta et al. 1992, l. 176); bloom when SLN passes 17 (l. 183);
  shoot leaf area SLA = d SLN^f with d 5.39, f 2.13 (l. 93); LAI = SLA NS / (COV PLA)
  with 11 shoots, 0.75 cover, 3 m² a plant (l. 94-100); interception 1 − exp(−0.5 LAI)
  (l. 96, after Wermelinger & Baumgärtner 1991); biomass = radiation × RUE 1.001 g/MJ,
  cut by a quadratic in 0.25 Tmn + 0.75 Tmx (l. 95, 128, 256); fruit growth after LAG
  40 °C·d from bloom to MAT 1,440 °C·d above 10 °C, the fruit share rising 0.00443 a day
  (l. 89-101, 197-199).
- **Form:** the leaf rate is linear in temperature and accumulates daily, so leaf number
  is a degree-day sum above 7 °C (a/b) scaled by (1 + c SLN), and bloom at 17 leaves is
  a heat-sum threshold; the fruit phases are degree-day thresholds; leaf area is
  allometric; biomass a radiation-use chain.
- **Indicators** (Table 2): days are the steadiest predictor of budburst (CV 6-7 %),
  degree-days of bloom (CV 3.5-4.5 %) and maturity (4-5 %); Pouget's sum is worse
  (CV 13 %) (l. 147-162, 256-259).
- **Flags:** SLA = 5.39 SLN^2.13 gives about 2,250 at 17 leaves against a figure axis of
  0-2 m² (l. 93; Fig. 2); units of a-f not printed; K unsourced; the model overestimates
  vegetative mass late in fruit growth and was parameterised on one data set (l. 279-302).

## Dependence

- **Borrows** the leaf-appearance rate (Miglietta et al. 1992, the same authors), the
  interception form (Wermelinger & Baumgärtner 1991, not held) and the RUE temperature
  approach (Ritchie & Otter 1984); fitted to the authors' 1992 observations, budburst
  observed.
- **Kin to the engine** (kin report 2026-10-14): the same form as the six degree-day
  pieces (`cortazar2009.budburst`, `cortazar2009.brin`, `richardson1974.forcing_hours`,
  `ramos2017.budburst`, `molitor2014.shoots`, `cooptera.shoots_derived`), because leaf
  number and bloom run on a heat sum; Orlandini is an author of `sentelhas2008.wetness`
  (a flag only).

## Bearing (2026-10-14)

- For the truth's growth: a complete, runnable vine from budburst to maturity with every
  constant printed, but its clock is the engine's heat sum, so the phenology and leaf
  count are kin to the engine; the leaf-area allometry and the radiation-use chain are
  not. One season of one cultivar; part II tells how it transfers.
