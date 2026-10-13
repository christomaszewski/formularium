---
id: martinezluscher2016
citation: Martínez-Lüscher, Johann, Kizildeniz, Tefide, Vučetić, Višnja, Dai, Zhanwu, Luedeling, Eike, van Leeuwen, Cornelis, Gomès, Eric, Pascual, Inmaculada, Irigoyen, Juan J., Morales, Fermín & Delrot, Serge. 2016. Sensitivity of grapevine phenology to water availability, temperature and CO2 concentration. Frontiers in Environmental Science 4:48
doi: 10.3389/fenvs.2016.00048
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py; the sensitivities (p. 5) read in the page image by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Croatia, Navarra]
processes: [phenology, budburst, flowering, harvest, chilling, sensitivity]
records: [martinezluscher2016.sensitivity]
datasets: [martinezluscher2016.croatia]
files: [martinezluscher2016_fenvs.pdf]
---

# Martínez-Lüscher et al. 2016: days per degree in Croatian records and in pots

Fifty-three years of Croatian stage dates read two ways, a partial least squares scan of
daily chill and heat for the windows that move budburst, and straight lines of each
interval's length on its mean temperature, beside a Pamplona greenhouse trial of
temperature, CO2 and water on Tempranillo cuttings.

## What it holds

- **Data** (`martinezluscher2016.croatia`): nine plantings at five stations, 42.75-46.03
  °N, 307 seasonal records 1961-2013 from PEP725 (l. 34, 173-186); E-OBS gridded
  temperature and rain, hourly values rebuilt with chillR after Linvill 1990 (l. 149-155).
- **PLS** (Fig. 1): Riesling Italico at Mandicevac, 41 datasets of 694 daily chill
  portions and degree hours (base 4, optimum 26 °C), VIP above 0.8 (l. 161-190):
  chilling 23 September to 27 February and heat from 22 January to 1 May advance
  budburst (l. 229-252); no flowering PLS. An interpolated surface gives 0.03 d/°C
  for the chilling phase and −4.38 d/°C for the warming phase (l. 278).
- **Field lines** (`martinezluscher2016.sensitivity`; Fig. 3, p. 5): 1 March to
  budburst −4.49 d/°C, budburst to flowering −3.29, flowering to harvest −2.57, slopes
  only; rain had no general effect on budburst and shortened the ripening period only
  with warmth (l. 292-297, p. 5).
- **Greenhouse** (Pamplona, 2014-2015): fruit development −1.52 and +0.15 d/°C (Red
  Tempranillo), −2.03 and −0.90 (White) (l. 294-296); elevated CO2 advanced ripening
  4.4 d at ambient and 3.5 d at +4 °C, 6.75 and 4.06 d over all (l. 324-330); water
  deficit lengthened ripening by about 3 d (l. 346-349). Daily means 22-27 °C, 8-50
  days above 35 °C (Table 1).

## Dependence

- **Borrows** the Dynamic Model and growing degree hours (Luedeling's chillR); fitted
  to observed Croatian dates on gridded weather. Luedeling and van Leeuwen are authors;
  no engine model.

## Bearing (2026-10-13)

- Sensitivities of the size Ruml and Fraga find (3-4.5 d/°C for budburst), with the
  greenhouse showing them collapse under heat: the warming phase, not chilling, moves
  budburst here too.
