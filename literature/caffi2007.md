---
id: caffi2007
citation: Caffi, T., Rossi, V., Cossu, A. & Fronteddu, F. 2007. Empirical vs. mechanistic models for primary infections of Plasmopara viticola. OEPP/EPPO Bulletin 37:261-271
doi: 10.1111/j.1365-2338.2007.01120.x
read: 2026-10-08, in full (equations on the page images) by a reading agent (claude-sonnet-5-5); 60 quotes checked by scripts/verify_quotes.py, the dating of infections read by the main session (l. 239-242, 359, 430)
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Sardinia]
processes: [primary infection, oospore maturation, season onset]
records: []
datasets: [caffi2007.siniscola]
files: [EPPO Bulletin - 2007 - Caffi - Empirical vs  mechanistic models for primary infections of Plasmopara viticola.pdf]
---

# Caffi, Rossi, Cossu & Fronteddu 2007: four primary-infection models in Sardinia

From the Università Cattolica, Piacenza (Caffi, Rossi), Sardinia's agrometeorological
service (Cossu) and ERSAT Sardegna (Fronteddu). Presented at the EPPO conference on
computer aids, Wageningen, October 2006 (l. 61-62).

## What it holds

- **Data:** cv. Cannonau at Siniscola, 1996-2004 (l. 226-227): an unsprayed plot inspected
  weekly (l. 232-235). Disease appeared in 8 of 9 years, first onsets 2-25 May (l. 265,
  268).
- **Four models compared:** the 3-10 rule, EPI, DMCast and the UCSC model (Rossi's) (l. 26).
- **EPI as Sardinia's service runs it** (l. 84): a potential energy every 10 days from
  1 October to 31 March (l. 92), with ct = 1.2, 1 and 0.8 (l. 112-113); a kinetic energy
  daily from 1 April to 31 August, coefficient 0.012 (l. 152, 155); first infection when
  EPI exceeds -10 and rises for 3 days (l. 191). The text copy drops the square roots,
  which the page images show. EPI was built on Bordeaux data from 1907-1915 (l. 556) and
  needs local calibration (l. 562); the paper does not say whether the printed constants
  are Bordeaux's or Sardinia's.
- **DMCast:** a normal curve of maturity, μ = 118 - 0.3·Ra and σ = 13.5 + 0.02·Ra
  (l. 158), where Ra is POM's rain index from 21 September to 31 January, cited to Tran
  Manh Sung et al. 1990 (l. 163-168). The season starts at 3% mature, a threshold from
  New York (l. 190-191); germination needs more than 11 °C and 2 mm (l. 195). The maturity
  formula was fitted at Geneva, New York, 1985-1993 (l. 545-546).
- **Results:** EPI right in 2 of 9 years (l. 564); DMCast simulated 22% of infections
  (l. 540) and started its seasons between 29 May and 6 August (Table 4; the text says
  16 July, l. 410).

## Dependence

- **Its infection dates are a model's.** "The most probable period of infection was
  determined every year by going backward through the incubation period starting from the
  observed onset of symptoms, as shown in Rossi et al. (2002)" (l. 239-242), and every
  model's predicted onset was dated with the UCSC model's incubation (Tables 3 and 4,
  footnotes l. 359, 430). The observed onsets are data; the inferred infection dates are
  shaped by Rossi's incubation, the one `rossi2008.primary` computes.
- DMCast computes POM's index, and POM borrows EPI's idea of rain limits.
- Caffi and Rossi are authors of several engine models: flags.

## Bearing (2026-10-08)

- Formularium records the Siniscola data as `caffi2007.siniscola`, with the dating. A
  formulation fitted or scored on its infection dates is calibrated with
  `rossi2008.primary`; one matched to the observed onsets alone is not.
- The one held printing of EPI's and DMCast's equations, for anyone building them; take
  POM's own coefficients from [tranmanhsung1990](tranmanhsung1990.md).
- Cooptera's STATUS cites this paper for the 3-10 rule; the other session ("Disease
  models") has passed it the caveat about the dates.
