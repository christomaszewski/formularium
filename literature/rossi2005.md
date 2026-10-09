---
id: rossi2005
citation: Rossi, V., Caffi, T., Giosuè, S., Girometta, B., Bugiani, R., Spanna, F., Dellavalle, D., Brunelli, A. & Collina, M. 2005. Elaboration and validation of a dynamic model for primary infections of Plasmopara viticola in North Italy. Rivista Italiana di Agrometeorologia 3:7-13
read: 2026-10-08 by the paper search session (its model description); 2026-10-09 the model description and references again by the main session, for the incubation question
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Emilia-Romagna, Piedmont, Lombardy]
processes: [oospore maturation, oospore germination, primary infection, incubation, validation]
records: [rossi2008.primary]
datasets: [goidanich1957]
files: [RIAM_3_2005.pdf]
---

# Rossi et al. 2005: the first account of Rossi's primary-infection model

The model later published in full as Rossi et al. 2008 (Ecol. Model.); "a detailed
description of the model will be published in a separated paper".

## What it holds

- **Stages:** oospore maturation (an index, IMO, rising hourly from 1 January with
  temperature and leaf-litter humidity, itself from vapour pressure deficit), germination of
  a cohort on each rain ≥ 0.2 mm/h with a rate depending on temperature "(Laviola et al.,
  1986)", sporangia survival ("6 hours to 6 days ... (Blaeser and Weltzien, 1979)", ΔSUR =
  1/(SURmax·24)), zoospore release (Ravaz 1914; Galet 1977), splash dispersal on rain ≥
  0.2 mm/h, infection on temperature and wetness "(Blaeser, 1978)", incubation.
- **Incubation (lines 181-185):** "the model calculates the length of the incubation period
  as a function of temperature and relative humidity (Goidanich et al., 1957). The model
  uses two regression equations relating temperature to the length of incubation, at two
  extreme levels of relative humidity." What they were fitted to is not stated.
- **Validation:** untreated plots in commercial vineyards, 1995-2004: Emilia-Romagna,
  Piedmont (1998-2002 at one site) and Oltrepò Pavese; weekly inspection for first oil
  spots; hourly weather from in-vineyard stations, and in Emilia-Romagna from the regional
  network (nearest station to 2000, a 5 × 5 km grid from 2001).
- States the 3-10 rule as Goidanich et al. 1957 give it: 10 °C in 24 h, shoots 10 cm, 10 mm
  of rain in 24-48 h.

## Dependence

- Computes Blaeser & Weltzien's survival (through Rossi 2008) and their infection data's
  rule; germination rate after Laviola et al. 1986 (literature/laviola1986); incubation
  regressions attributed to Goidanich et al. 1957.

## Bearing (2026-10-09)

- Agrarium asked whether this paper says what Rossi's incubation regressions (Rossi 2008
  eqs 8-9) were fitted to. It does not. Sanna 2017 (literature/sanna2017) says they were
  "adapted to the evaluation table of the incubation period of Goidànich (1957)", citing
  Giosuè et al. 2002: a third party's statement, recorded in `goidanich1957` as `trail`.
