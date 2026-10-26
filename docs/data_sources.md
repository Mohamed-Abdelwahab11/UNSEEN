# Independent Data Sources & Event Catalogs

The UNSEEN methodology hinges on comparing media output against independent, non-media ground-truth event repositories. This document outlines the primary data sources for the initial research domain (Natural Disasters & Humanitarian Emergencies) and future extensions.

---

## 1. Ground-Truth Event Registries (Initial Scope)

To ensure that the reference reality is free from journalistic selection bias, UNSEEN utilizes established scientific, intergovernmental, and non-governmental disaster monitoring databases:

### A. EM-DAT (The International Disaster Database)
- **Institution**: Centre for Research on the Epidemiology of Disasters (CRED), UCLouvain, Belgium.
- **Coverage**: Global natural and technological disasters from 1900 to present.
- **Inclusion Criteria**: Meets at least one of:
  - $\ge 10$ people reported killed
  - $\ge 100$ people reported affected
  - Declaration of a state of emergency
  - Call for international assistance
- **Key Attributes**: Event ID, Disaster Type, Sub-type, ISO Country, Start Date, End Date, Total Deaths, Injured, Affected, Homeless, Estimated Economic Damage (USD).
- **Access Protocol**: Academic research extract via CRED licensing agreement.

### B. GDACS (Global Disaster Alert and Coordination System)
- **Institution**: Joint initiative of the United Nations (UN OCHA) and the European Commission.
- **Coverage**: Real-time disaster alerts for earthquakes, tsunamis, tropical cyclones, floods, volcanoes, and droughts.
- **Key Attributes**: Alert Level (Green, Orange, Red), Hazard Magnitude, Affected Population within buffer zones, Geolocation polygons, Alert Timestamps.
- **Access Protocol**: Structured RSS/XML and JSON feeds (`https://www.gdacs.org/`).

### C. ReliefWeb API
- **Institution**: United Nations Office for the Coordination of Humanitarian Affairs (UN OCHA).
- **Coverage**: Situational reports, humanitarian disasters, and crisis appeals globally.
- **Key Attributes**: Disaster Name, Primary Country, Disaster Type, Glide Number, Status, Description.
- **Access Protocol**: Public REST API (`https://api.reliefweb.int/v1/disasters`).

---

## 2. News Article Repositories & Media Corpus

For evaluating outlet-specific coverage, UNSEEN structures news ingestion across a curated panel of media organizations representing distinct geographic scopes (international wire services, national public broadcasters, regional newspapers, commercial outlets):

- **Panel Archetypes**:
  - Global wires (e.g., Reuters, Associated Press)
  - Public broadcasters (e.g., BBC, Deutsche Welle, NPR)
  - Regional / Continental outlets across diverse geographic locations
- **Ingested Fields**:
  - `article_id`: Unique cryptographic hash (e.g., SHA-256 of canonical URL)
  - `outlet_id`: Standardized outlet identifier
  - `published_at`: UTC timestamp of publication
  - `headline`: Title string
  - `lead_paragraph`: Initial summary or snippet
  - `url`: Canonical article link

---

## 3. Copyright Protection & Data Ethics Policy

1. **Zero Text Redistribution**: The UNSEEN GitHub repository contains **no proprietary article text**.
2. **Derived Representations**: Modeling relies on extracted numerical features (TF-IDF vectors, dense embeddings, metadata flags, sentiment neutrality scores).
3. **Data Acquisition Reproducibility**: Scripts in `scripts/` provide automated ingestion workflows for researchers possessing appropriate institutional API access or data subscriptions.
