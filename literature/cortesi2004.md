---
id: cortesi2004
citation: Cortesi, P., Ottaviani, M.-P. & Milgroom, M. G. 2004. Spatial and genetic analysis of a flag shoot subpopulation of Erysiphe necator in Italy. Phytopathology 94:544-550
doi: 10.1094/PHYTO.2004.94.6.544
read: 2026-10-25, lightly: the abstract, the vineyard layout and the disease-focus section (the genetic analyses not read; two columns interleaved), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [Italy, Tuscany]
processes: [dispersal gradient, flag shoots, primary inoculum, disease foci, row direction, spatial autocorrelation]
records: []
datasets: []
files: [dr1025_cortesi2004.pdf (the 2026-10-25 drop)]
---

# Cortesi et al. 2004: disease foci round flag shoots in a Tuscan vineyard, with a hint that spread favours the row

A vineyard was surveyed for flag shoots of grape powdery mildew for eight years; in 1997 disease was assessed on the 21 vines round each of two flag shoots.

**Read this first.** An analogue: grape powdery mildew (Erysiphe necator), not downy mildew. The along-row result is in a figure only (Fig. 2, bar charts of incidence and severity by vine position); the text gives no numbers for it, so there is no ratio to take. And it is not a clean row effect. Vines in the same row stand 1.2 m apart, while the neighbouring rows are 3 m away (l. 99), so part or all of the difference may be plain distance. No distance was fitted and no kernel.

## What it holds

- **Site:** Santa Cristina vineyard, Montefiridolfi (Firenze), Tuscany, about 1 ha, Chardonnay and Malvasia, cordon trained and spur pruned; 3 m between rows and 1.2 m between vines in the row (l. 98-99). Flag shoots were surveyed each year from 1994 to 2001 (l. 92).
- **Focus design (1997):** disease was assessed on 21 vines round each of two flag shoots: the vine itself, three vines each side in the same row, and the seven corresponding vines in the rows either side (l. 134 and the lines after it).
- **Foci:** distinct disease foci developed round flag shoots early in the epidemic, "demonstrating a steep dispersal gradient of conidia" (l. 30); no distances or kernel were fitted.
- **Early spread:** by 19 May 1997 disease was on the vines closest to the flag shoots, on 6 and 8 of the 20 other vines surveyed round the two flag shoots (l. 223-224).
- **Row direction:** at all survey dates incidence and severity were typically higher on vines in the same row as the flag shoot than on vines in adjacent rows, 3 m away (l. 225-226); numbers only in Fig. 2.
- **Interpretation (the authors'):** flag shoots were spatially aggregated within and between years, which they attribute to short-distance dispersal of conidia from flags early in the season (l. 16).

## Dependence

- No dispersal model: spatial autocorrelation by randomisation (1,000 randomisations). The third author, Milgroom, also wrote papers on Erysiphe populations in held notes: a shared author, no shared model.

## Bearing (2026-10-25)

- **dm.row_barrier 2 [1-4]:** weak and only qualitative. Disease was higher along the row than in rows 3 m over (l. 225-226), which fits a row barrier above 1, but the along-row vines are also nearer, and no ratio can be taken from the text. Powdery mildew, Tuscany, 1997, one vineyard and two foci. A measurement of incidence, not a fit. Read with `calonnec2009`, which has a numeric but self-contradictory term.
- **dm.wind_scale_m 3 m [2-10]:** "steep" gradient round a flag shoot, with 6 and 8 of 20 neighbouring vines infected by 19 May (l. 223-224): metres, consistent with the registered scale, but no number for any distance and a different pathogen.
- **Not shown:** any wind-borne distance beyond the 21-vine blocks, a tail, or an effect of wind speed.
