---
id: merot2020
citation: Merot, A., Fermaud, M., Gosme, M. & Smits, N. 2020. Effect of Conversion to Organic Farming on Pest and Disease Control in French Vineyards. Agronomy 10:1047
doi: 10.3390/agronomy10071047
read: 2026-10-25, lightly (abstract, introduction, the methods on the network and protection strategies with Table 1, and the discussion passage on mildew management; about lines 1-210 and 640-655 of 879; the results tables not read in full), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 7 of 7 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew, grey mould]
crops: [grapevine]
regions: [France, Rhône, Gard, Languedoc]
processes: [fungicide treatments, conversion to organic, copper, sulfur, spray count, protection strategy]
records: []
datasets: []
files: [dr1025_merot2020.pdf (the 2026-10-25 drop)]
---

# Merot et al. 2020: fungicide treatments a year on Mediterranean Grenache plots in conversion to organic farming, 2013 to 2016

A plot-monitoring study of conventional and converting vineyards in the Mediterranean part of the Côtes du Rhône and Languedoc, whose Table 1 gives treatments a year.

**Read this first.** The treatment counts pool powdery and downy mildew fungicides, so the downy mildew share cannot be separated (sulfur is counted against powdery mildew). Two details need care. (1) The abstract says "48 vineyard plots" (l. 19) but the methods say 25 plots and 48 plot-years (l. 140), which is the reading used here. (2) In Table 1 the conventional row's insecticide cell reads 15, which is probably 1.5 with a lost decimal point (garbled; not used). Only parts of the paper were read; the results tables were not read in full.

## What it holds

- **Network:** 25 commercial plots in the Mediterranean Côtes du Rhône region of south-east France (Rhône, Ventoux, Costières de Nîmes, Languedoc, southern Gard), all Grenache, 48 plot-years in 2013 to 2016, conventional or in year 1 to 3 of conversion to organic (l. 140).
- **Conventional plots, Table 1:** 11 synthetic fungicide treatments a year (powdery and downy mildew together) plus 4.4 biocontrol (mostly sulfur) fungicide treatments (l. 198).
- **Conversion, Table 1:** year 1 has 5.2 non-synthetic plus 4.8 biocontrol fungicide treatments a year (l. 199), about 10 in all; year 2 has 6.4 plus 6.4 (l. 200), about 12.8; year 3 has 5.6 plus 6.7 (l. 201), about 12.3 (sums are arithmetic, not printed).
- **Authors' reading:** copper and sulfur products are leachable and less effective in Mediterranean conversions, so organic growers need more treatments and depend on rainfall events after each spraying (l. 651).
- **Cited from the French national survey (Agreste 2016):** average TFI 15.3 (biocontrol excluded), equal to an average of 20.1 treatments a year; fungicides are 80 % of treatments (l. 50).

## Dependence

- Plot monitoring with protection strategies recorded by the growers. The national figures are cited from the Agreste 2016 survey. Authors Merot, Gosme and Smits are also authors of held notes (`fouillet2024`; Smits also `leroy2013`); a shared author is only a flag.

## Bearing (2026-10-25)

- **Sprays per season (spray.per_season):** 11 synthetic plus 4.4 biocontrol fungicide treatments a year on conventional Grenache plots in southern France, 2013 to 2016, for both mildews together (l. 198). It is an upper bound for downy mildew passes alone; the open-data count for the same area (about 6 downy mildew passes, `nefti2024data`) is lower. Kind: plot monitoring (measurement of recorded practice).
- **Organic response:** about 10 to 12.8 fungicide treatments a year in the three conversion years, more than the 5 to 7 downy mildew passes of the DEPHY records, again with both mildews pooled (l. 199-201). Supports a higher count for organic growers, with copper and sulfur washing off in rain (l. 651).
- **Not shown:** downy mildew alone, intervals, delay from warning to spray, Catalonia.
