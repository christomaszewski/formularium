---
id: orlandini2008
citation: Orlandini, S., Massetti, L. & Dalla Marta, A. 2008. An agrometeorological approach for the simulation of Plasmopara viticola. Computers and Electronics in Agriculture 64:149-161
doi: 10.1016/j.compag.2008.04.004
read: 2026-10-09, in full by the main session; equations 1-6 and Figures 3-7 read in the page images
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Tuscany]
processes: [leaf area, sporangia survival, sporulation, infection, incubation, calibration, validation]
records: [orlandini2008.plasmo, orlandini2008.survival]
datasets: [orlandini2008.mondeggi, blaeser1978.survival, lalancette1988a, goidanich1957]
files: [03_Orlandini_Massetti_DallaMarta_2008.pdf]
---

# Orlandini, Massetti & Dalla Marta 2008: PLASMO as a severity model

The version Brischetto et al. 2020-2021 and Franche 2012 cite as "Orlandini et al. 2008".
PLASMO now simulates the infected leaf area, not only infection dates.

## What it holds

- **Inputs:** hourly temperature, RH, leaf wetness (0/1) and rain; start at budbreak.
- **Leaf area (eq. 1):** logistic growth to a maximum per shoot, rate a parabola in
  temperature (Sall 1980), 4-46 °C; tuning F. MAE 456 cm², MAPE 5.26 against 1995-1996.
- **Start:** the 3-10 rule ("Goidanich, 1959"), or the first severity observed (p. 154).
- **Lesion (oil spot) survival (eq. 2) and sporangia survival (eq. 4),** both credited to
  Blaeser & Weltzien 1978:
  - f = 1/6 above 30 °C, else 1/[(b0 + b1·e^-((RH - b2)/b3)²)·(T - 30) + 6] for RH
    30-100 %; area(t+1) = area(t)·(1 - B·f), with D in place of B for sporangia.
  - Figs 3 and 5 (survival in days) peak at about 13-14 days at 5 °C near saturation, are
    about 3-4 days at 5 °C in dry air, and near 0 at 30 °C.
  - b0-b3 and d0-d3 are not printed.
- **Sporulation (eq. 3),** credited to Lalancette et al. 1988a (the sporulation paper,
  78:1316):
  - seven consecutive night hours with RH above 90 % produce sporangia;
  - f2 = (c2T² + c1T + c0)/cs,max·(e^-((H-7)/2) - e^-((H-6)/2)) for H = 7-12 h and
    10-30 °C. Fig. 4 peaks near 0.155.
- **Inoculation (eq. 5),** credited to Lalancette et al. 1988b (infection, 78:794):
  - at least two wet hours, from wetness or rain;
  - f4 = (e3T³ + e2T² + e1T + e0)·(e^-((H-2)/2) - e^-((H-1)/2)) for H = 2-9 h and
    5-30 °C. Fig. 6 peaks near 1.1.
  - Once leaf area passes 75 % of its maximum, a leaf-age coefficient reduces
    susceptibility (Reuveni 1998).
- **Incubation (eq. 6),** credited to Goidanich et al. 1958 and Magarey et al. 1991:
  - hourly progress f5 = fm·(T - Tmin)(Tmax - T)/(Tmax - Tmin)², times a square root of
    (RH - RHmin)/(RHmax - RHmin);
  - **bounds T = [10, 34] °C, RH = [30, 100] %**, the bounds Franche 2012 left out;
  - fm is not printed. As typeset, the humidity root sits in the denominator, but Fig. 7
    rises with humidity. Fig. 7 peaks near 8.5 % at 22 °C, its time unit not stated.
- **Calibration (pp. 158-160):**
  - C (sporangia per cm²) and D (survival, days) were run from 2 to 40 in steps of 2
    against 1995-1996 severity; C22 D18 minimised both errors (MAE 0.63, MAPE 0.42).
  - Severity was 18.65 % in 1995 and 0.80 % in 1996.
- **Validation, 1998-2003 (Tables 2-4):**
  - Observed severity was 1.80, 6.00, 20.00, 5.58, 39.47 and 2.85 %.
  - The risk class was right in 4 of 6 years; the other two were "Low" simulated as "No
    risk". RMSE ran from 0.74 to 5.55.
  - The 2002 and 2003 classes in Table 2 (4 for 39.47 %, 0 for 2.85 %) disagree with the
    text, which puts class 4 in 2003.
- **Site:** Paretaio vineyard, Mondeggi-Lappeggi farm, northern Chianti (43°47' N, 180 m,
  16 % slope facing south), Sangiovese, rows north-south, 1 × 3 m. Three untreated plots
  of about 1000 m²; 800 leaves and 400 clusters on 200 vines every 10 days.

## Dependence

- **Cannot be run from the paper:** none of the coefficients are printed (a0-a2, b0-b3,
  c0-c2, cs,max, d0-d3, e0-e3, fm, B, F).
- **Survival:** confirms Brischetto et al. 2020 and 2021.
  - Temperature and RH "after Blaeser and Weltzien (1978)", with no parameters printed.
  - The form is not Blaeser & Weltzien's polynomial in the saturation deficit.
  - Recorded as calibrated on `blaeser1978.survival` (inferred), so kin to
    `blaeser1979.survival` and its borrowers.
- **Sporulation:** its form is the engine's in two tags: dark moist hours
  (`caffi2013.sporulation`) and a temperature band (`lalancette1988.sporulation_bounds`).
- **Inoculation:** Lalancette's infection data (`lalancette1988a`, inferred). The form is a
  temperature polynomial times wet hours, tagged strictly as an infection index; the
  engine's Botrytis index carries that tag.
- **Incubation:** Goidanich's (strict reading), as in 1993. **The start** borrows the 3-10
  rule.
- PLASMO is kin to the engine in every process here, so it can only drive a development
  family.
- Orlandini and Dalla Marta are authors of Sentelhas et al. 2008 (the engine's wetness): a
  flag only.

## Bearing (2026-10-09)

- Settles two leads: Franche's missing bounds (10-34 °C, 30-100 % RH) and Brischetto's
  unprinted survival.
- Franche's 2.616 is not here, nor in Rosa et al. 1995 (see [rosa1995](rosa1995.md)).
- Eight seasons of untreated Sangiovese severity at one Chianti vineyard (1995-1996 in
  Fig. 12, 1998-2003 in Table 2): a season-severity pattern for the truth, outside the
  engine's calibration.
  PLASMO's C and D were tuned on 1995-1996, so only 1998-2003 is clean of PLASMO.
