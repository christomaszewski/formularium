---
id: skelsey2008
citation: Skelsey, P. 2008. Multi-scale modeling of potato late blight epidemics. PhD thesis, Wageningen University
doi: 10.18174/122020
read: 2026-10-25, lightly: chapters 2 and 3 (kernels, evaluation, escape fraction) and the passages on escape and deposition efficiency in the model chapters; not read in full, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 15 of 15 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [potato late blight]
crops: [potato]
regions: [Netherlands, Wageningen]
processes: [dispersal kernel, Laplace kernel, thin tail, spore escape, deposition efficiency, canopy deposition, focus velocity, wind]
records: []
datasets: []
files: [dr1025_skelsey2008thesis.pdf (the 2026-10-25 drop)]
---

# Skelsey 2008: kernels, escape from the canopy and deposition back onto the crop in a potato late blight thesis

A Wageningen thesis that models late blight in 3.75 x 3.75 m potato plots and in fields, with a dispersal kernel, a check of how many sporangia escape the canopy, and a deposition efficiency back onto the crop.

**Read this first.** An analogue (Phytophthora infestans on potato) and a thesis, not a measurement paper. Three cautions.
- The kernel values are cited from Paysour and Fry (1983), which was not fetched; the thesis does not measure them.
- The thesis's own escape check does not reproduce. With its printed Eq. 7 and Eq. 8, LAI 5 and the 0.5 m/s it states, the escape is about 23 % (arithmetic, not printed), but the text prints 2 % (l. 3155). Not reconciled.
- Two deposition velocities are used: vd = (1 + LAI) vs in chapter 3 (Eq. 8, l. 3139) and a fixed vd = 3 vs = 0.0255 m/s in chapter 4 (l. 4338-4339). Eq. 5 prints with its exponent broken across a line; it is read as printed from l. 4335.

## What it holds

- **Kernels:** two radial Laplace (2-D exponential) kernels, K = alpha^2/(2 pi) exp(-alpha r), parameterised with Paysour and Fry (1983) data: alpha 0.82 per m in non-irrigated potatoes and 2.1 per m in irrigated potatoes (l. 1400-1401, cited). The mean dispersal distance is 2/alpha (l. 1397): 2.44 m and 0.95 m (l. 1402). A radial Gaussian with theta 1.95 m has the same 2.44 m mean (l. 1397).
- **Tail:** the Laplace kernel is "thin-tailed"; a fat-tailed kernel would turn spread from a travelling wave into an accelerating one (l. 3626). The author judges thin-tailed kernels appropriate for the model (plots 3.75 x 3.75 m, l. 2817), because Minogue and Fry (1983) found a constant spread velocity (l. 3637-3639); the constancy may reflect the limited time and space scales of their experiments (l. 3640-3641).
- **Loss from a field:** with the wide Laplace kernel (mean 2.44 m), about 5 % of the spores produced are dispersed outside the field boundary in a wrap-around check (l. 10164).
- **Focus velocity (cited):** 3.0 m per day for unprotected susceptible potato, from Minogue and Fry (1983) (l. 2950).
- **Escape check, chapter 3:** LAI fixed at 5 (l. 3120); escape fraction fe = exp(-LAI vd/(kappa u)) after de Jong et al. 2002 (Eq. 7), vd = (1 + LAI) vs (Eq. 8), vs 0.0085 m/s for P. infestans sporangia (Gregory 1973; l. 3133-3144, 4338). With wind of 1 m/s in the site and half that in the canopy (l. 3145-3154), the text prints an escape of 2 % (l. 3155) and concludes that ignoring escape is justified. Every spore that disperses to another plant is assumed to deposit on host tissue, delta = 1 (l. 3159, assumed).
- **Deposition efficiency, chapter 4:** delta = 1 - fe = 1 - exp(-LAI vd/(kappa u)) (Eq. 5; l. 4335), kappa = 0.35, vs = 0.0085 m/s, vd = 3 vs = 0.0255 m/s (l. 4338-4339); LAI 2 and u 1 m/s give delta 0.14, and u 0.5 m/s gives 0.25 (arithmetic, not printed). A constant 2 m/s at crop height is assumed during dispersal events in the Netherlands (l. 4340).

## Dependence

- Kernel parameters from Paysour and Fry 1983 (not fetched); focus velocity from Minogue and Fry 1983 (cited); escape model of de Jong et al. 2002 (Sclerotinia ascospores from pasture) with deposition velocity after Ferrandino and Aylor 1985 and Gregory 1973. The deposition velocity of Eq. 8 follows Ferrandino and Aylor 1985 and Aylor 1999 (l. 3135-3136), the line of work behind `aylor1983` and `aylor1985`; the authors are not shared.

## Bearing (2026-10-25)

- **dm.capture_fraction 0.3:** the thesis's delta, 0.14 to 0.25 for LAI 2 at 0.5 to 1 m/s (arithmetic on l. 4335-4340), is the nearest formula for a canopy-retention share, but it is 1 minus the escape fraction, a model output on assumed deposition speeds for P. infestans sporangia, not a leaf-only share and not measured. Its own check misses by about a factor of ten (l. 3155 against the arithmetic above). It does not support 0.3, and gives no vine value.
- **dm.wind_scale_m 3 m [2-10] and dm.wind_shape 0.8 [0.3-1]:** a plot-scale Laplace kernel with mean 0.95 to 2.44 m (l. 1402), thin-tailed by the author's own argument at 3.75 m plots (l. 3626, 3639). By mean distance the wide kernel sits at the low end of the registered scale; by e-folding length, 1/alpha is 1.2 m (arithmetic, not printed), below it. Cited from another paper, potato, no vine, and silent on a fat tail.
- **dm.kernel_radius_m 40 m:** no support; the 5 % loss (l. 10164) is a wrap-around check on a micro-plot, not a radius.
