# Research Methodology

The UNSEEN methodology formalizes the detection of statistically unexpected media omissions as an end-to-end data science and machine learning pipeline operating across 10 structured stages.

---

## 1. Mathematical Formulation

Let $\mathcal{E} = \{e_1, e_2, \dots, e_N\}$ be a universe of cataloged real-world events from independent ground-truth registries. Each event $e \in \mathcal{E}$ is represented by a feature vector:

$$\mathbf{x}_e = [\text{type}, \text{timestamp}, \text{latitude}, \text{longitude}, \text{severity}, \text{fatalities}, \text{affected\_population}, \dots]$$

Let $\mathcal{O} = \{o_1, o_2, \dots, o_M\}$ denote the set of monitored media organizations. Each outlet $o$ possesses historical coverage attributes $\mathbf{z}_o$.

For each pair $(e, o)$, let $Y_{e,o} \in \{0, 1\}$ represent the ground-truth coverage indicator:
- $Y_{e,o} = 1$: Outlet $o$ published at least one relevant article covering event $e$ within a temporal window $\mathcal{W}_e = [t_e - \delta_{\text{pre}}, t_e + \delta_{\text{post}}]$.
- $Y_{e,o} = 0$: Outlet $o$ did not publish any report matching event $e$ in $\mathcal{W}_e$.

The primary learning task is to approximate the conditional expectation:

$$\mathbb{E}[Y_{e,o} \mid \mathbf{x}_e, \mathbf{z}_o, \mathbf{c}_{e,o}] = P(Y_{e,o} = 1 \mid \mathbf{x}_e, \mathbf{z}_o, \mathbf{c}_{e,o})$$

where $\mathbf{c}_{e,o}$ encapsulates contextual and temporal interactions (e.g., geographic distance between outlet headquarters and event coordinates, global news congestion index at time $t_e$).

---

## 2. The 10-Stage Research Pipeline

```
+------------------------------------+      +------------------------------------+
| 1. Independent Event Collection    |      | 2. News Article Collection         |
| (EM-DAT, GDACS, ReliefWeb)         |      | (Target Outlets, Timestamps, URLs) |
+-----------------+------------------+      +-----------------+------------------+
                  |                                           |
                  +---------------------+---------------------+
                                        |
                                        v
                       +---------------------------------+
                       | 3. Event-Article Matching       |
                       | (BM25 Lexical + Dense Embeddings|
                       |  + Cross-Encoder Reranking)     |
                       +----------------+----------------+
                                        |
                                        v
                       +---------------------------------+
                       | 4. Coverage Matrix Construction |
                       | (Event x Outlet Label Matrix)   |
                       +----------------+----------------+
                                        |
                                        v
                       +---------------------------------+
                       | 5. Expected Coverage Modeling   |
                       | (Hierarchical GLMs, GBDT, etc.) |
                       +----------------+----------------+
                                        |
                                        v
                       +---------------------------------+
                       | 6. Counterfactual Event Matching|
                       | (Nearest-Neighbor Twins C(e))   |
                       +----------------+----------------+
                                        |
                                        v
                       +---------------------------------+
                       | 7. Anomaly Scoring Engine       |
                       | (Residual & Tail Deviation)     |
                       +----------------+----------------+
                                        |
                                        v
                       +---------------------------------+
                       | 8. Uncertainty & Calibration    |
                       | (Platt Scaling, Isotonic, ECE)  |
                       +----------------+----------------+
                                        |
                                        v
                       +---------------------------------+
                       | 9. Explainability (XAI)         |
                       | (SHAP Attributions + Twin Evid.)|
                       +----------------+----------------+
                                        |
                                        v
                       +---------------------------------+
                       | 10. Research Audit Interface    |
                       | (Visual Interactive Inspection) |
                       +---------------------------------+
```

### Stage 1: Independent Event Data Collection
Ingest structured occurrences from non-media, ground-truth repositories (e.g., EM-DAT disaster database, GDACS alerts). Standardize dates, geographic coordinates, hazard typologies, and quantitative impact measurements.

### Stage 2: News Collection & Normalization
Harvest article metadata from target media organizations across identical observation periods. Normalize article publication timestamps, headline text, lead paragraphs, bylines, and URLs.

### Stage 3: Event–Article Matching
Identify whether any published article $a \in \mathcal{A}_o$ corresponds to event $e$.
1. **Candidate Retrieval**: Lexical (BM25) and dense semantic retrieval (bi-encoder sentence embeddings) filter candidate articles within window $\mathcal{W}_e$.
2. **Relevance Scoring**: A cross-encoder or calibrated similarity threshold computes $\mathrm{sim}(e, a)$.
3. **Thresholding**: Article $a$ matches event $e$ iff $\mathrm{sim}(e, a) \ge \tau_{\text{match}}$.

### Stage 4: Coverage Matrix Construction
Construct the binary observation matrix $\mathbf{Y} \in \{0, 1\}^{N \times M}$ where $Y_{e,o} = \mathbb{I}(\exists a \in \mathcal{A}_o \text{ matching } e)$.

### Stage 5: Expected Coverage Modeling
Train predictive models to estimate $\hat{P}_{e,o} = \hat{P}(Y_{e,o} = 1)$.
- **Statistical / Classical**: Logistic Regression, Generalized Linear Models (GLMs), Hierarchical / Mixed-Effects Models (capturing outlet-level random intercepts and event-type random slopes), Bayesian Logistic Regression.
- **Machine Learning**: Gradient Boosted Decision Trees (XGBoost, LightGBM, CatBoost), Random Forests.

### Stage 6: Counterfactual / Matched-Event Analysis
For an event $e$ with $Y_{e,o} = 0$, construct a counterfactual cohort $\mathcal{C}(e)$ of historically similar events where outlet $o$ previously had high coverage rates:
- Matching metrics: Mahalanobis distance or propensity score distance across normalized covariates (hazard type, severity, fatalities, region).
- Counterfactual evidence: "Outlet $o$ covered 4 out of 5 historically comparable magnitude-7.0 earthquakes in Southeast Asia, but omitted event $e$."

### Stage 7: Anomaly Detection
Compute an anomaly score indicating whether non-coverage represents an unexpected divergence:

$$\mathrm{AnomalyScore}(e, o) = \hat{P}_{e,o} \times \left(1 - \frac{1}{|\mathcal{C}(e)|}\sum_{e' \in \mathcal{C}(e)} Y_{e', o}\right)^{-1} \cdot \mathbb{I}(Y_{e,o} = 0)$$

Events exceeding a statistical significance threshold $\alpha = 0.05$ with high expected probability ($\hat{P}_{e,o} \ge 0.70$) are flagged as candidate media blind spots.

### Stage 8: Uncertainty Estimation & Calibration
Raw model outputs can suffer from calibration drift. Post-hoc calibration ensures that when the model outputs $\hat{P} = 0.80$, the empirical coverage frequency is indeed 80%.
- Algorithms: Isotonic Regression, Platt Scaling, Temperature Scaling.
- Metrics: Expected Calibration Error (ECE), Brier Score Decomposition.

### Stage 9: Explainable AI (XAI)
Explain why coverage was expected:
1. **Feature Attribution**: SHAP (SHapley Additive exPlanations) values quantifying the contribution of severity, geographic proximity, and outlet topical focus.
2. **Case-Based Evidence**: Side-by-side presentation of matched historical events from $\mathcal{C}(e)$.

### Stage 10: Research Interface & Auditing Dashboard
A modular analytical interface allowing domain researchers to inspect events, investigate expected vs. observed coverage distributions, review calibration reliability curves, and audit flagged omissions.
