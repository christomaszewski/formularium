---
id: laurenson2002
citation: Laurenson, M., Otuka, A. & Ninomiya, S. 2002. Developing Agricultural Models Using MetBroker Mediation Software. Journal of Agricultural Meteorology (Nogyo Kishō) 58(1):1-9
doi: 
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: []
regions: [Japan, New Zealand]
processes: [weather data access, mediated architecture, Java applets and servlets, weather database integration]
records: []
datasets: []
files: [laurenson2002.pdf (the 2026-10-25 other-sources drop)]
---

# Laurenson et al. 2002: three ways to build agricultural models on the MetBroker weather mediator

A software design paper on MetBroker, a Java mediator that gives agricultural models one interface to many weather databases, and three ways to build model software on it.

## What it holds

- **Mediator:** MetBroker is a Java mediator with one interface to 11 weather databases
  (Table 1, l. 113), among them the Japanese AMeDAS data and the New Zealand CliDB (l. 125-130).
- **Three approaches** (abstract, l. 14-18): Java applets, small bridging Java applications
  that write weather files for models in other languages, and Java servlets that return HTML.
  All but the servlets need Java 2 on the client (l. 18).
- **Demonstration:** a New Zealand station (Whakatu, Hawke's Bay) with records from 1997 onwards
  (l. 145-149). No model is validated and no error statistic is given.
- **Licence:** the source is under the GNU Lesser General Public Licence (l. 122-126), and
  the documentation is on the MetBroker web site (l. 133).

## Dependence

- **Builds on** the MetBroker design of Laurenson et al. (2000) (l. 39-40), the mediated-access
  architecture of Wiederhold (1992) (l. 47), and the AMeDAS and CliDB databases (l. 125-130).

## Bearing (2026-10-26)

- classes.tsv names no search for this key. It is software design, with no crop or vine
  content: a growers' decision engine could take the mediator pattern (one interface to many
  weather sources) but not any model.
- The paper was not read in full, and it gives no model validation.
