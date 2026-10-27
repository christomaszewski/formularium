---
id: zwankhuizen1998
citation: Zwankhuizen, M. J., Govers, F. & Zadoks, J. C. 1998. Development of potato late blight epidemics: disease foci, disease gradients, and infection sources. Phytopathology 88:754-763
doi: 10.1094/PHYTO.1998.88.8.754
read: 2026-10-25, lightly: the abstract, the methods on gradients, the results and Table 4 (full text extracted, not every section read; two columns interleaved), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [potato late blight]
crops: [potato]
regions: [Netherlands, Flevoland, Friesland, Noordoostpolder]
processes: [dispersal gradient, exponential gradient, point source, area source, refuse piles, prevailing wind, crosswind gradient]
records: []
datasets: []
files: [dr1025_zwankhuizen1998.pdf (the 2026-10-25 drop)]
---

# Zwankhuizen et al. 1998: disease gradients of potato late blight downwind of refuse piles and of infested organic fields

Field and regional gradients of late blight in Dutch potato fields, fitted with a negative exponential, used to show that refuse piles act as steep point sources and infested organic fields as flat area sources.

**Read this first.** An analogue: Phytophthora infestans on potato in the Netherlands, and a gradient of disease in a field, not a dispersal kernel (it mixes spore flux, infection and later disease growth). Three cautions for use.
- The intensity unit differs by field: percent leaf area for the 1965 and 1968 fields, proportion of diseased plants for one field and lesions per 30 m2 for the rest (Table 4 footnote b, l. 416).
- The "distance to source" in Table 4 runs from the centre of the source to the centre of the field (l. 420); the slope is fitted over the 4 to 30 observation points inside each field.
- The mean point-source slope is carried by one steep field (see below). The reading JSON called the field at 34 m (-0.033 per m) the flattest point-source field; Table 4 also lists -0.016 per m at 59 m (l. 394).

## What it holds

- **Model:** y = a exp(-bx), after Kiyosawa and Shiyomi, with x in m; b is the slope and 1/b the e-folding distance (l. 218-219); fitted by non-linear regression (l. 424).
- **Headline:** the mean slope of field gradients downwind of refuse piles (point sources) was -0.35 per m, and downwind of organic fields (area sources) -0.0045 per m, a 100-fold difference (l. 363-364; abstract l. 21-24). The mean is -0.35 +/- 0.26 (standard error) and uses significant regressions only (l. 425). 1/b for -0.35 is 2.9 m (arithmetic, not printed).
- **Point-source fields (Table 4, 1965, Friesland; sources are refuse piles 15 to 70 m from the field centre):** 15 m, 25 observation points, b -1.35 per m, R2 0.71 (l. 397); 30 m, 4 points, -0.30, R2 0.97 (l. 396); 34 m, 30 points, -0.033, R2 0.53 (l. 393); 59 m, 30 points, -0.016, R2 0.15 (l. 394); 70 m, 13 points, -0.051, R2 0.86 (l. 395). These five slopes average -0.35 (arithmetic, not printed), so the printed mean appears to use these five; their 1/b run from 0.74 m to 62 m (arithmetic), and their median slope is -0.051 per m, 1/b about 20 m (arithmetic).
- **Area sources:** seven conventional fields 950 to 3,140 m from the organic fields taken as a virtual source have slopes of -0.0027 to -0.0076 per m (l. 400-406); the printed mean, -0.0045, uses significant regressions only (l. 425). The regional gradient downwind (east, with the prevailing wind) of the organic fields as a virtual source has slope -0.0029 per m, observable over about 4 km (1994, Flevoland; l. 521).
- **Crosswind:** a crosswind gradient at 1,306 m from the source was fitted by a Gaussian, y = 0.78 + 8.24 exp(-0.5 [x/211.14]^2), R2 0.70, with the bisector of the cone pointing east, with the prevailing wind (l. 371-372).
- **Context:** in August 1994 infested organic fields became the main mid-season inoculum sources for neighbouring conventional fields (abstract); the genotypes along the gradients matched those in the sources (abstract).

## Dependence

- The exponential gradient model of Kiyosawa and Shiyomi (1972). The 1965 and 1968 rows of Table 4 come from earlier surveys by Zadoks and co-workers, re-analysed here (per the reading agent); the 1994 to 1996 surveys in Southern Flevoland are this paper's own. The third author, Zadoks, is among those earlier workers: a shared author, a flag only.

## Bearing (2026-10-25)

- **dm.wind_scale_m 3 m [2-10] and dm.kernel_radius_m 40 m [20-80]:** the mean point-source slope gives a scale of 2.9 m (arithmetic), the same as the registered 3 m, but the five fields behind it span 0.74 to 62 m, and the mean rests on one steep field. The flatter fields (1/b of 20, 30 and 62 m) are in the range of the kernel radius. A potato late blight analogue, gradients of disease inside fields at 15 to 70 m from a pile, not a kernel; it supports no single value.
- **dm.wind_shape 0.8 [0.3-1]:** only a pure exponential was fitted (shape 1 in exponential-power terms), and R2 ranges from 0.15 to 0.97, so no tail test was made. The 100-fold gap between point-source and area-source slopes (l. 363-364) shows that one exponential does not span tens of metres and kilometres, which is in the direction of a fat tail but gives no exponent.
- **dm.wind_stretch_per_ms 0.3:** the crosswind cone lies along the prevailing wind (east; l. 371-372, 521). That is direction, not wind speed; no per m/s value.
