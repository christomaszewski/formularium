---
id: dubuis2019
citation: Dubuis, P.H., Bleyer, G., Krause, R., Viret, O., Fabre, A-L., Werder, M., Naef, A., Breuer, M. & Gindro, K. 2019. VitiMeteo and Agrometeo: two platforms for plant protection management based on an international collaboration. BIO Web of Conferences 15:01036 (42nd World Congress of Vine and Wine)
doi: 10.1051/bioconf/20191501036
read: 2026-10-08, in full by a reading agent (claude-sonnet-5-5); 62 quotes checked by scripts/verify_quotes.py, the calibration sentences read by the main session
status: read
diseases: [downy mildew, powdery mildew, black rot]
crops: [grapevine]
regions: [Switzerland, Baden-Württemberg]
processes: [oospore maturation, primary infection, decision support]
records: [vitimeteo.oospores]
datasets: []
files: [bioconf-oiv2019_01036.pdf]
---

# Dubuis et al. 2019: VitiMeteo and Agrometeo

From Agroscope (Nyon, Wädenswil), the Freiburg wine institute, Geosens and the Vaud
agriculture service. A four-page overview of the platforms that run VitiMeteo Plasmopara,
whose oospore rule the engine runs (`vitimeteo.oospores`).

## What it holds

- VitiMeteo, a consortium since the early 2000s (l. 79), runs a mechanistic Plasmopara
  model described only by citation (Viret 2005, Bleyer 2008, Dubuis 2012; l. 96-97). No
  equations.
- **Calibration, in its words:** the models were "validated by observations in an external
  laboratory and in fields", and "the different parameters were adjusted according to
  these observations" (l. 83-84). The example is oospore maturation (l. 85): overwintered
  leaf pieces moved in spring to 100% RH and 20 °C, mature if they germinate within 24 h
  (l. 90-91). No rule, threshold, site or years are given. Experts can also change most
  parameters to fit their own observations (l. 104-105).
- **Changins field laboratory:** rows of 12 vines each of Pinot noir, Gamay and Chasselas
  over infected leaves laid on the soil every autumn (l. 95-97). Table 1 compares
  predicted primary infection, the computed end of incubation and the first oil spots,
  2003-2018 (l. 143): first oil spots from 5 May (2014) to 11 June (2004) (l. 159, 149);
  10 of 16 years right, 3 early, 3 late (l. 117-120), tolerance not stated.
- VitiMeteo's phenology is "after Molitor" (l. 114).

## Dependence

- It is VitiMeteo's own description, so its pieces are one model with the engine's
  `vitimeteo.oospores` (D26).
- **Calibration:** the oospore rule was adjusted to germination observations whose place
  and years are not given. Whether the Changins field-laboratory years were among them is
  not said. Formularium's record for `vitimeteo.oospores` notes this (read here).
- Bleyer, Krause, Viret, Naef and Breuer are among the engine's VitiMeteo authors; Molitor
  (the engine's phenology) is thanked for the phenology and black rot models.

## Bearing (2026-10-08)

- **Changins's oil-spot dates are risky to match a truth to.** They may be among the data
  VitiMeteo was adjusted to, and Leoni et al. 2026's model (also run by the engine) was
  fitted at Changins too. Until VitiMeteo's calibration data are named, treat a truth
  matched to them as calibrated with VitiMeteo, in a sensitivity arm.
- Nothing to compute here; the model papers (Viret 2005, Dubuis 2012) are not held.
