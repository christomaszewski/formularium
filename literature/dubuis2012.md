---
id: dubuis2012
citation: Dubuis, Pierre-Henri, Viret, Olivier, Bloesch, Bernard, Fabre, Anne-Lise, Naef, Andreas, Bleyer, Gottfried, Kassemeyer, Hans-Heinz & Krause, Ronald. 2012. Lutte contre le mildiou de la vigne avec le modèle VitiMeteo-Plasmopara. Revue suisse de viticulture, arboriculture, horticulture 44(3):192-198
doi:
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 58 of 58 quotes found at their lines by scripts/verify_quotes.py; Fig. 1 (pp. 194), the validation text and Fig. 4 (p. 196) read in the page images by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Switzerland, Changins, Valais, Germany, Austria, northern Italy]
processes: [oospore maturation, primary infection, secondary infection, incubation, sporulation, sporangia survival, sporangia density, leaf wetness, validation, spray timing]
records: [vitimeteo.oospores]
datasets: []
files: [dubuis2012_vitimeteo.pdf]
---

# Dubuis et al. 2012: VitiMeteo-Plasmopara's rules, and nine years at Changins

Wanted item C17 of the 2026-10-09 search, found 2026-10-12 in Agroscope's repository
(open access). The fullest printed account of VitiMeteo-Plasmopara held here: every step's
criterion is in Fig. 1 (p. 194) and the oospore rule, the soil-infection rule and the
sporulation rule are spelt out in the text (pp. 195-196), with the model's validation
against first oil spots at Changins for 2003-2011 (Fig. 4, p. 196). No equation is
printed; three steps are functions "f(...)" whose form is not given.

## What it holds

- **Use and network:** more than 150,000 ha in Switzerland, Germany, Austria and northern
  Italy (Trentino, South Tyrol, Veneto) by 2012 (l. 59, 70-72); 157 Agrometeo stations of
  several types, 82 of them transmitting ten-minute values twice a day by GSM (49 in
  French-speaking Switzerland, 27 in German-speaking Switzerland, 6 in Ticino; l. 77-82,
  118-119); regional tables updated at about 09:00 and 19:00 (l. 181); five-day risk from
  Meteoblue forecasts (l. 197). Sprays per year vary from six to ten by region and year
  (l. 26, 34).
- **The model** (Fig. 1, read in the image; l. 123-168): two modules, soil infections and
  secondary infections (l. 112), every parameter adjustable by an expert for regional
  features (l. 92-93), values not printed.
  - Oospore maturation: Σ temperature above 8 °C reaching 140-160 °C, cited to Gehmann 1987
    (Fig. 1, l. 139-141); in the text, "la somme de température de 140 °C au seuil de 8 °C
    depuis le 1er janvier" (l. 236-239) and the Fig. 3 caption (l. 206). The unit is
    printed as °C.
  - Oospore germination: RH above 80 % or wet leaves, with temperature above 8 °C, for 8 h
    (algorithm 1); more than 5 mm of rain in 48 h (algorithm 2) (l. 125-131).
  - Dispersal by splashing: rain intensity above 3 mm/h at temperature above 8 °C, within
    6 h of germination (l. 129-131).
  - Primary (soil) infection: a sum of hourly mean temperatures during leaf wetness above
    50 °C (degree-hours) (l. 128, 229-236).
  - Incubation: f(temperature) after Müller & Sleumer 1934 (l. 142-143), shown as a curve
    per infection; oil spots become visible as incubation nears 100 % (p. 196).
  - Sporulation: 4 h of darkness with wet leaves, temperature above 12 °C and RH above
    92 %, cited to Bläser & Weltzien 1979 (l. 156-161, 242-246).
  - Sporangia density: f(temperature) after Hill 1989 (l. 153-154); survival:
    f(saturation deficit), with temperature and RH, no citation (l. 146-147).
  - Secondary infection: 3-29 °C, wet leaves, degree-hours above 50 °C (l. 141, 249-254).
  - Growth: Schultz 1992's leaf model (l. 94-96).
- **Validation at Changins, 2003-2011** (Fig. 4, read in the image; l. 229-261, 266): each
  year, oospore maturity in an outdoor test (leaf pieces in soil tubes, mature when they
  germinate within 24 h; l. 85-93), first infections in the outdoor laboratory and the
  epidemic in an untreated plot were compared with the model. In six of nine years the
  calculated end of incubation coincided with the first oil spots (l. 245-246); in 2005
  and 2007 the first spots came more than two weeks after it, so the model placed the
  primary infection too early (l. 247-251), which the authors put down to a weak
  calculated infection on small untreated areas (p. 196); in 2009 the model predicted
  the primary infection for 27 May while the first spot was seen on 25 May, probably from
  the rain of 14-15 May, which gave 5 mm in 48 h but never 3 mm/h, so no infection was
  computed (l. 255-260). The observed first-spot dates are in Fig. 4 only (an image).
- **Spray trials at Changins, 2009-2011,** Gamay and Pinot noir on 3309 (l. 97): the
  model strategy (a preventive spray before the next rain once the primary infection's
  incubation reaches 80 %, l. 287-288) saved 1.7 treatments a year on average (printed as
  24.6 %) against 6.7 in the reference plot (l. 297-298), regional practice being eight to
  ten (l. 300-301); 2007 and 2008 are called difficult years in which treatments were cut
  without loss of efficacy (l. 306). Protection lasts 8-10 d for contact products, 10-12 d
  for penetrant and systemic ones (l. 320-327).
- **Not printed:** any equation; the incubation curve's values; the survival and density
  functions; the regional parameter values; who scored the untreated plot; the 2003-2011
  first-spot dates as numbers.

## Dependence

- **VitiMeteo computes,** by this paper: Gehmann 1987's oospore sum (140-160 above 8 °C),
  Müller & Sleumer 1934's incubation, Hill 1989's sporangia density, Bläser & Weltzien
  1979's sporulation rule, Schultz 1992's growth model (l. 139-161, 94-96). Its 50
  degree-hour infection gate is given no source.
- **Calibrated on** the Changins observations since 2003 (oospore test, outdoor laboratory,
  untreated plot), by the paper's own account that these "serve to validate" the model and
  that experts adjust its parameters (l. 91-93, 230-234); no fit is described. Inferred.
- **Engine pieces:** `vitimeteo.oospores` is this rule (140 at 8 °C from 1 January), now
  read at a VitiMeteo source; the record's 2004 citation (Siegfried et al.) is still
  unread. The sporulation rule's form (4 h dark, RH threshold, 12 °C) is the engine's
  `caffi2013.sporulation` form (dark moist hours), by a different route (Bläser & Weltzien
  1979, where Caffi fitted its own data); the 50 °C·h gate is what `puelles2024.ur`
  credits to this paper.
- **Authors:** Bleyer, Kassemeyer, Viret, Bloesch, Krause: flags shared with `viret2005`,
  `viret2007`, `bleyer2008`, `bleyer2010`, `bleyer2022`, `leoni2026` (Dubuis).

## Bearing (2026-10-12)

- The VitiMeteo rules the catalogue and other notes carried as trails (`institutvitivinicole2015`,
  `zipse2010`, `bleyer2008`, `puelles2024`) are now read at a source paper: oospores 140
  (text) or 140-160 (figure) above 8 °C from 1 January; germination 8 h above 8 °C with RH
  above 80 % or wet leaves, after 5 mm in 48 h; dispersal at 3 mm/h within 6 h; infection
  above 50 degree-hours of wetness at 3-29 °C; sporulation 4 h dark above 12 °C at RH above
  92 %. The catalogue record `vitimeteo.oospores` is updated with this reading.
- For a truth: the model's own validation shows two of nine years with the primary
  infection placed more than two weeks early and one year with a missed rain, which is
  the error a truth should not reproduce by sharing these rules (Agrarium decision D27).
