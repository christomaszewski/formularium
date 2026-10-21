---
id: kleinhaneveld2007
citation: Klein Haneveld, P. 2007. Evading Murphy: a sensor network deployment in precision agriculture. Report, Technical University of Delft, 28 June 2007 (as printed; no series or number)
doi:
read: 2026-10-21, lightly: abstract, sections 1-7 (2006 deployment, range, sensors, results, conclusions), figures by caption and printed values only; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [phytophthora]
crops: [potato]
regions: [Netherlands (inferred: Delft and Wageningen are named; the country is not printed)]
processes: [wireless sensor network, data loss, packet delivery, battery life, radio range, sensor failure, gateway power, air temperature, relative humidity]
records: []
datasets: []
files: [kleinhaneveld2007.pdf (the 2026-10-21 drop)]
---

# Klein Haneveld 2007: a 26-node potato-field network that delivered 51 % of its messages in its second year

A single-author project report on the 2006 LOFAR Agro deployment of temperature and humidity nodes in a potato field, with the causes of data loss.

**Read this first.** Potato, not grapevine, and a Mica2-class node of 2006. Per-node rates are in figures only. "Normalised" rates are the share of messages expected from the sampling schedule, corrected for broken sensors and for the gateway's night shutdown by the author's own method.

## What it holds

- **Yield** (l. 14, 20-21, 562): in 2005, 97 nodes gave 5874 messages in three weeks, 2 % of those generated; in 2006, about 51 % of expected. Over 2.5 million measurements are in the database (l. 562).
- **Per node** (l. 289, 294-296, 359): over about two months, 26 nodes operating continuously, the normalised message rate was 79 % for the first 10 nodes and 49 % for all nodes together; with the daytime correction 92 % for the first 10 nodes (+13 points). Node 26 sent 6 messages (l. 296).
- **Failures** (l. 256, 266, 354, 360, 572): the sensor, shielded only by a small cap, is the most vulnerable part; a broken sensor slows the node by a factor of three. From 14 August the gateway switched off every night because its solar panels could not keep it on. Broken sensors and gateway downtime are the two main causes of loss in 2006. The 2005 problems (night battery drain, spontaneous resets) are cited from Langendoen et al. 2006 (l. 84, 86).
- **Range** (l. 201, 206, 214, 219, 228): no reception beyond 5 m at first, caused by a debug RSSI setting; about 40 m after it was removed. A multihop application (installed 14 September) gave no messages from multihop nodes after one day; only single-hop nodes worked.
- **Weather** (l. 479, 481): the sink received around 60 % of expected messages in a humid spell and above 70 % in the dry part of September.
- **Battery** (l. 540): most single-hop nodes ran more than two months on one battery.

## Dependence

- Follow-up to Langendoen, Baggio and Visser (2006), "Murphy loves potatoes", the source of the 2005 problem list (l. 81-84). Built on T-MAC, MintRoute and Deluge (Deluge dropped in 2006). None of the numbers above is borrowed.

## Bearing (2026-10-21)

Node part of the sensor menu of D48.

- **Data yield and failures:** 51 % of expected messages for a 26-node field network (79 % to 92 % for the best 10 nodes), with named causes: broken sensors, a gateway that shut down at night, and single-hop range of about 40 m. Usable as an upper bound on how bad node loss was for an early research network, not for a current LoRaWAN node.
- **Battery:** measured, more than two months on one battery (l. 540). Solar life of the gateway was not enough at night. Maintenance: sensor replacement implied; no visit count or interval printed.
- **Radio range:** about 40 m single hop (measured); multihop failed.
- **Costs:** none printed.
- **Kind of result:** a field deployment report, one potato field, one summer, no replicate network and no baseline.
