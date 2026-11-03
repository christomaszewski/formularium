---
id: verdugo2025
citation: Verdugo-Vasquez, N., Gutierrez-Gamboa, G., Valdes-Gomez, H. & Acevedo-Opazo, C. 2025. Development of a predictive model of phenology in grapevines cv. Cabernet Sauvignon under conditions of high spatial variability in Maule Valley. Agrociencia Uruguay 29(NE2):e1242
doi: 10.31285/agro.29.1242
read: 2026-11-03, the methods and the passages on zones (abstract and model sections checked by the note writer with grep), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine (Cabernet Sauvignon)]
regions: [Chile (Maule Valley)]
processes: [phenology, budburst, growing degree-days, Mitscherlich model, management zones]
records: []
datasets: []
files: [dr1103_verdugo2025.pdf (the 2026-11-03 drop)]
---

# Verdugo-Vasquez et al. 2025: a degree-day phenology model for Cabernet Sauvignon in Chile

A model of phenological stage against growing degree-days for one Chilean Cabernet Sauvignon block with two zones that differ in phenology.

## What it holds

- **Grid (l. 195):** phenology scored every 7 days from budburst to veraison on a regular grid of 18 sites (reading agent), as published before (verdugo2015).
- **Two zones (l. 222-224):** because of high spatial variability within the block, it was divided into 2 management zones with significantly different phenology. Zone 1 is the more advanced in all seasons and is 78 % of the area; zone 2 is 22 % (l. 224-225).
- **Lag (l. 430-431):** a lag between the zones begins at budburst and extends to harvest; the largest, 5 to 6 days, is at flowering (stage 23) (l. 430-432, the days on the following line).
- **Model form (l. 227-237, 33-38):** a monomolecular Mitscherlich equation (Eq. 1); stage W from budburst (stage 4) to technological harvest (stage 38), against growing degree-days t.
- **It is a heat-sum model:** GDD with a base temperature of 10 °C, by the equation of Bindi and others (Eq. 2) (l. 239-240). The rate k was fitted in Matlab (l. 240).
- **Fitted on:** data from both zones for the 2009-10 and 2010-11 seasons (l. 225-227; abstract l. 38-40). Validated on 2011-12 for the same block and on three Cabernet Sauvignon fields of low spatial variability (abstract), R2 above 0.98 and SD between 1.0 and 1.84 phenological units (abstract, units of the scale, not days).

## Dependence

- Builds on the Mitscherlich form of Ortega-Farias and others and the GDD of Bindi and others (both cited, l. 227-240). Fitted on the authors' own 2009-11 observations of the block in verdugo2015 (field 1). Authors overlap with verdugo2015 (a flag only).

## Bearing (2026-11-03)

- **host.vine_sd_days (1.5 days):** confirms the two-zone structure of verdugo2015 (78 % / 22 %) and a 5 to 6 day lag at flowering. No per-vine SD in days.
- **Phenology model:** a calibrated heat-sum model for Cabernet Sauvignon in a Chilean block, not a budburst model for Agrarium's regions. Kind of evidence: model fitted and validated on the authors' observations.
