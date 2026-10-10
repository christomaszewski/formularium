---
id: monteiro2015bol
citation: Monteiro, José Eduardo Boffino de Almeida, Conceição, Marco Antônio Fonseca, Cavalcanti, Fábio Rossi & Angelotti, Francislene. 2015. Avaliação do risco de ocorrência de doenças da videira em três regiões produtoras. Embrapa Informática Agropecuária, Boletim de Pesquisa e Desenvolvimento 38
doi: 
read: 2026-10-09, in full in an OCR of the scan, by a reading agent (claude-haiku-5-5); 60 quotes checked by scripts/verify_quotes.py; both equations read in the scan (p. 10) and compared with lalancette1988.infection and broome1995.botrytis by the main session
status: read
diseases: [downy mildew, grey mould]
crops: [grapevine]
regions: [Rio Grande do Sul, São Paulo, Pernambuco]
processes: [infection, climatic risk]
records: [lalancette1988.infection, broome1995.botrytis]
datasets: []
files: [embrapa_boletim38.pdf]
---

# Monteiro et al. 2015 (Boletim 38): downy mildew and grey mould risk in three regions

The congress paper [monteiro2015](monteiro2015.md) extended to Botrytis.

## What it holds

- **Downy mildew:** the same equation and results as monteiro2015 (read in the scan, p.
  10): intercept -0.061, e^(+ρ), exponent -5, no offset. High-risk days: Bento Gonçalves
  40 %, Jales 38 %, Petrolina 34 % and 7 %. Jales's 38 % is called both high and medium.
- **Botrytis:** Broome et al. 1995's logit, ln(Y/(1-Y)) = -2.647866 - 0.374927W + 0.061601WT -
  0.001511WT² (R² 0.75), copied (p. 10, scan). High-risk days: Bento 26 %, Jales 12 %,
  Petrolina 7 % in each cycle; Jales's shares sum to 99 %.
- **Wetness:** estimated by Sentelhas et al. 2006's energy-balance method where missing.
- **No validation.**

## Dependence

- **Botrytis:** Broome's coefficients match the engine's `broome1995.botrytis` exactly
  (Cooptera's `botrytis.py`), so the paper computes an engine model.
- **Downy mildew:** a misprinted copy of Lalancette's infection equation.

## Bearing (2026-10-09)

- An independent printing of Broome's coefficients, agreeing with the engine's.
