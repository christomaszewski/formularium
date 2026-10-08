---
id: magarey1991
citation: Magarey, P. A., Wachtel, M. F., Weir, P. C. & Seem, R. C. 1991. A computer-based simulator for rational management of grapevine downy mildew (Plasmopara viticola). Plant Protection Quarterly 6(1):29-33
read: 2026-10-08, the incubation model and the reference list; open access
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [South Australia]
processes: [incubation, primary infection, sporulation, survival]
records: []
datasets: []
files: []
---

# Magarey et al. 1991: the Australian downy mildew simulator

From the South Australian Department of Agriculture (Loxton) and NYSAES, Cornell.

## What it holds

- A simulator of models, one per phase of the life cycle, "compiled mainly from European
  literature", run on 10-minute weather.
- **Incubation:** y = 42.0 - 3.6x + 0.1x² - 0.0005x³, y in days and x the mean
  temperature (°C), operative between 8 and 35 °C, accumulated each 10 minutes after
  infection. "The polynomial was derived from data from Muller and Sleumer (1934), Zachos
  (1959) and Rafaila et al. (1968), and incorporated modifications by Magarey and Wachtel
  (unpublished data)". Initial predictions use 34 years of median daily temperatures at
  Loxton.
- The paper calls the incubation model "a most important component" for spray timing.

## Dependence

- The incubation cubic shares data with [zachos1959](zachos1959.md) and
  [rafaila1968](rafaila1968.md), and with Müller & Sleumer 1934.
- Authors: P. A. Magarey (Magarey's 2010 fact sheet, a model Cooptera shows; Kennelly
  2007's trigger) and Seem (Kennelly 2007): flags.
- Cooptera's `magarey2010.rules` computes no incubation curve, only the fact sheet's 5-day
  lower bound, so nothing Cooptera runs is this cubic (Cooptera, 2026-10-08).

## Bearing (2026-10-08)

- Its incubation is not a candidate beside Zachos or Rafaila (shared data), and its
  polynomial form is Rossi's, so a Rossi truth would hold it out by structure.
- It is the source that led to Zachos 1959 and Rafaila et al. 1968.
