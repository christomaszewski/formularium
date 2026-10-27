---
id: camposarguedas2026
citation: Campos-Arguedas, F., Kirchhof, E., North, M. G., Londo, J. P., Bates, T., van Leeuwen, C., Destrac-Irvine, A., Bois, B. & Kovaleski, A. P. 2026. Cold hardiness dynamics predict budbreak and associated low-temperature threats in grapevine. New Phytologist 250(4):2203-2220
doi: 10.1111/nph.71074
read: 2026-10-26, a light reading from Europe PMC's JATS XML (no PDF held), by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; Eqns 1-7 from the XML's MathML, not a page image
status: read
diseases: []
crops: [grapevine]
regions: [New York, Ontario, Bordeaux, Alsace, Franconia]
processes: [budbreak, cold hardiness, deacclimation, frost risk]
records: [camposarguedas2026.budbreak_hardiness]
datasets: []
files: [camposarguedas2026.xml (the 2026-10-25 other-sources drop)]
---

# Campos-Arguedas et al. 2026: budbreak as the day modelled hardiness reaches a threshold

The NYUS.1 cold hardiness model (Kovaleski et al. 2023, not held), run on daily temperatures
with no tuning to budbreak, predicts budbreak as the day its projected 50 % hardiness
reaches +10 °C (vinifera) or +5 °C (Concord): RMSE 7.3 d on 329 records from eight sites
over 68 seasons. Freeze damage is read off the same curves.

## What it holds

- **Records** (l. 32, 39): 329 budbreak observations (50 % of buds at BBCH 05-09 or E-L 4),
  68 seasons from 1955-56 to 2022-23, eight sites in New York, Ontario, Pennsylvania,
  Bordeaux, Alsace and Franconia, three cultivars (Cabernet-Sauvignon, Riesling, Concord).
- **Weather** (l. 40-46): Daymet v4 (1 km) for North America, easyclimate downscaled 1 km
  for Europe, station records at Portland NY (1926-2023) and Bordeaux 2023.
- **Model** (l. 29, 34, 47-51): NYUS.1 fitted to Geneva NY hardiness; its 10th and 90th
  percentile parameters fitted here; chill by the Dynamic Model (chillR 0.76).
- **Budbreak rule** (l. 55-56): the day projected CH50 reaches +10 °C (Cabernet-Sauvignon,
  Riesling) or +5 °C (Concord), 0 °C for the Bordeaux 1981-2008 series, +5 °C for BBCH 05
  records.
- **Fit** (l. 84-89): uncorrected RMSE 7.3 d, bias -0.8 d, r² 0.88; freeze-corrected 7.2 d
  and 0.6 d; 129 of 329 seasons had predicted damage (bias -2.7 d with damage, +0.3 without);
  damage check at Portland NY (Concord, n 97) sensitivity 0.75, accuracy 0.73.
- **Damage and risk** (Eqns 1-7, l. 59-77): the damaged share interpolated between CH10, CH50
  and CH90, the corrected curves, the safety margin Tmin - CH50 and freeze-risk days.
- **Sensitivity** (l. 96-104): chill shifts of -6 to +6 °C raise the RMSE; budbreak -5.8 d
  per °C of mean dormant-season temperature (Concord -6.0, Riesling -5.5,
  Cabernet-Sauvignon -5.7).
- **Not printed:** per-site and per-cultivar statistics; NYUS.1's coefficients (its Table S2);
  PhenoFlex's RMSEs (l. 115).

## Dependence

- **Computes** NYUS.1 (Kovaleski et al. 2023) and the Dynamic Model's chill; the budbreak
  thresholds are chosen from Kovaleski et al. 2018's data (`kovaleski2018.deacclimation`),
  not fitted to the budbreak records. Kovaleski and Londo again.
- **Compared with** PhenoFlex (Luedeling et al. 2021), two parameterisations.

## Bearing (2026-10-26)

- For Agrarium's phenology truth (the 10-14 search): a budbreak rule that needs no heat sum
  to a threshold, only a hardiness model, validated on 329 records; it cannot run here
  without NYUS.1. Kin by form (cold hardiness, chilling) to the engine's Ferguson records and
  to kovaleski2018.
