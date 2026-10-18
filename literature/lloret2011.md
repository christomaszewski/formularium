---
id: lloret2011
citation: Lloret, J., Bosch, I., Sendra, S. & Serrano, A. 2011. A wireless sensor network for vineyard monitoring that uses image processing. Sensors 11:6165-6196
doi: 10.3390/s110606165
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: [grapevine]
regions: [Spain]
processes: [wireless sensor network, image processing, leaf status, node design]
records: []
datasets: []
files: [jaime_2011.pdf (the 2026-10-18 drop)]
---

# Lloret et al. 2011: a vineyard wireless network with image processing in each node

Camera nodes on IEEE 802.11 hardware flag abnormal vine leaves and send a short alarm to a sink node (l. 32-36). It measures no weather and no wetness.

## What it holds

- **Aim:** detect an unusual leaf status, which may be deficiency, pest, disease or other harm; the system cannot tell these apart (l. 40-41).
- **Design:** radio coverage, camera field of view and a node-count estimate (l. 144-146); designed for flat fields or smooth hills (l. 294-295).
- **Test bed:** a flat vineyard in Spain (l. 40); site and year not found in the first pages.
- **Traffic:** a streamed camera needs 800 kbps, at most 30 cameras on 802.11g (l. 286-288); the system's mean traffic is 4.26 kbps (l. 1307), about 97% fewer bytes than a 4 Mbps stream (l. 1233).

## Dependence

- Builds on IEEE 802.11 access-point nodes and image-based leaf classification. No weather model.

## Bearing (2026-10-18)

- **s6 methods** (sensor-node design only): no temperature, humidity or wetness data, so nothing for a simulator to take. Not read in full.
