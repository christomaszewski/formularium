---
id: albasha2019
citation: Albasha, R., Fournier, C., Pradal, C., Chelle, M., Prieto, J. A., Louarn, G., Simonneau, T. & Lebon, E. 2019. HydroShoot: a functional-structural plant model for simulating hydraulic structure, gas and energy exchange dynamics of complex plant canopies under water deficit. Application to grapevine (Vitis vinifera). in silico Plants 1(1):diz007
doi: 10.1093/insilicoplants/diz007
read: 2026-10-26, a light reading of the HAL author manuscript by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; Eqs 1-16 and Tables 1-2 (manuscript pp. 7-12, 16, 24) read in the page images by the agent, since the text layer drops every equation
status: read
diseases: []
crops: [grapevine]
regions: [Montpellier]
processes: [whole-vine model, hydraulics, stomatal conductance, leaf energy balance, canopy architecture]
records: []
datasets: []
files: [albasha2019.pdf (the 2026-10-25 other-sources drop, a Wayback capture of the HAL deposit)]
---

# Albasha et al. 2019: HydroShoot, a leaf-level hydraulic and gas-exchange model of a vine

A functional-structural model that couples, hourly, the water flow through every shoot
segment, each leaf's energy balance and its photosynthesis and stomatal conductance, on a
3D canopy from the Louarn et al. 2008 reconstruction. A reference piece: its parameter
values sit in appendices this copy lacks, and the tools run no shoot-level model.

## What it holds

- **Structure** (l. 97-106, 363, 413-1127): three modules on OpenAlea (hydraulic, energy,
  exchanges); Eq. 1 segment flow as an Ohm's-law analogy, Eq. 2 a sigmoid loss of xylem
  conductivity with water potential, stomatal forms after Yin 2009, Leuning 1995 and
  Nikolov 1995, photosynthetic capacity from leaf nitrogen after Prieto et al. 2012, a leaf
  energy balance; MBE and RMSE as Eqs 15-16.
- **Printed values** (l. 460, 602-606, 670, 1106, 1640): c_x2 2.5-2.8 and c_x3 2.0-5.0 for
  the conductivity sigmoids; leaf length 70 % of the blade; basal mesophyll conductance
  0.1025 mol CO2 m⁻² s⁻¹; a 10 °C base; D0 5 (and 1 instead of 30). Appendices I-IV and the
  Supporting Information are not in this copy (l. 680, 932).
- **Tests** (l. 938-1036, 1657, 1709): three virtual canopies of 5.7 m² (VSP, GDC, Lyre) on
  the Montpellier weather of 29 July 2009; real Syrah on SO4 in VSP (2009, whole-plant gas
  exchange and leaf temperature) and GDC (2012, sap flow, conductance, leaf water potential
  under deficit); Table 1 for the well-watered VSP plant, sim0: assimilation MBE -0.05 µmol
  s⁻¹ and RMSE 5.49, transpiration MBE 89.47 and RMSE 141.66 g h⁻¹; 12-20 s per time step.
- **Inconsistencies** (l. 995-1027, 1412, 1495-1496, 1607): the systems' years reversed in
  one sentence; text MBEs that do not match Table 1; 60 and 250 % against Table 2's 66 and
  257 %.
- **Conclusion** (l. 1756): the hydraulic structure dominates net photosynthesis and
  transpiration under deficit.

## Dependence

- **Computes** the Louarn et al. 2008 canopy reconstruction (`louarn2008`, held), Prieto
  et al. 2012's nitrogen-based capacities, Farquhar 1980, Leuning 1995 and Tyree & Sperry's
  cavitation form; fitted to the authors' own 2009 and 2012 Syrah measurements at
  Montpellier. Louarn, Prieto and Lebon are authors: flags beside `lebon2004` and
  `louarn2007`.

## Bearing (2026-10-26)

- For Agrarium's growth truth (the 10-14 search): shoot-level carbon and water balance at
  a resolution the truth does not need; the one number of use is a well-watered VSP vine's
  transpiration error. No record.
