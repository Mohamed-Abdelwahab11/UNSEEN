# Data Governance & Storage Architecture

This directory manages ground-truth real-world event data and media coverage observations for the UNSEEN framework.

## Data Policy & Licensing Integrity

1. **No Copyrighted Article Bodies Committed**: To comply with media copyright, intellectual property law, and GitHub terms of service, full article texts or proprietary news scrapings are strictly excluded from version control via `.gitignore`.
2. **Metadata & Identifiers Only**: Publicly distributed datasets in this project contain event identifiers, standardized event attributes (type, geographic coordinates, severity, timestamp), news URLs, cryptographic hashes, and derived numerical feature representations.
3. **Reproducible Acquisition**: Ground-truth event catalogs and news metadata are ingested using reproducible extraction scripts located in `scripts/`.

## Directory Hierarchy

- `raw/`: Unmodified primary source dumps (e.g., raw CSV/JSON dumps from EM-DAT, GDACS RSS feeds, or ReliefWeb API records). All files except `.gitkeep` are ignored by git.
- `interim/`: Normalized intermediate schemas (e.g., standardized event records with geocoded coordinates, cleaned article metadata, tokenized lexical indices).
- `processed/`: Final modeling matrices (event × outlet observation matrices, feature-engineered tabular arrays, matched-pair evaluation splits).

## Primary Event Sources (MVP: Critical Humanitarian Events & Natural Disasters)

- **EM-DAT** (International Disaster Database - CRED): Global disaster database tracking dates, locations, fatalities, affected populations, and estimated damages.
- **GDACS** (Global Disaster Alert and Coordination System): Multi-hazard disaster monitoring (earthquakes, tsunamis, floods, tropical cyclones) with real-time severity alerts (Orange/Red alerts).
- **ReliefWeb API** (UN OCHA): Comprehensive humanitarian situation reports and event metadata.

For details on schema specifications and acquisition protocols, see [`docs/data_sources.md`](../docs/data_sources.md).
