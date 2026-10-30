---
id: rossi2008
citation: Rossi, V., Caffi, T., Giosuè, S. & Bugiani, R. 2008. A mechanistic model simulating primary infections of downy mildew in grapevine. Ecological Modelling 212:480-491
doi: 10.1016/j.ecolmodel.2007.10.046
read: 2026-10-07, the incubation section (eqs 8-9) and reference list, in place in the copy Cooptera holds
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Italy]
processes: [oospores, primary infection, incubation]
records: [rossi2008.primary, rossi2008.incubation, rossi2008.oospores]
datasets: [goidanich1957]
files: []
---

# Rossi et al. 2008: the primary-infection model

The model Cooptera shows on its portal, and whose pieces Agrarium's development family F1
uses. Only the incubation is noted here.

## What it holds

- **Incubation (eqs 8-9):** hourly progress 1/(24·(45.1 − 3.45·T + 0.073·T²)) and
  1/(24·(59.9 − 4.55·T + 0.095·T²)), summed to 1: the start and end of the window when
  oil spots appear. Credited "(Rossi et al., 2002)"; the paragraph cites Goidanich et al.
  1957 for incubation length that "depends mainly on T".
- **The source:** Rossi, Giosuè, Girometta & Bugiani 2002, Atti Giornate Fitopatologiche
  2002, 2:263-270 ([rossi2002](rossi2002.md), read 2026-10-09). Its Fig. 2 prints the same
  coefficients as days to oil spots, "adattate ai dati di Goidanich et al. (1957)".
- Rossi et al. 2005 (Riv. Ital. Agrometeorol. 3:7-13, read by a paper-search session)
  describes the model's incubation as "two regression equations relating temperature to
  the length of incubation, at two extreme levels of relative humidity", after Goidanich.
- Its survival form, 5.67 − 0.47x + 0.01x², comes from Blaeser & Weltzien 1979, and the
  60 °C·h infection threshold too.

## Dependence

- Eqs 8-9 are not Goidanich's table but regressions on its data, as Rossi et al. 2002
  state (p. 265): `calibrated_on: goidanich1957`, read since 2026-10-09.
- Computes Blaeser & Weltzien's survival equation.

## Bearing (2026-10-08)

- Cooptera relabelled its record: Rossi 2008 no longer "borrows" Goidanich's table
  (`cooptera@7b102e0`). The Rossi-Goidanich dependency holds through the calibration
  record instead.
- A truth using these curves holds Goidanich's table out of the engine. See
  [zachos1959](zachos1959.md) and [rafaila1968](rafaila1968.md) for incubations that stay.

## Outside Italy (2026-10-29, for Agrarium D67)

- Validation (p. 485-486): 43 natural epidemics in Emilia-Romagna, 1995-2006, 2-5 vineyards a year, first onset 11 May-29 June (median 25 May); 411 simulations, 79 % aborted; 57 accurate successful, 324 accurate aborted, 30 wrong successful, 0 wrong aborted; TPP 1, TNP 0.92.
- p. 482: the count starts on 1 January 01:00 for every year. "exposure to low temperature during winter seems to play an important role in breaking dormancy (Galbiati and Longhin, 1984), but this effect is not included in the model because it is assumed that oospores must experience such a low temperature in the winter of temperate climates". Dormancy break DOR = exp(-15.891 exp(-0.653(HT+1))); primary season starts at HT 1.3 (3 %), ends 8.6 (97 %).
- p. 487-489: 85 % of the 30 false alarms fell in the first week of May or earlier; early cohorts were of low density and plants had under 5-6 leaves.
- No site outside Emilia-Romagna, none in Germany or a mild oceanic climate; no southern-hemisphere start.
