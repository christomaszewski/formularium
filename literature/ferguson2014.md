---
id: ferguson2014
citation: Ferguson, John C., Moyer, Michelle M., Mills, Lynn J., Hoogenboom, Gerrit & Keller, Markus. 2014. Modeling dormant bud cold hardiness and budbreak in twenty-three Vitis genotypes reveals variation by region of origin. American Journal of Enology and Viticulture 65(1):59-71
doi: 10.5344/ajev.2013.13098
read: 2026-10-12, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 as the source of the catalogue's cold-hardiness record, read then by Agrarium without a note
status: read
diseases: []
crops: [grapevine]
regions: [Washington, Prosser, Paterson]
processes: [cold hardiness, dormancy, budbreak, phenology]
records: [ferguson2014.cold_hardiness, ferguson2011.hardiness]
datasets: [ferguson2014.prosser]
files: [2014-ferguson-10-5344-ajev-2013-13098.pdf]
---

# Ferguson et al. 2014: bud cold hardiness and budbreak for 23 genotypes

The source of the catalogue's `ferguson2014.cold_hardiness` (Table 4's parameters) and of
the dataset `ferguson2014.prosser`. Held since 2026-10-07; this is its note.

## What it holds

- **Data:** primary-bud cold hardiness (Hc, the LT50 from differential thermal analysis)
  measured since 1988 at about two-week intervals on up to 23 genotypes (21 V. vinifera
  and two V. labruscana, Concord and Sunbelt) at the IAREC vineyards at Prosser and the
  Ste. Michelle collection at Paterson, Washington (l. 79-105, 166; Table 1: Cabernet
  Sauvignon and Riesling 1988-2011, 24 years each, l. 133, 157); phenology since 1988 in
  the same vineyards (l. 122), turned into Hc values with published lethal temperatures
  (Gardea 1987 for V. vinifera, Proebsting et al. 1978 for Concord; Table 2, l. 187-190);
  observed budbreak as 50 % of buds with green tips (l. 306). The model uses "only two
  locations" (l. 632-633).
- **The model:** the discrete-dynamic model of Ferguson et al. 2011 (Ann. Bot. 107:389-396,
  l. 196-199, 665-667), with daily acclimation and deacclimation from the daily mean
  temperature, changed here in three ways: Hc,min becomes −1.2 °C for V. vinifera and
  −2.5 °C for V. labruscana instead of −3 (l. 220-223); a genotype-specific θ exponent
  enters the logistic deacclimation (Equation 1, displayed but absent from the text layer,
  l. 229-252); chilling degree days below a common 10 °C threshold set the ecodormancy
  boundary EDB (l. 258-269). Parameters per genotype were found by a stepwise search over
  1,653,750 combinations in eight dimensions (l. 273-274); each genotype's Hc,initial is
  regressed on Cabernet Sauvignon's (Table 3, l. 212-217, 284).
- **Parameters** (Table 4, l. 356-381, text layer): Tth,endo, Tth,eco, ka,endo, kd,endo,
  ka,eco, kd,eco, Hc,initial, Hc,max, Hc,min, θ and EDB per genotype; Hc,initial from −9.5
  (Mourvèdre) to −13.0 °C (Lemberger), Hc,max from −21.9 (Sangiovese) to −29.5 °C
  (Concord) (l. 345-346, 367, 374); EDB's units differ between the header (°C) and the
  text (a degree-day sum).
- **Fit and test:** combined n = 2,981, r² 0.97, RMSE 1.5 °C on the optimisation data
  (l. 381, 394); on the last three years of each genotype RMSE 2.0 °C, bias 0.2 °C, from
  1.2 (Mourvèdre) to 2.6 °C (Concord) (l. 400-409). Budbreak, predicted as the first day
  Hc reaches −2.2 °C (V. vinifera) or −6.4 °C (V. labruscana) (l. 318): 286
  observations, mean day 112 observed against 111 predicted, RMSE 6.7 d in fitting and
  7.3 d (r² 0.45, bias −1.0 d) on the evaluation years (Table 5, l. 447, 499). Genotype
  parameters explain 87 % of the variation in mean budbreak day (l. 340). Merlot case
  study: the November 2010 freeze at Alderdale, air −17.3 °C, Tmin −21.1 °C (l. 411-417).
- **Cited:** García de Cortázar-Atauri et al. 2009's budburst errors of 8-21 d (l. 597;
  `cortazar2009` prints 9-21 for its two common models); Nendel 2010's 4.5 d at 13
  northern European sites (l. 601).

## Dependence

- **Fitted to** the Prosser and Paterson DTA and phenology data, observed (`ferguson2014.prosser`).
- **Borrows** the structure of Ferguson et al. 2011 (`ferguson2011.hardiness`); the paper
  cites that model's eq. 6 as the one it alters and refers to the 2011 report for the
  rest (l. 196-199, 229), so the catalogue's "equations 1-6" is the 2011 paper's numbering,
  not this one's.
- **Authors:** Moyer (`moyer2010`, `moyer2016`), Hoogenboom and Keller (`salazargutierrez2016`,
  `zapata2015`): flags already recorded there.

## Bearing (2026-10-12)

- The records stand; the dataset's description is widened to name Paterson beside Prosser.
  For Agrarium, cold hardiness is a reference piece for the vine, not a disease process.
