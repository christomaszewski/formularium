---
id: karisto2023
citation: Karisto, P., Suffert, F. & Mikaberidze, A. 2023. Spatially explicit ecological modeling improves empirical characterization of plant pathogen dispersal. Plant-Environment Interactions 4:86-96
doi: 10.1002/pei3.10104
read: 2026-10-25, lightly: the methods and results in full, with Table 2 (from the Europe PMC full-text XML, PMC10243544, converted to plain text with tables as rows at the end; the introduction and discussion not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [septoria tritici blotch, stripe rust, potato late blight]
crops: [wheat, potato]
regions: [not stated in the parts read]
processes: [dispersal gradient, dispersal kernel, source extent, splash dispersal, wind dispersal, power-law kernel, exponential kernel]
records: []
datasets: []
files: [dr1025_karisto2023.xml (the 2026-10-25 drop; no PDF, Europe PMC XML)]
---

# Karisto et al. 2023: refitting three published dispersal gradients with the size of the source built in

Three field gradients (wheat splash, wheat stripe rust, potato late blight) are refitted with a model that integrates a kernel over the spatial extent of the source, and the resulting kernels are compared with the usual point-source fits.

**Read this first.** All three data sets are analogues and none is a vine or a downy mildew: Zymoseptoria tritici (splash, wheat), Puccinia striiformis (wind, wheat) and Phytophthora infestans (Gregory's 1968 potato plots). They are other people's gradients, refitted here. The table's "1D" column is the point-source fit, which the Table 2 caption says corresponds to the estimates in the earlier publications (l. 133); the "2D" column is this paper's own spatially explicit fit. Table 2 was read from the XML text, where the cells are rows.

## What it holds

- **Method:** the disease gradient is modelled as a kernel integrated over the source area and the measurement area; the point-source approximation is the 1-D version. In all three cases the 2-D fit gave steeper kernels and shorter dispersal distances than the point-source fit (l. 76). The exponential kernel has a mean distance of 2 alpha in two dimensions (l. 31); the modified power law is after Mikaberidze et al. 2016 because it describes stripe rust gradients better than exponential or Gaussian kernels (l. 55, cited).
- **Wheat splash (Z. tritici):** plots 1.125 m wide and 4 m long, with an inoculated strip 40 cm wide across the plot (l. 47). Exponential alpha 0.151 m (1-D) and 0.135 m (2-D) (l. 135, 138); median distance r50 0.25 and 0.23 m (l. 136, 139); r90 0.58 and 0.52 m (l. 137, 140).
- **Wheat stripe rust (wind-borne, Madras and Hermiston):** modified power law, gamma 2.4 and 2.5 (1-D) against 2.6 and 2.7 (2-D) (l. 135, 138); r50 4.2 and 3.0 m (1-D) against 2.3 and 1.9 m (2-D) (l. 136, 139); r90 241 and 76 m (1-D) against 35.3 and 20.4 m (2-D) (l. 137, 140), in plots at least 100 m long (l. 140). The r90 falls by factors of 6.8 and 3.7 (arithmetic, not printed).
- **Potato late blight (Gregory 1968, Table III, unsprayed):** plots 8.5 m wide and over 60 m long, rows along the gradient, lesions counted at 1 to 30 m (l. 62). Power law r to the minus gamma, gamma 1.4 (1-D) and 1.9 (2-D) (l. 135, 138). The authors call it "not a kernel" and say it cannot be normalised (l. 64, 66), so no r50 or r90 is given (l. 136, 137).
- **Reconstruction:** Gregory did not report the widths of the inoculated area or the measurement lines, nor the origin of the distances; the authors assumed 0.38 m between plants (15 inches), an inoculated width of 1.9 m and lines of 0.76 m (l. 63).

## Dependence

- Re-analyses of published gradients: the Z. tritici data from Karisto et al. 2022, the stripe rust data from Cowger et al. 2005 and Sackett and Mundt 2005 (not fetched), and the late blight data from Gregory 1968. Kernel forms after Nathan et al. 2012 and Mikaberidze et al. 2016. The authors' own earlier fits are the 1-D column.

## Bearing (2026-10-25)

- **dm.wind_shape 0.8 [0.3-1] (exponential-power):** a fat tail suits wind-borne spores, a thin exponential suits splash. The paper favours a modified power law for stripe rust over exponential and Gaussian kernels (l. 55), and fits a thin exponential to wheat splash. That is the shape of a thin short-range part plus a fat wind part, but gives no value for the exponent, and no vine data. Analogue, re-fit.
- **dm.wind_scale_m 3 m and dm.kernel_radius_m 40 m [20-80]:** the 2-D r90 for wheat stripe rust, 20.4 and 35.3 m (l. 140), is the same order as the registered radius; the 1-D values, 76 and 241 m (l. 137), are above it. The practical lesson is that a gradient measured from a single source is not a kernel: the same data give distances several times shorter once the source is given its size.
- **dm.splash_scale_m 1 m [0.5-2]:** the wheat splash scale is smaller: alpha 0.135 to 0.151 m, so a mean distance of 0.27 to 0.30 m (2 alpha, arithmetic from l. 31, 135, 138), below the registered range, and r90 about 0.5 to 0.6 m (l. 137, 140). It is a wheat canopy, with a different drop height and leaf surface from a vine, so it neither confirms nor refutes the vine value.
