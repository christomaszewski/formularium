---
id: kennelly2006
citation: Kennelly, M. M., Gadoury, D. M., Seem, R. C., Wilcox, W. & Magarey, P. 2006. Recent investigations of the biology of Plasmopara viticola: considerations for forecasting and management of grapevine downy mildew. Proceedings of the Fifth International Workshop on Grapevine Downy and Powdery Mildew, San Michele all'Adige, Italy, 2006 (eds not printed; preface by C. Gessler and I. Pertot)
read: 2026-10-09, in full by a reading agent (claude-haiku-5-5); every quote checked at its line by verify_quotes.py, key numbers checked by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [New York, South Australia]
processes: [primary infection, host susceptibility, sporangia survival, oospores]
records: [kennelly2007.trigger, kennelly2005.bunch_window]
datasets: [kennelly2006.chancellor]
files: [PDMildew_Proceedings_ALL.pdf]
---

# Kennelly et al. 2006: the trigger's data, berry susceptibility and sporangia in daylight

## What it holds

- **Primary trigger:** rain > 2.5 mm, temperature > 11 °C and growth past E-L stage 12:
  'consistent across 15 years of historical data on the highly susceptible cultivar
  Chancellor at one site', and predicted the first outbreak in 2 of 3 years at three other
  sites.
- **Susceptibility:** shoots susceptible from E-L stage 5, so oospore germination, not the
  host, limits the onset; berry susceptibility fitted to New York data, y = 1.008 -
  0.379·log(x + 1) against degree-days (r² = 0.996; Fig. 1A), and superimposed on South
  Australian data.
- **Oospores:** germinate through the season, not only near bloom, and survived more than
  one season.
- **Sporangia:** one day at 42.8 °C sharply cut sporulation of existing lesions; most
  sporangia died in daylight, but more than 50 % still released zoospores after 12-24 h of
  overcast; sporangia on lesions declined as Y = 4.757 - 0.496X (ln + 1 transform; Fig. 5).
- **Genotypes:** most lesions unique; common genotypes appeared earliest.

## Dependence

- Its authors wrote the engine's trigger and bunch window; this paper is the trigger's own
  evidence.

## Bearing (2026-10-09)

- Names the data behind the engine's trigger (`kennelly2007.trigger`): recorded as
  `kennelly2006.chancellor`, inferred to be its calibration data. The berry curve is the
  data behind `kennelly2005.bunch_window`'s source (Gadoury's model; gadoury2006). Survival
  observations as in kennelly2007php.
