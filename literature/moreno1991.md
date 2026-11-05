---
id: moreno1991
citation: Moreno García, M. del C. 1991. Notas acerca de la precipitación diaria en cuatro capitales catalanas [Notes on daily precipitation in four Catalan capitals]. Universitat de Barcelona, pp. 77-87 (also numbered (563)-(573) in the offprint); the journal is not printed in the extracted text
doi:
read: 2026-11-04, in full (11 pages of text, Cuadros 1 to 4), with Cuadros 3 and 4 read in the page image by the main session (p. 570), by a reading agent and a note writer; 22 of 22 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Spain, Catalonia, Barcelona, Tarragona, Girona, Lleida]
processes: [daily rain, wet day, Markov chain, rain persistence, wet-day probability, summer dip]
records: []
datasets: []
files: [dr1104_moreno1991.pdf (the 2026-11-04 drop)]
---

# Moreno García 1991: two-state Markov chain of daily rain, by month, at four Catalan capitals

A Spanish note that counts dry-to-wet and wet-to-wet day transitions by month at the first-order observatories of Barcelona, Tarragona, Girona and Lleida, 1970-85.

**Read this first.**
- The journal is not printed in the extracted text. The page numbers are 77-87 with (563-573) in parentheses; treat the venue as not printed.
- The text's "si el día precedente fue seco" (l. 176) is a slip for a wet preceding day: the same sentence gives 0.4406 as the annual P11 for Girona, and Cuadro 4 agrees. The next sentence (l. 177) gives 18.12 % for a wet day after a dry day.
- OCR garbles the notation: "Pu" is P11 (l. 173), P01 is read as "poo" or "pO!", and Lleida is spelled "L1eida" in the Cuadro 4 header. The P11 and pi1 columns of Cuadro 4 are only partly separated in the text; the order follows the caption and the text.
- Urban observatories; Lleida's wet-day share is probably inflated by winter-fog days with a few tenths of a millimetre (l. 165, from the text). Girona covers 1970-77 only (l. 32).

## What it holds

- **Data (l. 30-32):** daily rain at the first-order observatories of Barcelona, Tarragona, Girona and Lleida (INM, urban areas), 1970-85, except Girona 1970-77.
- **Method (l. 112-113):** two-state Markov chain; transitions dry-to-dry, dry-to-wet, wet-to-dry and wet-to-wet are counted by month for each city. A dry day is one with no or "inapreciable" rain. The threshold is not printed as a number; Cuadro 1 classes start at 0.1-0.9 mm (l. 244) and Barcelona has 353 days in that class (l. 165), so a wet day is probably 0.1 mm or more (inferred).
- **Wet days persist (l. 173):** the chance of rain is higher after a wet day than after a dry one. No capital exceeds 0.25 annual wet-day probability (l. 168).
- **Girona annual (l. 175-176):** wet-day probability 0.2446; P11 0.4406 (see the slip above).
- **Barcelona, annual (Cuadro 4, l. 366):** P11 0.3985 and wet-day share pi1 0.1999 (19.99 %, l. 159).
- **Barcelona by month (Cuadro 4, P11 then pi1):** January 0.4812 and 0.2164 (l. 354); May pi1 0.2601, the wettest month (l. 358); July 0.1633 and 0.0926 (l. 360); August 0.2717 and 0.1679 (l. 361); November P11 0.5000, the annual maximum, and pi1 0.2058 (l. 364).
- **Tarragona annual (Cuadro 3, l. 341):** p00 0.8721, p01 0.1279, p10 0.6170, p11 0.3830, pi0 0.8282, pi1 0.1717. Tarragona July p01 is 0.0669 (Cuadro 3, read in the page image by the main session, p. 570; no line).
- **Seasonal pattern (l. 218):** the highest monthly P11 reach or exceed 0.5 in Lleida, Girona and Barcelona; the lowest are in July and August. July is the driest month in all four capitals.
- **Intensity (l. 209):** the wettest 10 % of rain days give 50 % of the total rain at Lleida, 48 % at Girona and Tarragona, and 46 % at Barcelona (Barcelona 46 % from l. 209-210 of the text).

## Dependence

- Own counts from INM first-order observatory daily rainfall, 1970-85. No model is borrowed. The reading agent lists Lana & Burgueño 1998 (Int. J. Climatol. 18:793-815) as a lead for the same chain at 78 stations.

## Bearing (2026-11-04)

- **Weather generator (weather.p_wet_after_dry, weather.p_wet_after_wet, weather.rain_summer_dip; Agrarium):** a measurement of the Markov transition probabilities by month at Barcelona, Tarragona, Girona and Lleida, 1970-85, with a wet day as appreciable rain (probably 0.1 mm or more). Barcelona annual P11 is 0.3985 and the wet share 0.1999; Tarragona annual p01 is 0.1279, p11 0.3830 and July p01 0.0669. Kind of evidence: station counts from a 16-year series (8 years for Girona).
- **Summer dip:** July and August have the lowest P11 and wet share (Barcelona July P11 0.1633, pi1 0.0926), so a dry summer is in the data. Barcelona p01 by month is not printed in the text read here.
- **Limits:** urban sites, a short period, one wet-day threshold; Lleida is inflated by fog days. Not a vineyard station (Penedès is not among the four).
