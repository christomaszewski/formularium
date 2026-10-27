---
id: ebeling2018
citation: Ebeling, M. & Wang, M. 2018. Dissipation of plant protection products from foliage. Environmental Toxicology and Chemistry 37:1926-1932
doi: 10.1002/etc.4148
read: 2026-10-22, in full, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grasses, cereals, nongrass herbs]
regions: [European Union]
processes: [fungicide dissipation, foliar half-life, wash-off, rain, first-order kinetics, residue trials]
records: []
datasets: []
files: [gd1021_ebeling2018.pdf (the 2026-10-22 drop)]
---

# Ebeling and Wang 2018: foliar half-lives of 30 plant protection products from 396 residue trials

A re-estimate of the EU default foliar half-life (10 d) from company residue trials on grass, cereal and herb foliage: a median of 3.3 d, with rain explaining little.

**Read this first.** It holds no copper, no sulphur and no vine leaves: the 30 compounds are mostly synthetic actives and the substrate is grasses, cereals and nongrass herbs (l. 99, 135). Per-compound half-lives are only in Figures 1 to 3 and the Supplemental Data (not fetched), not in the text. The plus-or-minus sign is lost in the text layer, so the standard deviation of the arithmetic mean (4.1 d) prints blank (l. 190-194).

## What it holds

- **Data:** 396 field residue trials from 5 companies, 30 compounds (Table 1, PDF p. 2), all in the EU; leafy substrate of grasses and cereals or nongrass herbs (l. 99, 385). The fungicides include azoxystrobin, cyprodinil, dimethomorph, fenhexamid, fluopicolide, iprodione, mancozeb, propineb, tebuconazole and trifloxystrobin; there is no copper compound and no sulphur (l. 135).
- **Method:** a single first-order decline fitted per trial to give DT50; biphasic fits were no better for most trials; limits of quantitation treated after FOCUS (2014) (l. 95, 104). No equation is printed, only the DT50.
- **Half-lives:** 278 of 396 trials had enough measurements (l. 190). Median 3.3 d and arithmetic mean 4.1 d (SD lost, garbled) (l. 194); geometric mean over all trials, compounds and crops 3.2 d, 90th percentile 7.9 d (approach A, l. 195); per substance the geometric mean is 2.7 d and the 90th percentile 5.6 d (approach B, l. 197). The 10 d EU default rests on trials over 30 years old (l. 19).
- **Crop group:** grasses and cereals did not differ from nongrass herbs (approach A p = 0.42, B p = 0.91, C p = 0.82); medians 3.4 and 3.3 d (A), 2.9 and 2.8 d (B), 2.9 and 2.7 d (C) (l. 198).
- **Temperature:** no significant difference in DT50 between the northern and southern EU residue zones (p = 0.216 or higher, t-test on log DT50; l. 211). Cited, not tested here: Fantke et al. (2014) found a very low Q10 of 1.22 (factor 1.02) for foliar DT50, against 2.58 for soil (l. 308-309).
- **Rain:** over all trials daily dissipation correlated weakly with daily rain (Pearson r = 0.232, p < 0.001; R2 = 0.054, so 5 % of the variability; l. 243). Up to the 95th percentile of rain (6.5 mm d-1 or less) the correlation was not significant (r = 0.034, p = 0.289; R2 = 0.001; l. 249). The authors conclude dissipation is mainly driven by other factors and rain matters only for very heavy rain (l. 252, 360).
- **Cited wash-off values (not this paper's data):** mancozeb on apple seedlings, 90 % washed off after 5 mm of heavy rain (Hunsche et al. 2007; l. 315); chlorothalonil on tomato, 20 min or more at 13 to 25 mm h-1 cut residues by up to about 50 % (Fife and Nokes 2002; l. 318); on citrus, mancozeb, difenoconazole, iprodione, famoxadone, pyraclostrobin and copper kept their fungicidal activity despite 40 and 90 mm of artificial rain, measured indirectly by activity, not residue (Vincent et al. 2007; l. 320, 323). Cabras et al. 2001 (folpet and mancozeb on grapes and vine leaves under simulated rain) is among the cited sources (l. 298).
- **Data access:** proprietary; data and calculation tools are available from the corresponding author, and the Supplemental Data are on the publisher's site (l. 385).

## Dependence

- **Compares with** the EFSA (2009) default DT50 of 10 d, itself from Willis and McDowell (1987; 450 DT50 values, mean 5.9 d for insecticides); with Fantke and Juraske (2013; 4,500 foliar half-lives) and Fantke et al. (2014); kinetic rules from FOCUS (2014).
- **Data:** its own 396 company trials (BASF, Bayer, Dow, Monsanto, Syngenta). Nothing from the engine's models.

## Bearing (2026-10-22)

- **What it answers:** not the copper or sulphur half-life asked for; it holds neither. For synthetic fungicides on non-vine foliage the residue half-life is short: median 3.3 d, geometric mean 3.2 d, 90th percentile 7.9 d. That is residue dissipation, not loss of protection, so it does not set the protection window of Cooptera E6 or Agrarium's spray protection.
- **Rain and temperature:** it argues against a strong daily rain term for typical rain (rain explained 0.1 % of variability up to 6.5 mm d-1) and against a strong temperature term (Q10 1.22, cited). Takeable as a prior that wash-off needs heavy events; not takeable as a wash-off function, since no mm-to-fraction curve is printed and the cited values are for mancozeb and chlorothalonil on seedlings and tomato.
- **Leads for the vine and copper question:** Cabras et al. 2001 (vine leaves, folpet and mancozeb) and Vincent et al. 2007 (copper, activity-based). Kind of result: a pooled re-analysis of proprietary trials, first-order fits, with the per-compound table outside the text.
