# UNSEEN Research Interface & Auditing Dashboard

This directory is designated for the interactive web-based auditing interface planned for **Milestone 9** of the UNSEEN roadmap.

## Purpose

The UNSEEN research dashboard will serve as a specialized analytical cockpit for journalism scholars, media accountability researchers, and human-rights analysts to audit, visualize, and explain detected media omissions.

## Architectural Specification (Planned)

The interface will provide three core analytical views:

1. **Global Media Blind-Spot Map**:
   - Geospatial visualization of cataloged real-world events.
   - Interactive filtering by hazard type, severity threshold, and date range.
   - Color-coded coverage density and unexpected omission flags.

2. **Outlet Comparative Auditor**:
   - Outlet-specific expected coverage probability versus observed coverage status.
   - Calibrated confidence intervals and historical coverage distribution plots.
   - Direct breakdown of ordinary non-coverage vs. statistically anomalous omission.

3. **Counterfactual Case Inspector**:
   - Detailed side-by-side comparison between an audited omission and its nearest-neighbor historical twins.
   - Transparent feature attributions (SHAP values) explaining why coverage was expected.
   - Direct links to source event registries and matched articles.

## Development Note

Per the UNSEEN research engineering guidelines, the dashboard implementation will commence only after the core data ingestion, semantic matching, probabilistic modeling, calibration, and counterfactual matching engines are fully trained and validated in Python.
