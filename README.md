# UNSEEN: Counterfactual Intelligence for Auditing Systematic Media Omission

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linter: ruff](https://img.shields.io/badge/linter-ruff-red.svg)](https://github.com/astral-sh/ruff)
[![Academic Project: 27DSAI](https://img.shields.io/badge/Project%20ID-27DSAI-purple.svg)](#project-identity)

> **B.Sc. Graduation Project in Data Science and Artificial Intelligence (DSAI)**  
> **Applied Domain:** Media Intelligence, Computational Journalism, and Information Retrieval

---

## 1. Project Identity

| Attribute | Specification |
| :--- | :--- |
| **Project ID** | 27DSAI |
| **Project Name** | UNSEEN |
| **Full Academic Title** | **UNSEEN: Counterfactual Intelligence for Auditing Systematic Media Omission** |
| **Degree** | B.Sc. in Data Science and Artificial Intelligence (DSAI) |
| **Lead Researcher** | Mohamed Abdelwahab |
| **Domain** | Media Intelligence & Journalism Analytics |

---

## 2. Short Description

UNSEEN is an AI and Data Science research framework designed to detect statistically unexpected omissions and underreported real-world events across media outlets. Rather than assigning subjective bias labels to published text, UNSEEN pairs independent ground-truth event catalogs with historical news coverage to estimate outlet-specific expected coverage probabilities, auditing significant absences through counterfactual matched-event analysis, calibrated uncertainty estimation, and explainable anomaly detection.

---

## 3. Problem Statement

News organizations operate under bounded editorial attention, geographic scopes, and newsroom resources. Consequently, no media outlet can cover every occurrence in the world. Ordinary non-coverage is an inherent operational reality of journalism.

However, a critical challenge arises when trying to distinguish between:
1. **Ordinary Non-Coverage**: An event is not reported because it falls outside the outlet's geographic remit, lacks sufficient severity, or occurred during high-congestion domestic news cycles.
2. **Statistically Anomalous Omission**: An event that strongly matches an outlet's historical coverage patterns, topical priorities, and severity sensitivity receives unexpectedly low or zero coverage.

The central research inquiry of UNSEEN is:

$$\text{\textit{Can AI distinguish between ordinary non-coverage and statistically anomalous omission of important real-world events?}}$$

---

## 4. Why the Problem Matters

- **Information Ecosystem Integrity**: Media omissions define the public agenda just as powerfully as published headlines. Identifying neglected real-world crises is essential for informed democratic discourse.
- **Humanitarian Visibility**: Underreported humanitarian crises, localized environmental hazards, and human-rights developments often struggle to attract international relief because media attention remains concentrated in high-visibility regions.
- **Evidence-Based Media Accountability**: Shifts media critique away from qualitative accusations toward reproducible, transparent, and statistically grounded auditing frameworks.

---

## 5. Research Gap

> Existing research has studied media selection bias, news coverage prediction, and event-to-news matching. UNSEEN investigates a more specific research direction: whether outlet-specific expected-coverage models, independent real-world event data, counterfactual matched-event comparisons, uncertainty calibration, and explainable anomaly detection can be combined to identify statistically unusual media omissions.

This project approaches this hypothesis as a formal empirical research question rather than a proven novelty claim, systematically benchmarking predictive models against classical statistical and information-retrieval baselines.

---

## 6. Research Questions

- **RQ1 (Expected Coverage Estimation)**: Can historical outlet behavior and real-world event characteristics be used to estimate outlet-specific expected coverage probabilities $P(Y_{e,o} = 1 \mid \mathbf{x}_e, \mathbf{z}_o, \mathbf{c}_{e,o})$?
- **RQ2 (Anomalous Omission Discrimination)**: Can expected-coverage models distinguish ordinary non-coverage from statistically anomalous omission?
- **RQ3 (Counterfactual Matched-Event Analysis)**: Do counterfactual comparisons with similar real-world events improve the reliability and explainability of media blind-spot detection?
- **RQ4 (Calibration & Robustness)**: How well calibrated and robust are blind-spot predictions across outlets, event categories, regions, and time periods?

For formal hypotheses and statistical test designs, see [`docs/research_questions.md`](docs/research_questions.md).

---

## 7. High-Level Architecture

```
+---------------------------------------------------------------------------------+
|                                 UNSEEN PIPELINE                                 |
+---------------------------------------------------------------------------------+
   1. Independent Event Data Ingestion (EM-DAT, GDACS, ReliefWeb)
   2. News Article Collection & Metadata Normalization (Target Outlets)
   3. Event-Article Matching (BM25 Lexical + Dense Embeddings + Thresholding)
   4. Coverage Observation Matrix Construction (Event x Outlet Binary Labels)
   5. Expected Coverage Modeling (Hierarchical Logit, GBDTs, GLMs)
   6. Counterfactual / Matched-Event Analysis (Nearest-Neighbor Historical Twins)
   7. Anomaly Detection Engine (Residual & Probabilistic Tail Scoring)
   8. Uncertainty Estimation & Calibration (Platt Scaling, Isotonic Regression, ECE)
   9. Explainability & Evidence Extraction (SHAP Values + Case-Based Twins)
  10. Research Audit Interface (Interactive Diagnostic Exploration)
+---------------------------------------------------------------------------------+
```

For full architectural contracts and data schemas, see [`docs/architecture.md`](docs/architecture.md).

---

## 8. Main AI & Data Science Components

- **Information Retrieval & NLP**: Hybrid candidate retrieval combining lexical search (BM25) with dense multilingual sentence embeddings (`sentence-transformers`) and semantic cross-encoder verification.
- **Statistical & Hierarchical Modeling**: Mixed-effects logistic regression capturing outlet random effects, regional fixed effects, and temporal decay dynamics.
- **Machine Learning**: Gradient Boosted Decision Trees (LightGBM, XGBoost) for non-linear feature interactions across event severity, population density, and geographic proximity.
- **Counterfactual Inference**: Nearest-neighbor covariate matching and propensity-score matching across historical event distributions.
- **Uncertainty & Calibration**: Isotonic calibration, Platt scaling, and Expected Calibration Error (ECE) quantification to ensure probabilistic fidelity.
- **Explainable AI (XAI)**: SHAP-based feature attribution alongside case-based historical counterfactual comparisons.

---

## 9. Proposed Methodology

The framework models the conditional probability:

$$P(Y_{e,o} = 1 \mid \mathbf{x}_e, \mathbf{z}_o, \mathbf{c}_{e,o})$$

where:
- $\mathbf{x}_e$: Event attributes (hazard type, severity, fatalities, coordinates, affected population).
- $\mathbf{z}_o$: Outlet historical priors (geographic baseline coverage, topical distribution).
- $\mathbf{c}_{e,o}$: Contextual covariates (spatial distance to outlet headquarters, global news congestion index).

For detailed mathematical formulations and baseline algorithms, see [`docs/methodology.md`](docs/methodology.md).

---

## 10. Repository Structure

```text
UNSEEN/
│
├── README.md                      # Comprehensive academic project overview
├── LICENSE                        # MIT Open Source License
├── .gitignore                     # Git ignore rules for Python, data, and models
├── .env.example                   # Environment configuration template
├── requirements.txt               # Pinned project dependencies
├── pyproject.toml                 # Packaging, build system, and linter settings
│
├── configs/
│   ├── README.md                  # Configuration guidelines
│   └── default.yaml               # Baseline experiment hyperparameters
│
├── data/
│   ├── README.md                  # Data policy, licensing, and schema guide
│   ├── raw/                       # Unmodified source dumps (ignored by git)
│   ├── interim/                   # Geocoded and normalized intermediates
│   └── processed/                 # Final modeling matrices (event x outlet)
│
├── docs/
│   ├── project_overview.md        # Stakeholder context and academic positioning
│   ├── research_questions.md      # Formal hypotheses (RQ1-RQ4)
│   ├── methodology.md             # 10-stage pipeline and mathematical formulation
│   ├── architecture.md            # System contracts, interfaces, and data flow
│   ├── data_sources.md            # EM-DAT, GDACS, ReliefWeb specifications
│   ├── evaluation_plan.md         # Multi-tiered evaluation metrics and protocols
│   └── ethics_and_limitations.md  # Epistemic guidelines and responsible use
│
├── notebooks/
│   └── README.md                  # Guidelines for exploratory research notebooks
│
├── src/
│   └── unseen/
│       ├── __init__.py            # Package root and logging configuration
│       ├── data/                  # Ingestion loaders and Pydantic schemas
│       ├── retrieval/             # Lexical and dense candidate retrievers
│       ├── matching/              # Event-article semantic matcher protocols
│       ├── features/              # Spatial, temporal, and severity features
│       ├── models/                # Expected coverage predictor baselines
│       ├── counterfactual/        # Matched-event counterfactual engine
│       ├── anomaly/               # Residual anomaly scoring protocols
│       ├── calibration/           # Uncertainty calibrators and ECE estimation
│       ├── explainability/        # SHAP and case-based explanation builders
│       ├── evaluation/            # Brier score, ECE, and retrieval metrics
│       └── visualization/         # Reliability diagrams and coverage heatmaps
│
├── tests/
│   ├── README.md                  # Testing guidelines and execution instructions
│   ├── __init__.py
│   ├── conftest.py                # Test fixtures and synthetic entities
│   ├── test_package_structure.py  # Smoke tests for module imports
│   ├── test_schemas.py            # Validation tests for core data schemas
│   └── test_metrics.py            # Correctness tests for evaluation metrics
│
├── scripts/
│   ├── README.md                  # CLI script execution guide
│   └── verify_setup.py            # Self-contained environment verification script
│
├── reports/
│   ├── figures/                   # Generated publication figures (.gitkeep)
│   └── tables/                    # Generated experimental LaTeX tables (.gitkeep)
│
└── app/
    └── README.md                  # Specification for the future research dashboard
```

---

## 11. Current Project Status

- **Phase**: **Stage 0 — Research Repository Foundation & Engineering Architecture**
- Initial repository layout, typed schemas, testing suite, and academic documentation established.
- Core package interfaces and evaluation metric primitives verified.
- Initial experimental focus: **Natural disasters & critical humanitarian emergencies** (using EM-DAT, GDACS, and ReliefWeb ground-truth registries).

---

## 12. Installation & Setup

### Prerequisites
- Python 3.11+
- Virtual environment tool (`venv` or `conda`)

### Step-by-Step Installation

```bash
# 1. Clone repository
git clone https://github.com/Mohamed-Abdelwahab11/UNSEEN.git
cd UNSEEN

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Upgrade pip and install package with development dependencies
pip install --upgrade pip
pip install -e ".[dev]"

# 4. Configure local environment variables
cp .env.example .env

# 5. Run setup verification script
python scripts/verify_setup.py
```

---

## 13. Reproducibility Notes

- **Random Seed Control**: Global seed configured via `configs/default.yaml` (`random_seed: 42`) and propagated across NumPy, PyTorch, and Scikit-Learn components.
- **Temporal Split Integrity**: Evaluation uses strictly chronological data partitioning to prevent future-data contamination.
- **Data Policy**: Full news text is not redistributed in accordance with copyright law. All feature extraction workflows operate from reproducible acquisition scripts and standardized metadata schemas.

---

## 14. Ethics & Limitations

- **Absence $\ne$ Intentional Bias**: Statistical non-coverage reflects editorial selection relative to historical baselines, not malicious intent.
- **Uncertainty Transparency**: Predictions provide calibrated confidence intervals rather than definitive claims.
- **Ground-Truth Skew**: Disaster registries carry inherent reporting lags and regional sensor density imbalances that are explicitly accounted for in modeling.
- **Human Oversight**: High-stakes audit conclusions must be reviewed by qualified human researchers.

See [`docs/ethics_and_limitations.md`](docs/ethics_and_limitations.md) for full epistemological guidelines.

---

## 15. Roadmap

- [x] **Milestone 1**: Repository architecture, academic documentation, and schema specifications.
- [ ] **Milestone 2**: Ingestion adapters for EM-DAT and GDACS disaster event feeds.
- [ ] **Milestone 3**: Lexical and dense candidate article retrieval and semantic matcher benchmarking.
- [ ] **Milestone 4**: Historical coverage matrix construction across selected international and regional media panels.
- [ ] **Milestone 5**: Baseline expected coverage modeling (Logistic Regression, GLMs, LightGBM).
- [ ] **Milestone 6**: Counterfactual matched-event engine and residual anomaly detection implementation.
- [ ] **Milestone 7**: Probability calibration (Platt/Isotonic) and uncertainty evaluation.
- [ ] **Milestone 8**: XAI attribution module (SHAP feature importance and matched-case evidence).
- [ ] **Milestone 9**: Interactive research auditing dashboard.

---

## 16. Contributors & Academic Supervision

- **Lead Student Researcher**: Mohamed Abdelwahab ([GitHub](https://github.com/Mohamed-Abdelwahab11))
- **Degree Program**: B.Sc. in Data Science and Artificial Intelligence (DSAI)
- **Institution**: Department of Computer Science & AI

---

## 17. Academic Disclaimer

This software and research documentation are prepared as part of an academic Bachelor graduation project. The findings, model estimates, and anomaly scores produced by the UNSEEN framework represent statistical inferences derived from historical media observations and independent event catalogs. They do not constitute definitive legal, institutional, or ethical accusations against any media organization.
