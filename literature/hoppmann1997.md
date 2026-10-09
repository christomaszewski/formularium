---
id: hoppmann1997
citation: Hoppmann, D. & Wittich, K.-P. 1997. Epidemiologie-bezogene Modellierung der Blattnässedauer als Alternative zur Messung, gezeigt am Beispiel von Plasmopara viticola. Zeitschrift für Pflanzenkrankheiten und Pflanzenschutz 104:533-544
read: 2026-10-09, in full by a reading agent (claude-haiku-5-5); every quote checked at its line by verify_quotes.py, key numbers checked by the main session; p. 536 read by the main session in the page image
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Rheingau]
processes: [oospore maturation, secondary infection, leaf wetness, sporangia survival]
records: [vitimeteo.oospores]
datasets: []
files: [Hoppmann-Epidemiologyrelatedmodellingleafwetness-1997.pdf]
---

# Hoppmann & Wittich 1997: the Geisenheim (DWD) model and modelled leaf wetness

## What it holds

- **Leaf wetness:** Wittich 1993's model (built for apple orchards): an energy balance on a
  rigid plate for dew and its evaporation, and a module for rain drops' evaporation. No
  equations printed; storage capacity measured 0.135 mm, maximum dew 0.18 mm. Against a
  Lufft sensor in September 1995, r² = 0.91. Table 1 compares wetness sensors in the
  Geisenheim vineyard, May-July 1990.
- **The Plasmopara model** (Hoppmann 1996, a DWD report not held; p. 536, read in the page
  image): oospores mature after 170 degree-days above a daily mean of 8 °C 'during spring';
  primary infection after 5 mm of rain in 3 days; incubation a nonlinear function of
  temperature, 5 days at 22 °C; secondary infection after at least 4 h of wetness at a mean
  of at least 11 °C, more than 12.5 °C in the first wet hour, in darkness; germination after
  2-4 h of wetness above 6 °C; sporangia mortality by 'the exponential survival function of
  BLÄSER (1978)' (his dissertation); oil-spot propagation by Hill's (1989) cubic, zero below
  11 °C and 10 above 17.5 °C; dew nights a third of rain nights; 50 initial spots per
  hectare, losses above 5000.
- **Validation:** against oil-spot monitoring at Geisenheim, 1989-1995 (no infections in
  1991 and 1993); 'confirmed', with no statistic.

## Dependence

- Bläser 1978 is the laboratory basis of the whole model and of its survival function; Hill
  1989 of oil-spot propagation; Gehmann 1987 field data.
- Its oospore rule has VitiMeteo's form (`thermal-time-oospore-threshold`); not recorded as
  a formulation, since its equations are not printed.

## Bearing (2026-10-09)

- Kin to the engine: VitiMeteo's oospore form (170 against 140 degree-days; flagged on
  `vitimeteo.oospores`) and Bläser's survival data. Probably VitiMeteo's DWD ancestor
  (inferred).
- Wittich's wetness model is a physical alternative to the engine's RH thresholds and to
  Agrarium's canopy water bucket.
