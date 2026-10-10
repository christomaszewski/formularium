---
id: brischetto2020
citation: Brischetto, Chiara, Bove, Federica, Languasco, Luca & Rossi, Vittorio. 2020. Can spore sampler data be used to predict Plasmopara viticola infection in vineyards? Frontiers in Plant Science 11:1187
doi: 10.3389/fpls.2020.01187
read: 2026-10-09, in full, equations 1-2 in the page image, by a reading agent (claude-haiku-5-5); 58 quotes checked by scripts/verify_quotes.py; Table 1 and the classification counts checked in the page images (pp. 4, 7) by the main session, 2026-10-10
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Emilia-Romagna]
processes: [sporangia survival, aerobiology, infection]
records: [brischetto2020.survival, blaeser1979.survival]
datasets: [brischetto2020.piacenza]
files: [spore-sampler-infection-2020.pdf]
---

# Brischetto et al. 2020: viable airborne sporangia against infection at Piacenza

The source of the engine's `brischetto2020.survival`. Read before as the record's source
(`checked`); this is its first literature note.

## What it holds

- **Site:** the Piacenza campus vineyard, 2015-2017; a volumetric spore sampler, a
  station in the vineyard, and vines beside the sampler inoculated artificially (14 May
  2015, 19 May 2016, 18 May 2017).
- **Survival (eqs 1-2):** hourly mortality MOR' = 1/[24(9.27 - 1.12 VPD + 0.04 VPD²)]
  (attached) and MOR'' = 1/[24(5.67 - 0.47 VPD + 0.02 VPD²)] (detached), credited to Blaeser
  & Weltzien 1979, with VPD = T(1 - RH/100) (Steubing 1965). MOR is said to run "0 to 1/24";
  daily MOR is the mean of the two; SPV (eq. 3) carries sporangia for up to 7 days.
- **Infection assay:** leaves sampled on 108 dates, wetted and incubated 24 h at 23 °C;
  lesions counted after 10 days.
- **Fit:** logistic regression of infection (yes/no) on SPV: B0 -0.814, B1 0.323, so P = 0.5
  at SPV 2.52 viable sporangia/m³ air/day. AUROC 0.821 ± 0.040. No held-out data.

## Checked in the page images (2026-10-10)

- **Table 1's VPD is not the printed formula.** Its rows (22.4 °C and 57 %, 21.9 and 64.6,
  23.0 and 55.77) give VPD 11.6, 9.59 and 12.59 hPa. T(1 - RH/100) gives 9.6, 7.8 and 10.2;
  the saturation deficit E(T)(1 - RH/100) gives 11.6, 9.3 and 12.4 hPa (Magnus formula,
  computed by the main session). The discussion also defines VPD as the saturation deficit
  (Shuttleworth 1993). Which one the equations were run with is not stated.
- **Two counts are swapped.** The text prints P+O+ 40, P-O- 40, P+O- 6, P-O+ 22, then
  sensitivity 0.87, specificity 0.65, LR+ 2.45, LR- 0.20, P(O+) 0.426 and false positives on
  35 % of dates. Every one of those follows if P+O- is 22 and P-O+ is 6: 62 dates without
  infection, 22 of them flagged.
- **Zachos 1959** is cited for sporangia on lesions viable 4-8 days in shade when maxima did
  not exceed 22 °C.

## Dependence

- Eqs 1-2 are `blaeser1979.survival`'s, with c2 = 0.02 where the source prints 0.01.
- The regression's predictor (SPV) is computed with those equations, so the 2.52 threshold
  is calibrated through them. The outcome (lesions) is observed; no model dates infections.
- Rossi et al. 2008 is not cited.

## Bearing (2026-10-10)

- For the truth's survival: if the authors ran eqs 1-2 on the saturation deficit in hPa,
  their lifetimes are shorter than the T(1 - RH/100) form gives, and the engine copies the
  printed form. Recorded as a flag on `brischetto2020.survival`.
