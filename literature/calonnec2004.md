---
id: calonnec2004
citation: Calonnec, A., Cartolaro, P., Poupot, C., Dubourdieu, D. & Darriet, P. 2004. Effects of Uncinula necator on the yield and quality of grapes (Vitis vinifera) and wine. Plant Pathology 53:434-445
doi: 10.1111/j.1365-3059.2004.01016.x
read: 2026-10-22, in full (two columns interleaved; decimal marks print as middle dots), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [France, Bordeaux]
processes: [powdery mildew, yield loss, berry weight, must yield, wine quality, anthocyanins, aroma, damage function]
records: []
datasets: []
files: [gd1021_calonnec2004.pdf (the 2026-10-22 drop)]
---

# Calonnec et al. 2004: powdery mildew cuts berry weight, must, colour and aroma, by cluster class

Bordeaux Cabernet Sauvignon (1997, 1999) and Sauvignon blanc (1999): damage by the share of diseased berries, from the vine to the wine.

**Read this first.** This is berry-level and cluster-class damage, not a plot-scale loss-against-severity curve. The yield-loss percentages for classes C1 to C3 (4, 25, 32 % and so on) are estimates computed from berry weights, their frequencies and berries per cluster, not measured plot losses (l. 359-360). Severity here is the share of diseased berries; the area of a cluster under mycelium is not proportional to it (l. 352). Plots were protected against downy mildew and bunch rot, and mildew-free controls were sprayed with dinocap-sulphur (l. 163). Decimal marks are middle dots (0.91 prints as 0·91); some Table 3 cells are blank.

## What it holds

- **Design:** Cabernet Sauvignon (CSa) in 1997 and 1999 and Sauvignon blanc (Sa) in 1999, Bordeaux region (l. 85-87). Clusters scored 0 to 4 by the share of diseased berries: C0 none, C1 under 25 %, C2 26 to 50 %, C3 51 to 80 %, C4 over 80 % (l. 101-102). Also "I" batches: healthy berries mixed with 0 to 50 % by weight of diseased berries, set against naturally diseased "C" batches (l. 126). C classes overstate the effect compared with I batches (l. 555).
- **Berry weight:** diseased berries weighed 12 % (1997) and 20 % (1999) less than healthy ones: 1.50 against 1.32 g and 0.98 against 0.78 g (l. 26, 359, Table 3 l. 317). Fully diseased berries averaged 0.43 g against 0.81 g for the lightly and highly diseased together (1999; l. 340). At bunch closure in 1999, 80 days before harvest, diseased berries were already 9.7 % lighter (39 % for fully diseased), 6.6 against 7.3 mm across (l. 342). Berries per cluster did not differ significantly, so loss comes from smaller berries (l. 355).
- **Estimated yield loss by class:** about 4, 25 and 32 % in 1999 and 13, 15 and 22 % in 1997 for C1, C2 and C3 (l. 359-360). Must lost at vinification relative to healthy clusters, 1999: 10 % (C1), 26 % (C2), 34 % (C3), 45 % (C4) (l. 421). For the untreated plot in 1999 the total yield loss was estimated at 23.7 %, from mean cluster-class weights and class frequencies of 0.81 % (C0), 18.4 % (C1), 20.5 % (C2), 25.6 % (C3) and 34.6 % (C4) (l. 424-425). Mean cluster weight at harvest 1999, C1 123.9 g against C3 95.1 g (P = 0.04; l. 352).
- **Diseased berries by weight** (Table 4, PDF p. 6): 1997 CSa at harvest C1 12.1 %, C2 31.2 %, C3 62.9 % (l. 386); 1999 CSa C1 19.1 % (4.7 at bunch closure), C2 48 (23.9), C3 75.2 (63.6), C4 100 (96.8) (l. 399-400). C4 clusters had over 40 % fully diseased berries (l. 352).
- **Sugar:** 1999 CSa, Sg = 0.36 x %PM + 179.9 g per L (R2 0.97) in 700 g samples; diseased berries were 20 to 21 % (CSa) and 14 % (Sa) sweeter (l. 443). The 1997 sugar did not differ (abstract, l. 28).
- **Colour:** total anthocyanins fall 0.91 % (1997) and 0.66 % (1999) per percentage of mildewed berries added by weight; 1997 At = -10.01 x %PM + 1102.3 (R2 0.86; l. 470, 473).
- **Aroma:** 3-mercaptohexanol in the Sauvignon wine, 3MH = -5.4 x %PM + 427 (R2 0.84), 38 % lower at I30 and 63 % lower at I50; the olfactory threshold is 60 ng per L (l. 565).
- **Tasting:** experts recognised wines from berries with about 25 % powdery mildew (C2, I30); non-experts needed 50 % (l. 34, 583). In preference tests CSa wines with 30 % or more diseased berries by weight ranked worst; below that the preference was not significant (l. 588).
- **Economics and limits:** where yield is restricted for quality the slightest loss costs a lot; flexible systems can compensate (l. 620). The results need confirming on other cultivars and vintages and larger wine volumes (l. 681).

## Dependence

- **Own data:** field and winemaking, Bordeaux 1997 and 1999; none published beyond Tables 3 and 4. Vinification after Hatzidimitriou et al. (1996) and Darriet et al. (2001), anthocyanins after Glories (1998).
- **Compares with** Ough and Berg (1979), Pool et al. (1984), Gadoury et al. (2001a, b), Amati et al. (1996) and Piermattei et al. (1999). Calonnec and Cartolaro also wrote `calonnec2008` (same group): a flag, not a dependency.

## Bearing (2026-10-22)

- **What it answers:** a damage function for powdery mildew on yield and quality, by the share of diseased berries per cluster. Weight loss per diseased berry is 12 to 20 %; estimated yield loss by cluster class 4 to 32 %; must loss 10 to 45 %; quality loss starts at about 25 % of berries mildewed for experts.
- **For the engine and Agrarium economics:** takeable as a bunch-level loss table (class to loss) and as a quality threshold for pricing, once the model outputs a share of diseased berries per bunch; `calonnec2008` simulates leaves only and has no damage function (l. 737 there). The 23.7 % is one untreated plot in 1999.
- **Not shown:** a link from leaf severity or epidemic curves to the berry share, a curve over many plots or years, cultivars beyond two, money values. Kind of result: field and cellar measurements in two vintages, with class losses computed, not observed at plot scale.
