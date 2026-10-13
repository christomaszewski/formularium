---
id: pouget1988
citation: Pouget, R. 1988. Le débourrement des bourgeons de la vigne : méthode de prévision et principes d'établissement d'une échelle de précocité de débourrement. Connaissance de la Vigne et du Vin 22(2):105-123
doi:
read: 2026-10-13, a light reading (French, from a tesseract OCR of the scanned copy) by a reading agent (claude-haiku-5-5), which read the formulas and tables on page images; 30 of 30 quotes found at their lines by scripts/verify_quotes.py; Tables I, II, V and VII (pp. 108-111, 116) read in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Bordeaux]
processes: [phenology, budburst, cultivar precocity]
records: [pouget1988.budburst]
datasets: [pouget1988.bordeaux]
files: [pouget1988_oeno.pdf]
---

# Pouget 1988: forecasting budburst from summed bud actions, and a precocity scale

INRA Bordeaux's method: the rate at which buds burst follows a power law of temperature
measured in growth chambers, each day's action at the maximum and minimum is averaged
and summed from 1 January, and budburst comes when the sum nears a cultivar's constant.
The paper that the catalogue's RIOU and BRIN forcing pieces descend from, with a scale
of 22 cultivars.

## What it holds

- **Rate law** (pp. 107-108): V = 1000 / days to 50 % budburst = K t^c between 5 and 25
  °C, from chamber tests at 5, 10, 15, 20 and 25 °C (years and counts not printed; l.
  137-147); c for the references in Table I (Vitis thunbergii 1.150, Perle de Csaba
  1.285, Traminer 1.442, Merlot 1.702, Ugni blanc 1.865, Cabernet-Sauvignon 2.000).
- **Threshold** (Table II): the temperature at which V = 20, a 50-day budburst: 4.3, 5.6,
  7.0, 9.4, 11.0, 12.2 °C for the same six; in the field, budburst after 3-8 consecutive
  days at or above it (l. 211-229).
- **Daily action and sum** (pp. 109-111): a_j = (a_M + a_m)/2 with a = K t^c at the day's
  maximum and minimum, positive temperatures only; summed from 1 January for Bordeaux
  (Pouget 1967); budburst when the sum nears S (l. 248-338). Table V: S 1,788 ± 38
  (Perle de Csaba), 1,585 ± 41 (Traminer), 1,255 ± 12 (Merlot), 1,089 ± 15 (Ugni blanc)
  over "17 years (1961-1987)". At 80 % of S, budburst is 10-20 days off (l. 366). No
  chilling term; dormancy is taken as released by 7 consecutive days below 10 °C (l. 93).
- **Errors:** 1-3 d of observation error, 0-5 d between dates from 30-year mean
  temperatures and observed means, cold spells unmodelled; tested at Bordeaux only
  (l. 474-503, 614).
- **Precocity scale** (Table VII, p. 116; `pouget1988.budburst`): 22 cultivars over
  1970-1988, mean budburst day from 1 January with its confidence interval, and S, c, K
  and threshold derived from the references through S = 3737 − 30.4138 D, c = 2.824 −
  0.000869 S, log K = 2.57403 − 1.72494 c, threshold = −6.40 + 9.31 c (l. 752-798):
  Perle de Csaba day 63.5 to Sélect 97.9; Chardonnay 66.9 (S 1,703, c 1.345, 6.1 °C),
  Merlot 81.2 (1,255, 1.702, 9.4 °C), Cabernet Sauvignon 91.2 (985, 2.000, 12.2 °C),
  Carignan 85.2, Grenache 82.7, Mourvèdre 93.1.

## Dependence

- **Fitted to** INRA Bordeaux's own chamber tests and field dates; the 1 January origin
  and the near-constant S are Pouget 1967a,b's. `cortazar2009`'s RIOU (Riou 1994) is a
  development of this method, and BRIN's forcing idea follows it.

## Bearing (2026-10-13)

- A threshold model, but the primary source for cultivar precocity in days and for the
  per-cultivar response (c, K) that later models reuse; a Bordeaux-only calibration
  with no printed forecast error.
