# System Architecture & Component Design

The UNSEEN software architecture is structured around modular, loosely coupled components following strict interfaces and dependency inversion principles.

---

## 1. Architectural Layers

```
+---------------------------------------------------------------------------+
|                          PRESENTATION / AUDIT                             |
|               (CLI Scripts, Future Interactive Web Dashboard)             |
+---------------------------------------------------------------------------+
                                     ^
                                     |
+---------------------------------------------------------------------------+
|                       EXPLAINABILITY & CALIBRATION                        |
|       (SHAP Feature Attribution, Matched-Event Evidence, ECE Calibrator)   |
+---------------------------------------------------------------------------+
                                     ^
                                     |
+---------------------------------------------------------------------------+
|                   COUNTERFACTUAL & ANOMALY DETECTION                      |
|         (Nearest-Neighbor Twins C(e), Residual Dev. Scoring Engine)       |
+---------------------------------------------------------------------------+
                                     ^
                                     |
+---------------------------------------------------------------------------+
|                     EXPECTED COVERAGE PREDICTORS                          |
|         (Hierarchical Logit, GBDT, Mixed-Effects Coverage Regressor)      |
+---------------------------------------------------------------------------+
                                     ^
                                     |
+---------------------------------------------------------------------------+
|                 FEATURE ENGINEERING & MATRIX CONSTRUCTION                 |
|       (Spatial Proximity, Topic Affinity, Severity Index, Time Decay)     |
+---------------------------------------------------------------------------+
                                     ^
                                     |
+---------------------------------------------------------------------------+
|                    RETRIEVAL & EVENT-ARTICLE MATCHING                     |
|           (BM25 Lexical + Dense Embeddings + Cross-Encoder Reranker)      |
+---------------------------------------------------------------------------+
                                     ^
                                     |
+---------------------------------------------------------------------------+
|                       DATA INGESTION & NORMALIZATION                      |
|     (EM-DAT, GDACS, ReliefWeb Parsers, News Metadata Loaders, Schemas)    |
+---------------------------------------------------------------------------+
```

---

## 2. Directory Mapping & Separation of Concerns

All core logic resides within the `src/unseen/` package namespace:

| Module Path | Primary Responsibility | Key Classes / Protocols |
| :--- | :--- | :--- |
| `src/unseen/data/` | Ingestion, validation, standardized dataclasses | `RealWorldEvent`, `NewsArticle`, `MediaOutlet`, `CoverageObservation` |
| `src/unseen/retrieval/` | High-recall article filtering for events | `BaseEventArticleRetriever`, `BM25Retriever`, `DenseRetriever` |
| `src/unseen/matching/` | High-precision event-article pair verification | `BaseEventArticleMatcher`, `SemanticMatcher` |
| `src/unseen/features/` | Spatial, temporal, severity, and outlet feature engineering | `BaseFeatureExtractor`, `EventOutletFeatureBuilder` |
| `src/unseen/models/` | Probabilistic expected coverage modeling | `BaseCoverageModel`, `LogisticCoverageModel`, `GBDTCoverageModel` |
| `src/unseen/counterfactual/` | Finding historical matched events and estimating twin coverage | `BaseCounterfactualAuditor`, `MatchedEventCounterfactual` |
| `src/unseen/anomaly/` | Identifying unexpected non-coverage residuals | `BaseAnomalyDetector`, `ResidualAnomalyDetector` |
| `src/unseen/calibration/` | Post-hoc uncertainty estimation and probability calibration | `BaseCalibrator`, `IsotonicCalibrator`, `PlattCalibrator` |
| `src/unseen/explainability/` | Case-based and feature-based audit explanations | `BaseOmissionExplainer`, `CounterfactualExplainer` |
| `src/unseen/evaluation/` | Performance, calibration, and audit ranking metrics | `compute_brier_score`, `compute_ece`, `evaluate_retrieval` |
| `src/unseen/visualization/` | Diagnostic charts, calibration plots, coverage heatmaps | `plot_reliability_curve`, `plot_coverage_matrix` |

---

## 3. Data Contracts and Schemas

All inter-module communications use strongly typed data objects defined in `src/unseen/data/schemas.py`:

- **`RealWorldEvent`**: Contains standard unique identifier `event_id`, date `timestamp`, `event_type`, geocoded coordinates `(latitude, longitude)`, `country_code`, and quantitative indicators (e.g., `severity_score`, `fatalities`, `affected_population`).
- **`NewsArticle`**: Contains `article_id`, publication timestamp `published_at`, `outlet_id`, `headline`, `lead_paragraph`, `url`, and metadata.
- **`MediaOutlet`**: Defines `outlet_id`, `name`, `home_country`, `geographic_scope` (national, regional, international), and topical focus vectors.
- **`CoverageObservation`**: Encapsulates the resolved pair `(event_id, outlet_id)` with boolean flag `covered`, list of matched `article_ids`, and max matching similarity score.
- **`BlindSpotCandidate`**: Output of the anomaly detection engine containing `event_id`, `outlet_id`, `expected_prob`, `calibrated_prob`, `anomaly_score`, `confidence_interval`, and `counterfactual_twins`.

---

## 4. Design Principles

1. **Explicit Uncertainty**: No probabilistic prediction is consumed downstream without calibration and confidence intervals.
2. **Deterministic Reproducibility**: All modeling, feature partitioning, and sampling functions accept a configured random seed.
3. **No External Service Lock-In**: Baseline models and pipelines run offline with zero dependence on paid proprietary LLM APIs.
