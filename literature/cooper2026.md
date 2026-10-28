---
id: cooper2026
citation: Cooper, E., Hartley, Z. & French, A. 2026. Synthetic plant disease image generation to improve segmentation tasks in low-resource settings. Frontiers in Plant Science 17:1812323
doi: 10.3389/fpls.2026.1812323
read: 2026-10-27, lightly: abstract, methods (data, pipeline, downstream design), results (Table 4, KID and CLIP scores, ablation) and discussion with limitations, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 15 of 15 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [apple black rot, apple scab, cedar apple rust]
crops: [apple]
regions: [none]
processes: [synthetic data, image segmentation, rendering, diffusion model, data augmentation, lesion segmentation]
records: []
datasets: []
files: [syn1027_cooper2026.pdf (the 2026-10-27 drop)]
---

# Cooper et al. 2026: Blender apple leaves with sphere lesions, restyled by Stable Diffusion, to train lesion segmentation

A pipeline that renders procedural apple leaves in Blender (exact masks), restyles the renders with a disease-specific diffusion model so the lesions look real, and trains a U-Net on real plus synthetic images. No record: a method, with a small test on lab photos.

**Read this first.** Every image, real and synthetic, is a PlantVillage laboratory photo of an apple leaf (a bench background), and the authors say the result "is unlikely to generalise to in-field imagery" (l. 638). The real test set is 30 images, the mean is of five runs, and no significance test was done (l. 433, 434, 642). The masks of the diffusion images are inherited from the Blender render through ControlNet edges, so the labels are computed by the renderer, not by an annotator. The real masks were annotated by hand.

## What it holds

- **Generator** (l. 27, 29, 205 to 209, per the reading agent for the diffusion settings): procedural leaf geometry in Blender, with lesions placed as spheres at random positions on the mesh (counts and radii per disease, l. 205 to 208); the render is restyled by Stable Diffusion v1.5 with one LoRA per disease and ControlNet edge conditioning so the lesion stays where it was placed. 100 images per disease.
- **Real samples** (l. 168, 209 to 211, 311, 313): a restricted set of 25 PlantVillage images per disease (black rot, scab, cedar rust), hand-masked. The LoRA was fitted on 15 per disease and the other 10 were held out for the downstream test. The mixed training sets hold 100 synthetic and 10 real images per disease, 330 in all (l. 311). The test is a fixed held-out set of 30 real images, 10 per disease (l. 313).
- **Test** (l. 313, 433): real held-out images of the same lab set, not field images; U-Net with weighted Dice loss, 20 epochs, mean of five runs. The real-only arm uses basic augmentation (l. 303).
- **Scores, Dice (Table 4, l. 413 to 419)**, real-only / Blender-only / real+Blender / diffusion-only / real+diffusion:
  - black rot 0.27 / 0.15 / 0.31 / 0.39 / 0.76 (l. 415);
  - scab 0.19 / 0.10 / 0.10 / 0.23 / 0.54 (l. 417), so real+Blender is below real-only;
  - cedar rust 0.23 / 0.15 / 0.21 / 0.21 / 0.63 (l. 419);
  - healthy leaf 0.82 / 0.52 / 0.69 / 0.58 / 0.92 (l. 413), so real+Blender is below real-only here too.
- **Reading** (l. 605): the authors say rendering alone cannot capture lesion appearance and that diffusion style transfer is needed to reduce the gap to real diseased imagery.
- **Limits** (l. 638, 642): small dataset, lab photos, lesion placement uniformly random with no disease-specific pattern (per the reading agent's summary of the method).
- Image-distance scores (KID, CLIP) are in the paper (Table 5, Figure 6); they were not transcribed.

## Dependence

- Blender; Stable Diffusion v1.5 with LoRA and ControlNet (Canny and soft edges); U-Net. The diffusion model is fitted on 15 real images per disease from the same lab set that the test images come from (a different 10 per disease, l. 209), and Stable Diffusion's own training data are unknown here. Leaf templates were modelled by hand from PlantVillage leaves (l. 160 to 165).

## Bearing (2026-10-27)

- **Closest published case to Agrarium's viewer:** a 3-D renderer places lesions at known positions and gets exact masks, as the viewer could for the truth's lesions. The measured result is that unrestyled renders do not help (scab 0.19 to 0.10 with real+Blender) and that a restyle by a model fitted on real lesion photos does (black rot 0.27 to 0.76). So rendered lesions would have to be judged on real held-out images, per D58 (real data judge the variables) and D60 (synthetic outcomes test robustness, never establish a feature).
- **D45:** the restyling model is fitted on real lesion photos; a restyle fitted on the viewer's own renders would be kin to the truth's lesion model.
- **Not shown:** a vine leaf, downy mildew oil spots, any field photo, a test set larger than 30 images, a significance test, or a comparison with a real set of equal size.
