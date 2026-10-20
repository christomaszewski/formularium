---
id: bierman2019
citation: "Bierman, A., LaPlumm, T., Cadle-Davidson, L., Gadoury, D., Martinez, D., Sapkota, S. & Rea, M. 2019. A High-Throughput Phenotyping System Using Machine Vision to Quantify Severity of Grapevine Powdery Mildew. Plant Phenomics 2019: 9209727"
doi: 10.34133/2019/9209727
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [laboratory (leaf disks), USA]
processes: [leaf disk imaging, focus stacking, CNN classification, severity, time series, growth rate, AUDPC]
records: []
datasets: []
files: [bierman_2019.pdf (the 2026-10-20 drop)]
---

# Bierman et al. 2019: machine vision for grapevine powdery mildew on leaf disks

A lab imaging system that photographs 1 cm leaf disks and a GoogLeNet network that scores
the share of each disk with Erysiphe necator hyphae. It agrees with the hyphal transect
count closely for growth rate and AUDPC, and it works on leaf disks, not on vines.

## What it holds

- Imaging: 46-megapixel camera, 3.5x lens, focus stacks of 3 to 10 images per disk in 13.5 to
  26 s, about 1.44 µm² per pixel (l. 8). Throughput: 1,100 to 2,100 disks in an 8-hour day
  (l. 147).
- Network: GoogLeNet retrained on 14,180 subimages from 19 disk images (l. 54). About 800
  subimages per disk (l. 8).
- Agreement with three experts on 800 subimages: 89.3% to 94.8% (l. 90). The abstract gives
  89.3% to 91.7% for the independent set (l. 8). The two ranges do not match.
- Against the hyphal transect count, 9 days after inoculation: R² 0.933 for growth rate,
  0.951 for AUDPC, 0.867 for percent infected subimages (l. 132).
- Samples: isolates NY90, Musc4 and NY1-137 on susceptible, moderate and resistant vines
  (Table 1, l. 27). No field data.

## Dependence

- GoogLeNet (ref. 13) as the base network, retrained by transfer learning in the MATLAB
  Deep Learning Toolbox (l. 53). No shared data from another model.

## Bearing (2026-10-20)

- Strand t3 (powdery mildew). A severity measure for lab leaf disks, scored over time. Its
  growth-rate and AUDPC values could check a severity term in a simulator, if the lab
  growth matches the field.
- A growers' decision engine cannot use it directly: disks, controlled light, one
  isolate per run. Not read in full.
