---
id: navarro2014
citation: Navarro, M., Davis, T.W., Villalba, G., Li, Y., Zhong, X., Erratt, N., Liang, X. & Liang, Y. 2014. Towards Long-Term Multi-Hop WSN Deployments for Environmental Monitoring: An Experimental Network Evaluation. Journal of Sensor and Actuator Networks 4:297-330 (as printed in the header; the DOI reads jsan3040297)
doi: 10.3390/jsan3040297
read: 2026-10-21, lightly: abstract, Table 1, Sections 3 (deployment), 4 (performance), 5 (costs) and 6 (conclusions); Section 2 and the protocol detail of 4.1-4.2 skimmed; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 28 of 28 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [USA, Pennsylvania, Allegheny County, Fox Chapel]
processes: [wireless sensor network, packet reception rate, routing protocol, battery life, maintenance cost, deployment cost, data loss]
records: []
datasets: []
files: [navarro2014.pdf (the 2026-10-21 drop)]
---

# Navarro et al. 2014: four years of a 52-node forest sensor network, its packet delivery, battery visits and costs

A multi-hop MicaZ and IRIS network in a Pennsylvania nature reserve (soil moisture, sap flow, air temperature and humidity), April 2010 to 2014, with a measured delivery rate under two routing protocols and a cost breakdown.

**Read this first.** Forest, not vineyard: tree canopy, 45 % of sunshine hours (l. 223), NiMH cells, multi-hop mesh. Costs are dollars, presumed US dollars (the text does not say), cumulative to May 2014. No placement test and no reduced-network test.

## What it holds

- **Delivery** (l. 47-48, 785): CTP gave 79 % packet reception rate and 96 % packet success rate, with 0.2 % duplicates; XMesh gave 36 % and 46 %, with 3 % to 4 % duplicates. Study periods: XMesh August 2011 to August 2012, CTP November 2013 to April 2014. Under XMesh, 50 % to 61 % near the base station and 15 % to 40 % farther out (l. 1141); under CTP some nodes near and far exceeded 90 % and some stayed low (l. 1144).
- **Network** (l. 304, 337): 40 motes by July 2010, 52 nodes and 253 sensors by April 2014 (104 onboard, 149 external).
- **Failures** (l. 332, 1097, 1109): hardware failures and battery depletions caused the gap between deployed and connected nodes; a gateway outage of about six days took a relay battery to near depletion; the internet-facing gateway had 175 unauthorized access attempts in year one.
- **Battery** (l. 280, 932, 976): rechargeable NiMH AA cells; about 58 days between battery changes per node, about two years of cell life. Measured in the field.
- **Maintenance** (l. 964, 1172): 154 field visits in four years, 128 of them to replace batteries; visits almost every 12 days.
- **Costs** (l. 52-54, 918, 922, 990, 1030, 1173; Table 7 to May 2014): deployment $31,500 (hardware $15,940, external sensors $12,600, power $1,500, enclosures $1,400, mounting $60); labour $23,900 and maintenance $5,000 to April 2014; about $155 labour and $32 maintenance, $187 in all, per visit; $184 per m2 of sensed area per year. Relay and sensor-carrying nodes differ by about $330 and $700 (l. 918).

## Dependence

- Commercial XMesh and the open-source Collection Tree Protocol are the two protocols compared. Related long-term deployments (redwood, Springbrook, GreenOrbs) are cited for comparison (l. 233-247). Extends the authors' PIMRC 2013 paper. No borrowed equations.

## Bearing (2026-10-21)

Node part of the sensor menu of D48.

- **Yield, failures, battery, maintenance:** the best long-run figures on offer for a mesh network: 79 % delivery with a good protocol, 36 % with a poor one, a battery visit every 12 days, 58 days per battery set. Measured over years, in a forest.
- **Radio range:** no link distances in the parts read (antenna 4.9 dBi); manufacturer-level only.
- **Costs:** dollars, to May 2014: $187 per visit and $600 a month for labour and maintenance can price the upkeep of a node count. Not shown: a LoRaWAN or vineyard node.
- **Kind of result:** a multi-year deployment study of one network, two protocol periods, no replicate.
