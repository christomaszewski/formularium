---
id: bleyer2008
citation: Bleyer, Gottfried, Kassemeyer, Hanns-Heinz, Krause, Ronald, Viret, Olivier & Siegfried, Werner. 2008. „VitiMeteo Plasmopara" – Prognosemodell zur Bekämpfung von Plasmopara viticola (Rebenperonospora) im Weinbau. Gesunde Pflanzen 60:91-100
doi: 10.1007/s10343-008-0187-1
read: 2026-10-08, in full by a reading agent (claude-sonnet-5-5); 60 quotes checked by scripts/verify_quotes.py, dependence by the main session. Earlier read on 2026-10-07 (Agrarium's read-primary.md)
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Baden-Württemberg, Switzerland]
processes: [primary infection, sporulation, survival, incubation, decision support]
records: [vitimeteo.oospores]
datasets: []
files: [s10343-008-0187-1.pdf]
---

# Bleyer et al. 2008: VitiMeteo Plasmopara (in German)

From the Freiburg wine institute (Bleyer, Kassemeyer), Geosens (Krause) and Agroscope
Changins and Wädenswil (Viret, Siegfried). VitiMeteo's oospore rule is an engine model
(`vitimeteo.oospores`); this is the model's description.

## What it holds

- Developed in 2002-2003 (l. 151) and run on about 100 stations for about 42,000 ha
  (l. 35). **No equations or parameter values are printed.**
- **Sources it names:** sporulation and infection from the earlier Freiburg model of Bleyer
  & Huber 1996 (l. 153-154); the spores' death rate "adjusted" to Kast 1999 (l. 156); soil
  infections and sporulation intensity newly added, with no source (l. 158-159); a second
  primary-infection algorithm programmed in winter 2005/06, basis not named (l. 219); the
  growth model from Schultz (l. 173). Müller & Sleumer 1934 is cited as the incubation-time
  method (l. 95), without saying VitiMeteo computes it.
- **No oospore maturation rule** and no degree-day threshold is printed; maturation is
  called too little studied (l. 382-390). In 2006, oospores were ready to germinate on
  10 and 15 May at an early and a late site (l. 232).
- **PeroRisiko:** degree-hours of leaf wetness, 50-100 weak, 100-200 medium, above 200
  strong (l. 326-334), after Keil 2007 and experience (l. 336); unit and base not printed.
  Keil 2007 itself (read 2026-10-09, [keil2007](keil2007.md)) says VitiMeteo's infection
  strength had been set "nach Erfahrungswerten" and that its results were to be
  integrated; it prints its leaf-disc data but no VitiMeteo classes.
- **Checks:** symptoms appeared at about 70% of the computed incubation on young leaves
  (incubation over 10 days) and about 90% on old leaves (under 7 days) (l. 281-284).
  Validation against BIOMAT and HP 100 devices, 2001-2005 (l. 221); plots inoculated on
  13 May 2004 (l. 275); incubation trials of 100 and 73 leaves in 2005 (l. 303, 315).
  Inoculation dates were the infection dates, so no model dated these data.

## Dependence

- One model with the engine's `vitimeteo.oospores` (D26), though this paper does not print
  that rule. VitiMeteo's survival was adjusted to Kast 1999's data, and its infection
  builds on Bleyer & Huber 1996; the engine runs neither piece.
- PeroRisiko is a wet-degree-hours index, the form of the engine's Rossi and Puelles
  infection steps.

## Bearing (2026-10-08)

- The engine's 140 °C·day oospore rule is still sourced only through Leoni et al. 2026's
  description of Siegfried et al. 2004 (not held); this paper does not confirm it.
- A truth built on VitiMeteo's other pieces would hold out the engine's oospore rule (one
  model). Kast 1999 and Hill 1989 are papers VitiMeteo drew on, not pieces the engine
  runs: flags, not kin (Agrarium's candidates.json).
