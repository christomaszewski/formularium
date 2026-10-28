---
id: launay2020
citation: Launay, M., Zurfluh, O., Huard, F., Buis, S., Bourgeois, G., Caubel, J., Huber, L. & Bancal, M.-O. 2020. Robustness of crop disease response to climate change signal under modeling uncertainties. Agricultural Systems 178:102733 (HAL author manuscript hal-02885029)
doi: 10.1016/j.agsy.2019.102733
read: 2026-10-27, lightly: abstract, sections 2.1-2.5 (climate data, leaf wetness and infection models, indicators), the results summary on model combinations and the discussion of uncertainty, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 12 of 12 quotes found at their lines by scripts/verify_quotes.py; HAL author manuscript (open), not the journal's typeset version
status: read
diseases: [wheat leaf rust, Puccinia triticina]
crops: [wheat]
regions: [France, Estrees-Mons, Versailles, Bordeaux]
processes: [climate change impact, regional climate model, quantile mapping, hourly disaggregation, leaf wetness model, infection model, multimodel uncertainty, dew point]
records: []
datasets: []
files: [syn1027_launay2020.pdf (the 2026-10-27 drop)]
---

# Launay et al. 2020: six leaf wetness and infection model combinations for wheat leaf rust on hourly weather built from regional climate output

Hourly weather is built from daily output of one regional climate model (quantile-mapped, then disaggregated to hours); two leaf wetness models and three infection models are crossed, and their trends for 1950-2100 at three French sites compared. No record: a model-uncertainty study.

**Read this first.** The hourly weather is synthetic and no step of it is checked against observed hourly RH in what was read; the study compares model combinations with each other, not with observed disease or with a run on observed weather. The hourly chain is described in Launay et al. 2014, which was not obtained. Regional models disagree even on the sign of the change in summer rain (l. 726).

## What it holds

- **Climate input** (l. 206-221): ALADIN-Climat nested in ARPEGE-Climat, RCP 4.5 and 8.5, 1950-2100 (periods 1976-2005, 2021-2050 and 2070-2099), at three sites: Estrees-Mons, Versailles and Bordeaux. Daily output is quantile-mapped to site observations (Deque 2007; l. 215).
- **Hourly chain** (l. 221-235): the climate model gives daily temperature, RH and rain. Hourly temperature is a sinusoid between daily extremes; daily rain is disaggregated by a latent-Gaussian process (Allcroft and Glasbey 2003); RH is estimated "from vapor pressure values deduced from hourly air and dew point temperatures" (l. 235). The dew point step is not described in the text read.
- **Wetness and infection models** (l. 259-265, 270-387): MEDHI, an hourly decision tree on RH (thresholds fitted by optimisation), rain and the previous wetness state, so it consumes the synthetic RH hours; and Plata, a physical one-layer energy balance. Infection by Pope, ClimInfeR or Magarey (minimum wetness 5 h to reach 5 % infection, l. 370), fed with daily wetness durations and mean temperature during wetness (l. 385-387).
- **Spread from the models** (l. 511-523): mean annual days with infection efficiency above 5 % (NID5) are 3.7 with Magarey, 11.7 with Pope and 14.1 with ClimInfeR (l. 511); 9.0 with MEDHI and 10.6 with Plata (l. 513); "up to fourfold" between combinations, while the global infection risk varies by about 10 % (l. 523). The abstract says absolute values vary with the model combination "even more than" between present and future (l. 85).
- **Caution on climate-model rain** (l. 726): ALADIN-Climat gives a summer reduction of 0.38 mm per day and WRF an increase of 0.32 mm per day in France over the century (as cited from Jouzel et al. 2014).
- **Humidity statistics checked:** none on the synthetic hourly RH (hours at or above 90 %, dew point, daily cycle and monthly means all absent from what was read); no run on observed weather to compare with.

## Dependence

- Hourly chain of Launay et al. 2014 (not obtained); quantile mapping of Deque 2007; infection models of de Vallavieille-Pope et al. 1995, Launay et al. 2014 (ClimInfeR, shared author) and Magarey et al. 2005; MEDHI of Launay et al. 2014.

## Bearing (2026-10-27)

- **D45:** not a check on humid hours. It strengthens the gap: published disease studies use hourly RH made from daily climate output without scoring it, and the wetness model (MEDHI) is a threshold on exactly that RH.
- **D60:** supports "several physical models per gap" and per-model reporting: the choice of wetness model and infection model moves infection days up to fourfold, more than the climate signal, so conclusions on synthetic inputs should be stated per model combination. The quantile-map-then-disaggregate chain is a template; its hourly RH step is the unchecked part.
- **Not shown:** whether the synthetic hourly RH reproduces observed hours at or above 90 %; any comparison of infection days on synthetic against observed weather; any vineyard disease.
