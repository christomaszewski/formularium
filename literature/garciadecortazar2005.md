---
id: garciadecortazar2005
citation: García de Cortázar-Atauri, I., Córdova, C. & Pinto, M. 2005. Canopy structure and photosynthesis modelling of grapevines (Vitis vinifera L. cv. Sultana) trained on an overhead (parronal) trellis. Australian Journal of Grape and Wine Research 11(3):328-337 (page numbers as printed: see text header)
doi: 10.1111/j.1755-0238.2005.tb00032.x
read: 2026-10-28, leaf angle, extinction, porosity and light measurements; by a reading agent and note writer (claude-sonnet-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Chile]
processes: [leaf angle, extinction coefficient, light transmittance, overhead trellis, canopy photosynthesis]
records: []
datasets: []
files: [dr1028_garciadecortazar2005.pdf (the 2026-10-28 requests drop)]
---

# Garcia de Cortazar-Atauri, Cordova & Pinto 2005: leaf angle, k and light in a Sultana overhead (parronal) canopy

Canopy structure, light climate and photosynthesis of table-grape Sultana on an overhead trellis at two stages, with a geometric light model. No record; it measures what a light piece needs (k, leaf angle, LAI by gap fraction) for a pergola.

## What it holds

- **Leaf angle** (l. 25, 83, 213, 217): protractor, 96 adult leaves at 10 and 30 cm above the trellis; mean inclination 63 deg at flowering, 57 deg in berry growth; classes 0-30, 30-60, 60-90 deg = 0.10, 0.29, 0.60 then 0.16, 0.37, 0.48. "Erectophile", about 60 deg (l. 25).
- **Extinction** (l. 233-240): kdir 0.480 and 0.493 at solar noon (sun over 67 deg); day averages 0.705 and 0.670; diffuse 0.700. "Corresponded to a spherical leaf angle distribution" (l. 739).
- **Transmittance and LAI** (l. 254, 237-238): Tdir 0.313, 0.356, 0.381 at 11:30, 12:30, 15:30 at flowering (LAI 2.10, 2.17, 2.00); LAI 2.1 and 4.5 by gap fraction inversion at the two stages. Adult leaf PFD transmittance 8.6 and 6.5 % (l. 211).
- **Model** (text, l. 192-193): sunlit fraction at height z is exp(-kdir LAIz); leaves random in azimuth.
- **Site** (l. 241): vines 3 x 3 m. Tdir measured about 13:30 with sun elevation about 70 deg (l. 78).
- **Not printed:** cultivar's row direction (none; overhead), a G-function, Campbell's x.

## Dependence

- **Computes** Bonhomme & Varlet-Grancher 1977 geometry and Norman & Campbell 1989 gap fraction. Shares no equation with the engine's models. Own data.

## Bearing

- The only grapevine k printed here separately for direct and diffuse light, but for a pergola, not a hedgerow.
- For a spherical G, k = 0.5/cos(zenith); at a 67 deg elevation sun this is 0.5/sin(67 deg) = 0.54, near the 0.48-0.49 measured (arithmetic, not printed).
