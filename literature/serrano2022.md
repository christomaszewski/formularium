---
id: serrano2022
citation: Serrano, L. & Gorchs, G. 2022. Water availability affects the capability of reflectance indices to estimate berry yield and quality attributes in rain-fed vineyards. Agronomy 12:2091
doi: 10.3390/agronomy12092091
read: 2026-10-22, lightly: the site and methods, Tables 1, 2 and 4 and the yield sentences, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, Catalonia, Penedès, Masquefa]
processes: [yield components, vine water status, reflectance indices, vine-to-vine variability]
records: []
datasets: []
files: [gd1021_serrano2022.pdf (the 2026-10-22 drop)]
---

# Serrano & Gorchs 2022: yield per vine in ten rainfed Penedès Chardonnay vineyards, 2007 to 2011

A remote-sensing paper (reflectance indices against vine water status, yield and berry quality) whose Table 4 gives the only Penedès Chardonnay yield per vine in this batch.

**Read this first.** It reports kg of fruit per vine, not bunches per vine, and no bunch count or bunch weight is printed. The thirty vines were picked for contrasting vigour, so the vine-to-vine spread is wider than a random vine's. The held `serrano2012` is a different paper.

## What it holds

- **Site and years:** ten rainfed commercial vineyards of Chardonnay (clone K5V1) around Masquefa, DO Penedès, measured in 2007, 2008, 2009 and 2011 (l. 132-134); municipalities Masquefa, Piera, Sant Llorenç d'Hortons and Sant Sadurní d'Anoia, areas 0.9 to 13.8 ha (Table 1, l. 143-152).
- **Vines:** planted 1990 to 2001, 2,083 to 3,703 vines ha-1, Double Royat training (l. 163-165). Thirty vines (3 per vineyard) "with contrasting vigour" were measured, at veraison in the third and fourth week of July; harvest was around the second week of August (l. 167-173).
- **Yield per vine** (Table 4, l. 357-361; n, min to max, mean, SD): 2007 30 vines, 1.19 to 5.56, 3.41 ± 1.33 kg; 2008 27, 1.50 to 6.93, 3.77 ± 1.27; 2009 24, 1.92 to 7.28, 4.22 ± 1.49; 2011 29, 1.25 to 11.51, 5.82 ± 2.25 (CV 38.6 %). The CV is 33.7 to 39.0 % in every year; 2011 is significantly higher than the other years (l. 340).
- **Weather** (Els Hostalets de Pierola station of the Catalan network): long-term mean 15 °C and 550 mm a year; 2009 and 2011 were about 2 °C warmer and 163 and 188 mm wetter than that (l. 155, 271-275). Mean temperatures 15.0, 14.6, 17.5 and 17.2 °C for 2007, 2008, 2009 and 2011; pre-veraison P − ET0 −274.5, −97.0, −216.4 and −89.1 mm (Table 2, l. 300-303).
- **Station coordinates:** printed as 41°31′59″ N, 1°48′31″ W (l. 156, 295), although the vineyards are at positive longitudes, about 1.75 to 1.83 °E (Table 1): a sign slip. The station is the one `ramos2017` uses, and 1°48′31″ is about 1.81° (computed), the magnitude `ramos2017` prints with a minus sign: a west sign for an eastern place, which supports that note's reading of a misprint.

## Dependence

Own measurements. The same vineyards are described in more detail in Serrano et al. (the paper's refs 21 and 29) and González-Flor et al. (ref 23), cited and not read here (l. 166-167, 278); the yields may be shared with those papers, so the sets are probably not independent. The weather source (the Els Hostalets de Pierola station) is the one `ramos2017` uses: a shared source, not a shared model.

## Bearing (2026-10-22)

- **host.bunches_per_vine:** no count. Yield of 3.4 to 5.8 kg a vine (means by year) at 2,083 to 3,703 vines ha-1 is a crop-load check only; a count needs a bunch weight, which this paper does not give. Rainfed Penedès Chardonnay, four seasons between 2007 and 2011; the paper calls water restriction severe before veraison in 2007 and 2009 (l. 279-282).
- **host.vine_sd_days:** nothing; there are no phenology dates.
- **Cultivar susceptibility:** none; no disease is studied. The Penedès Chardonnay vineyards are a place for site data (rainfed, Double Royat), not a susceptibility rating.
- **Kind of result:** measurement of yield in ten vineyards over four years, with vines chosen for contrasting vigour.
