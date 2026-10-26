# Project Overview: UNSEEN

## Project Identity

| Attribute | Specification |
| :--- | :--- |
| **Project ID** | 27DSAI |
| **Project Name** | UNSEEN |
| **Full Academic Title** | **UNSEEN: Counterfactual Intelligence for Auditing Systematic Media Omission** |
| **Degree** | B.Sc. in Data Science and Artificial Intelligence (DSAI) |
| **Applied Domain** | Media Intelligence, Computational Journalism, and Information Retrieval |

---

## Executive Summary

UNSEEN is an applied AI and Data Science research framework formulated to audit and identify statistically unexpected omissions and underreported real-world events in media coverage.

Traditional media analytics tools typically prioritize sentiment analysis, political polarity classification, or fake-news verification on already published text. However, such approaches fundamentally ignore the **agenda-setting** stage of the information ecosystem: the systematic non-reporting or selective omission of verifiable real-world occurrences.

UNSEEN shifts the paradigm from analyzing *what was said* to scientifically modeling *what was expected to be said but omitted*.

```
+------------------------------------+       +------------------------------------+
|  Conventional Media Analytics      |       |  UNSEEN Counterfactual Auditing    |
+------------------------------------+       +------------------------------------+
| • Evaluates existing articles only |  VS   | • Compares real-world events vs news|
| • Classifies sentiment / polarity  |       | • Estimates expected coverage P(Y) |
| • Static labels (biased / neutral) |       | • Identifies statistically anomalous|
| • Blind to non-reported events     |       |   omissions with calibrated bounds  |
+------------------------------------+       +------------------------------------+
```

---

## Core Problem Statement

Every day, thousands of verifiable real-world events occur globally—natural hazards, humanitarian emergencies, civilian casualties, labor disputes, and policy shifts. News outlets operate under constrained editorial bandwidth, regional priorities, and topical focus, resulting in selective event filtering.

While ordinary non-coverage is an unavoidable consequence of limited news capacity, **systematic omission** occurs when an outlet repeatedly fails to report on events that closely match its established historical editorial focus, geographic scope, and severity sensitivity.

UNSEEN addresses the central research question:

> **Can AI distinguish between ordinary editorial non-coverage and statistically anomalous omission of important real-world events?**

---

## Important Academic Positioning

To preserve scientific rigor and objectivity, UNSEEN maintains strict boundaries regarding its scope and claims:

- **Not a Political-Bias Classifier**: The system does not assign binary or continuous "bias scores" to news organizations.
- **Not a Fake-News Detector**: The focus is solely on verified, factual occurrences cataloged in independent ground-truth event repositories.
- **Not an LLM Wrapper**: The framework relies on statistical modeling, hierarchical mixed models, calibrated probabilistic predictors, and counterfactual matching, rather than qualitative generative prompts.
- **No Definitive Accusations**: Non-coverage of an event by an outlet is framed as a **statistical anomaly relative to historical expectations**, acknowledging latent unobserved variables (e.g., local correspondent access, competing breaking news spikes).

---

## Target Stakeholders & Application Domains

1. **Media Monitoring & Journalism Research**: Enabling computational journalism scholars to study empirical coverage patterns at scale across diverse outlets and time horizons.
2. **Public-Interest Research & NGOs**: Assisting humanitarian organizations (e.g., Red Cross, Amnesty International, UN OCHA) in identifying critical humanitarian events that suffer from global media neglect.
3. **Editorial Self-Auditing**: Providing media organizations with evidence-based internal tools to detect unintentional editorial blind spots and geographic reporting skews.
4. **Media Accountability Organizations**: Supplying transparent, reproducible statistical evidence rather than subjective critique.
