---
id: aylor1983
citation: Aylor, D. E. & Taylor, G. S. 1983. Escape of Peronospora tabacina spores from a field of diseased tobacco plants. Phytopathology 73:525-529
doi: 10.1094/phyto-73-525
read: 2026-10-25, in full (5 pages, a scan read through OCR, which garbles some symbols), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [tobacco blue mould]
crops: [tobacco]
regions: [United States, Connecticut]
processes: [spore escape, canopy deposition, dispersal, wind, spore flux, transport model]
records: []
datasets: []
files: [dr1025_aylor1983.pdf (the 2026-10-25 drop)]
---

# Aylor and Taylor 1983: how many spores leave a diseased tobacco field, measured and modelled

Spore concentration and wind were profiled above a small, severely diseased tobacco field, and a transport model was tuned to them to estimate the share of released spores that escape from a large field.

**Read this first.** An analogue. Tobacco blue mould (Peronospora tabacina) is a downy mildew, but the crop is tobacco 0.7 to 1.0 m tall in a 50 x 50 m field, not a trellised vine. The "93 to 97 % never leave the crop" is a model output for a large, uniformly diseased field in neutral air, tuned to measured concentrations; it is not a measured share. It counts spores deposited on crop and ground together, so it does not say what share lands on leaves. The scan was read by OCR: the symbol before "of 1, 2, and 3" prints as "ms" and units as "m-s '"; the row spacing prints as "| m" (read as 1 m); the spores-per-lesion exponent prints as "2 X 10°" and is not used here. The 1, 2 and 3 m/s are wind speeds 1 m above the canopy, with friction velocities of 0.13, 0.26 and 0.39 m/s (l. 479-480; the friction-velocity symbol is OCR-garbled too).

## What it holds

- **Site:** broadleaf tobacco in a 50 x 50 m area at Windsor, Connecticut, 1981 (l. 54-55); rows spaced "| m" apart (OCR; probably 1 m) with plants 0.6 m apart in the row (l. 58); crop about 0.7 m tall in the first experiments and about 1.0 m in the last (l. 59-60).
- **Measured:** the rate of spore escape derived from vertical profiles of concentration and wind over the small, severely diseased field was 1 to 7 spores per m2 per s (l. 30); the summary gives 7 to 10 as the maximum measured (l. 586-588).
- **Model:** the escape model balances horizontal and vertical transport, settling, deposition to the crop and release (equation 6; l. 324); deposition to the crop is by sedimentation and impaction (l. 325). Neutral atmosphere only.
- **Source strength:** a release of about 290 spores per m2 per s inside the crop (l. 486) was chosen because it gave concentrations and fluxes in reasonable agreement with experiments 1, 3 and 5 at 20 m downwind (l. 483-490). That is about half of the available spores in 7 h (l. 576), at 50 lesions per plant (the spores per lesion are garbled).
- **Escape from a large field:** for wind speeds of 1, 2 and 3 m/s, some 97, 95 and 93 % of the released spores never leave the crop (l. 577-578), so escape is 3, 5 and 7 % (arithmetic, not printed). Fewer leave at lower wind speed because settling matters more (l. 578). Flux 1 m above the crop is nearly constant after about 50 m of wind run (l. 483-486).
- **Largest escape:** about 20 spores per m2 per s from an extensive diseased crop at 3 m/s, "correct to within an order of magnitude" (l. 590-592).

## Dependence

- Builds on the transport model of Aylor (the paper's refs 2 and 6) and a boundary-layer treatment (ref 11); deposition to the crop is per unit canopy volume, fitted to the measured concentrations, not measured per leaf. The same first author wrote `aylor1985`: a shared author is a flag, not a dependence.

## Bearing (2026-10-25)

- **dm.capture_fraction 0.3** (share of sporangia landing in a vine's cell that land on its leaves): not measured here. The paper supports only that most spores released inside a closed canopy stay in it, 93 to 97 % in the model (l. 577-578). It does not split leaves from ground, and its share is of spores released inside the crop, not of spores arriving from outside. Tobacco, Connecticut; a model output tuned to measured flux.
- **Not shown:** anything for a vine canopy or a trellis, a deposition velocity for P. viticola sporangia, or how far spores go inside the crop (no distance gradient). It gives no support to dm.wind_scale_m, dm.wind_shape or dm.kernel_radius_m.
- **Kind of result:** a measurement of flux above one small field, plus a tuned model. An analogue for the canopy-retention idea only.
