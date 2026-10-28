---
id: miftahushudur2025
citation: Miftahushudur, T., Sahin, H.M., Grieve, B. & Yin, H. 2025. A Survey of Methods for Addressing Imbalance Data Problems in Agriculture Applications. Remote Sensing 17(3):454
doi: 10.3390/rs17030454
read: 2026-10-27, lightly: abstract, the data-collection causes and the start of the disease-detection section; a keyword search for weather and time-series content found none, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [various]
regions: [none]
processes: [class imbalance, oversampling, undersampling, data augmentation, GAN, VAE, evaluation metrics, review]
records: []
datasets: []
files: [syn1027_miftahushudur2025.pdf (the 2026-10-27 drop)]
---

# Miftahushudur et al. 2025: survey of class-imbalance methods in agricultural machine learning (mostly images, review)

Surveys resampling, algorithm-level methods and generative augmentation for imbalanced agricultural data (disease detection, soil, crop classification). No record: a review.

**Read this first.** An image-oriented survey: the disease examples are image classification, and a keyword search of the text for weather, meteorology and time series found nothing. It is context for oversampling and generative augmentation, not a weather-forecasting source. No scores of its own.

## What it holds

- **Scope** (l. 7): the review covers "generative models, like GANs and VAEs, for data augmentation in agricultural applications", beside resampling and algorithm-level methods.
- **Where imbalance comes from** (l. 29, 147): "natural rarity, such as rare diseases in crops or specific pest infestations that only occur in certain environmental conditions"; in disease detection, diseased samples are far fewer than healthy ones. The second statement is about image sets.
- **Metrics** (l. 7): recommends F1-score, G-mean and MCC rather than accuracy for imbalanced classes; open problems named are noisy and incomplete data and few public data sets.
- **Validation, labels, synthetic data:** none of its own; the survey reports other studies' methods.

## Dependence

- Secondary source. None recorded.

## Bearing (2026-10-27)

- **Rare outbreaks:** it names natural rarity of severe outbreaks as a cause of imbalance, which is the case for outbreak records; it gives no tested remedy for weather-driven forecasting. Use its metric advice (F1, G-mean, MCC) when scoring rare-event models.
- **D60 (synthetic outcomes):** no evidence on whether generated minority cases help on held-out seasons; the survey's generative examples are images.
