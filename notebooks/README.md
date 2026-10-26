# Exploratory Research Notebooks

This directory is designated for experimental prototyping, diagnostic visualizations, and exploratory data analysis (EDA).

## Notebook Naming Conventions

Notebooks should follow a sequential, structured naming convention:

1. `01_event_data_ingestion.ipynb`: Exploratory inspection and validation of EM-DAT, GDACS, and ReliefWeb event catalogs.
2. `02_news_corpus_profiling.ipynb`: Analysis of monitored news outlet panels, article volume distributions, and metadata completeness.
3. `03_retrieval_and_matching_evaluation.ipynb`: Benchmarking lexical (BM25) and dense semantic retrieval models against ground-truth event-article pairs.
4. `04_coverage_matrix_construction.ipynb`: Generation and statistical profiling of the event × outlet coverage matrix.
5. `05_expected_coverage_modeling.ipynb`: Baseline modeling experiments (Logistic Regression, Mixed-Effects, LightGBM).
6. `06_counterfactual_matching_analysis.ipynb`: Nearest-neighbor event matching and counterfactual twin cohort exploration.
7. `07_anomaly_detection_and_calibration.ipynb`: Evaluation of residual anomaly thresholds, ECE, and reliability diagrams.
8. `08_case_studies_and_explainability.ipynb`: In-depth qualitative audits of detected blind spots and SHAP feature attributions.

## Hygiene Guidelines

- **Clear Outputs**: Strip heavy outputs and plot caches before pushing commits to prevent repository bloat (`nbstripout` recommended).
- **No Hard-Coded Credentials**: Load API tokens and file paths exclusively via environment variables or `configs/default.yaml`.
- **Reproducibility**: Always initialize seeds at the top cell:
  ```python
  import random
  import numpy as np
  RANDOM_SEED = 42
  random.seed(RANDOM_SEED)
  np.random.seed(RANDOM_SEED)
  ```
