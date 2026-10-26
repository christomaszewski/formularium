---
id: gaskin2005
citation: Gaskin, R.E., Steele, K.D. & Forster, W.A. 2005. Characterising plant surfaces for spray adhesion and retention. New Zealand Plant Protection 58:179-183
doi: 10.30843/nzpp.2005.58.4244
read: "2026-10-25, in full (5 pages), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [grapevine, onion, potato, pea, bean, dock]
regions: [New Zealand]
processes: [leaf wettability, contact angle, spray adhesion, spray retention, surfactant]
records: []
datasets: []
files: [dr1025_gaskin2005.pdf (the 2026-10-25 drop)]
---

# Gaskin et al. 2005: contact angles of a 20 % acetone solution on leaves, with two grape values (82 deg; 93 and 132 deg), for spray adhesion

A New Zealand agrochemical paper that ranks leaf surfaces by the static contact angle of aqueous acetone droplets and links it to spray adhesion and retention.

**Read this first.** The contact angles are of a **20 % v/v acetone-in-water solution** (surface tension 41 mN/m), 1 microlitre drops, not of water (l. 52-53). A liquid of lower surface tension than water spreads more, so these angles are not water angles and cannot be set beside water contact angles such as those in `konlechner2016` (6 microlitre drops of water). They are a ranking within this method. The grape site is not stated beyond "grown outdoors"; the authors are in Rotorua.

## What it holds

- **Method:** static contact angle from the projected image of 1 microlitre drops of 20 % acetone in water (41 mN/m) on freshly detached leaves or fruit, at least 20 replicate drops on at least three separate leaf or fruit surfaces per species, plants grown outdoors (l. 52-64). The method is from earlier work by the group (Forster and Zabkiewicz 2001, l. 43), where the correlation between percentage adhesion and contact angle is given as R2 = 0.97 (cited, not the paper's own).
- **Aim and scale:** a simple static contact angle of aqueous acetone drops that ranks leaf surfaces as easy, difficult or very difficult to wet and predicts spray drop adhesion and the benefit of a surfactant (abstract). Table 2 sets the scale: dock 45 deg "very easy", bean 55 deg "easy", grape 82 deg "moderate", pea 180 deg "very difficult" (l. 137-140).
- **Adhesion test:** 850 micrometre drops falling 400 mm onto leaves at 22.5 deg, adhesion judged as sticking on first impact (l. 66-71). Adhesion with water: dock 100 %, bean 68 %, **grape (Vitis vinifera cv. Semillon, grown outdoors) 82 deg, 62 %** (72 and 82 % with 0.1 and 0.2 % surfactant), pea 0 % (l. 137-140, 73-74).
- **Spray retention (Table 3):** onion 131 deg; **grape cv. Cabernet Sauvignon 93 deg on the upper and 132 deg on the lower surface**; potato 78 and 71 deg (upper and lower) (l. 163-165). Normalised retention of a mancozeb spray: onion 1.65, Cabernet Sauvignon 3.90, potato 5.21 ug per cm2 with a nonylphenol surfactant (l. 163-165).
- **Authors' reading of grape:** "moderately difficult-to-wet on the upper, and very-difficult-to-wet on the lower surface" (l. 172). A spray tuned for the upper surface may not wet the lower.
- Cabernet Sauvignon appears in Table 3 only; its sampling site and date are not stated in the lines read.

## Dependence

- Own measurements by the method of Forster and colleagues (acetone-water contact angle, 1998 and 2001) and the adhesion method of Stevens et al. (1993). No model borrowed.

## Bearing (2026-10-25)

- **micro.wet_threshold_mm (0.02 mm) and micro.storage_mm_per_lai (0.25):** no film thickness and no retained volume. The paper gives the underside of a vine leaf as the harder to wet (132 against 93 deg, with the acetone solution), which is the same direction as Konlechner, but the angles are not water angles.
- **Drying and interception parameters:** not addressed.
- **Kind of result:** measurement with a surrogate liquid on one vine cultivar per table (Semillon; Cabernet Sauvignon), for spray work. Use only as a ranking, never as a water contact angle.
