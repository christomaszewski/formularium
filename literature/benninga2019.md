---
id: benninga2019
citation: Benninga, Harm-Jan F., van der Velde, Rogier & Su, Zhongbo. 2019. Impacts of Radiometric Uncertainty and Weather-Related Surface Conditions on Soil Moisture Retrievals with Sentinel-1. Remote Sensing 11:2025 (article number; 28 pages)
doi: 10.3390/rs11172025
read: 2026-10-08, the first pages and abstract, by a triage agent; header checked by the main session; section 4.2.4 and the dew passage of the discussion, 2026-11-05, by the main session
status: read
diseases: []
crops: []
regions: [Netherlands]
processes: [sensor error]
records: []
datasets: []
files: [10-3390-rs11172025.pdf]
---

# Benninga et al. 2019: Sentinel-1 radiometric uncertainty

Research article, Twente, eastern Netherlands (five forests, five meadows, five cultivated fields).

## What it holds

- Estimates Sentinel-1 radiometric uncertainty (0.85 dB at 0.25 ha to 0.30 dB at 10 ha for VV, roughly inverse square root of area) and masking rules for frozen conditions, snow and intercepted rain (>1.8 mm in the preceding 12 h) over forests, meadows and fields.
- It then propagates them to soil moisture retrieval error; this is a sensor-error law in generic form, not vineyard or disease content.

## Dependence

- No formulation of its own that a tool could run.
- No author of a model the engine runs.

## Bearing (2026-10-08)

- A generic radar error law; Agrarium's satellite operator (M2) uses optical sensors first. Little.

## Dew (2026-11-05, for hunt test H9)

The first reading stopped at the abstract's error law. This finding bears on sensing leaf wetness.

- **No systematic dew effect on Sentinel-1 (section 4.2.4):** "We could not find a systematic effect of dew on the Sentinel-1 σ0
  observations, so we do not mask them for dew." Dew was not measured: relative humidity above 90 % at wind under 2.5 m/s on
  morning passes stood in for it. Forests, meadows and cultivated fields, not vines.
- **Rain is different:** σ0 is affected by intercepted rain but seems unaffected by dew. Dew deposits are typically 0.1-0.3 mm a night,
  against about 2 mm of interception storage for a dense forest (the storage figure is forest only).
- **Earlier C-band work disagrees, as Benninga cites it** (`memory` for the originals): Gillespie found a rise with dew; Riedel a fall of
  0.5-2 dB in VV and VH. No general conclusion can be drawn on frequency, angle and polarisation.
- **Scale:** the 0.85 dB uncertainty at 0.25 ha is about the size of those effects, and 0.25 ha is a 50 m window.
