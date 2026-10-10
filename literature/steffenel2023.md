---
id: steffenel2023
citation: Steffenel, Luiz Angelo, Langlet, Axel, Hollard, Lilian, Mohimont, Lucas, Gaveau, Nathalie, Copola, Marcello, Pierlot, Clément & Rondeau, Marine. 2023. AI-driven strategies to implement a grapevine downy mildew warning system. In: Industrial Artificial Intelligence Technologies and Applications, ch. 13, pp. 177-187
doi: 10.1201/9781003377382-13
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 28 quotes checked by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Champagne]
processes: [primary infection, secondary infection, forecasting]
records: [rule_3_10]
datasets: []
files: [steffenel2023-dm-warning-chapter.pdf]
---

# Steffenel et al. 2023: classifiers taught the 3-10 rule at Reims

## What it holds

- **Data:** one station at a Champagne vineyard (Reims), hourly, 2019-2021.
- **Labels:** made by rules from Mezei et al. 2022: the 3-10 flag (above 10 °C, at least 10
  mm in 48 h, then night rain or wind above 3.4 m/s) and a secondary rule (RH above 80 %
  and T above 12 °C for 2 h, then leaf wetness above 2 h).
- **Models:** decision tree, random forest, SVM, dense and convolutional networks; one per
  year, tested on the others. Agreement 82-97 % (primary) and 98 % (secondary).
- The authors say the scores measure agreement with the rules, not with infections.

## Dependence

- Its targets are the 3-10 rule's output, so any model trained this way reproduces the
  engine's rule.

## Bearing (2026-10-09)

- None for the truth. Recorded so that it is not read again.
