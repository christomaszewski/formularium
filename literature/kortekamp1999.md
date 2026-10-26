---
id: kortekamp1999
citation: Kortekamp, A., Wind, R. & Zyprian, E. 1999. The role of hairs on the wettability of grapevine (Vitis spp.) leaves. Vitis 38(3):101-105
doi:
read: "2026-10-25, in full (5 pages, two columns interleaved in the text; the figures not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Germany, Siebeldingen]
processes: [leaf wettability, water droplet adhesion, leaf hairs, trichomes, dew, drying, Plasmopara viticola]
records: []
datasets: []
files: [dr1025_kortekamp1999.pdf (the 2026-10-25 drop)]
---

# Kortekamp et al. 1999: water drops cling less to hairy wild-Vitis leaves (0.2-0.4 mN) than to non-hairy V. vinifera cultivars (0.4-1.2 mN)

A Siebeldingen study of 13 Vitis species and cultivars by drop adhesion force and cryo-scanning electron microscopy, linking leaf hairs to downy mildew.

**Read this first.** The measure is the force to pull a 15 microlitre water drop off with a glass loop (adhesion), not a contact angle; the OCR prints the volume as "15 J.Ll" (l. 99). The leaf side measured is not stated in the lines read. Cultivars of V. vinifera (Riesling, Morio Muskat, Mueller-Thurgau) are called "completely wettable" or "extremely wettable", while `konlechner2016` measures contact angles of 125 and 133 deg on Riesling with 6 microlitre drops: the methods differ, and a wetted leaf of either kind spreads a drop given time. The suggestion that pearling drops speed drying is the authors' inference, not measured here (l. 176). The reading JSON and the strand's LEADS.md say that hairy leaves lose their repellency within an hour; the text applies the convergence at 1 h to the cultivars, and says the hairy species stayed clearly apart from them (l. 190-195).

## What it holds

- **Method:** June and July 1998; adhesion of a 15 microlitre water drop on a 5 mm glass loop (cleaned with sodium hydroxide and hydrogen peroxide), force read on a torsion balance at 0, 10 and 30 s and 1, 5, 10, 30 and 60 min after placing the drop; apical leaves from the 5th to 7th insertion of field-grown plants (V. davidii in a greenhouse); 10 measurements per variety at each time (l. 95-105). 13 Vitis species and varieties (l. 88, 107).
- **Result:** force to remove a drop was 0.2-0.4 mN on pubescent (hairy) leaves and 0.4-1.2 mN on non-pubescent leaves (abstract; l. 17). The reading agent takes the hairy leaves to be the wild species and the non-pubescent ones the cultivars. The varieties are Kerner, Morio Muskat, Mueller-Thurgau, Orion, Phoenix, Regent and Riesling (some are crosses with other species) and the species V. cinerea, davidii, doaniana, girdiana, labrusca and rotundifolia (l. 106-110); which is hairy is not tabulated in the lines read.
- **V. vinifera:** the susceptible Morio Muskat and Mueller-Thurgau are "extremely wettable", needing great force to remove a drop (l. 179); Riesling is "completely wettable" in cryo-SEM, drops flattening and spreading (l. 88). Riesling and Siegerrebe have hairs but are completely wettable (l. 113-114).
- **Hairy species:** drops stay spherical on V. doaniana and V. davidii and cannot reach the leaf surface (l. 89-92); V. labrusca held a fluorescein dye very poorly (l. 82-83), and dew droplets adhere very weakly to the hairs of very pubescent leaves such as V. labrusca (l. 184-186).
- **Time:** "all varieties", that is the cultivars compared, showed similar adhesion values 1 h after drop application (l. 190-191). In contrast, the hairy species "were clearly differentiated": their forces were at the same level but showed a greater difference 1 h after (l. 192-195). Riesling differed from the other cultivars shortly after wetting but became wettable within a rather short time (l. 184-187).
- **Authors' inference, not measured:** high contact angles make drops "pearl off", which speeds drying of the surface and reduces the area for spore penetration (l. 176).

## Dependence

- Own measurements. The contact-angle ranges the authors mention are cited from Barthlott and Neinhuis (1997). The torsion-balance adhesion test is the authors' own new method.

## Bearing (2026-10-25)

- **micro.wet_threshold_mm and micro.storage_mm_per_lai:** no film thickness, no volume per leaf area. Drop adhesion by cultivar tells which leaves hold a drop, not how much a canopy holds.
- **Drying parameters (micro.density_drying_slowdown, micro.evap_mm_h_per_hpa):** only the authors' unmeasured inference that hairy leaves dry faster (l. 176). Not a rate.
- **Disagreement to carry:** the "completely wettable" Riesling here and the high contact angles of Riesling in `konlechner2016` come from different methods (adhesion force of 15 microlitre drops against static angles of 6 microlitre drops) and are not directly comparable.
- **Kind of result:** measurement of drop adhesion on 13 Vitis species and cultivars at one site and season; the hairy wild Vitis species are an analogue for V. vinifera, not the crop.
