---
id: viret2005
citation: Viret, Olivier, Bloesch, Bernard, Fabre, Anne-Lise, Siegfried, Werner, Bleyer, Gottfried, Huber, Bernhard, Kassemeyer, Hans-Heinz & Steinmetz, Volken. 2005. Vitimeteo: un nouveau modèle de prévision pour le mildiou de la vigne (www.agrometeo.ch). Revue suisse de viticulture, arboriculture, horticulture 37(1):65-68 (the copy is the 'Le Guide Viti' reprint, with pages 66 and 68 printed)
doi:
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 58 of 58 quotes found at their lines by scripts/verify_quotes.py; the reference list and Fig. 1 checked by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Switzerland, Changins, Suisse romande, Baden-Württemberg]
processes: [primary infection, sporulation, incubation, sporangia survival, leaf wetness, forecasting, leaf growth]
records: []
datasets: []
files: [viret2005_vitimeteo.pdf]
---

# Viret et al. 2005: VitiMeteo-Plasmopara presented to Swiss growers

Open access since 2026-10-12 (Agroscope's repository). The first French description of
VitiMeteo-Plasmopara, written for growers: it names the model's inputs and the knowledge
it builds on, and prints no equation, coefficient or threshold.

## What it holds

- **The model:** developed in 2002-2003 and programmed by the firm Geosens (R. Krause,
  Ebringen; l. 8-10, 202); validated in 2004 "avec des données historiques et actuelles",
  no data, years or statistic named (l. 12); tested in practice in Germany and
  Switzerland (l. 14). It is called an expert system whose every step can be checked and
  whose elements can be set per region (l. 138-141).
- **What it computes,** in words only: daily infection periods, sporulation conditions and
  the progress of incubation for a chosen interval (l. 146-148); sporangia survival and an
  infection intensity (l. 142-146); a primary-infection trigger from a temperature sum
  (Gehmann 1987), vine phenology, rainfall intensity (Viret & Bloesch 2002), leaf wetness
  duration and temperature (l. 133-137). The thresholds are "algorithms" (l. 15) and are
  not printed. The time step is a day: weather is recorded each day (l. 147).
- **Sporangia survival:** earlier models were assumed to underestimate it; VitiMeteo takes
  the longer survival found by Hill 1989 and Kast & Stark-Urnau 1999 (l. 143-146,
  181-182), which is why it indicates slightly more infections than Lufft's Smartgraph
  (l. 178-179).
- **Comparison with Smartgraph** (Lufft) on Suisse romande weather from sites with
  untreated plots followed in detail (l. 161-165): the two systems' infection periods
  agree on 1999-2003 retroactive data and on 2004 (l. 168-169).
- **Changins 2004** (Fig. 1, a VitiMeteo report, l. 24-85): oospore germination date
  03.05.2004 and budburst 30.04.2004 are printed on the report, so they are model output
  unless the paper says otherwise (l. 26-27, 77-78). A primary infection was reported on
  1 June 2004 over almost all of French-speaking Switzerland (l. 170-171); the first oil
  spots at Changins appeared on 11 June 2004 on untreated vines (observed, l. 173), and
  VitiMeteo's sporulation dates for them are 11 and 12 June (model, l. 175-176). Mildew
  stayed low until August 2004 (l. 177).
- **Leaf growth:** the report's leaf numbers and leaf area come from the Geisenheim model of
  Schultz 1992, made for Riesling, validated in 1999 in southern Germany on
  Müller-Thurgau and Pinot noir against leaf-area measurements, correlation not
  quantified (l. 130-131, 172-179); only main leaves are simulated (l. 179).
- **The network:** about 100 Swiss stations (Campbell, Lufft HP-100, Opus II) feed the
  Agrometeo database (HES Valais, Sion), with outliers and gaps replaced from a substitute
  station (l. 140-150, 156).
- **Garbled:** Fig. 1's table columns are interleaved in the text layer and its footnotes
  (units of "Degrés-heures") are missing, so no table value is taken from it.

## Dependence

- **Computes, by its own account:** a temperature sum credited to Gehmann 1987 (the
  dissertation; l. 134, 201-203), a rainfall-intensity term credited to Viret & Bloesch
  2002 (l. 136, 220-225), and Schultz 1992's leaf-appearance model (l. 130-131, 216-219).
  None of the three is printed here.
- **Takes its sporangia survival from** Hill 1989 (Vitic. Enol. Sci. 44:86-90) and Kast &
  Stark-Urnau 1999 (Vitis 38(4):185-186; held since 2026-10-12, see its note when written).
- **Cites for history:** Bläser 1978 (the Bonn dissertation, `blaeser1978diss`), Bleyer &
  Huber 1996 (the Freiburg forecast model), Hill 1997 and 2003 on primary infection, and
  Viret et al. 2001 (Revue suisse 33(2):I-XII), the warning-station paper before
  VitiMeteo. Bläser & Weltzien 1979 is in the reference list only (l. 196).
- **Authors:** Bleyer, Kassemeyer and Viret are authors of the VitiMeteo papers
  `bleyer2008`, `bleyer2010`, `bleyer2020`, `bleyer2022` and `dubuis2012`: a flag, not a
  dependence (D27).

## Bearing (2026-10-12)

- It does not print the oospore rule (140 or 160 °C·day above 8 °C), the 50 °C·h infection
  gate, Müller's incubation or the sporulation rule that other notes credit to VitiMeteo,
  so the catalogue's `vitimeteo.oospores` stays sourced through Leoni et al. 2026 and
  Siegfried et al. 2004 (still not held). Dubuis et al. 2012 (`dubuis2012`) is the paper to
  check for the rules.
- Its one dated observation, first oil spots at Changins on 11 June 2004 after a primary
  infection reported on 1 June, is a point a truth could be checked against; the dates on
  the Fig. 1 report are the model's.
