---
id: gleason2008
citation: Gleason, Mark L., Duttweiler, Katrina B., Batzer, Jean C., Taylor, S. Elwynn, Sentelhas, Paulo Cesar, Monteiro, José Eduardo Boffino Almeida & Gillespie, Terry J. 2008. Obtaining weather data for input to crop disease-warning systems: leaf wetness duration as a case study. Scientia Agricola 65(special issue):76-87
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 11 of 11 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [sooty blotch, flyspeck]
crops: [grapevine, maize, apple, cotton, coffee, soybean, tomato, muskmelon]
regions: [Iowa, Wisconsin, São Paulo State, Ontario, Costa Rica, New York State]
processes: [leaf wetness, spray timing, season severity, infection]
records: [sentelhas2008.wetness]
datasets: []
files: [gleason2008.pdf]
---

# Gleason et al. 2008: weather data and leaf wetness in warning systems

A light read (the deep-research B list).

## What it holds

- Review of how weather data reach disease-warning systems, with leaf wetness duration (LWD) as the case study, 12 pages (abstract).
- LWD is the period of free water on the leaf from dew, rain or fog (l. 307-309); it is the most spatially variable input (l. 364).
- Grape hedgerow LWD did not differ between the top and the inside of the canopy in São Paulo (l. 415).
- Sentelhas et al. (2007b) used RH above 90% as a surrogate for LWD; a regional RH threshold made it as accurate as physical models (l. 587-592).
- Grape canopy-top LWD sensor data for Jundiaí, 2003/04 (l. 631, cited to Sentelhas 2006).

## Dependence

- Describes the engine's sentelhas2008.wetness: Gleason's Sentelhas et al. (2007b) is the same paper (Agricultural and Forest Meteorology 148: 580-591, doi 10.1016/j.agrformet.2007.09.011, as printed in the reference list at l. 765-768; the engine's record gives the same doi and year 2008). The RH>90% surrogate and the regional RH-threshold adjustment (l. 587-592; l. 665-666) are the engine's RH-threshold form. Gleason computes no new model here; he reports the paper's result. Shared author: Gleason is an author of the engine's record (a flag only, D27). The 'Magarey et al. 2005' cited at l. 401 and 569 is an Agronomy Monograph chapter on surface wetness, not checked against the engine's Magarey 2005 infection record.

## Bearing (2026-10-10)

- For the truth it is a secondary source on the RH>90% wetness surrogate that the engine's sentelhas2008.wetness record uses (with dew-point depression), and it confirms that the RH form is a model the truth must not share with the engine; it gives no parameter values usable by the truth.
