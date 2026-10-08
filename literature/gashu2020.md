---
id: gashu2020
citation: Gashu, Kelem, Persi, Noga Sikron, Drori, Elyashiv, Harcavi, Eran, Agam, Nurit, Bustan, Amnon & Fait, Aaron. 2020. Temperature Shift Between Vineyards Modulates Berry Phenology and Primary Metabolism in a Varietal Collection of Wine Grapevine. Frontiers in Plant Science 11:Article 588739
doi: 10.3389/fpls.2020.588739
read: 2026-10-08, in full except the reference list; Tables 1-2 partly garbled, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Israel]
processes: [phenology, berry composition]
records: []
datasets: []
files: [10-3389-fpls-2020-588739.pdf]
---

# Gashu et al. 2020: two Negev vineyards, phenology and berry metabolism

From Ben-Gurion University and Israeli research centres. Thirty cultivars at two sites 1.5 °C apart.

## What it holds

- Field study of 30 wine-grape cultivars (20 red, 10 white), all on 140 RU rootstock, at two Negev sites 53 km apart: Ramon, 850 m asl, and Ramat Negev, 300 m asl (l. 28, 138-139, 147).
- Three seasons, 2017-2019; stages scored weekly on E-L scale, four replicates of 8-9 vines (l. 149, 154).
- The sites differ by 1.5 deg C in mean daily temperature (l. 29). Huglin index (Huglin 1978) summed March to August with k = 1.02-1.06 (l. 136, 147): hot (HI > 3,000) at Ramat Negev, warm (> 2400) at Ramon (l. 285).
- Harvest is defined by reaching a target Brix, 20+-1 white and 23+-1 red, not by a model (l. 473-474).
- Whites reached harvest 6-14 days earlier at the warmer site (l. 243); reds varied more by season than by site.
- Veraison to harvest took 23-29 days in whites and 36-47 days in reds (l. 471-472).
- Authors report that bud break onset does not predict harvest in this arid setting (l. 858-860).
- No phenology model is fitted or run; the data are observations, usable as an out-of-region test set. Metabolite data (sugars, acids) are not about phenology.

## Dependence

- Its own dates (2017-2019); harvest set by sugar thresholds, so no model dated them. It computes only the Huglin index (l. 204), a heat index of the Winkler kind, which the engine holds as a reference piece.
- No author of an engine model.

## Bearing (2026-10-08)

- Clear and observational: how a 1.5 °C shift moves stage intervals across 30 cultivars. A check on a truth's phenology at hot, dry sites, not a model.
