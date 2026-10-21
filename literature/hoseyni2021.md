---
id: hoseyni2021
citation: Hoseyni, S. M., Di Maio, F. & Zio, E. 2021. Optimal sensor positioning on pressurized equipment based on Value of Information. Proceedings of the Institution of Mechanical Engineers, Part O: Journal of Risk and Reliability (venue, year and DOI from OpenAlex, 2026-10-21; the copy read is the Politecnico di Milano accepted version, which prints no journal, year, volume or pages)
doi: 10.1177/1748006x21989661
read: 2026-10-21, lightly: abstract, Section 2 (value of information, the sensor-positioning framework, the Gaussian-field case, the greedy algorithm, Equations 2-18), the case-study set-up and Table 2 in Section 3, conclusions; figures by caption only; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [none (a simulated steam generator manifold of a Prototype Fast Breeder Reactor; authors at Politecnico di Milano, Italy)]
processes: [value of information, sensor placement, greedy optimisation, Gaussian random field, creep degradation, thickness measurement, decision loss]
records: []
datasets: []
files: [hoseyni2021.pdf (the Politecnico di Milano accepted version, 2026-10-21 drop)]
---

# Hoseyni et al. 2021: greedy sensor placement by value of information on a Gaussian thickness field

Chooses where to put thickness gauges on a simulated pressurised manifold by the expected loss reduction (value of information, VoI) of each candidate, added greedily until it matches the VoI of the 32-gauge standard layout. No record.

**Read this first.** The copy read is an accepted version with no journal name, year, volume or pages printed; the venue and DOI here come from OpenAlex and are unchecked against the published paper, whose numbers may differ. Three internal flags are unchecked: the text says the greedy method needs 5, 17, 18 and 32 sensors for cases 1-4, but Table 2 has 28 for case 4 (l. 654, 692); the denominator of the exponential correlation, Equation (8), is printed as lambda with an ambiguous superscript (lambda or lambda squared); and Equations (2), (3), (4), (8) and (16) have lost glyphs in the text layer. All data are simulated: no field data, no held-out test, and no random placements as a baseline.

## What it holds

- **Framework** (Eqs. 2-7, PDF pp. 6-7, l. 257-329): VoI is the prior expected loss without a measurement minus the posterior expected loss with it (Eq. 5, l. 303), the expected loss being the best action under the prior or posterior field. A measurement set is cost-effective when its cost is at most its VoI, with utility M = VoI minus cost (Eq. 6, l. 315). The best set maximises M over all subsets (Eq. 7), impractical by enumeration (l. 325-327).
- **Greedy search** (Figure 8, l. 333, 337, 618, 631): find the best single sensor by simulation, update the prior with it, then add the next. Each candidate is scored by K = 10,000 simulated measurements at each iteration, among 160 candidate locations. The search stops when the set's VoI reaches that of the UNI 11096 layout of 32 thickness gauges (l. 468, 470). Greedy is cited to Malings & Pozzi (2019) and Hoseyni et al. (2019).
- **Gaussian case** (Eqs. 8-13, PDF pp. 8-9, l. 340, 348, 383): the field has an exponential correlation with scale lambda = 100 mm; the measurement mean is R mu and its covariance R Sigma R^T plus noise (Eqs. 9-10), with a closed-form conjugate posterior (Eqs. 11-13).
- **Case study** (l. 412, 445, 499): simulated creep degradation of a steam generator manifold, thickness a Gaussian field with mean 20 mm and SD 1 mm (2 mm at welds and the heat-affected zone, HAZ), with a failure threshold of 16.9 mm everywhere. Losses: failure 200 k EUR if degraded and untreated, mitigation 5 k EUR (Eqs. 16-18, PDF p. 12, l. 523-537; partly garbled).
- **Benchmark target** (l. 601): the UNI 11096 target VoI is taken with inspection cost zero, so the largest VoI is filling all 160 locations.
- **Results** (Table 2; l. 654, 684-692, 696): the greedy set matches the standard's VoI with fewer sensors in cases 1-3 and gives a higher VoI per sensor than UNI 11096 in all cases, with a coefficient of improvement of 6.43, 2.00, 1.83 and 1.18 for cases 1-4. Case 4 is flagged above (28 in Table 2, VoI 6156.1, against 32 in the text).
- **Symmetry** (l. 727): 8 candidate HAZ locations with equal uncertainty and geometry were each selected with probability about 62 % +/- 5 % over 1000 repeats, so ties are broken by simulation noise.
- **Limitation** (l. 748): the greedy method may struggle because VoI is not a submodular metric, as cited from ref 26.

## Dependence

- Builds on Raiffa & Schlaifer (1961) and DeGroot (2005) for VoI, Straub (2014) and Haladuick & Dann (2018) in reliability, Malings & Pozzi (2016a, 2018, 2019) for spatial VoI and submodularity, and the authors' own Hoseyni, Di Maio & Zio (2019) on VoI and submodularity; the UNI 11096 (2012) layout is the benchmark. Gaussian-process background from Kocijan (2016) and Rasmussen-type models. A shared author with the 2019 paper is only a flag.

## Bearing (2026-10-21)

For Agrarium's D48 study: decision-focused (value of information) placement on a spatial Gaussian process, and scoring a placement against a standard layout.

- **Takeable:** the recipe. Gaussian field with an exponential correlation, a two-action loss (mitigate at a fixed cost or accept a failure cost), a per-location expected loss min(C_f P_F, C_m) (Eq. 17), a Monte Carlo VoI per candidate, a greedy add with the posterior as the next prior, and a stopping rule against a reference layout. The coefficient of improvement VoI per sensor over the standard's is a scoring form usable against a regular grid of nodes.
- **Not shown:** any vineyard or crop, any real data, a random baseline, a held-out check, a re-plan over time, or a sensor menu. The paper itself flags that VoI is not submodular, so greedy has no guarantee (see `krause2009`). The kind of result is a simulation on one structural case, under the flags above.
