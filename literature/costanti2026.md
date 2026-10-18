---
id: costanti2026
citation: Costanti, F., Cappelli, I., Bianchini, M. & Fort, A. 2026. Spatio-temporal graph autoencoder for sensor data reconstruction in vineyard microclimate monitoring. Sensors 26:4368
doi: 10.3390/s26144368
read: 2026-10-18, LIGHT, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 26 of 26 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Italy, Tuscany, Siena]
processes: [sensor network, missing data, gap filling, reconstruction, graph neural network, air temperature, relative humidity]
records: []
datasets: [costanti2026.siena_five_nodes]
files: [filippo_2026.pdf (the 2026-10-18 drop)]
---

# Costanti et al. 2026: reconstructing missing vineyard sensor data with a graph autoencoder

Five LoRaWAN nodes in a Siena vineyard, and a model that fills masked temperature and humidity readings from the node's own history and its two nearest neighbours. No record: a gap-filling method, not a formulation of disease or weather.

## What it holds

- **Network** (l. 239-283): five battery-powered nodes with a Sensirion SHT30 (air temperature and relative humidity), light sensors, resistive leaf-wetness probes and a tipping-bucket rain gauge; at the Istituto Tecnico Agrario B. Ricasoli, Siena; inter-node distance under 500 m, slightly different elevation and exposure. No coordinates or pair distances printed. SHT30 nominal accuracy about +/-0.2 C and +/-2 % RH (authors, from the datasheet; l. 925). Leaf wetness and rain are collected but not analysed.
- **Data** (l. 268-269, 537-542): July 2023 to May 2025, nominal 5-min sampling with irregular LoRaWAN timestamps mapped to a common grid; raw missing rate about 10 % across nodes from communication and hardware failures; no per-node rate or outage duration.
- **Cross-node structure** (l. 280, 900-908, 1047): temperature is coherent across nodes (coherence above 0.9) and more uniformly correlated than humidity; daily relative humidity fluctuates about 2.5 times as much as temperature (normalised). No spread values or coefficients printed.
- **Model** (l. 317-460, 574-620, 669-695): GRU encoder with GRU-D-style time-decay imputation toward month-hour means, GraphSAGE over a 2-nearest-neighbour static graph, GRU decoder; loss 0.6 MAE + 0.4 (1 - mean Pearson r); latent 128, 2 GRU and 2 GNN layers, learning rate 2e-4, batch 32; sentinel -4.0 for missing inputs; training corruption 0.5; windows 36 steps (3 h) and 144 (12 h). Split in time, 50 / 20 / 30 % (train 88,582, validation 1149, test 1495 windows at 36 steps).
- **Reconstruction error** (Tables 3 and 5; l. 796-799, 987): at 36 steps, corruption 0.3: temperature MAE 0.022 C, relative humidity 0.095 % RH; corruption 0.9: 0.133 C and 0.425 % RH (144 steps: 0.226 C and 0.783 %). At corruption 0.9, linear interpolation gives 0.627 C and 2.093 % RH, forward fill 0.785 C and 2.598 %. Without the graph module, the loss on a fully masked node rises to 0.174 (temperature) and 0.156 (humidity) from 0.022 and 0.025 (l. 967). Ten-run sd about 0.0002 to 0.0004 in loss.
- **Data:** on request from the authors; no repository, licence or coordinates (l. 1159).

## Contradiction carried, not resolved

The abstract says two years of data; the dates given (July 2023 to May 2025, l. 268) are about 23 months. Other small differences are rounding (0.095 % in Table 3 and 0.1 % in the abstract) or different settings (Tables 2 and 3), not conflicts. The ablation table rows were not parsed; only the text values are recorded.

## Dependence

- Standard components (GRU, GRU-D imputation idea, GraphSAGE, Pearson loss). No model computed by another paper, no shared calibration. The sensor platform is the authors' own earlier work (refs 7, 17, 23, 27).

## Bearing (2026-10-18)

Strand 5 (sensor error) and strand 4 (microclimate):

- **Failure, gaps:** a field figure for a vineyard sensor network of about 10 % missing readings, from radio and hardware faults. A sensor-error model in Agrarium can draw dropouts at that rate, and a sweep can test how much a gap-filling step (here an error of 0.02 to 0.13 C, far under the sensors' own 0.2 C) changes a threshold count; linear interpolation was 5 times worse at heavy loss.
- **Placement:** with nodes under 500 m apart, temperature is nearly redundant between nodes (coherence above 0.9) and humidity is not, so neighbours can stand in for a failed node for temperature more safely than for humidity. This supports spreading humidity or wetness sensors over more positions than temperature sensors.
- **Limits:** one site, 5 nodes; reconstruction was tested on artificially masked data (random corruption), not on real outages; leaf wetness untouched.
