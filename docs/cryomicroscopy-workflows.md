# Cryomicroscopy and imaging resources

A curated starting point for imaging cells, solutions, ice, and cryopreservation processes at low temperature. Use this guide to choose a modality, find a reproducible analysis tool, and record enough acquisition context for another researcher to interpret the result.

## Scope

Cryomicroscopy can refer to several different experimental families:

- **Low-temperature light microscopy:** observes samples during cooling, freezing, storage, or warming.
- **Cryogenic spectroscopy:** maps chemical or physical state at low temperature, for example with Raman microscopy.
- **Cryo-electron microscopy:** images vitrified or cryofixed structures in an electron microscope.

Cryo-EM is included as a related resource area, but it is not interchangeable with live-cell freezing microscopy. The preparation, scale, instrumentation, data formats, and scientific questions differ.

## How resources are selected

Prefer resources that provide at least one of the following:

- peer-reviewed methods or validation;
- openly accessible documentation;
- open-source software with a stable project page;
- public data with provenance and reuse terms;
- enough acquisition and analysis detail to reproduce the workflow.

A listed tool or paper is not an endorsement for a particular biological assay. Confirm suitability for the sample, objective, cryostage, temperature range, fluorophore, detector, and intended conclusion.

## Start with the scientific question

| Question | Useful starting modality | Critical evidence |
|---|---|---|
| When and where does ice appear? | Brightfield or phase-contrast video cryomicroscopy | Temperature, cooling rate, nucleation event, frame rate, spatial calibration |
| Does a membrane-integrity signal change during freezing? | Fluorescence cryomicroscopy | Dye controls, spectral settings, exposure, bleaching, temperature history |
| Where is a signal within a thick sample? | Confocal or multiphoton imaging | Optical sectioning settings, depth, scattering, power at sample, thermal drift |
| How are solutes or ice phases distributed? | Raman cryomicroscopy | Spectral calibration, peak assignment, spatial resolution, temperature |
| What ultrastructure is preserved after vitrification or cryofixation? | Cryo-EM or cryo-electron tomography | Preparation route, dose, defocus, reconstruction and validation |
| Can events be detected automatically? | Image analysis after validated acquisition | Ground truth, independent test data, error analysis, retained raw images |

## Brightfield and video cryomicroscopy

### What it supports

- freezing-front and ice-interface tracking;
- intracellular ice formation observations;
- cell-volume and morphology measurements;
- directional-freezing experiments;
- cooling and warming event timing.

### Foundational and methods papers

- [Toner et al. (1991), cryomicroscopic analysis of intracellular ice formation in mouse oocytes](https://pubmed.ncbi.nlm.nih.gov/2015761/) describes an optically improved cryostage and links intracellular ice formation to freezing conditions.
- [Acker et al. (1999), intracellular ice formation and cell interactions](https://pubmed.ncbi.nlm.nih.gov/10413578/) uses cryomicroscopy to examine prevalence and kinetics in interacting cells.
- [Stott et al. (2009), visualization of intracellular ice formation using high-speed video cryomicroscopy](https://pubmed.ncbi.nlm.nih.gov/19041300/) demonstrates why temporal resolution matters during rapid freezing.
- [Karlsson et al. (2015), measurement of intracellular ice formation kinetics](https://pubmed.ncbi.nlm.nih.gov/25428007/) provides a methods-focused description of high-speed video cryomicroscopy and kinetic analysis.
- [Yu et al. (2026), automated image analysis for intracellular ice detection](https://www.nature.com/articles/s44303-026-00181-8) presents a contemporary example of quantifying intracellular ice from cryomicroscopy images.

### Acquisition checks

Record:

- sample geometry and chamber thickness;
- objective, numerical aperture, illumination mode, camera, and pixel size;
- temperature-sensor type, position, calibration, and uncertainty;
- commanded and measured cooling and warming profiles;
- nucleation method and observed nucleation temperature;
- frame rate, exposure time, bit depth, and dropped frames;
- freezing-front position and motion where relevant;
- frost, condensation, focus drift, stage drift, and occlusion.

Do not infer sample temperature from the controller set point alone.

## Fluorescence cryomicroscopy

### What it supports

- membrane-integrity and permeability measurements;
- mitochondrial, oxidative-stress, or redox-associated signals;
- spatial localization of cryoinjury;
- comparison of pre-freeze, freezing, and post-thaw states.

### Controls and cautions

- Include unstained, single-stain, negative, and positive controls appropriate to the assay.
- Report staining concentration, incubation, washing, medium, and time from staining to imaging.
- Measure or report excitation power at the sample when possible.
- Keep exposure, gain, binning, and display scaling separate from biological interpretation.
- Check spectral overlap from the cryostage, window, medium, and fluorophores.
- Test photobleaching and phototoxicity under the actual time-lapse sequence.
- Treat temperature-dependent probe response as a potential confounder.
- Preserve single-channel source images even when a merged view is presented.

A fluorescence-positive region shows detected signal under stated conditions. It does not by itself prove viability, molecular mechanism, or causation.

## Confocal and multiphoton imaging

### What these modalities add

Confocal imaging can reject out-of-focus light and support optical sectioning. Multiphoton imaging can support deeper imaging and localized excitation in suitable samples. Neither modality automatically solves low signal, spectral mismatch, thermal drift, refractive-index change, or cryostage background.

### Planning checklist

- Confirm objective working distance and compatibility with the stage window and medium.
- Record excitation wavelength, emission filters, detector, gain, offset, dwell time, and averaging.
- Record z-step, pinhole setting, scan direction, and time per volume for confocal data.
- Record laser power at the sample across the tested range for multiphoton data.
- Check whether the selected fluorophore is detectably excited at the available wavelength.
- Measure background from the empty stage, window, medium, and unstained sample.
- Assess saturation, signal-to-noise ratio, bleaching, and visible damage.
- Verify that scan time is fast enough for the thermal or ice event being studied.
- Document focus and registration corrections instead of silently realigning data.

## Raman cryomicroscopy

### What it supports

- cryoprotectant and solute distribution;
- ice, glass, and crystalline-phase characterization;
- chemical changes without an added fluorescent label;
- spatially resolved quality-control measurements.

### Selected research examples

- [Yu et al. (2018), interfacial interactions of sucrose during cryopreservation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8023323/) uses low-temperature Raman spectroscopy to study sucrose, ice, and interfaces.
- [Dörr et al. (2012), noninvasive quality control of cryopreserved samples](https://pmc.ncbi.nlm.nih.gov/articles/PMC3698688/) demonstrates Raman detection of ice formation in vitrified samples.
- [Joules et al. (2025), Raman cryomicroscopy of cryopreservation damage in natural killer cells](https://www.sciencedirect.com/science/article/pii/S1465324925000350) maps chemical and ice-related changes in frozen cells.

### Reporting checks

Record:

- excitation wavelength and power at the sample;
- objective, grating, spectral resolution, and integration time;
- wavenumber calibration and background subtraction;
- cosmic-ray removal and preprocessing;
- temperature and thermal history for every spectrum or map;
- peak-assignment source and uncertainty;
- spatial sampling and registration with any companion image.

Avoid assigning a biological mechanism from a single spectral peak without controls or supporting evidence.

## Cryo-EM and cryo-electron tomography

### Distinction from light cryomicroscopy

Cryo-EM typically examines vitrified or cryofixed specimens under vacuum at cryogenic temperature. It is well suited to structural questions but does not normally record a living cell continuously through a freezing and thawing protocol.

### Public infrastructure

- [EMPIAR](https://www.ebi.ac.uk/empiar/) archives raw electron-microscopy images underpinning 3D cryo-EM maps and tomograms.
- [Electron Microscopy Data Bank](https://www.ebi.ac.uk/emdb/) archives reconstructed 3D electron-microscopy maps.
- [RELION](https://relion.readthedocs.io/) provides open-source workflows for single-particle analysis and tomography.
- [cryoSPARC Guide](https://guide.cryosparc.com/) documents a widely used cryo-EM processing environment. Check its current licensing and deployment requirements before use.

For training or benchmarking, preserve the link between raw images, processed particles or tilt series, reconstruction parameters, masks, and final maps.

## Open image formats and data management

### Standards and software

- [OME-TIFF](https://ome-model.readthedocs.io/en/stable/ome-tiff/) stores multidimensional image pixels with OME metadata.
- [OME-Zarr](https://ngff.openmicroscopy.org/latest/) supports cloud-friendly, chunked multidimensional bioimaging data.
- [Bio-Formats](https://bio-formats.readthedocs.io/) reads many proprietary microscopy formats and exposes their metadata.
- [OMERO](https://www.openmicroscopy.org/omero/) manages, visualizes, and annotates microscopy data.
- [Ten recommendations for organising bioimaging data](https://pmc.ncbi.nlm.nih.gov/articles/PMC10938051/) provides practical guidance for data organization and reuse.

Keep an unchanged archival copy of the source acquisition. Record any export, conversion, bit-depth change, channel selection, compression, or resampling.

## Public image and microscopy archives

- [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/) stores and distributes biological images associated with publications or broader reuse value.
- [Image Data Resource](https://idr.openmicroscopy.org/) integrates published reference imaging datasets for exploration and reuse.
- [EMPIAR](https://www.ebi.ac.uk/empiar/) is the specialist raw-image archive for electron microscopy.

Search terms such as “cryopreservation,” “freezing,” “ice formation,” “vitrification,” and the relevant cell type can help locate candidates. Before reuse, confirm the license, provenance, biological unit, acquisition metadata, controls, and whether train and test partitions can be kept independent.

## Open-source analysis tools

| Tool | Best starting use | Official resource |
|---|---|---|
| Fiji/ImageJ | Inspection, measurement, macros, time series and plugin workflows | [Fiji documentation](https://imagej.net/software/fiji/) |
| napari | Interactive multidimensional viewing and annotation in Python workflows | [napari documentation](https://napari.org/stable/) |
| scikit-image | Scripted image processing and reproducible Python analysis | [scikit-image documentation](https://scikit-image.org/docs/stable/) |
| ilastik | Interactive pixel and object classification | [ilastik documentation](https://www.ilastik.org/documentation/) |
| Cellpose | Generalist and fine-tuned instance segmentation | [Cellpose documentation](https://cellpose.readthedocs.io/en/latest/) |
| StarDist | Instance segmentation for approximately star-convex objects | [StarDist project](https://github.com/stardist/stardist) |
| TrackMate | Object tracking within Fiji | [TrackMate documentation](https://imagej.net/plugins/trackmate/) |
| OMERO | Image, metadata, annotation, and collaboration management | [OMERO documentation](https://omero.readthedocs.io/) |

Choose tools after defining the measurement target and ground truth. A visually convincing overlay is not sufficient validation.

## Reproducible image-analysis workflow

1. Preserve raw images and acquisition metadata.
2. Define the biological unit, image unit, endpoint, and exclusion criteria.
3. Create a read-only manifest linking each image to sample, acquisition session, condition, and controls.
4. Separate train, validation, and test data by the highest relevant biological grouping.
5. Develop preprocessing on copies and record every operation and parameter.
6. Annotate a calibration set independently and measure reviewer agreement.
7. Freeze the test set before model or threshold optimization.
8. Report object-level and image-level errors, including difficult and failed cases.
9. Retain software versions, environment files, code, random seeds, and model checksums.
10. Export results with image identifiers and units, not only summary figures.

Avoid splitting adjacent video frames, fields from one specimen, or repeated acquisitions from one sample across training and test sets.

## Minimum acquisition record

For each experiment, record:

- project and pseudonymous sample identifier;
- specimen type, preparation, cryoprotectant, and medium;
- staining and control details;
- microscope, objective, detector, stage, and window;
- excitation, emission, exposure, gain, bit depth, channels, and pixel size;
- temperature-sensor identity, position, calibration, and uncertainty;
- complete cooling, nucleation, hold, warming, and imaging timeline;
- filenames, acquisition software, and software version;
- deviations, missing metadata, artifacts, exclusions, and failed runs.

Use the repository's [reporting standards](reporting-standards.md) and [dataset template](../datasets/dataset-template.md) when preparing a reusable record.

## Before interpreting a result

Ask:

1. Was the signal measured at the stated temperature and time?
2. Could the stage, window, medium, detector, or processing create the feature?
3. Were appropriate controls imaged with identical settings?
4. Does the spatial and temporal resolution support the claim?
5. Were exclusions and failed acquisitions reported?
6. Is the analysis validated on independent biological data?
7. Can another researcher trace the result back to an unchanged source image?

## Related repository resources

- [Cryopreservation fundamentals](cryopreservation-fundamentals.md)
- [Cryoinjury](cryoinjury.md)
- [Cryostage engineering](cryostage-engineering.md)
- [Reporting standards](reporting-standards.md)
- [Troubleshooting guide](troubleshooting.md)
- [AI and computational cryobiology guide](../website/ai.md)
- [Dataset template](../datasets/dataset-template.md)
- [AI model card template](../software/model-card-template.md)

## Contribution guidance

When proposing a new resource, provide:

- full title and stable link;
- resource type and imaging modality;
- why it is useful for cryobiology;
- access and license status where known;
- validation or provenance evidence;
- known limitations.

Do not list a model, dataset, or workflow as validated solely because it is public or visually impressive.
