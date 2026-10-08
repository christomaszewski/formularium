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
  2002:263-270 (eds Brunelli & Canova, CLUEB, Bologna). Held by no one on 2026-10-08.
- Rossi et al. 2005 (Riv. Ital. Agrometeorol. 3:7-13, read by a paper-search session)
  describes the model's incubation as "two regression equations relating temperature to
  the length of incubation, at two extreme levels of relative humidity", after Goidanich.
- Its survival form, 5.67 − 0.47x + 0.01x², comes from Blaeser & Weltzien 1979, and the
  60 °C·h infection threshold too.

## Dependence

- Eqs 8-9 are not Goidanich's table, but very probably regressions on Goidanich's (that
  is, Casarini's Emilia) data: recorded as `calibrated_on: goidanich1957`, inferred.
- Computes Blaeser & Weltzien's survival equation.

## Bearing (2026-10-08)

- Cooptera relabelled its record: Rossi 2008 no longer "borrows" Goidanich's table
  (`cooptera@7b102e0`). The Rossi-Goidanich dependency holds through the calibration
  record instead.
- A truth using these curves holds Goidanich's table out of the engine. See
  [zachos1959](zachos1959.md) and [rafaila1968](rafaila1968.md) for incubations that stay.
