---
id: gajinov2022
citation: Gajinov, S., Popović, T., Drajić, D., Gligorić, N. & Krčo, S. 2022. Qualitative parameter analysis for Botrytis cinerea forecast modelling using IoT sensor networks. Journal of Networking and Network Applications 2(3):129-135
doi: 10.33969/j-nana.2022.020305
read: 2026-10-27, lightly: abstract, study sites, methods introduction and the results and discussion lines found by search (not every paragraph), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [Botrytis cinerea (grey mould)]
crops: [grapevine]
regions: [Serbia (Fruska Gora), Montenegro (Podgorica)]
processes: [rule-based model, IoT sensors, leaf wetness, relative humidity, rain, decision support, sensor value]
records: []
datasets: []
files: [syn1027_gajinov2022.pdf (the 2026-10-27 drop)]
---

# Gajinov et al. 2022: how much each humidity sensor adds to a rule-based Botrytis forecast in four vineyards

Runs an expert rule set for Botrytis cinerea on sensor data from four vineyards and counts how often a relative humidity sensor, a leaf wetness sensor or a rain gauge triggers it. No record: an evaluation of a rule, with no disease observations.

**Read this first.** Nothing is fitted and no disease outcome is compared. The percentages are shares of observed time in which the rule's humidity step fires: trigger share, not forecast skill. The "reduced the use of pesticides up to 20%" claim in the abstract has no comparison design in the parts read.

## What it holds

- **Rule, not a trained model** (l. 8): the existing expert model "is implemented as a rule-based algorithm and applied on the data collected from IoT sensor nodes". A moisture measurement (relative humidity, leaf wetness or rain) above its threshold triggers a second, temperature-based risk index (l. 4, 63).
- **Real data** (l. 8, 58): four vineyards in Serbia and Montenegro, monthly tables April to September 2020; air temperature, relative humidity, rain and leaf wetness. Some stations have a measured leaf wetness sensor, others a calculated value (l. 18).
- **Labels:** none; no disease observation is used. **Synthetic or augmented data:** none.
- **Average trigger shares** (l. 4): a low-cost relative humidity sensor detects on average 14.61% of risk cases, a leaf wetness sensor a further 3.99%, a rain sensor a further 0.59%, so risk is detected in 19.19% of the time. The leaf wetness sensor therefore widens the risk time by about a quarter over humidity alone (arithmetic, not printed).
- **Monthly maxima** (l. 73): humidity up to 33.9% of observed time, leaf wetness up to 10.5%, rain up to 1.4%.
- **Validation design:** none in the sense of held-out years; one season, rule evaluated on sensor records.

## Dependence

- The rule is an agronomists' expert Botrytis model (the paper's reference 4), digitalised in a decision support tool. No disease observations are used. None recorded for training data.

## Bearing (2026-10-27)

- **D58 (variable search):** it measures how much a wetness sensor adds to a humidity trigger, not whether it improves disease prediction. It supports the narrower point that humidity is the trigger in most hours and wetness and rain add little; it gives no skill ceiling.
- **D60:** a data point on leaf wetness as a sensor reading that a humidity-only record omits; no estimate of the error from filling it with a model.
- **Not shown:** any link between the extra triggered hours and observed grey mould.
