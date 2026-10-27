---
id: english1993
citation: English, J.T., Kaps, M.L., Moore, J.F., Hill, J. & Nakova, M. 1993. Leaf removal for control of Botrytis bunch rot of wine grapes in the midwestern United States. Plant Disease 77:1224-1227
doi: 10.1094/PD-77-1224
read: "2026-10-25, in full (4 pages, a scan read through OCR; tables checked against the text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 12 of 12 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: [Botrytis bunch rot]
crops: [grapevine]
regions: [United States, Missouri]
processes: [leaf removal, canopy density, leaf layers, evaporative potential, drying, atmometer, Botrytis bunch rot, microclimate]
records: []
datasets: []
files: [dr1025_english1993.pdf (the 2026-10-25 drop)]
---

# English et al. 1993: in Missouri wine grapes, leaf removal cut fruit-zone leaf layers and raised atmometer drying by about 20 % or less

A two-year, two-vineyard trial of leaf removal for Botrytis bunch rot, in which the drying of the fruit zone was measured with atmometers.

**Read this first.** Drying was measured as "evaporative potential", the evaporation of a white spherical atmometer (a wet porous sphere) left in the fruit zone for 24 to 48 h, twice per season, one per plot (l. 211-216). It feels wind and radiation; it is not a film of water on a leaf, and no leaf wetness duration was measured here. "Leaf layers" are leaf contacts of a rod at fruit-zone height (point quadrat), not LAI. The PDF is a scan read through OCR: the ambient rows of Tables 1 and 3 carry OCR marks (the numbers were read as 1.0 and 1.1, 1.49 and 1.39, 0.93 and 0.91, 1.09 and 0.87). The fruit-zone-to-ambient ratios below are arithmetic from those tables, not printed.

## What it holds

- **Design:** two Missouri vineyards, 1991 and 1992. Vignoles (planted 1980, Phelps county, quadrilateral cordons on a Geneva double curtain) and Seyval blanc (planted 1987, Gasconade county, upper and lower bilateral cordons on a two-wire trellis in 1991, retrained as low cordons on a single wire in 1992) (l. 113-140). Leaf removal in early June, about 2 weeks after full bloom (l. 144-145, 164); four replicate plots of four adjacent vines per treatment (l. 153-156, 173-175).
- **Canopy density:** leaf layers in treated canopies were reduced by at least 40 % in both cultivars in 1991 (l. 265); by about 67 % in Seyval blanc in 1992 (l. 477). In Vignoles in 1992 the cut was smaller, 3.2 against 4.3 layers (l. 405-406), about 26 % (arithmetic, not printed).
- **Drying measure:** atmometers in the fruit zone for 24 to 48 h, ml evaporated per hour, plus one atmometer 1 m above the canopy as the ambient reference (l. 213; Table 1 note).
- **1991, Seyval blanc upper cordon (Table 1):** leaf removal 2.3 layers, 5.8 % of ambient light, evaporative potential 0.99 and 0.66 ml/h at the two samplings (l. 290); control 4.5 layers, 3.2 % light, 0.74 and 0.54 ml/h (l. 291). Ambient 1.49 and 1.39 ml/h (l. 295), so fruit-zone over ambient is 0.50 and 0.39 for the control and 0.66 and 0.47 with leaf removal (l. 295 claim). Leaf removal raised evaporative potential in these canopies by more than 20 % (l. 321-322).
- **1992, Vignoles (Table 3):** leaf removal 3.2 layers, 27.8 % light, 0.64 and 0.66 ml/h (l. 405); control 4.3 layers, 22.1 % light, 0.56 and 0.64 ml/h (l. 406); ambient 0.93 and 0.91, so the control ratio is 0.60 and 0.70 (arithmetic, not printed).
- **1992, Seyval blanc (Table 3):** leaf removal 1.4 layers, 14.0 % light, 0.78 and 0.62 ml/h (l. 409); control 4.2 layers, 5.0 % light, 0.67 and 0.52 ml/h (l. 410); ambient 1.09 and 0.87.
- **Light against drying:** "although light penetration to the fruit zone was increased by 180 %, evaporative potential was increased by less than 20 % on both 3 and 21 August" (1992 Seyval blanc, l. 485-488).
- **Arithmetic, not printed (from the tables):** fruit-zone over ambient averages 0.62 across the ten sampling values at 2.3 leaf layers or fewer and 0.57 across the ten at 3.2 or more (0.57 across the six at 4.2 or more).
- **Disease:** the dry 1991 season gave little bunch rot (none in Vignoles); the wet 1992 season gave more, and leaf removal reduced incidence and severity in both cultivars (abstract; l. 18-28).

## Dependence

- Own measurements. The evaporative-potential (atmometer) method is cited to refs 4 and 5 of the paper (l. 212); point-quadrat density after Smart (ref. 14). Leaf removal is said to open the canopy, raise wind movement and the drying conditions, cited from refs 4-6 (l. 65), not shown here separately.

## Bearing (2026-10-25)

- **micro.density_drying_slowdown (0.4 per unit LAI above 1, a divisor):** a dense canopy dried the fruit zone more slowly, but only by tens of percent. Leaf removal raised atmometer drying by about 15 to 20 % at most while cutting leaf layers by two thirds (l. 485-488), and by more than 20 % in one 1991 canopy (l. 321). The registry's divisor 1 + 0.4 (LAI - 1) gives 0.89 at LAI 1.3 and 0.42 at LAI 4.5 (arithmetic, not printed), a steeper fall than the 0.62 against 0.57 means above. Leaf layers are not LAI, and an atmometer is not a leaf film, so this is a hint that 0.4 is on the high side, not a re-fit.
- **micro.evap_mm_h_per_hpa, micro.evap_radiation_per_kw:** the ambient atmometer rates (0.87 to 1.49 ml/h) are atmometer figures; no VPD or radiation was recorded alongside in the parts read. Not usable for these.
- **micro.interception, micro.storage_mm_per_lai, micro.wet_threshold_mm:** not addressed.
- **Kind of result:** measurement of a proxy for drying (atmometers), Missouri hybrid cultivars on cordons, two summers; no vine leaf wetness or LAI.
