# AI and Computational Cryobiology

Artificial intelligence can support cryobiology when the biological question, acquisition conditions, and validation plan are defined before model selection. This guide maps common cryobiology tasks to practical tools and minimum evidence requirements.

## Application map

| Cryobiology task | Typical input | Useful approach | Minimum validation |
| --- | --- | --- | --- |
| Cell or organelle segmentation | Brightfield, fluorescence, confocal, or multiphoton images | Instance or semantic segmentation | Expert-reviewed masks, Dice or IoU, object-level error review |
| Ice crystal segmentation | Cryomicroscopy images or videos | Semantic segmentation plus morphology measurements | Boundary agreement, crystal-size error, temporal consistency |
| Viability classification | Validated fluorescence channels | Supervised classification after cell detection | Per-class sensitivity and specificity against assay-supported labels |
| Sperm tracking | Time-lapse videos | Detection, linking, and trajectory filtering | Identity switches, track completeness, motility error |
| Cryoinjury prediction | Images, thermal histories, assay results, or omics | Classification, regression, or multimodal models | Donor- or sample-level held-out testing and calibrated uncertainty |
| Thermal prediction | Temperature sensors, stage geometry, and boundary conditions | Physics-based simulation, surrogate modeling, or hybrid models | Comparison with independent sensor measurements |
| Anomaly detection | Images, sensor traces, or instrument logs | Unsupervised or one-class models | Expert review of false alarms and missed events |

## Recommended workflow

1. **Define the scientific question.** State the biological unit, outcome, imaging modality, and intended use.
2. **Preserve raw data.** Keep original pixel values and acquisition files immutable. Perform derived processing in versioned outputs.
3. **Create a data inventory.** Record specimens, biological replicates, technical replicates, controls, channels, dimensions, bit depth, calibration, and thermal conditions.
4. **Write annotation rules.** Define class boundaries, ambiguous cases, exclusion criteria, and quality-control checks before annotation begins.
5. **Establish a simple baseline.** Compare AI methods with thresholding, classical image processing, or a simple statistical model.
6. **Split by biological unit.** Keep images or frames from the same donor, sample, straw, experiment, or video in one data partition to prevent leakage.
7. **Train and tune reproducibly.** Record software versions, random seeds, parameters, preprocessing, hardware, and model checkpoints.
8. **Evaluate beyond one metric.** Report class-specific errors, uncertainty, failure cases, and performance across acquisition conditions.
9. **Review outputs scientifically.** Confirm that predicted labels do not exceed what the staining protocol or measurement can support.
10. **Document intended use and limits.** Use the repository's [AI model card template](../software/model-card-template.md).

## Tool selection

### General bioimage inspection and annotation

- [Fiji/ImageJ](https://imagej.net/software/fiji/) supports established microscopy inspection and measurement workflows.
- [napari](https://napari.org/stable/) provides interactive multidimensional image viewing, annotation, and plugin-based analysis.
- [ilastik](https://www.ilastik.org/) offers interactive machine-learning workflows that can provide strong low-code baselines.

### Cell and object segmentation

- [Cellpose](https://www.cellpose.org/) provides generalist cell-segmentation models and supports custom training.
- [StarDist](https://github.com/stardist/stardist) is suitable for approximately star-convex objects, including many nuclei and compact cells.
- [DeepCell](https://deepcell.readthedocs.io/) provides deep-learning tools for cellular image analysis.
- [Segment Anything 2](https://github.com/facebookresearch/sam2) can assist interactive image and video segmentation, but cryobiology-specific validation remains essential.
- [Ultralytics YOLO](https://docs.ultralytics.com/) supports detection, segmentation, classification, and tracking workflows.

Tool popularity is not evidence of suitability. Selection should follow object geometry, image quality, annotation volume, deployment requirements, and validation performance.

## Task-specific guidance

### Cell segmentation

Report object-level false positives, missed cells, merged objects, split objects, and performance across fluorescence intensity ranges. For sperm images, evaluate the head, midpiece, and tail separately when the scientific question depends on those structures.

### Ice crystal analysis

Validate both boundaries and derived measurements such as area, equivalent diameter, aspect ratio, number density, and growth rate. Record temperature, cooling or warming rate, elapsed time, optical scale, and field position. Separate genuine crystals from frost, debris, bubbles, and illumination artefacts.

### Viability classification

Use labels supported by the assay rather than visually inferred biological states. For example, propidium iodide supports classification of membrane-compromised cells under the validated protocol. A model should not convert that observation into unsupported claims about fertility or overall cellular function.

### Sperm tracking

Evaluate track completeness, identity switches, missed detections, and frame-rate sensitivity. Report how immotile cells, collisions, cells leaving the field, and overlapping trajectories are handled. Do not treat multiple frames from one video as independent biological replicates.

### Cryoinjury and thermal prediction

Combine image features with thermal history only when timing and sample identifiers are synchronized. Compare learned models with physically meaningful baselines. Validate thermal predictions against independent sensor data and report where spatial interpolation or boundary assumptions are used.

## Dataset and evaluation requirements

A reusable dataset description should include:

- species, cell or tissue type, and preparation method
- number of donors, samples, experiments, fields, images, and videos
- imaging modality, objective, detector, excitation and emission settings
- cooling and warming rates, cryoprotectant conditions, and storage history
- raw file format, bit depth, spatial calibration, frame rate, and channel order
- annotation protocol, annotator expertise, adjudication, and inter-rater agreement
- data-partition rule and confirmation that related observations do not cross partitions
- licensing, consent, privacy, and reuse constraints

Use the [dataset template](../datasets/dataset-template.md) to record these details.

### Suggested metrics

- **Segmentation:** Dice, IoU, precision, recall, object count error, and boundary error
- **Classification:** sensitivity, specificity, precision, recall, F1, ROC-AUC where appropriate, and calibration
- **Tracking:** identity switches, track completeness, trajectory error, and motility-measurement error
- **Regression:** MAE, RMSE, bias, confidence intervals, and error across the measurement range
- **Thermal models:** sensor-level error, spatial error, transient response error, and uncertainty

Always pair summary metrics with representative failure cases and stratified results.

## Reproducibility checklist

- [ ] Raw data remain unchanged
- [ ] Biological and technical replicates are distinguished
- [ ] Controls and acquisition metadata are documented
- [ ] Annotation rules and exclusion criteria are available
- [ ] Data splitting occurs at the biological-unit level
- [ ] A simple baseline is reported
- [ ] Software versions, seeds, and parameters are recorded
- [ ] Metrics match the scientific task
- [ ] External or prospectively collected data are used when available
- [ ] Limitations and intended use are documented in a model card

## Contribution priorities

High-value additions include:

- openly licensed cryobiology benchmark datasets
- validated annotation protocols
- reproducible notebooks using non-sensitive example data
- comparisons between classical and deep-learning methods
- failure-case collections across imaging systems
- model cards with external validation
- physics-informed or hybrid thermal models

Resources should meet the repository's [curation criteria](../docs/curation-criteria.md). Avoid unsupported biological claims, unclear licensing, private data, unvalidated leaderboards, and workflows that cannot distinguish biological from technical replication.
