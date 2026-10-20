---
id: mahlein2019
citation: "Mahlein, A.-K., Alisaac, E., Al Masri, A., Behmann, J., Dehne, H.-W. & Oerke, E.-C. 2019. Comparison and Combination of Thermal, Fluorescence, and Hyperspectral Imaging for Monitoring Fusarium Head Blight of Wheat on Spikelet Scale. Sensors (Basel) 19(10): 2281"
doi: 10.3390/s19102281
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [Fusarium head blight (Fusarium graminearum, F. culmorum)]
crops: [wheat]
regions: [controlled conditions, greenhouse and laboratory (Germany)]
processes: [thermal imaging, chlorophyll fluorescence, hyperspectral reflectance, spikelet scale, SVM classification, early detection, sensor fusion]
records: []
datasets: []
files: [mahlein_2019.pdf (the 2026-10-20 drop)]
---

# Mahlein et al. 2019: thermal, fluorescence and hyperspectral sensors for head blight on wheat

Spikelet-level sensing of Fusarium head blight in spring wheat, inoculated in a greenhouse
and measured for 30 days. Hyperspectral reflectance showed infection at 3 days after
inoculation, before visible symptoms were clear. Combining sensors gave the best
classification. The work is on wheat, not vines.

## What it holds

- Design: spring wheat cv. Passat, two Fusarium species, spikelets from six spikes per
  treatment, measured at 3, 5, 7, 12, 17, 21 and 30 days after inoculation (l. 19 to 22,
  33).
- Symptoms: first lesions at 3 days (1% on glumes) (l. 38). Thermal temperature
  heterogeneity rose from 7 days and peaked at 12 days (l. 40).
- Fluorescence: maximal fluorescence (Fm) fell from 7 days; Fv/Fm and yield (Y[II]) fell
  only from 12 days (l. 43).
- Reflectance: changes from 3 days at 500, 675 and 760 nm, and water bands at 1,440, 1,880
  and 2,000 nm (l. 46).
- Correlation with disease severity: strongest for Fv/Fm (r = -0.88), weakest for ΔT (r =
  -0.72) (l. 48).
- Classification (SVM): 78% at 3 days with IRT or HSI, up to 100% at 12 to 21 days with HSI,
  and 67% at 30 days with IRT (l. 53). Mean accuracy 90% for IRT with HSI and 87% for all
  three sensors (l. 54).

## Dependence

- Vegetation indices and the masking tool (HSVaP) from the group's earlier work (Alisaac et
  al. 2018, ref. 15); imaging methods from Mahlein 2016 (ref. 14). No shared dataset from
  another group is recorded.

## Bearing (2026-10-20)

- Strand t2 (observation), by analogy only. An early reflectance signal before visible
  symptoms is the sort of thing a vineyard observation step could check against field
  counts.
- Off the point for vines: wheat head blight, spikelets, controlled conditions, no field
  data. Not read in full.
