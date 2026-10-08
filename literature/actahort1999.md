---
id: actahort1999
citation: Wagenmakers, P. S., van der Werf, W. & Blaise, Ph. (eds) 1999. Proceedings of the Fifth International Symposium on Computer Modelling in Fruit Research and Orchard Management. Acta Horticulturae 499 (IOBC/WPRS Bulletin 22(6)); read: Blaise, Ph., Dietrich, R. & Gessler, C., Vinemild: an application-oriented model of Plasmopara viticola epidemics on Vitis vinifera, pp. 187-191; and Blaise, Ph., Dietrich, R. & Jermini, M., A new demand function for grapevine fruits in Vinemild, pp. 253-259
read: 2026-10-08, the two Vinemild papers in full by a reading agent (claude-sonnet-5-5); 90 quotes checked by scripts/verify_quotes.py, dependence by the main session. The rest of the volume (fruit trees) only by its contents
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Switzerland]
processes: [epidemic progress, berry growth]
records: []
datasets: []
files: [1999_6.pdf]
---

# Acta Horticulturae 499 (1999): the Vinemild papers

A whole proceedings volume (Wageningen, July 1998), mostly fruit trees. Two papers are
from ETH Zurich's Vinemild group; the heading prints "Pb. Blaise" and "M. Jennini" for Ph.
Blaise and M. Jermini.

## What it holds

- **Vinemild** (Blaise, Dietrich & Gessler): three submodels, Fungus, Epidemic and
  Grapevine, on a one-hour step (l. 8951). The Fungus submodel is "based on literature
  data" (l. 8863), naming no source and printing no rule; the only parameter named is a
  humidity threshold for sporulation, without a value (l. 8988).
- The one equation is the epidemic's, an extended Vanderplank progeny-parent model
  (l. 8918): dx/dt = Rc·[x(t - p(T) - i) - x(t - p(T))]·[1 - x(t)] (l. 8891), no parameter
  values printed.
- **Evaluation:** ten years of the authors' control plot, judged by "visual agreement" of
  curves (l. 9001-9008); no years, place or plot size given, and nothing said to be fitted.
- **Berry demand** (Blaise, Dietrich & Jermini): berry dry weight
  Y = P1·(1 - e^(-P2·t)) + P3/(1 + e^(-P4·(t - P5))), t in degree-days above 10 °C after
  fruit set (l. 11949), a form from Génard & Bruchou 1993 for peach (l. 11947); P1 4.95E-02 g,
  P2 1.05E-02, P3 3.08E-01 g, P4 9.03E-03, P5 6.27E+02 (l. 12081). Fitted to the authors' Merlot of
  1997 in southern Switzerland (l. 11916, 11939); fresh to dry weight y = 0.2884x - 0.1122,
  R² 0.9411 (l. 12189). It missed 1996, when berries were 54% heavier (l. 12020).

## Dependence

- No borrowed equation is named for Vinemild's Fungus submodel; the earlier guess that it
  computes Blaeser & Weltzien 1979 is not supported in these pages.
- The berry function replaced Wermelinger et al. 1991's quadratic (l. 11981).
- Gessler and Jermini are not authors of engine models; Gessler co-wrote with Gobbin, who
  co-wrote with Rossi: a remote flag.

## Bearing (2026-10-08)

- Vinemild is clear of the engine, but these papers print too little to run it: Blaise &
  Gessler 1992 (theory and parameters) is the paper to find.
- The berry demand function is clear and complete, a host-growth formulation if Agrarium
  ever simulates bunch mass.
