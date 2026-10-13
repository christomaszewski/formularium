---
id: molitor2025
citation: Molitor, Daniel, Heilemann, Kristina, Jiménez-Rodríguez, César Dionisio, Hüther, Silke, Trapp, Oliver, Stalport, Anouck, Louvieaux, Julien, Viret, Olivier, Ladach, Martin et al. 2025. UniPhen 'PIWI': high-resolution simulation of the phenological development of 13 fungus-tolerant cultivars based on a broad observation data set from Central Europe. OENO One 59(2)
doi: 10.20870/oeno-one.2025.59.2.8457
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5), which checked the degree-day function on the page image; 26 of 26 quotes found at their lines by scripts/verify_quotes.py; the author list beyond the ninth name is not transcribed; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Luxembourg, Germany, Belgium, Switzerland, Austria]
processes: [phenology, budburst, flowering, veraison, maturity]
records: []
datasets: []
files: [2025-molitor-10-20870-oeno-one-2025-59-2-8457.pdf]
---

# Molitor et al. 2025: UniPhen's cumulative degree-days for 13 fungus-tolerant cultivars

The UniPhen model of `molitor2020` (degree-days with 10, 20 and 30 °C thresholds,
counted from Riesling's budburst) given cultivar values for 13 PIWI and 3 traditional
cultivars from four complete years at eight sites. A threshold model; the per-cultivar
sums are in a heat map and a supplement, not the text.

## What it holds

- **Data:** BBCH 01-89 at 15 vineyards (Ath, Belgium at 60 m to Haidegg, Austria at 600
  m), every 2-3 days by one observer per site, six plants a cultivar; eight sites with
  four complete years 2021-2024 calibrate (l. 164-218, 407-412); BBCH 89 is the day the
  must reaches 60 °Oechsle (l. 413); Riesling's budburst is virtual at three sites, from
  Pinot noir's 6.1 degree-days earlier (l. 416-421); stations within 200 m (l. 427).
- **Model:** daily degree-days 0 below 10 °C, t − 10 to 20 °C, 10 from 20 to 30 °C,
  falling to 0 at 40 °C (l. 448-456); cumulative from the day after Riesling BBCH 09;
  the thresholds the unified triplet of Molitor et al. 2020, no cultivar fitting beyond
  each stage's mean sum (l. 444-461); the UNIPHEN-Tool R script (l. 441).
- **Values:** Riesling BBCH 61 at 251, 81 at 859, 89 at 1,012 degree-days (l. 472-473);
  the 16 cultivars' sums in Fig. 2 and Table S3.
- **Errors:** normalised SD 5.5 d at 15 °C over all stages and cultivars, 1-2 d at
  budburst, 13.3 d at BBCH 89 (l. 84, 494, 579, 603); mean absolute error 10-18
  degree-days by site, mean bias −12.7 to +7.6 (l. 569, 752); the discussion reads the
  bias sign the other way from the methods (l. 445-447, 496, 680); Regent's 25.1 is
  2021 in Table 5, 2023 in the text (l. 482).

## Dependence

- **Computes** UniPhen (`molitor2020`'s thresholds); fitted to the consortium's
  observations with Riesling's budburst as the clock.

## Bearing (2026-10-13)

- A threshold model; the point for Agrarium is the error floor of a well-run multi-site
  degree-day model, 5.5 d, with maturity the loose end (13 d).
