---
id: mounir2026
citation: Mounir, S., Cieslak, M., Dhieb, N., Ghazzai, H., Klein, J., Froehlich, K., Pirk, S., Palubicki, W., Setti, G., Eltawil, A.M. & Michels, D.L. 2026. Text-conditioned Segmentation for Tomato Phenotyping via Procedural Synthetic Data. arXiv:2607.18576v1 [cs.CV] (preprint)
doi: 10.48550/arXiv.2607.18576
read: 2026-10-27, lightly: abstract, the contributions, the data and model sections, results (Tables 2 and 3) and the discussion, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [tomato]
regions: [none]
processes: [synthetic data, rendering, L-system, procedural plant model, foundation model, fine-tuning, LoRA, image segmentation, sim-to-real]
records: []
datasets: []
files: [syn1027_mounir2026.pdf (the 2026-10-27 drop)]
---

# Mounir et al. 2026: L-system tomato greenhouse renders, with a foundation segmenter fine-tuned on them and judged on three real mask sets (preprint)

Renders a procedural L-system cherry-tomato model in an Unreal Engine 5 greenhouse, fine-tunes Segment Anything Model 3 (SAM 3) on the renders in three ways, and compares it with three networks trained from scratch on the same renders, on synthetic and on real masks. No record: a method; a preprint dated July 2026.

**Read this first.** A preprint (not peer reviewed), tomato and not grapevine. The real data are used for testing only, so there is no real-only training arm; the "without synthetic data" comparison is zero-shot SAM 3. Labels on two of the three real sets are incomplete (l. 338 to 342), so IoU there understates quality. The paper's own Table 2 caption says that synthetic validation alone does not predict real-world transfer.

## What it holds

- **Generator** (l. 217, 218, 226): a procedural cherry-tomato model (Solanum lycopersicum var. cerasiforme) built with L-systems, in an Unreal Engine 5 greenhouse with varied viewpoint, light and morphology; a large synthetic corpus of 68k frames (l. 251, 280). The paper says the authors release the model, dataset and fine-tuned weights (per the reading agent; the location was not read).
- **Models** (l. 245 to 260, 280 to 282): SAM 3 fine-tuned by LoRA, by full fine-tuning, and with weight interpolation toward the zero-shot weights (WiSE-FT); DeepLabV3+, SegFormer and EoMT trained from scratch on the same renders.
- **Synthetic validation** (Table 2, l. 287, 306, 313): 5,553 frames; mean foreground IoU (mFG) 0.6953 for DeepLabV3+, the best; Full FT SAM 3 0.6158; zero-shot SAM 3 0.3014. The authors: "synthetic validation alone does not predict real-world transfer" (l. 302).
- **Real test sets** (Table 1, l. 199, 200, 201): TomatoMAP-Seg 725 images, LaboroTomato 804, Rob2Pheno 105; fruit IoU, binary fruit against not-fruit.
- **Real fruit IoU, macro over the three sets** (Table 3, l. 319 to 326): Full FT SAM 3 0.6562 (TomatoMAP 0.7785, Laboro 0.7371, Rob2Pheno 0.4529); zero-shot SAM 3 0.5269; SegFormer from scratch on renders 0.2264; DeepLabV3+ 0.0403; EoMT 0.0149. The network best on synthetic validation is near zero on real images (l. 325). Fine-tuning on renders lifts the foundation model by 0.129 over zero-shot (arithmetic, not printed).
- **Reading** (l. 349, 340): supervised models trained on the renders stay far below the fine-tuned foundation model on real data (macro fruit IoU below 0.23); on Rob2Pheno many visible fruits are unlabelled.
- **Cited, not the paper's own** (l. 145): Khan and colleagues 2025 report that calibrating procedural data to real images improved accuracy "ten-fold" (maize and canola); not read.

## Dependence

- L-system plant models (Prusinkiewicz and Lindenmayer; Cieslak, a shared-author flag with the L-system lineage), Unreal Engine 5, SAM 3 pre-training. The real benchmark masks are public sets by others.

## Bearing (2026-10-27)

- **The strongest warning in the strand for rendered data (D58, D60):** the model that won on the renders (0.6953) scored 0.04 on real images, and a render-only validation would have picked it. Agrarium's viewer renders its own vines; any model fitted on them has to be judged on real images.
- **What worked:** a pre-trained foundation model, lightly fine-tuned, gained on real images; supervised models from scratch on renders did not. That says renders can move a model that already knows real images, which is how Agrarium's tier-3 canopy imagery sensors might use them.
- **Not shown:** a real-only training arm, vines, disease or lesions, or any number from a field, and the labels on two of three test sets are incomplete.
