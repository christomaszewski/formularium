---
id: bourgeon2015
citation: "Bourgeon, Marie-Aure. 2015. Conception et évaluation d'un dispositif d'imagerie multispectrale de proxidétection embarqué pour caractériser le feuillage de la vigne. Thesis, Université de Bourgogne (HAL tel-01291695, NNT 2015DIJOS066); pages not printed in the text read"
doi:
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full; French thesis, read through the abstracts, the trial description, the calibration and the NDVI chapters
status: read
diseases: []
crops: [grapevine]
regions: [Burgundy, France]
processes: [proximal multispectral imaging, reflectance calibration, NDVI, canopy leaf area]
records: []
datasets: []
files: [bourgeon2015.pdf]
---

# Bourgeon 2015: a mobile multispectral imaging rig for vine foliage

A Burgundy PhD on a mobile proximal imaging rig for vine foliage. It calibrates images to reflectance with a colour chart and checks its NDVI against a GreenSeeker.

## What it holds

- **Rig:** a GPS, a visible and near-infrared multispectral camera and a GreenSeeker RT-100, observing the foliage in the trellis plane in daylight (abstract, l. 84-92).
- **Trial:** a Terroir plot of nine blocks in a Latin square, with Chardonnay, Pinot Noir and Meunier. Six image datasets in 2013 at different stages (l. 91-92; Figure 3, l. 2194).
- **Calibration:** a MacBeth chart is the reference. Hidden-chart parameters are interpolated and checked by leave-one-out validation with RSCE and NAE (l. 99; l. 3485-3498). Per-channel regression lines have R2 above 0.98 (l. 3274-3275).
- **Photo leaf area check:** a black-and-white photo estimate on twelve vines, against the reference measure, gives R2 0.44, which the author calls poor (l. 1864-1866).

## Dependence

- Builds on the MacBeth chart as radiometric reference, the GreenSeeker RT-100 NDVI (Drissi et al. 2009; Debuisson et al. 2009; l. 1694-1698), the vertical leaf area index of Drissi et al. 2009 (l. 1700-1704), and leave-one-out validation after Picard and Cook 1984 (l. 3485).

## Bearing (2026-10-26)

- classes.tsv names no search for this row. By the triage question list it falls under the 10-21 sensors item, on calibration.
- A sensing plan could take the chart-based calibration and the GreenSeeker comparison as a method. The rig is a canopy imaging tool, not a weather node. Not read in full.
