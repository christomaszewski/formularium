---
id: benavente2010
citation: Benavente, J. C. C. 2010. Monitoramento ambiental de vinhedos utilizando uma rede de sensores sem fio que coleta dados com um intervalo de amostragem variável. Dissertação (Mestrado), Escola Politécnica, Universidade de São Paulo, 177 p.
doi: not printed
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: [grapevine]
regions: [Bento Gonçalves, Rio Grande do Sul, Brazil]
processes: [wireless sensor network, vineyard microclimate, canopy-height gradient, sensor board variability]
records: []
datasets: []
files: [juan_2011.pdf (the 2026-10-18 drop)]
---

# Benavente 2010: a vineyard wireless sensor network with variable sampling interval

A Portuguese master's thesis (USP, supervisor Cugnasca) on MICAz motes with a self-chosen sampling interval, tested in a plastic-covered vineyard at Bento Gonçalves; the record's year (2010) and title are right, the author is printed "Juan Carlos Congona Benavente". Network engineering first; the microclimate data are a by-product.

## What it holds

- **Network:** ten nodes (nine MICAz with MTS400, one with MTS420) and a MIB520 base station (l. 2959-2961); 5 min sampling, 0 dBm; runs of 135 h at canopy height and 164 h at cluster height (l. 2968-2971). Slope about 15 degrees, rows 3.00 m apart (l. 2964-2966).
- **Heights:** cluster 1.85 m and canopy 2.10 m above ground (l. 2950, 2962); a third position above the canopy in the microclimate run (l. 3039).
- **Microclimate run:** 40 h of RH, temperature and light on 3 to 5 February 2010 (l. 4934). RH above the canopy was on average 5 % higher than at canopy height at night and 24 % lower by day (l. 5048-5050); cluster RH was 2 % higher at night and 10 % higher by day than canopy RH (l. 5054-5055).
- **Sensor variability:** an adjustment factor between the sensor boards of the nodes is applied to T and RH (Table 6, l. 4936-4937). No leaf-wetness measurement and no drift or failure rate was found; the only leaf-wetness sensor named is a commercial listing (eS1301, l. 2194).

## Dependence

- MICAz/TinyOS motes, XMesh, Sensirion SHT11 and Intersema sensors (l. 3742); no earlier microclimate dataset is the data.

## Bearing (2026-10-18)

- **Strand s4 (vineyard microclimate), gap d_lw_pt (leaf wetness at several positions):** it does not close the gap, since wetness was not measured; it gives night and day RH offsets between three heights of one Brazilian trellis (40 h) that a simulator could use to shift canopy RH from a reference-height station. Not read in full; only the first 150 lines and located passages.
