---
id: trilles2020
citation: Trilles, S., Juan, P., Díaz-Avalos, C., Ribeiro, S. & Painho, M. 2020. Reliability Evaluation of the Data Acquisition Potential of a Low-Cost Climatic Network for Applications in Agriculture. Sensors 20:6597
doi: 10.3390/s20226597
read: 2026-10-21, lightly: abstract, Sections 1-2, 3.1-3.6 text and Table 2-3 summaries, conclusions; Appendix A figures by caption only; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Spain, Castelló, Valencian Community]
processes: [sensor error, low-cost sensor network, data loss, homogenisation, cross-correlation, relative humidity range]
records: []
datasets: []
files: [trilles2020.pdf (the 2026-10-21 drop)]
---

# Trilles et al. 2020: are three low-cost SEnviro vineyard nodes consistent with nearby official stations

Three SEnviro nodes in Castelló vineyards, 1 April to 31 October 2018, compared with AEMET and AVAMET stations by homogenisation and lagged cross-correlation. No record.

**Read this first.** Two text-layer garbles, unchecked: the price is printed "e 256.45" with the currency symbol lost, read as a euro sign; and the energy use is printed "21,4625 mA" with a decimal comma (l. 223), so the battery-runtime figures derived from it are not copied here. Tables 2 and 3 and the Appendix A figures were not read, so no loss percentage is available (the text gives none, l. 339-340). The paper gives no error in degC or %RH against a reference.

## What it holds

- **Set-up** (l. 186, 220-222): three nodes inside a 4 km circle, 1 April to 31 October 2018, a reading every 10 min, 20,160 observations expected per node; best case "uninterruptedly for 140 days" (l. 220).
- **Sensors** (l. 161-162): temperature +/-0.4 degC; humidity stated range 0 to 80 % with +/-3 RH, so the range does not reach 80 to 100 %RH. A 3G link (l. 155).
- **Loss** (l. 339-340, 373): missing values from "technical problems", humidity missing early in the period, mostly at AVAMET stations; outliers and transmission errors were removed (l. 288). Validity rule: five or more measurements per variable per time step (l. 363).
- **Agreement** (l. 506-509, 539, 607): 75 % of lag-0 cross-correlations with nearby stations fall between 0.275 and 0.625; precipitation from -0.26 to 0.97. Two maximum-RH pairs give zero, tied to missing values (l. 532). The nodes show no more inhomogeneities than official stations.
- **Price** (l. 223): 256.45 per unit (euro sign garbled, see above); the year is not printed.
- **Not measured:** RH above 90 % or wet periods; any bias or RMSE against a reference; drift; a percentage of data lost; radiation error against wind.

## Dependence

- **SEnviro:** the node is built on the authors' earlier open-hardware design (refs 21 and 22, l. 152-155); the components are not described here. This paper cites trillesoliver2019 only as ref 2, for the disease models (l. 40, 75, 284). The text does not say that the two papers share the same physical nodes. They share the SEnviro design and the same province and season (2018); trillesoliver2019 has four nodes and 130 days, this paper three nodes (the four-node figure is from that note). A shared author is a flag only.
- Climatol homogenisation (ref 27), SNHT and cross-correlation estimators are generic methods.

## Bearing (2026-10-21)

Sensor menu of D48 and its observation operators.

- **Error model supported:** weakly. It supports that a cheap vineyard node (256.45 per unit, currency read as euro and unchecked, year not printed) loses data in patches and that its RH sensor stops at 80 %, so an RH >= 90 % threshold cannot be seen directly by this sensor. It gives no bias or RMSE to draw from, and no packet-delivery figure.
- **Not measured:** the items under "Not measured" above.
- **Kind of result:** a field reliability study by consistency tests, vineyards in Castelló, one season.
