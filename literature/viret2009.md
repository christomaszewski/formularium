---
id: viret2009
citation: Viret, O., Gindro, K., Dubuis, P.-H., Bloesch, B. & Fabre, A.-L. 2009. Situation du mildiou en 2008 et prévision des risques [Downy mildew in 2008 and risk forecasting]. Revue suisse de Viticulture, Arboriculture et Horticulture 41(1):71-74
doi:
read: 2026-11-03, the 2008 season text and Table 1 (station table), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 20 of 20 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Switzerland, Changins (Vaud), Geneva, La Côte, Lavaux, Valais, Neuchâtel, Ticino]
processes: [oospore maturity, germination test, 140 C temperature sum, VitiMeteo, primary infection, incubation, first oil spots]
records: []
datasets: []
files: [dr1103_viret2009.pdf (the 2026-11-03 drop)]
---

# Viret et al. 2009: downy mildew in Switzerland in 2008, with a ten-station table of model oospore dates and first oil spots

A Swiss review article on the 2008 season, with a laboratory germination date for Changins in the text and, in Table 1, the model oospore date, VitiMeteo's primary infection and the observed first oil spots at ten stations.

**Read this first.**
- The "Germination oospores" column of Table 1 is the date the sum of temperature above 8 C passes 140 C (the table heading says so), so it is a model date, not a germination test. The only laboratory test date is in the text: 5 May at Changins (l. 140).
- The primary infection and end-of-incubation columns are VitiMeteo's calculation. Only the first-spot column is observed. Whether each station's spots were in an untreated plot is not stated in the facts read.
- Changins is in both this article and Table 12 of viret2014 (2008: model 11 May, first spot 26 May); the two agree.

## What it holds

- **Laboratory test, Changins (l. 140):** oospores mature (germination within 24 h at 100 % RH) from 5 May 2008; the temperature sum at the 8 C threshold was 140 C on 11 May, and the vine had unfolded its fourth leaf (l. 140).
- **Rule change (l. 356, raw text):** the sum from 1 January at the 8 C threshold was lowered from 160 C to 140 C in VitiMeteo-Plasmopara, which gives an extra safety margin for the date of primary infections.
- **Table 1, model date of the 140 C sum, then observed first oil spots, 2008:** Anières (Geneva) 10 May, 28 May (l. 109); Soral (Geneva) 9 May, 30 May (l. 110); Perroy (La Côte) 10 May, 29 May (l. 112); Changins 11 May, 26 May (l. 113); Pully (Lavaux) 7 May, 15 June (l. 115).
- **Table 1, continued:** Leytron (Valais) 5 May, 28 May (l. 117); Chalais (Valais) 7 May, 27 May (l. 118); Gorgier (Neuchâtel) 11 May, 30 May (l. 120); Praz (Neuchâtel, Vully) 12 May, 27 May (l. 121); Cugnasco (Ticino) 26 April, 27 May (l. 123).
- **Primary infection and incubation (VitiMeteo):** at Changins the primary infection was 16 May with 4.6 mm of rain and the incubation ended 25 May (l. 113). At nine of the ten stations the primary infection fell on 15 to 18 May; at Cugnasco it was 29 April with 10.4 mm, and the incubation ended 7 May (l. 123).
- **Spread of first spots:** eight of ten stations had first spots on 27 to 30 May, Changins on 26 May (l. 113); Pully was 15 June, three weeks after its end of incubation on 24 May (l. 115); Cugnasco had first spots 20 days after its end of incubation on 7 May (l. 123).
- **Infection days, May to August:** 28 (Gorgier, l. 120) to 61 (Cugnasco, l. 123) per station; Changins 44 (l. 113).

## Dependence

- **Own observations and VitiMeteo output** of Agroscope Changins and its partners (the model's calculation is the Table 1 oospore date, primary infection and end of incubation). The 5 May test is the Changins group's own laboratory test, which Dubuis et al. 2012 say serves to validate VitiMeteo; so the Changins values are not independent of the model.

## Bearing (2026-11-03)

- **literature/oospore_maturity_2026-11-03.csv (Agrarium D67):** adds one observed row, Changins 2008-05-05 (laboratory), which duplicates the viret2014 Table 12 value. The ten model dates in Table 1 are model rows, not observations; use them to compare model and Rossi output, not as maturity truth.
- **literature/real_outcomes_2026-11-03.csv:** adds ten first-oil-spot dates for 2008 at ten stations (Geneva, La Côte, Lavaux, Valais, Neuchâtel, Ticino). Changins 2008-05-26 duplicates Table 12. Kind of evidence: field observation by the network.
- **Use:** a one-year, multi-region test of how well the first spot follows the model's primary infection plus incubation; the spread (Pully, Cugnasco) shows the first-spot date is sometimes late.
