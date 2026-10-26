# Comprehensive Evaluation Plan

To guarantee experimental validity and guard against methodological shortcuts, UNSEEN specifies a multi-tiered evaluation framework assessing each computational stage independently.

---

## 1. Event–News Matching Evaluation

Evaluating how accurately the retrieval and matching stage pairs raw articles with cataloged real-world events.

### Benchmark Setup
A curated gold-standard benchmark $\mathcal{D}_{\text{match}} = \{(e_i, a_j, y_{ij})\}$ where $y_{ij} \in \{0, 1\}$ denotes human-verified relevance across a stratified sample of events.

### Metrics
- **Mean Reciprocal Rank (MRR)**: Evaluates ranking quality of candidate articles.
- **Recall@K ($K \in \{5, 10, 50\}$)**: Measures the proportion of relevant articles retrieved in the top $K$ candidate pool.
- **Precision, Recall, and F1**: Evaluates binary match classification against the semantic threshold $\tau_{\text{match}}$.

---

## 2. Expected Coverage Predictive Performance

Evaluating how accurately models estimate $P(Y_{e,o} = 1 \mid \mathbf{x}_e, \mathbf{z}_o, \mathbf{c}_{e,o})$.

### Data Splitting Strategy (Strict Temporal Split)
To prevent temporal data leakage and lookahead bias, splits are defined strictly chronologically:
- **Training Set**: Events occurring in interval $[T_0, T_1]$
- **Validation Set**: Events in interval $(T_1, T_2]$
- **Test Set**: Events in interval $(T_2, T_3]$

### Metrics
- **ROC-AUC (Area Under the ROC Curve)**: Measures global discriminative capacity across decision thresholds.
- **PR-AUC (Precision-Recall AUC)**: Critical for addressing severe class imbalance (rare events with sparse coverage).
- **Brier Score**: Measures mean squared difference between predicted probabilities $\hat{p}$ and actual binary outcomes $y$:
  $$\mathrm{BS} = \frac{1}{N} \sum_{i=1}^{N} (\hat{p}_i - y_i)^2$$
- **Log Loss (Binary Cross-Entropy)**: Penalizes confident misclassifications.

---

## 3. Probability Calibration Evaluation

Raw machine learning models (particularly tree ensembles and neural nets) frequently yield uncalibrated confidence scores. UNSEEN measures calibration reliability explicitly.

### Metrics
- **Expected Calibration Error (ECE)**:
  $$\mathrm{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{N} |\mathrm{acc}(B_m) - \mathrm{conf}(B_m)|$$
- **Maximum Calibration Error (MCE)**: Identifies the worst-case bin deviation.
- **Reliability Diagrams**: Graphical comparison of mean predicted probability versus empirical true positive frequency across 10 equal-width bins.

---

## 4. Blind-Spot Detection & Anomaly Auditing

Evaluating the downstream system's ability to prioritize genuine, statistically significant media omissions.

### Evaluation Protocol
1. **Expert / Expert-Assisted Human Evaluation**: A double-blind panel of journalism researchers reviews top-$K$ flagged blind-spot candidates against control omissions (ordinary non-coverage with low expected probability).
2. **Review Metrics**:
   - **Audit Precision@K**: Proportion of top-$K$ flagged omissions deemed genuine, noteworthy coverage gaps by expert annotators.
   - **Explainability Plausibility Score**: Likert-scale rating (1–5) measuring the coherence of matched-event counterfactuals and feature attributions.

---

## 5. Statistical Rigor & Sensitivity Analysis

- **Confidence Intervals**: 95% bootstrap confidence intervals (1,000 resamples) reported for all primary metrics.
- **Significance Testing**: Paired Wilcoxon signed-rank tests or McNemar's tests to verify performance differences between baseline models and counterfactual architectures.
- **Sensitivity Analysis**: Testing stability against perturbations in matching threshold $\tau_{\text{match}}$, coverage temporal window $\mathcal{W}_e$, and missing feature imputations.
