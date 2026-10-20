---
id: kontogiannis2024b
citation: "Kontogiannis, S., Konstantinidou, M., Tsioukas, V. & Pikridas, C. 2024. A cloud-based deep learning framework for downy mildew detection in viticulture using real-time image acquisition from embedded devices and drones. Information 15:178"
doi: 10.3390/info15040178
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Greece]
processes: [object detection, drone imagery, IoT camera nodes, cloud inference, leaf symptom detection]
records: []
datasets: []
files: [kontogiannis_2024.pdf (the 2026-10-20 drop)]
---

# Kontogiannis et al. 2024: cloud and embedded detectors for downy mildew spots from drones and IoT cameras

A pipeline sends drone and camera-node images to cloud or embedded object detectors, and compares Faster R-CNN, YOLO and lighter models on downy-mildew leaf spots in Zitsa, Greece.

## What it holds

- **Images:** 1200 annotated images for training and validation (80 / 20 split), and 300 more kept for testing. Debina vines at Zitsa, May to July 2023 (l. 584-587).
- **Cloud models, mAP0.5 at 100 epochs:** ResNet-152 0.995 and Faster R-CNN VGG16 0.995 (Table 2, l. 654, 658).
- **Embedded models, mAP0.5 at 100 epochs:** MobileNetV3 0.99, YOLOv8n 0.94, ViTDet-tiny 0.901 (l. 664-667).
- **Embedded, mAP0.5:0.95:** MobileNetV3 87 %, YOLOv8n 84.4 % (l. 724-725).
- **Speed:** YOLOv5 at least 60 % faster in frames per second than any Faster R-CNN model (l. 687-688).

## Dependence

Built from published detector and classifier designs (Faster R-CNN, YOLO, ResNet, VGG16, MobileNetV3, ViTDet, EfficientNet, SqueezeNet) and the labelImg annotation tool (l. 583). No other model's output is an input.

## Bearing (2026-10-20)

- **Strand t2 (observation).** A per-leaf detector on drone or IoT images. Its scores come from its own annotated set, one village and one season, and the output is boxes, not severity or spread.
- **Not read in full.** A decision engine could take a detection rate, with its test error, as an observation term. It does not model infection.
