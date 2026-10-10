---
id: lopezfrias2009
citation: López Frías, Ramón, Rodríguez de Acuña Pego, Fernando, Trujillo García, Eugenia & Perera González, Santiago. 2009. Validación del modelo predictivo de mildiu Goidanich en viña en cinco comarcas vitícolas de Tenerife (campaña 2009). Technical report, Cabildo Insular de Tenerife (inferred; no publisher line)
doi:
read: 2026-10-09, in full (Spanish, 9 pages), by a reading agent (claude-haiku-5-5), Tabla 1 read from the page image at 300 dpi; 42 quotes checked by scripts/verify_quotes.py; Tabla 1 compared row by row with Cooptera's incubation.py by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Canary Islands]
processes: [primary infection, incubation, validation, forecasting]
records: [goidanich.incubation]
datasets: []
files: [tenerife-goidanich-viti246.pdf]
---

# López Frías et al. 2009: Goidanich's table checked in five Tenerife vineyards

## What it holds

- **Model:** the Cabildo's Goidanich programme.
  - **Trigger:** about 10 °C, shoots of 10 cm, about 10 l/m² of rain in a day.
  - **Incubation:** counted from the day after the rain with Tabla 1's daily development by
    mean temperature and mean RH, summed to 100.
  - Neither Goidanich nor Baldacci is cited.
- **Tabla 1:** 12.00-25.00 °C in 0.25 °C steps, with RH below and above 75 %. The note says
  development is constant above 25 °C.
  - It is identical, all 53 rows of both columns, to the engine's table as Porras Soriano
    2006 prints it (Cooptera's `incubation.py`, compared 2026-10-09). That includes the
    non-monotonic humid value at 18.25 °C (15.20 after 15.30).
- **Plots:** Orotava, Icod, Santa Úrsula, Güímar and Arico, with stations at 340-725 m. The
  Cabildo has 41 stations in 18 municipalities.
- **2009 dates:**

  | Plot | Index reached | Oil spots |
  |---|---|---|
  | Orotava | 106.75 on 8 May | 5 May |
  | Santa Úrsula | 108.4 on 11 April | 15 April |
  | Güímar | 107.9 on 6 April | 7 April, fruiting 11 April |
  | Icod | over 100 on 8 May | one day after; fruiting 22 May |
  | Arico | none | no symptoms |

- **Result:** four of five plots matched; no statistics. In 2008 three northern plots
  matched and the southern one did not.
- **Observation effort** rose when the index reached 70-80 %, so the observed dates depend
  partly on the model.

## Dependence

- Computes Goidanich's table in the Spanish version the engine uses (`goidanich.incubation`):
  kin to it by definition.

## Bearing (2026-10-09)

- **Confirms the engine's transcription:** Porras Soriano's table is the version circulating
  in Spain, printed identically in Tenerife. Its derivation from Goidanich et al. 1957's
  data is not shown here either.
- A small subtropical-oceanic pattern of first symptoms at altitude, model-assisted.
