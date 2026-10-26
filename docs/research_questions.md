# Research Questions & Operational Hypotheses

The UNSEEN research project investigates the theoretical and empirical foundations of automated media omission auditing through four formal Research Questions (RQs).

---

### Research Question 1 (RQ1: Expected Coverage Estimation)

> **Can historical outlet behavior and real-world event characteristics be used to reliably estimate outlet-specific expected coverage probabilities?**

#### Operational Formulation
Given an independent event $e \in \mathcal{E}$ parameterized by attribute vector $\mathbf{x}_e$ (severity, event category, geocoded distance, affected population) and a media outlet $o \in \mathcal{O}$ characterized by its historical coverage profile $\mathbf{z}_o$ and temporal context $\mathbf{c}_{e,o}$, can a statistical or machine learning estimator compute a well-conditioned coverage probability:

$$\hat{P}(Y_{e,o} = 1 \mid \mathbf{x}_e, \mathbf{z}_o, \mathbf{c}_{e,o})$$

where $Y_{e,o} \in \{0, 1\}$ denotes whether outlet $o$ published at least one matched news report covering event $e$ within time window $[t_e, t_e + \Delta t]$?

#### Hypothesis $H_1$
Statistical models incorporating outlet-specific historical priors and spatial-topical affinity will achieve significantly higher predictive discrimination (measured by ROC-AUC and PR-AUC) and probabilistic fidelity (measured by Brier score and Log Loss) than global, outlet-agnostic baselines.

---

### Research Question 2 (RQ2: Distinguishing Ordinary vs. Anomalous Non-Coverage)

> **Can expected-coverage models distinguish ordinary editorial non-coverage from statistically anomalous omission?**

#### Operational Formulation
For events where $Y_{e,o} = 0$, can an anomaly scoring function $S(e, o)$ isolate events where the expected coverage probability was high ($\hat{P} \ge \tau$) with low epistemic/aleatoric uncertainty, such that the omission deviates significantly from the outlet's baseline distribution?

$$S(e, o) = \frac{\hat{P}(Y_{e,o} = 1) - 0}{\sqrt{\mathrm{Var}(\hat{P}_{e,o}) + \epsilon}}$$

#### Hypothesis $H_2$
A calibrated residual anomaly threshold can separate baseline non-coverage (driven by low event relevance, foreign geographic distance, or competing breaking news congestion) from statistically anomalous omission with a precision substantially higher than random or severity-only filtering.

---

### Research Question 3 (RQ3: Counterfactual Matched-Event Analysis)

> **Do counterfactual comparisons with similar real-world events improve the reliability and explainability of media blind-spot detection?**

#### Operational Formulation
Let $\mathcal{C}(e)$ denote a set of historical counterfactual twins for event $e$, identified via nearest-neighbor distance in normalized event covariate space $\mathcal{X}$. Does conditioning the anomaly assessment on the actual observed coverage rate of outlet $o$ across $\mathcal{C}(e)$:

$$\Delta_{\mathrm{CF}}(e, o) = \frac{1}{|\mathcal{C}(e)|} \sum_{e' \in \mathcal{C}(e)} Y_{e', o} - Y_{e,o}$$

reduce false-positive blind-spot alerts and provide human-interpretable comparative evidence for domain experts?

#### Hypothesis $H_3$
Counterfactual event matching acts as a non-parametric sanity check that eliminates false anomaly flags caused by global unobserved confounders (e.g., quiet news cycles vs. saturated international crises).

---

### Research Question 4 (RQ4: Calibration & Cross-Domain Robustness)

> **How well calibrated and robust are blind-spot predictions across outlets, event categories, regions, and time periods?**

#### Operational Formulation
Does post-hoc probability calibration (e.g., Platt scaling, Isotonic regression) minimize the Expected Calibration Error (ECE) across distinct geographic subgroups $\mathcal{G}$ and temporal epochs $\mathcal{T}$:

$$\mathrm{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{N} \left| \mathrm{acc}(B_m) - \mathrm{conf}(B_m) \right|$$

preventing systematic overconfidence in under-reported developing regions or infrequent disaster categories?

#### Hypothesis $H_4$
Without explicit probability calibration and hierarchical grouping, uncalibrated estimators exhibit inflated confidence in high-density regions while exhibiting severe miscalibration in sparsely covered developing regions.
