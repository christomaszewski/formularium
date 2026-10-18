---
id: depaula2012
citation: de Paula, V. A., Bergamaschi, H., Del Ponte, E. M., Cardoso, L. S. & Bosco, L. C. 2012. Duração do período de molhamento foliar em pomares de macieira em céu aberto e sob tela antigranizo, em Vacaria-RS (Leaf wetness duration in apple orchards in open sky and under hail net cover, in Vacaria, Brazil). Revista Brasileira de Fruticultura 34(2):451-459
doi:
read: 2026-10-18, LIGHT, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py; page 3 read in the page image for the sensor-facing sentence and Equation 1
status: read
diseases: []
crops: [apple]
regions: [Brazil, Vacaria, Rio Grande do Sul]
processes: [leaf wetness duration, canopy microclimate, hail net, sensor position, wetness sensor]
records: []
datasets: []
files: [viviane_2012.pdf (the 2026-10-18 drop, second pass)]
---

# de Paula et al. 2012: leaf wetness hours at three canopy heights, open and under hail net

One season of leaf wetness sensors at three strata of two Royal Gala apple blocks, 15 m apart, one in the open and one under black hail net. No record: a measurement, not a formulation. The DOI is not printed in the text layer. The paper is in Portuguese with an English abstract; the file key is `viviane_2012`.

## What it holds

- **Setting** (l. 135-153, 136-137): Royal Gala on M9, ten years after planting, Vacaria-RS, October 2009 to March 2010. Blocks 15 m apart (l. 143); net mesh 4 x 7 mm, about 30 cm above the tree tops (l. 143, 151). Tree height 2.7 m open, 3.0 m under net (l. 153). Spacing 1.0 m x 3.5 m in the methods (l. 139) but 1 m x 3 m in the abstract (l. 38); the two disagree and the paper does not say which holds.
- **Sensors** (l. 137-146, 169, 179, 126): Campbell 237-L and Epagri PVC-plate sensors, painted white latex to raise sensitivity (after Sentelhas 2004), calibrated between fully wet and fully dry and matched to each other; set at 45 degrees facing south (the sentence runs from l. 179 to l. 126). Read every 30 s, recorded every 30 min (l. 135). Sensor heights above ground are not printed.
- **Mean wetness, h per day** (l. 201, 206-207): open, lower 13.5, middle 12.7, upper 12.3; under net, lower 13.9, middle 13.8, upper 13.2. Wetness was highest in the lower stratum in both blocks (l. 40). Covered against open differed significantly only at the upper and middle strata (l. 41).
- **Differences between strata, h per day** (Table 2, l. 312-314): whole period, open, lower minus middle 0.8, lower minus upper 1.2, middle minus upper 0.4; under net 0.2, 0.7, 0.7. Rain days, open 0.9, 1.1, 0.2; under net 0.6, 0.9, 0.5. Dry days, open 0.8, 1.2, 0.5; under net -0.1, 0.5, 0.8. In the open block the lower third exceeded the middle on 66 % of days and the upper on 73 %; the middle exceeded the upper on 61 % (l. 248).
- **Sensor agreement** (Table 3, l. 330, covered block, whole period): Willmott's index of agreement D 0.97 (lower with middle), 0.98 (lower with upper), 0.98 (middle with upper); r 0.94, 0.97, 0.97. Equation 1, D = 1 - sum(Oi - Pi)^2 / sum((|Pi - Om| + |Oi - Om|)^2), compares sensors; it does not model wetness.
- **Cited, not measured here** (l. 252, 256, 215): in the same experiment the net did not change daily mean air temperature or relative humidity at a given stratum (Cardoso et al. 2009; Bosco et al. 2010), cut incident solar radiation by about 30 % and wind by about 40 %. At Ames, Sentelhas (2004) and Sentelhas et al. (2005) found about 2 h more wetness at the top of dense Golden Delicious canopies, the opposite order to this open, low-vigour canopy.
- **Not printed:** an RH or dew-point threshold, any station or reference sensor, sensor heights, the wetness threshold of the sensor output, a data statement.

## Dependence

- No formulation; nothing computed from another model and nothing fitted. It cites Cardoso et al. 2009 and Bosco et al. 2010 for the microclimate of the same two blocks (not read). One season at one orchard pair (Schio Agropecuária Ltda.).

## Bearing (2026-10-18)

Strand 4 (measured microclimate, here an orchard) and strand 5 (sensor placement as a source of error).

- **Where the sensor sits changes the answer by about an hour a day.** In the open block, the lower third reads 0.8 h per day more than the middle and 1.2 h more than the upper (l. 312); under the net, 0.2 and 0.7 h. A sweep that moves a wetness sensor within the canopy should take a stratum offset of that order, signed by the canopy (low vigour: lower is wetter), not zero.
- **Net effect, computed from l. 201 and 206-207:** under the net the sensors read 0.4 (lower), 1.1 (middle) and 0.9 h (upper) per day more than in the open, while the cited daily mean RH did not change. An RH-based wetness estimate cannot see this, so a net or other cover is a systematic wetness bias to represent, in the direction of more hours.
- **Against the engine's RH >= 90 % stand-in:** no comparison is made. The paper has no RH threshold and no reference station, so it gives the spread among strata, not the stand-in's error.
- **Kind of result:** a field measurement of one season; apple, not vine; the stratum order is canopy-dependent (it reversed at Ames).
