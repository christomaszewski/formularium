---
id: roberts2006
citation: Roberts, M. J., Schimmelpfennig, D., Ashley, E. & Livingston, M. (with Ash, M. & Vasavada, U.) 2006. The value of plant disease early-warning systems: a case study of USDA's soybean rust coordinated framework. USDA Economic Research Service, Economic Research Report No. 18
doi:
read: 2026-10-18, LIGHT, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py; appendix tables and figures not rendered
status: read
diseases: [soybean rust]
crops: [soybean]
regions: [United States, Corn Belt]
processes: [value of information, early warning, fungicide decision, forecast quality, decision tree]
records: []
datasets: []
files: [roberts_2006.pdf (the 2026-10-18 drop)]
---

# Roberts et al. 2006: the value of soybean rust early-warning information

A decision model of what the 2005 USDA soybean rust information framework was worth to producers, as a function of how much infection uncertainty the forecasts resolve. No record: an economic study. No DOI (USDA ERS report). Not the same as roberts2017.

## What it holds

- **Result** (l. 87-90, 186-187, Table 3 at l. 1027): framework information raised US soybean producer profits by 11 to 299 million dollars in 2005 (0.16 to 4.12 dollars per acre); base-case totals 11,247,380 / 113,715,650 / 298,521,730 dollars for forecasts resolving 20 / 50 / 80 % of uncertainty. Reported framework cost 2.6 million to almost 5 million dollars. Corn Belt 6.01 dollars per acre at high quality; regional high-quality values 3.48 (Southeast) to 6.01; range over prior and quality 0 to 6.38 dollars per acre (l. 788, 827).
- **Strategies and inputs** (l. 468, 530-535, 737, 880): preventive fungicide 25.63 dollars per acre (1 % yield loss); monitor and apply curative treatment if infection is found (7 % loss); no management (25 % loss); production cost 125 dollars per acre, base yield 44.6 bu per acre, soybean price 6.19 dollars (May 2 futures). Costs and losses are from Livingston et al. (2004, OCS-04D-02).
- **Representative farm** (Table 2, l. 737; Corn Belt, 742 acres), profit in dollars, infection / no infection: preventive 91,031 / 93,079; curative 82,532 / 107,118; no management 60,885 / 112,097. Thresholds (l. 721): prior below 19 % do nothing; 19 to 63 % monitor and treat if found; above 63 % treat preventively.
- **Priors** (l. 804, 1639-1644): the probability of infection is the share of years with wheat stem rust epidemics times the share where climate favoured rust, weighted by soybean production 1995-2004. National 0.53; Appalachia 0.67, Corn Belt 0.55, Delta 0.55, Lake States 0.49, Northeast 0.62, Northern Plains 0.43, Southeast 0.76, Southern Plains 0.51.
- **Information model** (l. 1514-1539): forecast quality f in [0,1]; signal probabilities b = f(1 - P) + P (high-risk signal), g = P(1 - f), a = P; f = 0 is no information, f = 1 resolves all uncertainty; used 0.2, 0.5, 0.8. Value is the difference in expected profit with and without the signal. Risk-averse variant: constant relative risk aversion, coefficient 4 (l. 1691; the utility formula is garbled in the text layer). A price-effect variant regresses price on yield loss.
- **Forecasts** (l. 570): from the IAMS / Soybean Rust Aerobiology Prediction System (Penn State, ZedX); the value model takes quality as a parameter and does not run it.
- **Data:** GAO-05-668R data, NASS unpublished planting intentions, USDA production data; no public route for the unpublished NASS data (l. 101).

## Contradiction carried, not resolved

The curative-treatment cost. The text gives 13.81 dollars per acre for the curative fungicide (l. 530) and 6.71 dollars per acre for monitoring (l. 535); the Table 1 cell for the curative option reads 2.52 dollars per acre. Without the rendered table this is open.Appendix tables 1-5 and figures 1-6 were not rendered; the infection-probability formula is described in words only.

## Dependence

- Costs and yield losses come from the authors' own 2004 report. Priors use wheat stem rust records as a proxy for soybean rust, not soybean records. f is free, not fitted to IAMS output, so the model does not depend on IAMS's calibration. No model shaped the observed 2005 data.

## Bearing (2026-10-18)

Strand 6 (methods); strand 5 for how much a sensor or forecast is worth:

- **Method:** a simple value-of-information recipe Agrarium's sweep or sensor-placement method can take: three actions (spray early, monitor then spray late, do nothing), a prior probability of an epidemic year, a quality f for the signal, and the profit difference. It gives the break-even for a sensor: the signal is worth buying where the prior sits between the do-nothing and preventive thresholds (here 19 to 63 %), and worth nothing at the ends.
- **Numbers to compare, not borrow:** soybean in the US in 2005, a low-rust year; vineyard costs and losses differ.
- **Limits:** quality f is assumed, never measured; the prior is from a proxy disease; one season; cost inconsistency above.
