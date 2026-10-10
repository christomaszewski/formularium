---
id: monteiro2015
citation: Monteiro, José Eduardo B. A., Conceição, Marco Antônio F., Cavalcanti, Fábio Rossi & Angelotti Segundo, Francislene. 2015. Caracterização do risco de ocorrência de míldio da videira em três regiões produtoras. XIX Congresso Brasileiro de Agrometeorologia, Lavras, 23-28 August 2015
doi: 
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 47 quotes checked by scripts/verify_quotes.py; the coefficients compared with lalancette1988.infection by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Rio Grande do Sul, São Paulo, Pernambuco]
processes: [infection, climatic risk]
records: [lalancette1988.infection]
datasets: []
files: [embrapa_monteiro2015_caracterizacao.pdf]
---

# Monteiro et al. 2015: downy mildew risk in three Brazilian regions

The same results appear in Embrapa's Boletim 38 ([monteiro2015bol](monteiro2015bol.md)).

## What it holds

- **Method:** Lalancette's infection efficiency over ten years of daily weather
  (2003-2013/14), at Bento Gonçalves, Jales and Petrolina. Classes: high above 50 %,
  medium 3.5-50 %, low up to 3.5 %, where 100 % = 0.1 lesion per zoospore.
- **The equation as printed:**
  - EI = (-0.061 + 0.018T - 0.0005T²) x [1 + e^(-0.24W + 0.07WT - 0.0021WT²)]^(-5);
  - against Lalancette's eq. 5, the intercept (-0.071), the offset (+0.01) and the sign of
    the exponent (e^-ρ) all differ.
  - Wetness is estimated by an energy-balance method (Sentelhas et al. 2006) where missing.
- **High-risk days:** Bento Gonçalves 40 %, Jales 38 %, Petrolina cycle 1 34 %, cycle 2
  7 %. From year to year: Bento near 40 % (61 % in 2009/10), Jales 19-67 %, Petrolina
  cycle 1 1-66 %.
- **No validation** against disease.

## Dependence

- Computes a misprinted copy of Lalancette 1988's infection equation.

## Bearing (2026-10-09)

- Model output only. It shows how far a copied equation drifts from its source.
