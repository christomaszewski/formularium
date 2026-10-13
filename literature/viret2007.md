---
id: viret2007
citation: Viret, O., Bloesch, B., Fabre, A.-L. & Siegfried, W. 2007. Prévision du mildiou sur www.agrometeo.ch et gestion de la lutte. Revue suisse de viticulture, arboriculture, horticulture 39(1):57-59
doi:
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; Figs 1 and 3 read in the page images by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Switzerland, Changins, Valais, Suisse romande, Freiburg]
processes: [primary infection, secondary infection, incubation, sporulation, sporangia survival, sporangia density, oospore maturation, leaf wetness, forecasting]
records: [vitimeteo.oospores]
datasets: []
files: [viret2007_agrometeo.pdf]
---

# Viret et al. 2007: VitiMeteo's seven steps and their printed thresholds, 2006

Open access since 2026-10-12 (Agroscope's repository). Three pages for growers after the
2006 season, and the first VitiMeteo paper held here that prints the model's thresholds:
Fig. 1 lays the epidemic out in seven steps with a criterion each, and Fig. 3 prints the
oospore rule.

## What it holds

- **The network:** 66 stations forecast downy mildew in 2006 (25 in German-speaking
  Switzerland, 9 in Geneva, 7 in La Côte, 3 in Lavaux, 2 in the Chablais, 12 in Valais, 4
  in the Trois-Lacs region, 4 in Ticino; l. 5-9), sending data twice a day, forecasts at
  09:30 and 20:30 (l. 9, 14-15); on the internet since 2005 (l. 23). VitiMeteo is by
  Agroscope Changins-Wädenswil and the Freiburg institute (l. 12-13).
- **The seven steps** (Fig. 1, p. 57, read in the image): (1) oospore maturation, "manuel ou
  automatique"; (2) primary infection: oospore germination, dispersal by splashing,
  infection; (3) incubation by "courbe d'incubation (Müller)"; (4) sporulation at
  temperature above 12 °C, in darkness, with wet leaves or 92 % RH, for 4 h; (5) sporangia
  density "selon Hill (1989)"; (6) sporangia survival, mortality as a function of
  temperature and RH; (7) infection at 3-29 °C with wet leaves and degree-hours above 50
  (l. 30-57). Primary infections can occur all year from the soil, and several before the
  first one's incubation ends, as in 2006 (l. 19-24).
- **The oospore rule** (Fig. 3 callout, p. 59, read in the image): the oospore germination
  date is where the sum of temperatures above 8 °C reaches 160 ("Σ températures > 8 ° =
  160 °", l. 104; the unit is printed as degrees only); budburst for the growth model is the
  first unfolded leaf, BBCH 11 (l. 106). No start date for the sum is printed.
- **The infection value:** the sum of hourly temperatures over the leaf-wetness period, in
  degree-hours; above 50 a new infection is possible (l. 91-94; Fig. 3: 24 h of wetness
  without rain gave 377 degree-hours, limit 50, l. 133-140). Incubation progress in % is
  updated daily from temperature with the Müller curve (l. 146-147). Sporangia density is
  on a 0-300 scale, in thousands per cm² (l. 82-83).
- **2006 at Changins** (Fig. 3, the station's detailed report, model output unless said
  otherwise): oospore germination 13.05.2006, budburst 01.05.2006; primary infection of
  medium intensity on 18 May, incubation to 27 May; sporulation conditions met on 28 May
  with 171,000 sporangia/cm²; a strong secondary infection from those spores, incubation to
  7 June (l. 76, 120-143). Observed: the first oil spots appeared at the end of the
  incubation in untreated plots, and did not sporulate, under cold and dry weather to
  mid-June (l. 77-80). Primary infections were computed on 8-9 May at the earliest sites
  (Ticino, Valais, Geneva) and 14-18 May elsewhere (l. 74-75). The epidemic grew
  exponentially from early July to 100 % of leaves in untreated controls by August, with
  rain on 16 days at Changins (160 % of the 1960-90 norm) and 25 days at Wädenswil (287
  mm, 183 %) (l. 85-89).
- **How the algorithms were set:** untreated plots at Changins, Perroy, Allaman, Leytron,
  Wädenswil, Stäfa, Maienfeld and Freiburg were followed in 2006 and compared with
  VitiMeteo's computed infections "to parameterise the algorithms"; the computed
  infections agreed with the disease's course (l. 65-71). Which parameters, and how, is not
  printed.
- **Growth model:** on maximum temperatures, Pinot noir as reference, validated for Pinot
  noir, source not named here (l. 117-119, 151; Schultz 1992 in `viret2005`).
- **Not printed:** every equation; the Müller curve's values; the survival function's
  coefficients; the start date of the oospore sum; who observed the untreated plots.

## Dependence

- **VitiMeteo computes,** by this paper: Hill 1989's sporangia density (l. 57), a Müller
  incubation curve (l. 47, 146-147; no year or reference, so unidentified: Müller &
  Sleumer 1934 is the usual citation, `bleyer2008`), and a temperature sum above 8 °C to
  160 for oospore germination (l. 104; cf. Gehmann 1987 in `viret2005`). It was tuned on
  the 2006 untreated plots (l. 68-70): calibration data, unprinted.
- **Engine pieces:** `vitimeteo.oospores` (140 °C·day above 8 °C as Leoni et al. 2026 give
  Siegfried et al. 2004) is here printed as 160 above 8 °C; `institutvitivinicole2015`
  also gives 160 and `hoppmann1997` 170 for the Geisenheim model. No engine equation is
  computed; the 50 degree-hour gate is also the Puelles 2024 UR rules' (`puelles2024`,
  which Formularium records as borrowing VitiMeteo's 50 °C·h).
- **Authors:** Viret, Bloesch, Siegfried: flags shared with `viret2005`, `dubuis2012`,
  `bleyer2008`.

## Bearing (2026-10-12)

- The first held source that prints VitiMeteo's thresholds. The oospore sum is 160 above
  8 °C in 2007, not the 140 that Leoni et al. 2026 attribute to Siegfried et al. 2004:
  recorded as a flag on `vitimeteo.oospores`, with the 140 kept as its value until Siegfried
  2004 or Dubuis 2012 (`dubuis2012`) settles which the model ran and when.
- The 2006 Changins season gives a truth two observed facts (oil spots at the end of the
  first incubation, around 27 May; no sporulation under the cold dry spell to mid-June) and
  a set of model dates to keep apart from them.
