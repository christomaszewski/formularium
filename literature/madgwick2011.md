---
id: madgwick2011
citation: Madgwick, J. W., West, J. S., White, R. P., Semenov, M. A., Townsend, J. A., Turner, J. A. & Fitt, B. D. L. 2011. Impacts of climate change on wheat anthesis and fusarium ear blight in the UK. European Journal of Plant Pathology (author manuscript EJPP1954R1; volume and pages not on the pages read)
doi: 10.1007/s10658-010-9739-1
read: 2026-10-27, lightly: abstract, the model-choice paragraph and the weather-generation and validation paragraphs only, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py; author manuscript with margin line numbers, so the file lines run through the margin numbers
status: read
diseases: [fusarium ear blight]
crops: [wheat]
regions: [United Kingdom]
processes: [weather generator, LARS-WG, climate change impact, crop growth model, rainfall-temperature disease model, validation on observed weather]
records: []
datasets: []
files: [syn1027_madgwick2011.pdf (the 2026-10-27 drop)]
---

# Madgwick et al. 2011: fusarium ear blight from rain and temperature around anthesis, run on LARS-WG daily weather at 14 UK sites

A temperature-and-rain model for fusarium ear blight, with anthesis dates from the Sirius wheat model, run on daily synthetic weather from the LARS-WG generator for baseline, 2020s and 2050s scenarios. No record: an impact study. A context paper.

**Read this first.** The model was built around what a daily generator provides: the authors chose rain and temperature because RH is "not easily included in projected weather" (l. 383-385). So this paper avoids the humidity problem and says nothing on humid hours. Author manuscript, not the journal's typeset version.

## What it holds

- **Why no RH** (l. 383-385): existing weather-based fusarium models (Moschini, De Wolf, Rossi and others) use relative humidity, "a parameter that is not always measured" by UK synoptic stations and "not easily included in projected weather".
- **Disease model** (l. 31, 664): incidence is related to rainfall in the week before anthesis and to mean temperature in the 4 weeks from 6 to 2 weeks before anthesis (logit scale); one relationship for all UK areas, because data were too few to form regional ones (l. 664-678).
- **Weather** (l. 722-752): daily minimum and maximum temperature, rainfall and solar radiation for 14 sites, made with LARS-WG (Semenov 2007), for a baseline (1960-1990 site parameters) and four scenarios (2020s and 2050s, high and low CO2, from UKCIP02), 50 simulated years each. No humidity variable.
- **Validation** (l. 680-698): the disease model was validated using observed weather and mean observed anthesis dates against regional incidence data, on data independent of model construction; missing weather was filled by collating nearby stations. The generated weather was not itself compared with observed-weather disease output.
- **Humidity statistics checked:** none; humidity is not used.

## Dependence

- LARS-WG (Semenov 2007, as cited; shared author Semenov with `semenov2010`, a flag), the Sirius wheat model, UKCIP02 scenarios, HGCA incidence data as named in the text.

## Bearing (2026-10-27)

- **D45:** no check on humid hours; it sidesteps humidity by choosing a rain-and-temperature model, which shows how common it is for generator-driven studies to avoid RH rather than test it.
- **D60:** a useful contrast: a disease rule that needs only what a daily generator makes can be run on synthetic weather, but a wetness rule that needs hourly RH cannot, which is the case Agrarium's engine is in. Gap filling by collating nearby stations (l. 689-690) is one simple filler for missing station data.
- **Not shown:** generator output against observed-weather disease output; any hourly variable.
