---
id: maruyama2023
citation: Maruyama, A., Kuwagata, T. & Watanabe, T. 2023. Observations on dew formation in the rice canopy and its simulation using a multilayer microclimate model. Journal of Agricultural Meteorology 79(1):28-37
doi: 10.2480/agrmet.D-22-00016
read: 2026-10-18, in full (light reading), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py; Eqs 1-5 from the text layer, not checked against an image
status: read
diseases: []
crops: [rice]
regions: [Japan, Kumamoto]
processes: [dew, multilayer canopy model, leaf wetness]
records: []
datasets: [kuwagata2024.kumamoto]
files: [atsushi_2022.pdf (the 2026-10-18 drop)]
---

# Maruyama, Kuwagata & Watanabe 2023: dew in the rice canopy by layer

The paper is dated 2023 (received 15 May 2022, accepted 22 July 2022; the drop key says 2022).
It measures dew on leaves layer by layer on four nights in a Kumamoto paddy and simulates it
with a multilayer microclimate model. No record: the model is the Watanabe et al. (2004, 2005)
family and its equations are not new here.

## What it holds

- **Observations** (l. 26-129): rice 'Hinohikari', transplanted 11 June 2003, 0.2 x 0.3 m;
  dew every 2 h at 0.2 m intervals by weighing bagged leaves (Wilson et al. 1999), 10-15 leaves
  per layer. Whole-canopy dew at 06:00 on 19, 21, 24 August and 1 October: 0.10, 0.07, 0.15 and
  0.23 mm (the times are for the previous night, Table 1 note). Largest leaf dew 0.13 mm at
  0.8-1.0 m on 1 October. Dew per leaf area is larger in the upper layers.
- **Model** (l. 128-250): leaf energy balance per layer with K-theory and two-stream radiation;
  Eq 1 boundary-layer conductance, Eq 2-3 Re' and Gr, Eq 4 stomatal conductance (Jarvis form),
  Eq 5 condensation Ec = Eg - E (distillation or dewfall by sign). Step 30 min; D_L 0.03 m
  (here; 0.1 m in Kuwagata et al. 2024); g_Smax 0.023 m/s; S_absH 66 W m-2; ε = 1; F = 0.5.
- **Result:** "good agreement" with no statistic; the model's upper-lower difference is larger
  than observed; on 22-23 August (strong wind) almost no dew in model or observation. Dewfall
  dominates at low water temperature and distillation at high.
- **Limits** (l. 499): four nights, one site, one climate.
- **Not printed:** layer values as numbers, error statistics, dew duration, data location
  (the same observations carry DOI 10.17632/fmvr43csy3.3 in Kuwagata et al. 2024).

## Dependence

- **Shared data and model with `kuwagata2024`:** this paper is where the Kumamoto
  observations and the multilayer (MLC) reference of Kuwagata et al. 2024 come from, by the same
  authors. The MLC model was confirmed against these data, so Kuwagata's W0 and Wp against MLC
  is not a second check.
- **Borrowed:** Watanabe et al. 2004, 2005; Kondo (1982); Watanabe & Mizutani (1996); Maruyama
  & Kuwagata (2008).

## Bearing (2026-10-18)

For strand 3 and what Agrarium's truth can take:

- **Wetness here is dew amount from an energy balance, not an RH threshold.** Against the
  engine's RH ≥ 90 % stand-in it gives a physical reference, but only for a rice canopy, four
  nights, with no error statistics.
- **Use:** a data source for the Kumamoto dew profile (the dataset is recorded under
  `kuwagata2024.kumamoto`) and the multilayer idea (dew larger in the upper canopy); it is
  not a vineyard.
- **Can it run:** not from the paper: MLC details are in Watanabe et al., and the data are by
  DOI in the companion paper.
