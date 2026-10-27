---
id: ramanathan2006
citation: Ramanathan, N., Balzano, L., Burt, M., Estrin, D., Harmon, T., Harvey, C., Jay, J., Kohler, E., Rothenberg, S. & Srivastava, M. 2006. Rapid Deployment with Confidence: Calibration and Fault Detection in Environmental Sensor Networks. UCLA Technical Report, eScholarship (uc/item/8v26b5qh)
doi: 
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: []
regions: [Bangladesh]
processes: [sensor calibration, fault detection, rapid deployment, ion-selective electrodes, groundwater arsenic monitoring]
records: []
datasets: []
files: [ramanathan2006.pdf (the 2026-10-25 other-sources drop)]
---

# Ramanathan et al. 2006: calibration and fault rules for a rapid water-sensor deployment

A field report from a 12-day deployment of 48 water-quality sensor nodes in Bangladesh rice paddies, with ion-selective electrode calibration and five rules that flag faulty readings.

## What it holds

- **Deployment:** 48 sensors over 12 days in January 2006, about 25 000 measurements (l. 65-67),
  for a study of arsenic in groundwater.
- **Calibration:** ion-selective electrodes, with a regression kept only where R2 exceeds 0.97
  (l. 438-439); a Nernst-type temperature term (l. 222, 286). Pre-deployment calibration is
  described at l. 115-134.
- **Fault rules:** five rules run on every point (l. 577). NOISE flags 1 % of points, INVALID
  NLDR 11 % (l. 576, 588), BROKEN 12 % (l. 619) and SHORT 26 % (l. 640). Together they flag
  almost 40 % of the data points (l. 106).
- **Validity:** the authors say there is no ground truth, so the flags are not checked against
  true values (l. 135-138).

## Dependence

- **Builds on** the Nernst equation for electrode temperature correction (l. 222, 286), the
  NIMS sensor set-up of the CENS deployments (l. 174-188) and the TDR soil probes (l. 368-369), and expert rules for faulty
  data (l. 566-577).

## Bearing (2026-10-26)

- classes.tsv names no search for this key. A growers' decision engine could take the rule set
  as a first filter on sensor feeds, but the rule parameters were chosen for these probes, and
  the paper gives no error figures against truth.
- The sensors are water and soil probes, not vineyard weather sensors. The paper was not read
  in full.
