---
id: zipse2010
citation: Zipse, Wilfried. n.d. (2010 by the PDF creation date; approximate, not printed). Anleitung zum Peronospora-Prognosemodell Vitimeteo [Instructions for the Vitimeteo Peronospora forecast model]. DLR Mosel
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 19 of 19 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Mosel, Bernkastel-Kues, Germany, Baden (WBI Freiburg)]
processes: [infection, incubation, sporulation, sporangia density, leaf wetness, degree-hours, germination duration, soil infection, secondary infection, leaf-area spray rule, forecast]
records: []
datasets: []
files: [zipse2010_vitimeteo_anleitung.pdf]
---

# Zipse n.d.: instructions for the Vitimeteo Peronospora forecast model

A light read (the deep-research B list).

## What it holds

- Instructions for the VitiMeteo Plasmopara model, DLR Mosel after Gottfried Bleyer (WBI Freiburg) (l. 1-2).
- Sporangia density is a temperature-driven new-sporangium potential, 0 to 300 per cm2 x 1000; it is not a sporangia count (l. 18-20, 135-136).
- Infection risk is classed by degree-hours; a degree-hour sum of leaf wetness above 50 means infection risk (l. 23, 129-131).
- Heavy rain can start soil infections when germination duration is under 3 days (l. 117-119).
- Spray at 80 % incubation progress; worked example: 100 % incubation 8 days after a 13 June infection (l. 29-32).
- A leaf-area growth of 320-400 cm2 per main shoot since the last spray allows infection on unprotected leaf (l. 39).
- The manual shows a germination-readiness date but no oospore rule (l. 85).

## Dependence

- model: Blaeser & Weltzien 1979 wetness rule (summary: at least 50 degree-C hours of wetness); kind: shares a form and the threshold number; quote: Werten über 50 Infektionsgefahr herrscht; line: 131; detail: The manual's threshold of 50 degree-hours of leaf wetness for infection risk has the form of the Blaeser & Weltzien wet degree-hour rule, and the same number as its summary rule (per Formularium note blaeser1979.md). The manual cites no source. The 60 C·h figure is the slope in Blaeser & Weltzien, not in this manual. model: VitiMeteo oospore rule (engine model vitimeteo.oospores, per Formularium note bleyer2008.md); kind: describes the model; no rule printed; quote: das Datum der Keim-; line: 85; detail: The manual shows a germination-readiness date (Keimbereitschaft) in the event bar and in the example plot (Bernkastel-Kues), but prints no maturation or germination rule, no degree-day sum and no 1 January start. So it does not state the 140 degree-C-day rule. Relevant only as a description of the same model family. model: Sporangia density algorithm (shared author flag: Hill); kind: shared author flag only; quote: Der Algorithmus zur Berechnung der Sporangiendichte wurde modifiziert nach Dr. G.; line: 139; detail: The density algorithm is 'modified after Dr. G. Hill, DLR Oppenheim' (no equation printed). Hill is a shared-author flag, not a dependence on a listed model; the manual's sporangia density is a temperature-driven potential, not a count (l. 135-136). model: Bleyer (VitiMeteo author); kind: shared author flag only; quote: nach Gottfried Bleyer, WBI Freiburg; line: 2; detail: The instructions are 'after Gottfried Bleyer'. Flag only (D27).

## Bearing (2026-10-10)

- Offers the truth a description of the VitiMeteo incubation and sporangia-density outputs, but no printed oospore rule; the 50 degree-hour wetness threshold shares the Blaeser & Weltzien form and number, so it counts as a dependence for any truth built on it.
