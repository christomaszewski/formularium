---
id: franceschi2020
citation: Franceschi, V. T., Alves, K. S., Mazaro, S. M., Godoy, C. V., Duarte, H. S. S. & Del Ponte, E. M. 2020. A new standard area diagram set for assessment of severity of soybean rust improves accuracy of estimates and optimizes resource use. Plant Pathology 69:495-505
doi: 10.1111/ppa.13148
read: 2026-10-20, in full, by a reading agent (claude-haiku-5-5); 58 of 58 quotes found at their lines by scripts/verify_quotes.py; Table 1 read in the page image (p. 500) by the main session
status: read
diseases: [soybean rust]
crops: [soybean]
regions: [Brazil]
processes: [rater error, visual assessment, standard area diagram, sampling]
records: [franceschi2020.rater_error]
datasets: [franceschi2020.soybean_raters]
files: [franceschi_2020.pdf (the 2026-10-20 drop)]
---

# Franceschi et al. 2020: how far raters' severity estimates stray, with and without diagrams

Thirty-seven inexperienced raters estimated soybean rust severity on 50 leaflet images
unaided and then aided by an old or a new standard area diagram set; error models from the
estimates feed a simulation of how many leaflets a fungicide trial needs.

## What it holds

- Soybean rust severity estimated by 37 inexperienced raters on 50 leaflet images, 0.25–84%
  severity (l. 36).
- The 'actual' severity came from a discriminant function fitted to RGB samples; its values
  'were assumed to best represent' severity (l. 130, 132).
- New SAD: 10 diagrams at 0.2, 1, 3, 5, 10, 25, 40, 55, 70, 84% (l. 33, 35). Old SAD: six
  diagrams (l. 89).
- Lin's ρc, New SAD 0.96 and Old SAD 0.83 (l. 346, 347); Cb 0.99 and 0.92; r 0.96 and 0.77;
  Old SAD location shift −0.26 (l. 347).
- Unaided ρc 0.82 (New group) and 0.80 (Old group) (l. 349, 351).
- ICC: New SAD 0.94 [0.92–0.96], Old SAD 0.81 [0.74–0.87]; OCC 0.940 and 0.736 (l. 425,
  427).
- Error mean (percentage points, S in %): unaided 1.145 + 0.1002S; Old SAD −1.039 −
  0.11694S; New SAD 1.411 − 0.03738S (l. 316, 320, 323).
- Error SD: unaided −1.833 + 0.7794S − 0.007155S²; Old SAD −0.114 + 0.6151S − 0.006718S²; New
  SAD 1.061 + 0.199S − 0.001925S² (l. 318, 322, 324).
- Simulation: check and treatment severity 70%, Δ = 0 to 15 p.p., five plots per experiment,
  n = 5 to 55 leaflets, 2 × 10^4 runs (l. 211, 210, 210).
- For Δ = 5 at power 0.8: Old SAD 40 leaflets, New SAD 20, unbiased image analysis 10 (l.
  405, 408).
- Within-plot SD σS = μS × 0.006 × (100 − μS), maximum 15% at 50% (l. 280); the 0.006 is
  from Garcés and Forcelini (2013) (l. 281).
- Not printed: μ_C and σ_C of the control efficacy (l. 287); the inoculum exponent is
  flattened in the text layer (l. 118).
- Data: 50-image validation set on OSF PG6QE; all files on OSF 3zmv8; stated open; licence
  not printed (l. 161, 331).

## Dependence

- Its own rater experiment against image-analysis severity. The within-plot spread 0.006
  comes from Garcés & Forcelini 2013 (l. 281). Del Ponte is an author of the SAD review held
  as context; no engine author.

## Bearing (2026-10-20)

- Recorded as `franceschi2020.rater_error` (role observation) with the dataset
  `franceschi2020.soybean_raters`. Kin report (cooptera@6f8d0a2): independent, as expected;
  it is severity estimation, not the engine's detection sensitivity.
- For Agrarium's scout operator: a published form and magnitude for the error of a scout's
  severity number (bias up to a few points, spread up to about 19 points unaided at mid
  severities, a third of that with a diagram set). Soybean, not grapevine.
