---
id: lessio2014
citation: Lessio, F., Portaluri, A., Paparella, F. & Alma, A. 2014. A mathematical model of flavescence dorée epidemiology. arXiv:1407.4003 (preprint)
doi: 10.48550/arXiv.1407.4003
read: 2026-10-20, LIGHT, by a reading agent (claude-haiku-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [flavescence dorée]
crops: [grapevine]
regions: [Piedmont, Cuneo]
processes: [epidemic model, roguing, latency, recovery]
records: []
datasets: []
files: [lessio_2014.pdf (the 2026-10-20 drop)]
---

# Lessio et al. 2014: a compartment model of flavescence dorée with roguing

A healthy-latent-infected-young compartment model of flavescence dorée in a vineyard with
yearly replacement of infected vines, its parameters from the literature and a visual fit to
four years of counts from one vineyard near Cuneo.

## What it holds

- Model: four compartments (healthy S, latent L, infected I, young G) at density D; farmer
  replacement at intervention time tau (Eq 3, l. 271-280; rendered p. 6). Infection q S (I +
  epsilon)^2 (Eq 2, l. 189-203). A linear variant qhat S I is tested (Eq 10, l. 740).
- Parameters (Table 1, rendered p. 5): tau = 1 year (law, DM 32442/2000); D 2000 to 11000
  plants/ha; q = 1e-6 (1e-7 to 1e-5) ha^2 plants^-2 per year (l. 193).
- Rates: k1 = 0.4 per year, recovery 2 to 3 years (ref 10, l. 213); k2 = 1/3 per year,
  latency about 3 years (refs 2, 3, l. 245); k4 = 1/5 per year, aging (ref 3, l. 269); k3 =
  0.1 per year unmanaged (authors' estimate, l. 557).
- Non-dimensional constants c1 = 0.4, c2 = 1/3, c3 = 1, c4 = 1/5 (l. 431). Linear variant
  qhat 1e-3 to 1e-2 ha plants^-1 per year (l. 793).
- Fit: a 0.475 ha vineyard near Cuneo, D = 3000 per ha, counts of infected and symptomless
  plants 2009 to 2012, no treatments (l. 939-941). q about 1e-6 gives a reasonable fit from
  2009; about 1e-5 fits better from 2008; 1e-7 needs unrealistic epsilon (l. 958-961). The
  fit is visual; epsilon values appear only in the plot.
- Hotbeds: epsilon decays with distance (ref 13, l. 205).
- Table 2 (not fitted): first reports and epidemic starts by region (Piemonte 1998, ref 3,
  l. 823).

## Dependence

- Rates from cited studies (recovery, latency, ageing); the infection rate q chosen by eye
  against one vineyard's 2009-2012 counts. A preprint.

## Bearing (2026-10-20)

- For a vector-borne disease in Agrarium (not planned): yearly rates (recovery 0.4, latency
  1/3, ageing 1/5 a year) and a quadratic infection term; a frame, not a fitted model.
