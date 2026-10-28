---
id: zhao2022safy
citation: Zhao, Y., Han, S., Meng, Y., Feng, H., Li, Z., Chen, J., Song, X., Zhu, Y. & Yang, G. 2022. Transfer-learning-based approach for yield prediction of winter wheat from Planet data and SAFY model. Remote Sensing 14(21):5474
doi: 10.3390/rs14215474
read: 2026-10-27, lightly: abstract, methods 2.3.3 (the transfer-learning steps), the data description and the yield results; the text layer is partly garbled (overprinted duplicate text), so only clean lines were used; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 11 of 11 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [wheat]
regions: [China, Beijing]
processes: [pretraining, fine-tuning, transfer learning, crop model, SAFY, data assimilation, synthetic data, satellite imagery, yield prediction]
records: []
datasets: []
files: [syn1027_zhao2022safy.pdf (the 2026-10-27 drop)]
---

# Zhao et al. 2022: a network pretrained on 200,000 SAFY runs, fine-tuned on measured wheat, compared with data assimilation of SAFY (crops, winter wheat)

A four-layer fully connected network is pretrained on simulated biomass-to-yield pairs from the SAFY crop model (200,000 Monte Carlo parameter sets), then fine-tuned on measured data from winter wheat plots near Beijing with biomass estimated from Planet imagery. It is compared with data assimilation of SAFY on the same data. No record: a method with a measured result.

**Read this first.** There is no real-only network arm, so the value of pretraining cannot be read from this paper; the comparator is the process model run on the real data (data assimilation). The gain the authors claim is computing time, not accuracy (l. 35). The fine-tuning counts are not clean in the text layer (overprinted lines about 280-320) and are not used here.

## What it holds

- **Simulator and synthetic samples** (l. 25, 635-636, 643): SAFY (Simple Algorithm For Yield), 200,000 sets of parameter combinations drawn by Monte Carlo sampling, giving simulated above-ground biomass and yield pairs on which the network is pretrained (l. 643). Calibration to these plots is not stated in the lines read; the parameter sets cover a range instead.
- **Real data**: field experiments near Beijing over three seasons (2017-2019, per the reading agent; the table text is garbled), with Planet imagery. The counts of plots and samples are garbled in the text layer and are not given here. Fine-tuned on measured data (l. 645).
- **Validation design**: against measured yield, with a farm-scale test (l. 34); how train and test were split (plots, years) is not clean in the lines read.
- **Biomass step** (l. 30): the biomass estimated from imagery (CBA-Wheat algorithm) against measured biomass gave R2 0.83, RMSE 1.91 t/ha.
- **Yield scores** (l. 32-34): the transfer-learning model R2 0.64, RMSE 1.05 t/ha; data assimilation of SAFY R2 0.64, RMSE 1.01 t/ha; "similar in performance". At the farm scale RMSE 1.33 t/ha for data assimilation and 1.13 t/ha for transfer learning.
- **Real-only baseline**: none reported.
- **Efficiency** (l. 35-36, 920-925): the time of transfer learning with the complete simulated set was significantly lower than that of the other two yield estimation tests (data assimilation, and transfer learning without the complete set); at about 16,000 pixels the efficiency of data assimilation "was the same" (the comparator is not clear in the text), and above 16,000 pixels transfer learning without the complete simulated set was more efficient than data assimilation (l. 923-925).

## Dependence

- SAFY crop model (Simple Algorithm For Yield) and the CBA-Wheat biomass algorithm from Planet reflectance; data assimilation is the comparator. The network is kin to SAFY by construction.

## Bearing (2026-10-27)

- **Matches the accuracy of the process model on real data, and the authors' claim is speed.** For Agrarium (D45) that is a use of a simulator-trained model as a fast stand-in for the simulator: a valid use only if it is checked against the simulator and the field separately. It does not show that pretraining beats a network trained on the field data alone.
- **D60:** the Monte Carlo parameter sets are a way of covering the simulator's own uncertainty with many runs, comparable to using several physical models per gap; the paper does not test the effect of that coverage.
- **Not shown:** a real-only arm, held-out sites or years in the clean text, a disease, or more than one region.
