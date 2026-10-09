---
id: liu2026robot
citation: Liu, Ertai, Gold, Kaitlin M., Cadle-Davidson, Lance, Kanaley, Kathleen, Combs, David & Jiang, Yu. 2026. PhytoPatholoBot: Autonomous Ground Robot for Near-Real-Time Disease Scouting in the Vineyard. Journal of Field Robotics (accepted 9 August 2025; printed in the 2026 volume) 43 (issue 1):442-453
doi: 10.1002/rob.70049
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [downy mildew, grapevine leafroll]
crops: [grapevine]
regions: [New York, California]
processes: [detection, scouting, observation]
records: []
datasets: []
files: [Journal of Field Robotics - 2025 - Liu - PhytoPatholoBot  Autonomous Ground Robot for Near‐Real‐Time Disease Scouting in.pdf]
---

# Liu et al. 2026: PhytoPatholoBot, a ground robot scouting for disease in vineyards

From Cornell (Geneva) and UC Davis; deployed in New York and California.

## What it holds

- Two New York sites only: a Cornell fungicide trial at Geneva in 2023 (80 panels, Chardonnay) (l. 312), and one Finger Lakes commercial vineyard (three rows of Cabernet Franc) on 15 August 2024 (l. 335), (l. 338). The Introduction also mentions California deployments, with no results (l. 73).
- Robot: strobe-lit RGB camera, 4096 x 3000 pixels (l. 217); 0.5 m/s at about 0.75 m from the canopy (l. 278); 1 FPS in the field (l. 324).
- Segmentation model DMNR: 83.07 % mIoU and 0.151 s per frame with TensorRT (l. 287). These numbers are from the 2022 IROS paper (l. 283).
- Geneva scouting on 2, 9 and 16 August (l. 315). The text gives no correlation values, only "positive" and "high" (l. 392); values are in Fig. 5 (image). The model was fine-tuned on 10 images from 2 August (l. 320).
- Human ratings dropped on 16 August while robot ratings rose (l. 389).
- Commercial vineyard: worst panel 2.83 % by humans and 3.25 % by robot (l. 415). No correlation at that level (l. 417).
- Leafroll (GLRaV-3): 100 % agreement on obvious panels (l. 432), 70 % on mild ones (l. 407); 15 of 21 panels under 5 % found (l. 445). Some leafroll was misread as downy mildew (l. 416).
- No detection rate at a stated true severity is given. Observation role only.

## Dependence

- Its own robot images; the segmentation model (DMNR) and its accuracy (mIoU 83.07%) are from the authors' 2022 paper. It was fine-tuned on images from 2 August 2023, also a scored date. Kanaley is an author, and a Kanaley co-author scouted.
- No author of an engine model.

## Bearing (2026-10-08)

- Clear, and the closest thing to a rover operator's numbers. **A correction:** the r values the earlier notes gave (0.63, 0.81, 0.79 against human scouts) are in Fig. 5, an image, not in the text: unchecked.
