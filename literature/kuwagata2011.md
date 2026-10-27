---
id: kuwagata2011
citation: Kuwagata, T., Yoshimoto, M., Ishigooka, Y., Hasegawa, T., Utsumi, M., Nishimori, M., Masaki, Y. & Saito, O. 2011. MeteoCrop DB: an agro-meteorological database coupled with crop models for studying climate change impacts on rice in Japan. Journal of Agricultural Meteorology 67(4):297-306
doi: 
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: [rice]
regions: [Japan]
processes: [daily weather database, solar radiation estimate, downward longwave estimate, paddy water temperature, panicle temperature, rice phenology]
records: []
datasets: []
files: [kuwagata2011.pdf (the 2026-10-25 other-sources drop)]
---

# Kuwagata et al. 2011: MeteoCrop DB, a Japanese weather database for rice models

A research note on MeteoCrop DB, a daily weather database for Japan with estimated agro-meteorological variables, coupled to rice phenology and paddy temperature models, with no accuracy figures printed.

## What it holds

- **Coverage:** daily data at about 850 AMeDAS stations (1980 to 2011) and about 160
  surface meteorological observatories (1961 to 2011) (l. 17-19).
- **Estimated variables:** solar radiation and downward longwave radiation are estimated
  from sunshine duration and dew point by the empirical formulas of Kondo et al. (1991b), with
  a turbidity coefficient of 0.1 and albedo of 0.2 (l. 224-238). The text prints no equation
  for either, and no error statistic for the estimates.
- **Coupled models:** Nakagawa & Horie (1995) phenology for Koshihikari (l. 235-236); paddy
  water temperature and panicle temperature models (l. 247-262). The checks are in figures
  only (l. 336-342).
- **Access:** free to use on the website, which was then Japanese only (l. 258-259, 448-449).

## Dependence

- **Builds on** the Kondo et al. (1991b) solar and longwave formulas (l. 224-238), the Nakagawa
  & Horie (1995) phenology model (l. 236), and JMA AMeDAS and observatory data (l. 113-116).
- The longwave method is named, not written out, so it cannot be checked from this paper.

## Bearing (2026-10-26)

- classes.tsv names no search for this key. Its reason is that the longwave formula that
  kuwagata2024 credits to it is not printed here: this paper names the formula and does not print it.
- A vineyard simulator with sunshine and humidity but no radiometer could take the method in
  outline, but the constants and the Kondo formula would need the original. The paper was not
  read in full.
