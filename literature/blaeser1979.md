---
id: blaeser1979
citation: Blaeser, Marlene & Weltzien, H. C. 1979. Epidemiologische Studien an Plasmopara viticola zur Verbesserung der Spritzterminbestimmung (Epidemiological studies to improve the control of grapevine downy mildew). Zeitschrift für Pflanzenkrankheiten und Pflanzenschutz 86(8):489-498
read: 2026-10-09, in full by the main session, from the page images (the text layer cuts lines off); equations read at 300-400 dpi
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Ahr, Germany]
processes: [infection, sporangia survival, sporulation, spray timing]
records: [blaeser1979.survival, orlandini1993.infection, brischetto2020.survival]
datasets: [blaeser1979, blaeser1978.survival]
files: [Blaeser-EpidemiologischeStudienPlasmopara-1979.pdf]
---

# Blaeser & Weltzien 1979: the wet degree-hour rule and the survival curves

A 10-page paper from the Institut für Pflanzenkrankheiten, Bonn, in German with an English
summary. The source of two equations the engine runs through Rossi et al. 2008 and
Brischetto et al. 2020.

## What it holds

- **Material:** sporangia from potted Müller-Thurgau, processed fresh; methods in Blaeser &
  Weltzien 1977 and 1978 (p. 490).
- **Infection (Tab. 1, p. 491):** the least leaf wetness that infected at least half the
  inoculated leaves, at constant 6-25 °C: 9.0 h at 6 °C, 5.5 h at 10 °C, 3.5 h at 15 °C,
  2.0 h at 20 °C, 2.0 h at 25 °C. The products T × h run from 40.0 (20 °C) to 59.5 (7 °C)
  °C·h, mean 49.7, s² = 23.55. So "x · y = 49,7"; and regressing hours on x' = 1/T gives
  y = -0.67 + 60.0 x' (r = 0.993; Abb. 1, p. 492). The summary: at least 50 °C·h. The
  "60 °C·h" others cite is this slope.
- **Survival (Abb. 2-3, pp. 492-493):** maximum lifetime of sporangia on the leaf (I) and
  detached (II), by temperature and RH (Abb. 2, a 3-D chart), refitted against the
  saturation deficit "S_d = E (1 - F/100) (Steubing 1965)" in mm, F the RH:
  - y_I = 9.27 - 1.12x + 0.04x² (attached, days);
  - y_II = 5.67 - 0.47x + 0.01x² (detached, days).
  - Values at 100 % RH (lifetime set by temperature alone) and all of 30 °C ("die relative
    Luftfeuchtigkeit keine Rolle spielt") were left out; a 2nd-degree polynomial was fitted.
    The points on Abb. 3's axis stop near 17 mm.
  - E is not defined in the text; as Steubing's saturation deficit it is the saturation
    vapour pressure in mm Hg (inferred).
- **Summary rules (p. 489):** infection needs at least 50 °C·h of wetness; sporulation needs
  darkness, at least 13 °C and 98 % RH in the canopy; sporangia live at most 6 h above
  30 °C; they spread only by wind-blown rain.
- **Field (pp. 490, 493-497):** temperature-wetness recorder (Weltzien & Studt) in the
  canopy at Walporzheim ("Walporzheimer Himmelchen", Ahr), 1975-1977, and in a Portugieser
  vineyard at Bachem ("Bachemer Steinkaul") in 1978, where sprays were timed by the method:
  four sprays, one only against powdery mildew, no downy mildew. Calendars (Abb. 4-7) mark
  degree-hour sums for rain and dew wetness, sporulation nights (at least 13 °C between 22
  and 4 h and 98 % RH), and days with more than 6 h above 30 °C. In 1976 three of six sprays
  could have been saved. Infection appeared in untreated, favourable sites only in 1977 and
  1978, both late.
- **Discussion:** the wet-period temperature sum is constant, as for Venturia inaequalis
  (Mills & Laplante's curve, after Studt 1975); they reject a developmental zero, since the
  "zero" is when wetness and inoculum meet.

## Dependence

- Their own laboratory and field data; no model computed.
- The survival curves' data are the 1978 paper's tests (`blaeser1978.survival`): the 1979
  paper cites them and shows the same grid of conditions (inferred).
- **Who computes it:** Rossi et al. 2008 (eq. 6, detached curve, 0.01) and Brischetto et
  al. 2020 (eqs 1-2; eq. 2 prints 0.02) both use x = T·(1 - RH/100), not E·(1 - RH/100);
  PLASMO fits n/T to Tab. 1 (literature/orlandini1993); Brischetto et al. 2021's Magarey
  parameters were estimated partly from these data.

## Bearing (2026-10-09)

- Settles Agrarium's question for D30: c2 is 0.01 for detached sporangia; Brischetto's 0.02
  is a transcription error. The index both tools' sources compute is not the paper's.
- The curves are unsupported beyond about 17 mm and above 25 °C, and U-shaped: they cannot
  test Kennelly et al. 2007's hot, dry day (36.5 °C, 15 % RH; x about 39 mm) except by
  extrapolation. The paper's own heat rule is at most 6 h above 30 °C.
- Formularium: `blaeser1979.survival` gains its calibration data, published values and
  flags; Cooptera's list keeps its trail citation until Cooptera relists it (told
  2026-10-09).
