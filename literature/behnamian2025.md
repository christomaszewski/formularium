---
id: behnamian2025
citation: Behnamian, Sara & Fogh, Fatemeh. 2025. Interval-censored survival analysis of grapevine phenology: thermal controls on flowering and fruit ripening. Research Square preprint, posted 2025-09-11
doi: 10.21203/rs.3.rs-7544186/v1
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [USA]
processes: [phenology, flowering, ripening, survival analysis]
records: []
datasets: []
files: [behnamian2025_rs.pdf]
---

# Behnamian & Fogh 2025: the preprint behind the 2026 survival-model paper

The first version of `behnamian2026`: the same 41,274 USA National Phenology Network
records on seven vines at five sites, the same interval-censored Weibull and log-logistic
models, here with time ratios per standard deviation of the z-scored covariate rather
than per unit, and with the endogenous "to-cutoff" fits shown beside the fixed-window
ones.

## What it holds

- **Data:** 7 Vitis vinifera plants, 5 sites, 16 observers, 30 March 2012 to 16 May 2025
  (l. 161-163); 50 plant-site-year units, 30 flowering and 37 ripening events, median
  first detection day 150 and 205 (l. 166, 309-310); intervals (L, R] from the last
  absent to the first present observation, right-censored years (l. 185-187); NASA POWER
  weather, no gap filling (l. 198-202); 8,354 site-days (l. 318). Cultivars and
  locations not printed.
- **Model:** GDD10 = max((Tmax + Tmin)/2 − 10, 0) (l. 212); covariates z-scored; AFT by
  maximum likelihood, time ratio per +1 SD (l. 254-302); windows days 1-120 and 1-180
  (l. 283); site-years under 70 % coverage dropped (l. 295). Median pre-season GDD10 228
  (flowering) and 646 (ripening) (l. 413).
- **Results:** flowering on pre-season GDD, Weibull 0.938 and log-logistic 0.917 per SD;
  ripening 0.864 and 0.962 (the latter crossing 1); with precipitation, ripening 0.933
  (log-logistic) (l. 420-432). The to-cutoff fits give ratios above 1 (1.52 flowering,
  1.14 ripening; 1.575 and 1.085 in the text) which the authors call the artefact of an
  endogenous window (l. 358-393). Collinearity of heat and heat-day counts, VIF 8.9
  (l. 407-408). Fifty units limit power (l. 463).
- Code on GitHub (l. 491); the observations are restricted (l. 492).

## Dependence

- **As `behnamian2026`:** no model computed beyond GDD10; the 2026 paper is this with
  the ratios re-expressed per unit and the argument sharpened.

## Bearing (2026-10-13)

- Superseded by `behnamian2026`; kept because it shows the endogenous fits the published
  paper only describes.
