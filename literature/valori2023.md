---
id: valori2023
citation: "Valori, R., Costa, C., Figorilli, S., Ortenzi, L., Manganiello, R., Ciccoritti, R., Cecchini, F., Morassut, M., Bevilacqua, N., Colatosti, G., Pica, G., Cedroni, D. & Antonucci, F. 2023. Advanced forecasting modeling to early predict powdery mildew first appearance in different vines cultivars. Sustainability 15:2837"
doi: 10.3390/su15032837
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [Italy (Lazio)]
processes: [PLS-DA classification, first-appearance forecast, weather station data, fungicide timing, berry quality]
records: []
datasets: []
files: [valori_2023.pdf (the 2026-10-20 drop)]
---

# Valori et al. 2023: PLS-DA forecast of first powdery mildew appearance, with fewer sprays

A partial least squares discriminant model, built on weather and an untreated control, flags the first powdery mildew infection three days ahead. It was tested on Trebbiano and Sangiovese near Rome against a calendar spray programme.

## What it holds

- **Claim:** the flag comes three days before first appearance, and the model cut the spray count by about four (l. 28, 40-41).
- **Example, Sangiovese 2021:** the flag came on 18 June (DOY 169) and first infection on 28 June (DOY 179). The calendar gave five sprays, the first four before infection (l. 528-529, 535).
- **Quality:** soluble solids, pH and titratable acidity did not change significantly with the reduced programme (l. 1255-1256).
- **Design inconsistency:** the abstract gives three training years and two test years (l. 39). The introduction gives two training years (2019, 2021) and one test year (2022) (l. 103-104). Check the split before use.

## Dependence

The method is PLS-DA on the paper's own weather station and control-plot record. The trial agronomy follows Cecchini et al. (cited in Methods). None recorded beyond that.

## Bearing (2026-10-20)

- **Strand t3 (powdery mildew), with t1 (fewer sprays).** A weather-and-control rule that times the first spray. For a simulator the usable output is the flag date and the spray count, not a dose.
- **Not read in full.** One vineyard in Lazio, and the training and test years disagree (l. 39 against l. 103-104), so the timing claims are unchecked.
