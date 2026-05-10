# Fluorescence Viability Imaging

Fluorescence viability imaging is widely used in cryobiology to evaluate:

- membrane integrity,
- metabolic activity,
- oxidative stress,
- and cryoinjury progression.

These methods are commonly integrated into:

- cryomicroscopy,
- confocal imaging,
- multiphoton microscopy,
- and computational image-analysis workflows.

---

# Common Fluorophores

## Propidium Iodide (PI)

Typical application:
- detection of membrane-compromised or non-viable cells.

Key features:
- nucleic acid intercalating dye,
- excluded by intact membranes,
- strong signal in damaged cells.

Considerations:
- spectral overlap with some orange/red fluorophores,
- excitation and emission compatibility must be considered.

---

## Calcein AM

Typical application:
- viable cell detection.

Key features:
- converted into fluorescent calcein in metabolically active cells,
- commonly paired with PI.

Potential limitations:
- variable loading efficiency,
- signal reduction under some cryogenic conditions.

---

## CellMask Orange

Typical application:
- plasma membrane labeling.

Key features:
- membrane visualization,
- structural imaging.

Potential limitations:
- spectral overlap with PI,
- fluorescence behavior may vary during freezing.

---

## DAPI

Typical application:
- nuclear staining.

Key features:
- DNA-binding dye,
- commonly used in fluorescence microscopy.

Potential limitations:
- weak or inconsistent signal in some multiphoton configurations.

---

## Monochlorobimane (mBCl)

Typical application:
- glutathione (GSH) imaging.

Key features:
- used for redox-state investigations,
- potential indicator of oxidative stress.

Potential limitations:
- weak signal under some multiphoton conditions,
- fluorescence sensitivity may vary with temperature.

---

# Cryogenic Fluorescence Considerations

Cryogenic conditions may affect:

- fluorescence intensity,
- photobleaching behavior,
- spectral separation,
- fluorophore stability,
- and membrane interactions.

Important considerations include:

- thermal equilibration,
- environmental stability,
- and condensation prevention.

---

# Multiphoton Compatibility

Representative excitation wavelengths:

| Excitation Wavelength | Typical Notes |
| --- | --- |
| 780 nm | Often associated with UV-equivalent excitation behavior |
| 920 nm | Common biological imaging wavelength |
| 1064 nm | Used for deeper imaging and reduced scattering |

Signal detection depends on:

- laser power,
- pulse characteristics,
- detector sensitivity,
- filter configuration,
- and fluorophore properties.

---

# Spectral Overlap and Filter Selection

Careful filter selection improves:

- signal separation,
- quantitative reproducibility,
- and image interpretation.

Potential issues:

- bleed-through,
- autofluorescence,
- and overlapping emission spectra.

---

# AI and Computational Analysis

Potential computational tasks:

- live/dead classification,
- fluorescence quantification,
- segmentation,
- signal colocalization,
- and temporal analysis.

Potential tools:

- Fiji/ImageJ
- napari
- Cellpose
- StarDist
- PyTorch workflows

---

# Future Directions

Emerging opportunities include:

- AI-assisted viability scoring,
- automated fluorescence interpretation,
- multimodal cryogenic imaging,
- redox-state mapping,
- and real-time cryoinjury analysis.
