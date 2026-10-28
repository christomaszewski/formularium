---
id: carrasco2008
citation: Carrasco, M. & Ortega-Farias, S. 2008. Evaluation of a model to simulate net radiation over a vineyard cv. Cabernet Sauvignon. Chilean Journal of Agricultural Research 68(2):156-165
doi: 10.4067/s0718-58392008000200005
read: 2026-10-27, text in reading order; Eqs 1-3 and Table 1 in the page image; Tables 2-3 garbled in extraction and not used; by a reading agent (model not recorded in its JSON) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Chile, Maule]
processes: [net radiation, longwave radiation, emissivity, canopy temperature]
records: []
datasets: []
files: [dr1027_carrasco2008.pdf (the 2026-10-27 inputs-d60 drop)]
---

# Carrasco and Ortega-Farias 2008: net radiation over a Cabernet Sauvignon vineyard from air temperature, humidity and solar radiation

A vine-specific net radiation model (shortwave balance plus a Brutsaert-form atmospheric emissivity) checked against a net radiometer over a trellised vineyard in Chile.

**Read this first.** The coefficient phi was fitted on a different (Merlot) vineyard data set, not on this site, and its source (Ortega-Farias et al. 2004) is not held. Tables 2 and 3 (errors by season and sky) came out scrambled; only narrative maxima are used.

## What it holds

- **Site and canopy:** Cabernet Sauvignon, Pencahue Valley, Maule Region, Chile (l. 16); vertical shoot positioning 1.5 m high (l. 168); rows 3.0 m, vines 1.2 m, LAI 0.81-1.39 (from the JSON claim, l. 168).
- **Sensors and heights:** net radiometer REBS Q7.1 (l. 220); air temperature and RH at 2.7 m, canopy temperature at 1.2 m, solar and net radiation at 3.5 m above ground (Table 1, page image).
- **Model (Eq. 2, Eq. 3, page image):** Rn = (1 - alpha) Rsi + eps_a sigma Ta^4 - eps_f sigma Tf^4, with eps_a = phi (ew / Ta)^(1/7), ew in kPa (l. 132). Equations are printed complete.
- **Parameters:** canopy emissivity 0.98 and albedo 0.18 (l. 194); phi 1.51 for Rsi > 0 and 1.91 for Rsi < 0, fitted on a Merlot vineyard database (l. 232).
- **Error at 30 min:** MAE below 40 W m-2 and RMSE below 61 W m-2 (l. 24); the cloudy-day maxima are MAE 40 and RMSE 61 W m-2 (l. 335). The slope b is 0.91-0.93: Rn is overestimated by 7-9 % (l. 314). Daily error is below 1.68 and 1.75 MJ m-2 d-1 (l. 24).
- **Canopy temperature:** using it for the surface term in place of air temperature did not improve Rn (l. 32); dT between canopy and air was -3 to 4 degC (JSON claim).

## Dependence

- Eq. 3 is the Brutsaert form with an empirical coefficient from Ortega-Farias et al. 2004 (not held). phi was fitted on a Merlot data set from the same group.
- Shares the Brutsaert/Idso family with amir2016 and, in form only, the Brutsaert option in flerchinger2009. Independent of sentelhas2008.wetness, cooptera.rh90_wetness and cooptera.logistic_wetness (no shared threshold, equation or data).

## Bearing (2026-10-27)

- **Inputs it needs:** global radiation, air temperature, RH. All are on common station networks, so it can fill net radiation (and the longwave term for dewfall or wetness energy balance) where only a station is available. Kind of result: a validated model on vines, with one fitted coefficient.
- **Error to carry:** about 40-61 W m-2 (MAE, RMSE) at 30 min, worse under cloud, with Rn overestimated by 7-9 %. Daytime and night phi differ. Validated for one cultivar, one trellis and one year-span in Chile; not for Catalonia or other trellises.
- **Not shown:** nights alone (Tables 2-3 unreadable), dew or wetness. Useful for weighting a net radiation fill by its stated error.
