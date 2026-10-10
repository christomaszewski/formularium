---
id: maddalena2023
citation: Maddalena, Giuliana, Marone Fassolo, Elena, Bianco, Piero Attilio & Toffolatti, Silvia Laura. 2023. Disease forecasting for the rational management of grapevine mildews in the Chianti bio-district (Tuscany). Plants 12:285
doi: 10.3390/plants12020285
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 60 quotes checked by scripts/verify_quotes.py; the incubation sentence and its reference checked by the main session
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Tuscany]
processes: [forecasting, validation, spray timing, primary infection]
records: [epi1983.corrected]
datasets: [maddalena2023.panzano, goidanich1957]
files: [maddalena2023-chianti-forecast.pdf]
---

# Maddalena et al. 2023: EPI in nine organic Chianti vineyards

The same paper was found twice in the deep-research drop (med2 and oa-cites p09).

## What it holds

- **Sites:** nine organic vineyards at Panzano in Chianti, 2020 and 2021. Each had an
  untreated plot, an EPI-timed plot and a grower-timed plot.
- **Model:** EPI (Strizyk), run twice a week in IFV's Epicure; its formulas, thresholds and
  version are not printed. Weather came from sensors and interpolated grids, with real and
  forecast hourly inputs.
- **Seasons:** 2020 was very dry (about 100 mm in June); 2021 had 58 mm in May and almost no
  rain from 10 June.
- **Downy mildew:**
  - **2020:** EPI sprays from 25 May to 7 July. Table 1's totals were summed from the PDF:
    EPI 56, growers 69.
  - **2021:** first symptoms 7-21 June. Leaf incidence 22 % untreated, 7.2 % with EPI and
    10.6 % with growers' timing. Sprays: EPI 55, growers 59.
- **Powdery mildew:** first symptoms mid-May to 22 June 2020. In 2021, sprays were 6
  against 8 (p = 0.019), sulphur 19.3 against 24.5 kg/ha, cost 454 against 558 EUR/ha.
- **Savings:** 5 % of cost for downy mildew and 18.6 % for powdery.
- **Printed inconsistencies:** three different sets of spray reductions in the Discussion
  match none of the table totals. The untreated labels in one results paragraph are
  reversed against the Methods.

## Dependence

- **Infection dates are a model's:** "the length of the incubation period was calculated
  [55] so as to ascertain the most probable date of downy mildew infection occurrence".
  Reference 55 is Goidanich, Casarini & Foschi 1957. The timing validation of EPI rests on
  those dates.
- EPI itself is Strizyk's ([ronzon1987](ronzon1987.md), `epi1983.corrected`), in Epicure's
  current, unprinted form.

## Bearing (2026-10-09)

- **First-symptom dates and incidence are observed** (`maddalena2023.panzano`), a Tuscan
  pattern for the truth.
- The infection dates were made with Goidanich's incubation, so anything scored on them is
  calibrated with the engine's incubation data.
