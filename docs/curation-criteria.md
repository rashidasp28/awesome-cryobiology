# Curation Criteria

This document defines the quality standards used for selecting and retaining resources in Awesome Cryobiology.

## Repository philosophy

The goal is not to collect the largest number of links. The goal is to curate resources that are:

- scientifically valuable,
- educationally useful,
- reproducible,
- practically relevant,
- and described in proportion to the available evidence.

Quality is prioritized over quantity. Inclusion is not an endorsement of every claim made by a resource.

## Core evaluation criteria

### Scientific credibility

Prefer resources from credible journals, institutions, archives, standards bodies, or well-documented technical communities. Claims should be technically accurate and traceable to primary evidence where possible.

### Educational value

A resource should help readers understand a concept, reproduce a workflow, compare methods, or make a better scientific or engineering decision.

### Reproducibility

Give preference to resources that provide enough detail for independent use or evaluation, such as:

- protocols and operating conditions,
- acquisition and calibration metadata,
- source data and analysis code,
- software versions and dependency records,
- automated tests,
- validation datasets,
- or documented limitations.

### Accessibility

Prefer stable, public links and open-access or open-source materials. A paywalled resource may still be valuable when it is uniquely authoritative, but its access limits should be clear.

### Licensing and reuse

Figures, datasets, code, hardware designs, and educational materials should state their licence or reuse terms. A public download alone does not establish permission to reuse the material.

## Evidence classification

Reviewers should identify the strongest evidence supporting a resource and describe it accurately.

| Classification | Typical evidence | Appropriate description |
| --- | --- | --- |
| Established | Peer-reviewed findings, standards, consensus guidance, or independent replication | State the supported use and scope |
| Validated | Documented methods plus relevant experimental or benchmark validation | Summarize the validation and important limits |
| Reproducible | Public code or data, pinned dependencies, tests, and repeatable releases | Describe what can be reproduced and under which conditions |
| Preliminary | Preprint, early dataset, prototype, or author-only validation | Label it preliminary and avoid general claims |
| Conceptual | Educational model, simulation, design sketch, or unvalidated proposal | Label it conceptual and do not present outputs as measured evidence |

A resource may fit more than one row. Use the least mature classification that fairly describes the claim being highlighted.

## Resource-specific checks

### Papers and reviews

Confirm the publication record, DOI or other permanent identifier, study type, and whether the cited conclusion matches the source. Distinguish peer-reviewed articles from preprints.

### Protocols

Look for specimen or cell type, cryoprotectant composition, thermal profile, equipment, controls, outcome measures, and known failure conditions. Do not imply that a protocol transfers safely between biological systems without validation.

### Datasets

Check provenance, consent or ethical restrictions where relevant, acquisition conditions, calibration, annotations, splits, licence, and a stable identifier. Note whether the dataset is suitable for independent validation or only method development.

### Software and AI models

Check for a documented interface, licence, versioned releases, dependency reproducibility, automated tests, example data, and validation beyond the developers' own data. Model performance should name the dataset, split strategy, metric, and important limitations. Avoid claims based on data leakage or non-independent test sets.

### Open hardware

Check the bill of materials, schematics, firmware, assembly and calibration procedures, measurement uncertainty, safety boundaries, and validation against a reference instrument. A prototype should not be described as a validated instrument.

### Figures and educational material

Confirm attribution, licence, scientific accuracy, readable labels, accessible alternatives, and a clear distinction between measured data, simulation, and illustration.

## Conflicts of interest and promotional content

Contributors should disclose affiliation with a proposed resource. Affiliation does not prevent inclusion, but self-authored or commercial resources require the same evidence review as independent submissions. Marketing language, unsupported performance claims, and testimonials are not validation.

## Decision record

A resource addition should make the review decision understandable from the pull request or issue. Record:

1. why the resource is relevant;
2. its evidence classification;
3. what was independently checked;
4. access and licensing status;
5. important limitations or conflicts;
6. the section where it belongs; and
7. any follow-up or recheck date.

If key information cannot be verified, defer inclusion rather than silently filling the gap.

## Reassessment and removal

Recheck a resource when a link breaks, a project becomes inactive, a correction or retraction appears, licensing changes, validation claims change, or a stable replacement becomes available. Remove or relabel resources that no longer meet the criteria, preserving a short rationale in the pull request history.

## Discouraged content

The following are discouraged:

- broken or unstable links,
- duplicate resources,
- unverified scientific or performance claims,
- poorly documented repositories,
- inaccessible commercial material without unique educational value,
- AI-generated scientific content without expert validation,
- prototypes presented as established tools,
- and resources with unclear provenance or reuse rights.

## Long-term goal

Awesome Cryobiology aims to become a trusted, reproducibility-focused, and collaborative resource for cryobiology and cryomicroscopy.
