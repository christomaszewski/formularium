---
id: sanchezdemiguel2011
citation: Sánchez-de-Miguel, P., Junquera, P., de la Fuente, M., Jiménez, L., Linares, R., Baeza, P. & Lissarrague, J. R. 2011. Estimation of vineyard leaf area by linear regression. Spanish Journal of Agricultural Research 9(1):202-212
doi: 10.5424/sjar/20110901-354-10 (OpenAlex; not printed in the paper)
read: 2026-10-14, in full, by a reading agent (claude-haiku-5-5); 71 of 75 quotes found at their lines by scripts/verify_quotes.py, the other 4 split across the two columns; pp. 205-206 (Eqs 1-7) and 208 (Tables 5-7) read in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Madrid, Toledo]
processes: [leaf area, allometry]
records: [sanchezdemiguel2011.shoot_leaf_area]
datasets: [sanchezdemiguel2011.madrid_toledo]
files: [patricia_2011.pdf]
---

# Sánchez-de-Miguel et al. 2011: leaf area per shoot from leaf count and leaf sizes

The Lopes & Pinto 2005 method refitted on 4,856 shoots of five cultivars at Madrid and
Toledo, with per-cultivar leaf-area-from-main-vein lines and the leaf sizes and counts per
shoot at flowering and ripening that the truth's susceptible-tissue piece can use.

## What it holds

- **Data:** El Socorro (Madrid, 730 m; Syrah/110R, Cabernet Sauvignon/SO4, Cabernet
  franc/140R, Merlot/140R, Tempranillo/110R) and a Toledo vineyard (488 m; Syrah/140R),
  2003-2007 as Table 1 lists them, though the text says three years (l. 20, 115-146).
  Shoots measured from late April to early October: 1,229 Syrah Toledo, 215 Syrah
  Madrid, 257 Cabernet franc, 1,689 Cabernet Sauvignon, 547 Merlot, 919 Tempranillo
  (l. 177-183).
- **Per-leaf lines** (p. 205, Eqs 1-5; 25 primary and 25 lateral leaves a cultivar): ILA
  (cm²) from main vein length MVL (cm): Cabernet franc 1.9077 MVL^1.803 (R² 0.93);
  Cabernet Sauvignon 0.38 + 1.21 MVL² (0.93); Merlot 18.291 MVL − 58.452 (0.86); Syrah
  21.41 MVL − 75.409 (0.94); Tempranillo 20.306 MVL − 69.302 (0.93).
- **Per-shoot lines** (p. 206, Eqs 6-7; `sanchezdemiguel2011.shoot_leaf_area`): with
  MLA = leaves per shoot × (largest + smallest leaf area)/2, log10 LAsh1 = 0.012 +
  0.996 log10 MLA1 (R² 0.98) for primary leaves and log10 LAsh2 = 0.036 + 0.982 log10
  MLA2 (0.99) for laterals. The page prints "LAsh = 10 × [...]", which read literally
  gives a tenth of the fitted area; the log10 regression of Table 3 and the 1:1 master
  curves (R² 0.945 and 0.948, l. 301) make it a power of ten.
- **Validation** (Tables 5-6, p. 208): estimated against sampled-sum areas per cultivar,
  slopes 0.89-1.08, MAPE 6.3-11.3 %, MAE 90-214 cm² a shoot.
- **Leaf sizes and counts** (Table 7, p. 208): mean primary leaf area and leaves per
  primary shoot at flowering: Cabernet Sauvignon 96 cm², 20; Merlot 118, 17; Syrah 183, 12;
  Tempranillo 141, 12. At ripening: Cabernet franc 118, 17; Cabernet Sauvignon 98, 17;
  Merlot 114, 25; Syrah 173, 12; Tempranillo 144, 14. Lateral leaves are 40-71 cm² with
  3-36 a shoot. Lateral leaves 22-44 % of a vine's area (l. 80, cited).

## Dependence

- **Borrows** the form of Lopes & Pinto 2005 (Vitis 44:55-61, cited; read 2026-10-26 as
  `lopes2005.shoot_leaf_area`: natural logs there, base-10 powers here) and refits it;
  the reference areas come from this paper's own Eqs 1-5. Four authors (Baeza, Linares,
  Junquera, Lissarrague) recur in the Madrid theses read the same day. Nothing
  engine-related.

## Bearing (2026-10-14)

- **Allometry, independent of the engine:** no time or temperature term. It turns a leaf
  count and two leaf sizes into leaf area per shoot, and Table 7 gives the leaf size a
  first Plasmopara infection meets at flowering in Tempranillo and Syrah. Read for the
  truth growth search.
