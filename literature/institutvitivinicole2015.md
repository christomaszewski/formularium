---
id: institutvitivinicole2015
citation: Institut viti-vinicole, Abteilung Weinbau (no author printed). 2015. Hinweise zur Nutzung des Prognosemodells VitiMeteo Peronospora [Notes on using the VitiMeteo Peronospora forecast model]. April 2015, 6 pp.
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Germany (Freiburg Weinsberg)]
processes: [infection, leaf wetness, oospores, incubation, sporulation, secondary infection, spray timing]
records: [vitimeteo.oospores]
datasets: []
files: [lu_vitimeteo_peronospora_luxembourg.pdf]
---

# Institut viti-vinicole 2015: using the VitiMeteo downy mildew model, German notes

A light read (the deep-research B list).

## What it holds

- A six-page German user guide to the VitiMeteo Peronospora forecast, issued by the Abteilung Weinbau, Institut viti-vinicole, April 2015 (l. 178).
- Infection strength is leaf-wetness degree-hours, and infection conditions are met at 50 (l. 18-20).
- Oospores become capable of germination at a temperature sum, normally 160 degree-days (l. 123-124).
- Incubation runs from 0% to 100%; contact sprays are advised at 80% of incubation time (l. 127, 172).
- Leaf area growth of 320-400 cm2 (2-3 new leaves) allows new infection on unprotected leaves (l. 65).

## Dependence

- verdict: shares a form (not computed); text: (1) Wet degree-hours as an infection gate (l. 18-20, 136): the same form as Rossi et al. 2008's wet degree-hour infection, but the guide's threshold is 50, not the 60 °C·h of Blaeser & Weltzien 1979 that the brief lists. (2) Temperature-sum oospore readiness (l. 123-124): the same kind of rule as the engine's VitiMeteo oospore rule (140 °C·days above 8 °C from 1 January), with 160 as the normal value and no base temperature or start date given; it may be the same rule under another setting. (3) Sporangia death and density (l. 109, 139) shares the process of Blaeser & Weltzien's sporangia survival; no equation is given. No authors are printed, so no shared-author flag.

## Bearing (2026-10-10)

- Gives a second VitiMeteo figure (160 degree-days oospore readiness, a 50 degree-hour infection gate) to set beside the brief's 140 °C·d rule, but it is a user guide with no formula, so it supplies numbers to compare, not a model to build from.
