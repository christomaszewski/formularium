---
id: puelles2020
citation: Puelles Ruiz de Gopegui, Miguel. 2020. Evaluación de diferentes estrategias "en agricultura ecológica" en el control de mildiu en viña. Trabajo Fin de Grado (Grado en Enología), Universidad de La Rioja, Logroño, 8 September 2020
doi:
read: 2026-10-09, in full in an OCR (tesseract, Spanish) of the scan, by a reading agent (claude-haiku-5-5), Tabla 1 cross-checked against López Frías et al. 2009's image; 59 quotes checked by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [La Rioja]
processes: [oospores, infection, incubation, sporulation, spray timing, organic control]
records: [goidanich.incubation]
datasets: []
files: [rioja_mildiu_sostenible_2020.pdf]
---

# Puelles Ruiz de Gopegui 2020: a bachelor's thesis with the UR model's first rules

From the same department as [puelles2024](puelles2024.md), by its first author.

## What it holds

- **Model:** Goidanich's daily development (Tabla 1, RH split at 75 %) summed to 100;
  incubation 7-14 days. The OCR garbles four cells of the table; the scan agrees with
  López Frías et al. 2009 ([lopezfrias2009](lopezfrias2009.md)).
- **Modifications** (the rules later published as the UR model):
  - oospores mature at 140 °C·days from 1 January;
  - secondary infection at 50 °C·h;
  - sporulation after 4 h dark at T > 12 °C and RH > 95 %;
  - spores die after 6 h above 30 °C.
- **Trial (2019):** one Logroño campus plot of Tempranillo on 110 R, five treatments, four
  sprays timed by the model (5, 14 and 26 June, 18 July). Assessed on 26 June and 31 July,
  50 clusters a replicate.
- **Incidence (Table 5):**

  | Treatment | Incidence | Attack grade |
  |---|---|---|
  | unpruned control | 6.5 % | 2.4 |
  | control | 4.55 % (abstract: 4.50) | 1.4 |
  | conventional | 2.5 % | 0.6 |
  | IdaiNature | 2.0 % | 0.4 |
  | Agrichem | 1.0 % | 0.2 |

  Significance is given as letters only.
- 2019 was hot with very low disease pressure; sprinkling was used to raise it.
- **Printed slip:** IdaiNature's copper "with 4 applications" (652.8 g/ha) equals one
  application's.

## Dependence

- Computes Goidanich's table in the Spanish version (`goidanich.incubation`). Its added rules
  are those of `puelles2024.ur`.
- Spray timing followed the model, so the observed incidence partly reflects the model's
  output.

## Bearing (2026-10-09)

- An early, smaller form of the engine's UR model. It adds nothing a truth could use
  independently.
