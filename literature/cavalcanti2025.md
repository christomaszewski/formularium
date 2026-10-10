---
id: cavalcanti2025
citation: Cavalcanti, Fabio Rossi. 2025. Proposta de modelos de aprendizado profundo para diagnóstico de doenças foliares da videira [Deep learning approaches for grapevine leaf diseases diagnosis]. Boletim de Pesquisa e Desenvolvimento, no. 41, Embrapa Uva e Vinho, Bento Gonçalves, December 2025
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, mycosphaerella leaf spot]
crops: [grapevine]
regions: [Brazil (Embrapa Uva e Vinho Bento Gonçalves RS)]
processes: [symptom classification, image classification, diagnosis, transfer learning, precision agriculture]
records: []
datasets: []
files: [proposta-de-modelos-de-aprendizado-2025.pdf]
---

# Cavalcanti 2025: CNN image classifier for grapevine leaf diseases

A light read (the deep-research B list).

## What it holds

- Image classifier for grapevine leaves: healthy, downy mildew (Plasmopara viticola), and Mycosphaerella leaf spot (l. 64, 156-157).
- Images from three public repositories (Khan, Mandal, Redape), 256 x 256 RGB, 80/20 split (l. 142, 197-204, 435).
- Sequential CNN baseline, then InceptionV3 transfer learning with dropout 20% and augmentation up to 5% (l. 215, 264, 271).
- Early-stop rule at 95% accuracy, reached in five or six epochs for the early model; the final run uses 50 epochs (l. 260, 493).
- Conclusion: validation accuracy above 93%, TFLite conversion and a Flask app (l. 603-616).

## Dependence

- none. The paper is an image classifier (CNN, InceptionV3 transfer learning). It computes no engine-list model and uses no weather, infection or phenology formula. Shared authors: none on the list.

## Bearing (2026-10-10)

- None. Recorded so that it is not read again: a leaf-image classifier with no weather, incidence or model content for the truth or the Cooptera engine.
