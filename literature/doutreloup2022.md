---
id: doutreloup2022
citation: Doutreloup, Sébastien, Bois, Benjamin, Pohl, Benjamin, Zito, Sébastien & Richard, Yves. 2022. Climatic comparison between Belgium, Champagne, Alsace, Jura and Bourgogne for wine production using the regional model MAR. OENO One 56(3):1-17
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 19 of 19 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Belgium, Champagne, Alsace, Jura, Bourgogne, Ardennes]
processes: [bud break, flowering, veraison, spray timing, season severity, frost damage, heat stress, leaf wetness]
records: []
datasets: []
files: [q363.pdf]
---

# Doutreloup et al. 2022: regional climate model MAR for Belgian wine

A light read (the deep-research B list).

## What it holds

- MAR (5 km) is checked against 27 Belgian SYNOP and 141 Météo-France stations, 2000-2020 (l. 167-179).
- Huglin index base 10 °C, 1 April to 30 September; K 1.02 at 40° and 1.06 at 50° (l. 257; equation on page 4).
- Bud break from the SUWE model: Smoothed-Utah chill, then Wang and Engel heat units (l. 281); maturity from the GSR model, base 0 °C from DOY 91 (l. 310).
- Spring frost: Tmin at or below 0 °C from March to June; intense heat: Tmax at or above 35 °C from June to September (l. 300-301).
- Frost-day accuracy 91% (Belgium) and 94% (France) (l. 455); Belgium's main risk is frost after bud break (l. 42).
- No Belgian reference observations suited to the wine region (l. 747).

## Dependence

- Borrows one constant from Ferguson et al. 2011 (the -25 °C winter tolerance, l. 345) without computing Ferguson's cold-hardiness model. Its bud-break model (SUWE: Smoothed-Utah chill, then Wang and Engel heat units, l. 281) is a chill-then-forcing form, which shares a form with the engine's BRIN chilling and forcing model; the equations differ and no data or calibration is shared, so this is a form flag, not a dependence. Computes none of the other engine models (Huglin, GSR and GFV are not on the list). Shared author Bois (cited ref. Bois et al. 2017 for disease rainfall) is a flag only.

## Bearing (2026-10-10)

- A source of 2000-2020 daily station data for Belgium and north-east France (observed, l. 167-179) and a frost and heat threshold set for the truth's climate; it borrows the Ferguson -25 °C value, so it is not a clean source for a cold-hardiness parameter.
