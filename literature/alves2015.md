---
id: alves2015
citation: Alves, Maria Emília Borges, Cavalcanti, Fábio Rossi & Monteiro, José Eduardo B. A. 2015. Análise da favorabilidade de ocorrência de doenças fúngicas da videira no município de Santana do Livramento - RS [Favorability analysis of the occurrence of grapevine fungal diseases in Santana do Livramento–RS]. XIX Congresso Brasileiro de Agrometeorologia, Lavras, MG, Brazil, 23-28 August 2015, pp. 208-218
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, grey mould, bunch rot (botrytis)]
crops: [grapevine]
regions: [Brazil, Rio Grande do Sul, Campanha Gaúcha, Santana do Livramento, Serra Gaúcha]
processes: [infection, leaf wetness, season severity, spray timing, infection efficiency, climatic risk, sporulation]
records: [lalancette1988.infection, broome1995.botrytis]
datasets: []
files: [embrapa_alves2015_analise.pdf]
---

# Alves et al. 2015: favorability of downy mildew and grey mould, Brazil

A light read (the deep-research B list).

## What it holds

- Models of downy mildew and grey mould favourability for Santana do Livramento (RS), run on 2002-2013 INMET daily data (l. 20-25, 138-141).
- Downy mildew model: Lalancette et al. 1988a infection efficiency as Eq. 1 (l. 168-172).
- Grey mould model: Broome et al. 1995 infection index as Eq. 2, fitted to grape berries in humidity chambers (l. 189-193).
- Wetness duration is estimated by regression, not measured (l. 211-215).
- Modelled risk for 2002-2013: downy mildew 23% low, 45% medium, 32% high days; grey mould 15%, 78% and 7% (l. 31-32).
- The authors say the downy mildew output agrees with grower reports; the grey mould output does not (l. 353, 364-370).
- The models are not validated for the region (l. 356).

## Dependence

- verdict: computes; models: Lalancette et al. 1988a's infection-efficiency model (Eq. 1, l. 168-172, page 4 image): EI = (-0.061 + 0.018T - 0.0005T^2) x (1 + e^(-0.24 DPM + 0.07 DPM x T^2))^-5. The form and constants match the Formularium note for lalancette1988infection (k with the +0.01 offset folded in, m = 1.2 so the exponent is -5). Formularium's magarey2005 note says the P. viticola row of Magarey's Table 2 shares data with Lalancette 1988. So this paper computes a formulation tied to the engine's infection response; the note for magarey2005 should be checked before judging the kinship. Broome et al. 1995's Botrytis infection index (Eq. 2, l. 189-209, page 5 image). The brief lists it under other diseases, so it is noted, not a P. viticola dependence.; described_not_computed: Lalancette et al. 1988b (sporulation, l. 107), Sônego et al. 2005 wetness hours (l. 87-90), Gessler et al. 2011 optima (l. 81-83, 324-325). Cited for context only.; wetness_estimate: Equations 3 and 4 (l. 211-228) estimate wetness duration (DPM) and wetness-period temperature by regression on daily RH, wind, Tmed, precipitation and temperature range, fitted to two years of hourly data (site not printed). These are a leaf-wetness estimate of the kind the brief flags as a stand-in, though not an RH >= 90% threshold: this is for the record to judge.; shared_authors: none noted

## Bearing (2026-10-10)

- It computes Lalancette et al. 1988a infection-efficiency equation, whose data the Formularium magarey2005 note says the engine infection response shares, so it is a kinship flag for the truth; its Broome index is a Botrytis model and does not bear on the downy mildew truth.
