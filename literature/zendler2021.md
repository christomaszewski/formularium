---
id: zendler2021
citation: Zendler, Daniel, Malagol, Nagarjun, Schwandner, Anna, Töpfer, Reinhard, Hausmann, Ludger & Zyprian, Eva. 2021. High-Throughput Phenotyping of Leaf Discs Infected with Grapevine Downy Mildew Using Shallow Convolutional Neural Networks. Agronomy 11:1768
doi: 10.3390/agronomy11091768
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine (vitis vinifera; breeding crosses with vitis aestivalis and v. coignetiae parents)]
regions: [Siebeldingen Germany, Germany]
processes: [sporulation, variety resistance, disease severity scoring, leaf disc assay, image analysis]
records: []
datasets: []
files: [q293.pdf]
---

# Zendler et al. 2021: leaf-disc phenotyping of downy mildew with CNNs

A light read (the deep-research B list).

## What it holds

- Leaf discs from two F1 crosses (497 and 314 individuals), inoculated in 2020 with P. viticola at 18,000 sporangia/mL (l. 151-184).
- Scoring at 4 dpi on a reversed five-class OIV 452-1 scale (l. 228-237).
- Two shallow CNNs: background vs disc, 98 % validation accuracy; sporangiophores vs none, 95 % (l. 337-342).
- Ground truth: 30 discs, 15,180 slices, three experts (l. 300, 359).
- Median true positives 96-97 % on the training cross and 92-94 % on the untrained cross (l. 393-395).
- CNN percentage of disc area correlates with expert scores at r = 0.92 and 0.91 (l. 417-419); with OIV class at r = 0.96 and 0.92 (l. 428).

## Dependence

- none. The paper trains its own shallow CNNs on its own leaf-disc images and uses the OIV 452-1 descriptor for the expert scale. The humidity and light conditions (l. 196-197) are incubation settings, not a leaf-wetness rule or a listed engine model.

## Bearing (2026-10-10)

- An open, documented leaf-disc phenotyping method for downy mildew with labelled images and a percentage-of-area output, useful as a source of observed severity for a truth's observation side; it has no model the engine runs.
