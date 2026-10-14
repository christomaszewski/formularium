---
id: louarn2007
citation: Louarn, G., Guédon, Y., Lecoeur, J. & Lebon, E. 2007. Quantitative analysis of the phenotypic variability of shoot architecture in two grapevine cultivars. Annals of Botany 99(3):425-437
doi: 10.1093/aob/mcl276
read: 2026-10-15, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Table 1 read in the text layer by the main session, with its lost minus signs restored from the layout (Syrah expt 2 b3 is -0.0762; the eq. 6 a and c values printed with a leading 2 are negative)
status: read
diseases: []
crops: [grapevine]
regions: [Montpellier]
processes: [shoot architecture, phyllochron, branching, leaf area]
records: [louarn2007.shoot_architecture]
datasets: [louarn2007.montpellier_pots]
files: [mcl276.pdf]
---

# Louarn et al. 2007: shoot architecture of Grenache N and Syrah in pots

Two cultivars in well-watered pots at Montpellier, four years. The main stem is cut into
zones by a hidden semi-Markov model fitted to the sequence of phytomer types (P0, P1, P2);
branch leaf-appearance rates and durations are given by zone and by the type of the bearing
phytomer (R0, R1, R2).

## What it holds

- **Experiments** (l. 138-210): Grenache N and Syrah on Fercal in pots of 0.050 m³ outdoors
  at Montpellier, 2002 (expt 1) to 2005 (expt 4); 60 shoots a genotype for the phytomer
  sequences (expts 2-4); plants thinned to one branch at E-L 12 (l. 153); soil water kept above
  70-75 % of pot capacity (l. 187). Mean diurnal air temperature ran from 23.2 to 25.2 °C.
- **Thermal time** (Eq. 1, l. 176-180): the daily integral of the mean temperature above
  Tb = 10 °C, common to both cultivars (after Winkler et al. 1974 and Lebon et al. 2004).
- **Main-stem leaf appearance** (l. 726, 812): about 0.044 leaves per °Cd for both cultivars
  in expts 1-4; 0.044 ± 0.002 over three successive years, pooled. The print does not say
  whether the 0.002 is SD or SE. It is like Lebon 2004's 0.046 and Schultz 1992's Riesling.
- **Leaf area from lamina length** (Eq. 3, Table 1, l. 376-378): S = a L² + b L, S in cm², L
  in mm. Syrah expts 3-4: a 0.0111, b 0.1494 (n 182, r² 0.953). Grenache expts 3-4: a
  0.0091, b 0.2547 (n 135, r² 0.972). Syrah expt 2: a 0.0134, b -0.0762 (n 248, r² 0.971).
  Grenache expt 2: a 0.0100, b 0.1620 (n 233, r² 0.956).
- **Internode volume** (Eq. 4, Table 1): V = a4 π L (D/2)², a4 1.315 (Syrah, n 160, r² 0.95)
  and 1.510 (Grenache, n 75, r² 0.98); estimated in expt 3 by water displacement.
- **Leaf area by rank** (Eq. 6, Table 1): a logistic in rank, a6 + b6 / (1 + exp(-((r - c6)/
  d6))), eight sets (main stem and branch, expts 3 and 4, both cultivars), r² 0.56-0.84.
  The main-stem sets have a6 about -4800 and c6 about -46 in expt 3, so they are fitted far
  outside the data. Not in the record.
- **Zones** (l. 474-497): zone A (the first P0 run) is 4.0 ± 0.8 phytomers in Grenache N
  (n 58) and 2.7 ± 0.6 in Syrah (n 56, l. 488-490); zone B is three or four phytomers in
  Grenache and nine in Syrah. Budburst never comes before the shoot has ten phytomers
  (l. 666), nor on the first four positions (l. 731); the lag from phytomer to budburst is
  four to six phyllochrons (l. 680).
- **Branch leaf-appearance rate** (Table 5, leaves per °Cd, l. 826-828), R0 / R1 / R2:
  - Grenache N zone B 0.0334 / 0.0235 / 0.0260; zone A 0.0117 (R0 only).
  - Syrah zone B 0.0341 / 0.0337 / 0.0297; zone A 0.0125 (R0 only).
  - Zone C falls with distance: Grenache proximal 0.0341 / 0.288 / 0.0274, median 0.0268 /
    0.0138 / 0.0158, distal 0.0145 / 0.0097 / 0.0113.
- **Branch duration** (Table 5, °Cd, l. 831-835), R0 / R1 / R2: Grenache zone B 967 / 631 /
  650; Syrah zone B 912 / 930 / 720; zone C proximal Grenache 950 / 717 / 672, Syrah 1030 /
  1018 / 731.
- **State at 1200 °Cd** (Table 2, expt 3, l. 439, 443): primary phytomers 50.8 (Grenache N)
  and 52.9 (Syrah); secondary leaf area 2.00 m² (Grenache N) and 2.58 m² (Syrah). Expt 4:
  56.0 and 55.2 phytomers, 3.54 and 3.81 m².
- **Primary-axis internode length** (Table 4, mm, P0 / P1 / P2): Grenache N 67.3 / 68.7 /
  80.4; Syrah 86.3 / 82.1 / 100.4.
- **Not printed:** budburst probability and date as numbers (Fig. 7 only), the value of lu
  in Eq. 2, stage dates.

## Dependence

- **Borrowed:** thermal time and the rate method from Lebon et al. 2004 (l. 157-159, 359);
  the leaf-area form from Schultz 1992 (l. 352). It computes the same leaf-appearance rule
  as lebon2004.leaf_development.
- **A model made the zone labels:** the zones come from a hidden semi-Markov model fitted to
  the observed sequences and run with the Viterbi algorithm (l. 294); the sequences are
  observed, the labels are model output.
- **Shared authors** (Lebon, Lecoeur) with Lebon 2004 and Pallas 2008 (Louarn too): a flag
  only. Pallas 2008 reuses this paper's per-cultivar leaf lines (the expts 3-4 pair).

## Bearing (2026-10-14)

- **The cleanest printed phyllochron:** 0.044 ± 0.002 leaves per °Cd over three years and
  two cultivars.
- **The first printed branch rates and durations by zone and type**, for pots. Table 5's
  Grenache R1 zone C proximal rate prints 0.288, an order above its neighbours; probably
  0.0288, not corrected, and it is not in the record.
- **Kin to the engine by form** (growth on thermal time). Potted vines, not a vineyard.
