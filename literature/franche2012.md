---
id: franche2012
citation: Franche, J.-C. 2012. Modélisation du cycle du mildiou de la vigne dans un outil d'aide à la décision : intégration de nouveaux formalismes. Mémoire de stage, Master FAGE (BIPE), Université de Lorraine, Nancy; internship at SAS ITK, Clapiers. HAL hal-01871194
read: 2026-10-08, in full by a reading agent; the cold-day rule and the incubation equation checked in the extracted text. Minus signs and Greek letters were lost in extraction
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [France]
processes: [oospores, primary infection, splash, interception, sporulation, infection, incubation, host]
records: [rouzet2003.cold_days]
datasets: []
files: [BUS_M_2012_FRANCHE_JEAN-CHARLES.pdf]
---

# Franche 2012: the downy mildew cycle in ITK's decision tool

A master's internship report, supervised by Vianney Houlès at the company ITK, for its
tool ITK Protect. Built in Matlab and validated loosely on six estates (Val de Loire,
Charente, Aquitaine), 2002-2004, with infection dates inferred by experts.

## What it holds, process by process

| Process | Formulation | Source | Dependence |
|---|---|---|---|
| Start of oospore maturation | "60 jours de froid (7°C ≤ T max ≤ 15°C)" replaces Rossi's 1 January | Rouzet & Jacquin 2003 | independent |
| Dormancy, germination, release, survival | Rossi et al. 2008's equations, with Franche's logistic smoothing; a 2 mm/day germination trigger from DMCAST | Rossi 2008; Park et al. 1997 | depends on Rossi 2008 |
| Primary splash | y = a·exp(b·d) with d the trunk height, fitted by Franche to Rossi & Caffi 2012's heights | Esker et al. 2007; his own fit | not an engine model; Rossi and Caffi a flag |
| Interception | 1 − exp(−0.68·LAI), and 100/50/25 % to leaf layers 1-3 | assumed (k from Contreras-Medina 2009) | independent |
| Sporulation | ≥ 6 humid night hours (RH > 90 %); counts after Lalancette et al. 1988b and Kennelly et al. 2007 | Lalancette; Kennelly | shares the engine's Brischetto port's borrowing of Lalancette |
| Conidia survival | elements of Vinemild (T, RH); no equation printed | Vinemild | independent, but unusable as printed |
| Infection efficiency | a Richards-type curve in wet hours and temperature | Lalancette, Ellis & Madden 1988 | shares data with Magarey 2005's P. viticola row |
| Leaf susceptibility | Calonnec et al. 2008's leaf-age relation for powdery mildew, used as is | Calonnec 2008 (Bordeaux) | independent of the engine; a transfer between diseases |
| Incubation | incubRate = 2.616·(T − Tmin)(Tmax − T)·(RH − RHmin)/(RHmax − RHmin) / (Tmax − Tmin)² (eq. 15); the four bounds not printed | PLASMO (Orlandini et al. 2008) | no Goidanich here, but Orlandini 2008 credits Goidanich et al. 1958 (see below); Orlandini a flag through Sentelhas 2008 |

Also: hourly temperature from daily data by Sall 1979; Bordeaux models (POM, Potentiel
Système, EPI, MILVIT) described but not used.

## Bearing (2026-10-08)

- **Independent pieces worth keeping:** Rouzet & Jacquin's cold-day trigger for the start
  of oospore maturation; the splash-height and Beer-Lambert interception scheme; Calonnec's
  leaf-age susceptibility (with the caveat that it is powdery mildew's).
- **PLASMO's incubation form** is printed here for the first time we have seen, but without
  its parameters: a lead to PLASMO's own papers (Orlandini, Rosa et al. 1993), not a usable
  formulation.
- **PLASMO's incubation, followed up (2026-10-09):** Orlandini et al. 2008 (eq. 6) print
  the bounds, 10-34 °C and 30-100 % RH, credit Goidanich et al. 1958 and Magarey et al.
  1991, and put a square root on the humidity term; fm is not printed. Rosa et al. 1995
  print m = 0.082 on √(RH - 30). Neither has 2.616 ([orlandini2008](orlandini2008.md),
  [rosa1995](rosa1995.md)).
- Its primary chain is Rossi's, and its infection and sporulation share the Lalancette data
  the engine reaches through Magarey and Brischetto.
- **Rouzet & Jacquin's rule, followed up (2026-10-08, main session):** recorded as
  `rouzet2003.cold_days` from Franche's statement (§2-1-1, checked in the text). Franche
  cites "IOBC/WPRS Bull. 33"; Crossref gives *EPPO Bulletin* 33(3):437-442,
  doi:10.1111/j.1365-2338.2003.00670.x, closed access. Its abstract states no cold-day rule
  and doubts that maturation can yet be modelled, so the rule may be Franche's or ITK's
  reading. Not for a tool until the paper is read.
