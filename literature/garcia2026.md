---
id: garcia2026
citation: García Bu Bucogen, G., Viale, M. & Impagliazzo, F. 2026. Fine-scale topoclimatic patterns and their implications for high-altitude vineyards. Cuadernos de Investigación Geográfica 52(1):153-174
doi: 10.18172/cig.7105
read: 2026-11-03, abstract and results (l. 440-535), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 2 of 2 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Argentina (Mendoza, high-altitude vineyard)]
processes: [topoclimate, cold-air pooling, frost, minimum temperature, chilling hours, sensor network]
records: []
datasets: []
files: [dr1103_garcia2026.pdf (the 2026-11-03 drop)]
---

# García Bu Bucogen et al. 2026: fine-scale temperatures in a 1430 to 1550 m Mendoza vineyard

Twelve air-temperature sensors and one weather station over two growing seasons in one Monasterio vineyard, with maps of thermal zones.

**Read this first.**
- The first author's surname is printed "García Bu Bucogen" (byline: Grethel García Bu Bucogen); it is written as printed. The JSON agreed.
- The minus signs are split across a line break in the extraction (l. 527-528: "around –" then "10 °C", "near –14 °C"); the values are read as about -10 and -14 °C.
- The "4 °C colder" is arithmetic from the two printed values, not a printed difference. No season or date of the minimum is given in the passage read.

## What it holds

- **Design:** twelve HOBO air temperature sensors across the vineyard plus one automatic weather station, October-March over two growing seasons (l. 33, 129, 214).
- **Growing-season spread:** mean maximum and minimum temperatures differed by up to 3.5 and 2.5 °C between sensors (l. 40, abstract).
- **Cold-air pooling:** lower sectors were prone to nocturnal cold-air pooling and frost (abstract, l. 38).
- **Depression sensor:** sensors 10, 11, 14 and 18 recorded absolute minima around -10 °C, while sensor 13 reached an absolute Tmin near -14 °C, which the authors read as cold-air pooling in a topographic depression (l. 527-528). About 4 °C colder (arithmetic).
- **Chilling hours:** about 2000 h at sensors 10, 11 and 13 on gentle slopes (<7°), about 1700 h across all sensors (l. 524-526, passage read, not quoted).

## Dependence

- Own sensor data; regression maps made in SAGA. The data are not stated to be open in the part read.

## Bearing (2026-11-03)

- **micro.coldpool_max_c (4):** one depression sensor about 4 °C colder than neighbours on the absolute minimum, in a high-altitude vineyard. This is the same size as the assumed cap, as a single extreme-event value; it is not the deficit on a typical clear calm night.
- **micro.coldpool_c_per_m (0.6):** no depth of the depression is printed in the part read, so no per-metre value.
- **Kind of evidence:** field observation, one vineyard, sensors in situ.
