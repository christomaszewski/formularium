---
id: rossi2002
citation: Rossi, V., Giosuè, S., Girometta, B. & Bugiani, R. 2002. Influenza delle condizioni meteorologiche sulle infezioni primarie di Plasmopara viticola in Emilia-Romagna. Atti Giornate Fitopatologiche 2002, 2:263-270
doi:
read: 2026-10-09, in full, in an OCR (tesseract, Italian) checked against the page images for the equations and Tables 1 and 3. A scan without a text layer, from the Giornate Fitopatologiche archive (found by a Codex search)
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Emilia-Romagna]
processes: [incubation, primary infection, oospores, forecasting]
records: [rossi2002.onset, rossi2008.primary, rossi2008.incubation]
datasets: [rossi2002.emilia, goidanich1957]
files: [rossi2002.pdf]
---

# Rossi et al. 2002: weather and the timing of primary infections in Emilia-Romagna

The paper Rossi 2008 credits for its incubation (eqs 8-9). Eight pages, in Italian.

## What it holds

- **Data:** the date of the first oil spots in unsprayed plots of 127 vineyards in
  Emilia-Romagna, 1993-2000: 80 on the plain, 47 in the hills (Fig. 1). Leaves were
  inspected every 5-7 days; the first oil spots, however few, set the date (p. 264).
- **Zones:** western (Piacenza, Parma, Reggio Emilia), central (Modena, Bologna) and
  eastern (Ravenna, Forlì, Rimini), each on the plain and in the hills. Only the plain is
  analysed, with weather from Piacenza, Bologna and Ravenna (p. 265).
- **Mean first-symptom dates (Tab. 1, p. 266, checked in the page image):**

  | Plain | 1993 | 1994 | 1995 | 1996 | 1997 | 1998 | 1999 | 2000 |
  |---|---|---|---|---|---|---|---|---|
  | western | 22 May | 25 May | 2 Jun | 21 May | 28 Jun | 8 Jun | 15 May | 14 May |
  | central | - | 25 May | 27 May | 15 May | 13 Jun | 9 Jun | 12 May | 19 May |
  | eastern | 11 May | 24 May | 8 May | 18 May | 10 Jun | 3 Jun | 13 May | 10 May |

  A vineyard's date was usually within 5-7 days of its zone's mean (p. 266).
- **The incubation (p. 265, Fig. 2):** "La durata dell'incubazione è stata calcolata in
  funzione della temperatura dell'aria, mediante due equazioni di regressione adattate ai
  dati di Goidanich et al. (1957), relativamente ai periodi che i suddetti Autori hanno
  definito con umidità alta e bassa."
  - Days to oil spots: ŷ = 45.1 − 3.45·T + 0.073·T² at high humidity, and ŷ = 59.9 −
    4.55·T + 0.095·T² at low, T the daily mean air temperature. The figure spans 10-30 °C.
  - Humidity cannot be set objectively, so the two curves bound a window: the probable
    infection period (PPI). Daily progress is the reciprocal of the duration; incubation
    ends when the sum reaches 1.
  - These are Rossi 2008's eqs 8-9, coefficient for coefficient.
- **The PPI (p. 266):** early May to 20-25 June, 5-9 days before the mean oil-spot date,
  lasting 3-5 days on average.
  - Temperatures in it were 16-23 °C, except in 1995 (9.5 °C in the western zone).
  - There was always at least one rain event, often over 10 mm. Some PPIs had as little
    as 0.2 mm; the authors kept them, citing at least 4 h of leaf wetness above 20 °C as
    enough to infect (Lalancette et al. 1988).
- **Correlations with the PPI's pentad (Tab. 2, p. 267, read in the page image),
  September to May:**
  - Mean temperature: April −0.43, May −0.47 (P ≤ 0.05).
  - Rain days: March −0.72, February-April −0.69; March's longest wet spell −0.64
    (P ≤ 0.01).
  - Longest dry spell: February +0.47, April +0.53, May +0.41, February-April +0.52.
  - Rain amount: significant in no month. Nothing from September to January was.
- **Formulation (eq. 1, Tab. 3, p. 268):** PPI (pentads from 1 January) = 28.34 − 0.77 ×
  March rain days + 0.33 × April's longest dry spell (days).
  - R² 0.77, adjusted 0.75, standard error 1.37 pentads. March rain days explain 67 % of
    the variance and April's dry spell 33 %. The largest error was 2.3 pentads.
  - About 4 days earlier for each rain day in March, and 1.5 days later for each dry day in
    April. Year and zone dummies added nothing.
  - The authors: it "interpreta le relazioni esistenti fra i dati che lo hanno generato"
    (p. 269) and must be checked in new years and places (p. 270).

## Dependence

- **Settles a trail.** Rossi 2008's incubation regressions were fitted to Goidanich et
  al. 1957's data, as the authors state here. Formularium had inferred it from Rossi et
  al. 2005 and Sanna 2017. `rossi2008.primary`'s calibration to `goidanich1957` is now
  read, not inferred.
- **The onset regression** (`rossi2002.onset`) was fitted to PPIs counted back with those
  same regressions: `calibrated_with` `rossi2008.incubation`.
- Goidanich's reference here reads "Lotta antiperonosporica e calendario d'incubazione",
  Giornale di Agricoltura, 13 January 1957, 11-14. Rossi et al. 2005 titles it otherwise.
- Shares authors with Rossi 2008 (Rossi, Giosuè, Bugiani): a flag only.
- Leoni et al. 2026 cite this paper for oospore maturation stopping "when total rainfall
  remained below 5 mm over three weeks". It prints no such rule (checked in the OCR and
  page images): a misattribution.

## Bearing (2026-10-09)

- For Agrarium: confirms that a truth using Rossi 2008's incubation must hold out
  `goidanich.incubation` (its F1 already does).
- Tab. 1 is a first-symptom pattern for Emilia-Romagna's plain over eight years, usable
  in the truth's history matching.
- The 0.2 mm rain cases are field evidence that primary infection needs no 10 mm of rain.
- For Cooptera: the source of its engine's incubation.
