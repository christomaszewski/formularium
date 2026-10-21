---
id: pfender2011
citation: Pfender, W. F., Gent, D. H., Mahaffee, W. F., Coop, L. B. & Fox, A. D. 2011. Decision aids for multiple-decision disease management as affected by weather input errors. Phytopathology 101:644-653
doi: 10.1094/PHYTO-05-10-0131
read: 2026-10-21, in full (introduction, multi-decision DSS characteristics, Monte Carlo design, hop powdery mildew index, stem rust simulation, summary; references not read), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 43 of 43 quotes found at their lines by scripts/verify_quotes.py; Figures 1-3 not read (values only in figures)
status: read
diseases: [hop powdery mildew, perennial ryegrass stem rust]
crops: [hop, perennial ryegrass]
regions: [USA, Oregon, Willamette Valley]
processes: [weather input error, bias, virtual weather, decision support, Monte Carlo, spray decision, hop powdery mildew index, stem rust simulation]
records: []
datasets: []
files: [pfender2011.pdf (the 2026-10-21 drop)]
---

# Pfender et al. 2011: how bias and noise in the temperature input change a disease model's spray decisions

Degrades a clean hourly temperature series with set bias and variance, runs two spray decision aids on each version, and scores the season's decisions by their effect on an epidemic simulated with the true weather. No record.

**Read this first.** The economic result (AUDPC for days 160-180 and disease-related costs of the 90 simulations) is in Figure 3 only, and its values were not read (l. 358, 392, 398). The on-site series is treated as error-free (l. 196). The authors call the design "not intended to be exhaustive, nor definitive" (l. 207-208). Table 1 row labels are split across lines; the Table 2 numbers below come from the text layer. The temperature errors are drawn as independent half-day multipliers, with no spatial structure.

## What it holds

- **Accuracy defined by decisions** (l. 80): for a multi-decision aid, accuracy is choosing the season-long set of actions that minimises disease-related costs (management cost plus yield loss). Bias may be uniform or asymmetric (l. 68); unbiased random error lowers precision without a direction (l. 79).
- **Error levels** (l. 215-219, 222): from the hourly estimate errors of a virtual-weather service at three Willamette Valley sites, observed minus estimated was about normal, with a mean difference of -0.7 to +0.9 degC and an SD of 1.5 to 6.1 degC. The authors chose bias -1 to +1 degC and SD 2 to 8 degC. The error was neither strictly systematic nor random, since the diurnal shape of the estimates followed actual temperatures.
- **Degradation design** (l. 196, 206; algorithm l. 227-247): original data are hourly air temperature at 1.5 m above grass from a datalogger. A season-long mean bias per hour of day is added, then a random multiplier per half-day is drawn from a normal distribution and applied to the hourly differences, tuned until the season's differences have the target mean and SD. Nine bias-by-SD types, 10 realizations each, give 90 degraded series.
- **Hop powdery mildew index** (Box 1; l. 257, 260, 263, 246): hourly rules add or subtract points (more than six continuous hours above 30 degC subtracts 20; six hours between 16 and 27 degC adds 20), and bands 0-30, 40-60, 70-100 mean low, moderate, high risk. On the original data it recommended 10 fungicide applications. Growers using it made 1.2 fewer applications per season than non-users (l. 229, cited from Mahaffee et al. 2003).
- **Hop index under error** (l. 248, 271, 273, 274): outputs were relatively insensitive to a bias of the size tested. Variability mattered more than bias, and the effect grew with SD from 4 to 8 degC. At SD 2 degC and bias about 1 degC the application count changed by 0.3 or less; at SD 8 degC the mean count fell by 1.9 to 2.5, with a mean absolute index difference above 30.
- **Stem rust simulation** (Box 2; l. 303, 307, 327, 328, 426): a daily-step simulation for perennial ryegrass seed crops. On original data it prescribed three applications, on days of year 118, 126 and 141. At bias 0 and SD 8 degC the first, second and third spray dates averaged 115, 133 and 161, the third ranging 149-172 (l. 433); at bias +1 degC and SD 8 degC the count ranged 2-4 and the third spray 144-177 (l. 434). The spray dates spread wider with the noisiest inputs (l. 343).
- **Scoring** (l. 353, 358): spray decisions from degraded data are applied to an epidemic simulated with the true weather, in 90 simulations, so the outcome is that of using the aid. Reference is the aid run on the original data.
- **Conclusion** (l. 392, 398, 406, 449, 452): bias of +/-1 degC with low variance had little effect on economic outcomes; mean disease and cost did not differ greatly from the clean case for any degraded type; variance changed outcomes more than bias over the tested ranges. The authors expect larger effects for moisture-driven models than temperature-driven ones (l. 113), since moisture is estimated less accurately (l. 112).

## Dependence

- Stem rust model: Pfender (2001, 2003, 2004, 2009) and Pfender & Eynard (2009), fitted to field and controlled-environment experiments (l. 307, cited); five-year evaluation in Pfender et al. (2009) (l. 313, 318: a more favourable outcome than standard practice in 7 of 10 location-years, cited). Hop index: a Gubler-Thomas-type index modified for hop, as used by growers (Mahaffee et al. 2003). Error rates and the evaluation tool come from Coop et al. (2009) (l. 205, cited). A shared author with other disease-model papers is only a flag.

## Bearing (2026-10-21)

For Agrarium's D48 study: the decision-focused method and the scoring of weather inputs. This is the closest worked case found of scoring weather inputs by their effect on spray decisions, not by weather error.

- **Takeable:** the design. Degrade the true series with set bias and SD (here 3 bias levels by 3 SD levels, 10 draws each, 90 series), run the decision rule on each, apply the decisions to an epidemic simulated with the true weather, and score decisions and cost against the clean run. This maps onto scoring a placement or a virtual-weather source by the sprays it would trigger. Finding: "variance mattered more than bias", over a bias of +/-1 degC.
- **Takeable:** how error ranges are set, from the observed difference between estimated and observed hourly temperature at three sites (mean -0.7 to +0.9 degC, SD 1.5 to 6.1 degC), as a ready range for a gridded or virtual source.
- **Not shown:** any sensor placement, any spatial covariance, any value-of-information calculation, a regret measure, a held-out check, or any moisture variable (temperature only; leaf wetness and rain were not degraded in the text read). The kind of result is a simulation study of two models, with the economic outcome in a figure not read.
