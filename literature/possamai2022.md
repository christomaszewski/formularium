---
id: possamai2022
citation: Possamai, T. & Wiedemann-Merdinoglu, S. 2022. Phenotyping for QTL identification: a case study of resistance to Plasmopara viticola and Erysiphe necator in grapevine. Frontiers in Plant Science 13:930954
doi: 10.3389/fpls.2022.930954
read: 2026-10-25, lightly: the plant-material passages on organ age (l. 335-372 and 676-705), the first page and the Kennelly entries in the reference list; Tables 6 and 7 and the rest not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [general]
processes: [susceptibility, leaf age, ontogenic resistance, phenotyping, leaf disc bioassay, berry and rachis window, stomata]
records: []
datasets: []
files: [dr1025_possamai2022.pdf (the 2026-10-25 drop)]
---

# Possamai & Wiedemann-Merdinoglu 2022: a review of how resistance to downy and powdery mildew is phenotyped, with short statements on organ age

A methods review for QTL work on Rpv, Ren and Run loci; it has no data of its own, and its statements on organ age are citations.

**Read this first.**
- **A review: no measurement here.** Every statement below on when organs can be infected, and on ontogenic resistance, is cited from other papers. None is the authors' own data. What is the review's own is its survey of protocols, for example that leaves "are usually collected according to their position along the shoot" to avoid ontogenic resistance (l. 686-688), which it supports with example citations and Table 7 (not read).
- **The statement on very young leaves is not supported by its citation.** The review says young tissue is more susceptible "with the exception of very early leaves to P. viticola because of low stomata receptivity" and cites Kennelly et al. 2007 (l. 353-356). The cited paper is Phytopathology 97:512-522 (reference list, l. 1389-1392). The held record of that paper (`kennelly2007`) says shoots were susceptible from E-L stage 5, which is bud break. The same authors' 2007 Plant Health Progress summary (`kennelly2007php`) says shoots "are susceptible almost as soon as they begin to grow" and that "Host susceptibility, per se, does not limit infection before E&L stage 12" (l. 119-122 of its text). Nothing the strand held gives low stomata receptivity of very early leaves. The review's wording is "low stomata receptivity"; it does not say "no functional stomata". Do not use the sentence as evidence for a host threshold.
- **Powdery mildew mixed in.** The review treats downy and powdery mildew together; several leaf-age statements are for Erysiphe necator and are analogues here.

## What it holds

- **Organ age, general (cited):** resistance phenotype depends on the organ's development stage, physiology and source-sink relations (l. 351-353; the review's framing, no citation on this sentence). "Young tissue shows higher susceptibility to DM and PM" with the one exception above, cited to Kennelly et al. 2007 (l. 353-356). Old tissue "shows ontogenic resistance", cited to Delp 1954, Kennelly et al. 2005 and Develey-Rivière and Galiana 2007 (l. 356-358).
- **Leaf ontogenic resistance (cited, powdery mildew):** leaves are less susceptible to E. necator after the sink-to-source transition, cited to Doster and Schnathorst 1985 and Calonnec et al. 2018 (l. 358-361). The process "is promoted by stress and appears to be cultivar-dependent" (l. 364-366, cited), and the gain is considered higher in partially resistant cultivars (l. 366-368, cited to Peros et al. 2006). No downy mildew leaf-age curve or day count is given.
- **Berries and rachises (cited from Kennelly et al. 2005):** "Grape berries and rachises are receptive to DM until stomata convert to lenticels, 4-6 weeks post-bloom" (l. 368-370). The reading agent notes that kennelly2005 gives berries about 1 to 2 weeks and pedicels 4 weeks, so this summary is looser than its source. For powdery mildew, berries are receptive until 8 % sugar (l. 370-371, cited to Delp 1954 and Gadoury et al. 2003).
- **Leaf position in protocols (the review's survey, examples cited):** leaves are usually collected by position along the shoot to avoid ontogenic resistance (l. 686-688, Table 7). Young leaves for laboratory bioassays come from plants grown under optimal conditions, in greenhouse or vineyard (l. 682-686).
- **Powdery mildew analogue (cited):** maximal susceptibility to E. necator is "conserved up to the fourth to fifth unfolded leaf on cuttings" (Merry et al. 2013) and up to the second to third leaf on vineyard shoots (Barba et al. 2015; Calonnec et al. 2018) (l. 689-692). Merry et al. 2013 and Barba et al. 2015 were not obtained.
- **Stress and vigour (cited):** temperatures below 8 degC, nutrient deficiency and drought are said to reduce the development and susceptibility of organs and delay epidemics (l. 332-337, cited to Moyer, Keller and Heyman). Cultural strategies and stimulated growth are said to raise leaf and berry susceptibility (l. 348-350, cited to Fernandes de Oliveira et al. 2021).

## Dependence

- **Builds on, as it says:** the papers cited at each statement, listed above; Kennelly et al. 2005 and 2007 and Calonnec et al. 2018 are held in Formularium. It computes no model and holds no data of its own on organ age.
- **Authors:** Wiedemann-Merdinoglu is at the Colmar unit that also produced the poster `poutaraud2010`, which this review does not cite (no match in its text). A shared unit is a flag only.

## Bearing (2026-10-25)

- **Decision 19 (shoots infectable from budburst, against the engine's 10 cm or four unfolded leaves):** the review offers a statement that very early leaves resist, but it is a citation, and its cited paper and the same group's summary say the opposite (shoots susceptible from E-L stage 5 or bud break). So it supports no host-side threshold. Kind of result: a second-hand statement from a review.
- **Leaf ontogenic resistance (the truth has no leaf cohorts):** supports only the direction: older tissue is less susceptible. It gives no window in days or leaves for P. viticola on V. vinifera. The only leaf-count figures (fourth to fifth and second to third leaf) are for powdery mildew: an analogue, not to be moved to downy mildew.
- **host.inflorescence_after_budburst_days (25 d, assumed):** not addressed.
- **host.rachis_only_factor (0.3, assumed):** not addressed as a ratio. Its "4-6 weeks post-bloom" for berries and rachises is looser than its source and gives no share of whole-bunch infection. Do not take it for the window or the factor; use `kennelly2005`.
