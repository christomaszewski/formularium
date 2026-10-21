---
id: deresseguier2020
citation: de Rességuier, L., Mary, S., Le Roux, R., Petitjean, T., Quénol, H. & van Leeuwen, C. 2020. Temperature Variability at Local Scale in the Bordeaux Area. Relations With Environmental Factors and Impact on Vine Phenology. Frontiers in Plant Science 11:515 (article number; no page range printed; published 2020-05-20)
doi: 10.3389/fpls.2020.00515
read: 2026-10-21, lightly: abstract, Sections 2 (study area, sensors, data treatment, GFV model) and 3 (variability, canopy Winkler index, environmental factors, validation), discussion; figures and tables by caption and adjacent text only; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Bordeaux, Saint-Émilion and Pomerol]
processes: [temperature variability, canopy temperature, sensor network density, topography, phenology, station versus canopy logger, vineyard variability]
records: []
datasets: []
files: [ressguier2020.pdf (the 2026-10-21 drop)]
---

# de Rességuier et al. 2020: air temperature inside the vine canopy varies by several degrees across one Bordeaux area

A 90-logger canopy network over 19,233 ha of Saint-Émilion, Pomerol and satellite appellations, 2012-2018, with the spread of daily minimum and maximum temperature, its link to elevation and slope, and a phenology check. No record.

## What it holds

- **Network** (l. 27, 144-146, 163, 190): 90 loggers in solar radiation shields (RS3) at 1.2 m in the vine canopy, over 19,233 ha of which 12,200 ha is vineyard, one sensor per 214 ha. Altitude 2-107 m, slopes up to 45 %, various exposures. Two logger types over the years (Tinytag 2012-2015, LoRa 2016-2018).
- **Daily spread** (l. 295-297): the spatial amplitude across the network averages 3.9 degC +/- 1.7 for daily minimum (Tn), 3.2 degC +/- 0.9 for daily maximum (Tx), and reaches 9.8 degC for Tn on specific days.
- **Weather type decides the spread** (l. 321, 328-330, 335, 337, 354): on 2012-03-13 (clear, calm) the Tn amplitude was 9.2 degC, and elevation explained 51.7 % of the variance (59 % in all, SVR map model). On 2012-04-07 (cloudy, no wind) the amplitude fell to 1.1 degC, elevation explained 66 % (negative sign) and the multiple regression 76 %.
- **Season means** (l. 356-358, 391-392): the range from coldest to warmest sensor in a season mean is 2.6 degC +/- 0.3 (Tn) and 2.1 degC +/- 0.3 (Tx). The canopy Winkler index spreads by 320 degree-days +/- 41.7 within a vintage; the vintage means are 2041 +/- 72.6 (2018, warmest) and 1735 +/- 55.4 (2013, coolest).
- **Drivers** (l. 458-460): in linear mixed models Tn rose with elevation and slope and fell from west to east and from south to north (Table 1 coefficients were not read). Tx fell with elevation. Spatial variability is driven more by minimum temperature, year-to-year variability by maximum (l. 618).
- **One station against a canopy logger** (l. 207, 506, 508, 513): a Tinytag logger was placed 4 m from the Météo-France Saint-Émilion station at the end of 2015. Station minus logger is -0.2 degC +/- 0.3 for Tn and 1.2 degC +/- 0.7 for Tx, with a seasonal effect. A linear correction was applied so that the published GFV parameters could be used.
- **Phenology check** (l. 267, 580, 584, 613): the GFV model on corrected logger temperatures gives an RMSE of 2.2 d (flowering) and 3.6 d (véraison) from maps, against 5.6 d and 6.6 d published for Merlot (cited). Logger-based, not mapped, it is 2.3 d +/- 0.7 and 3.5 d +/- 1.5. Phenology was observed on 60 reference blocks, only 17 of them in 2012.

## Dependence

- Phenology is computed with the GFV model of Parker et al. (2011, 2013), as cited (see `parker2011`, `parker2013`); the daily maps use the support vector regression of Le Roux et al. (2017a) and the canopy Winkler index adapts Winkler (1974) (de Rességuier et al. 2018). Weather inputs are the authors' own loggers plus one Météo-France station. A shared author is only a flag.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): vineyard variability, and what one station misses.

- **Takeable:** a measured size of the within-area spread in a wine region, in canopy air temperature: a night-time (Tn) spread of 3.9 degC on average and up to 9.8 degC on clear calm nights, against 1.1 degC on a cloudy night. The spread depends on the weather type, so a placement scored on a mean will hide the nights that matter. Elevation alone explained 51.7 % and 66 % of the variance on the two example days.
- **Takeable:** the station-minus-canopy difference (Tn -0.2 degC, Tx 1.2 degC) is a worked size of the bias between a reference station and a canopy logger 4 m away, and a worked linear correction.
- **Not shown:** any placement method, any held-out loggers, any random baseline, any spatial covariance (no variogram in the text read). It is one region, one co-located pair, temperature only: nothing on leaf wetness or humidity. The kind of result is a descriptive network survey.
