# Ethics, Epistemology & Scientific Limitations

Auditing media coverage gaps involves delicate social, political, and institutional dimensions. UNSEEN enforces strict ethical and epistemological guidelines to prevent weaponization, unwarranted accusations, or methodological overreach.

---

## 1. Epistemological Position: Absence Does Not Imply Intentional Bias

A foundational tenet of UNSEEN is that **statistical absence of coverage is not synonymous with ideological malice or deliberate censorship**.

News editorial rooms operate under finite physical, human, and temporal constraints:
- **News Hole Constraints**: An outlet's daily print space, broadcast minutes, or homepage layout is bounded. A surge in a dominant domestic story inevitably suppresses reporting on other legitimate occurrences.
- **Access & Security Barriers**: Lack of field correspondents, visa denials, local communication blackouts, or armed conflict can prevent reporters from verifying an event on the ground.
- **Competing News Shocks**: High-severity domestic crises displace international reporting across all outlets simultaneously.

Therefore, UNSEEN categorizes outputs as **statistically unusual omissions relative to historical baselines**, explicitly avoiding subjective terms such as "censorship," "suppression," or "malicious bias."

---

## 2. Inherent Limitations of Ground-Truth Event Databases

While independent databases (such as EM-DAT, GDACS, and ReliefWeb) provide authoritative real-world catalogs, they are subject to their own systematic reporting biases:
1. **Reporting Lag**: Official fatality and damage assessments may take weeks or months to be verified in disaster registries, whereas news reporting occurs in real-time.
2. **Infrastructure Skew**: High-income nations possess dense sensor networks and administrative reporting systems that catalog minor events with high fidelity, whereas remote regions in developing nations may underreport lower-magnitude hazards.
3. **Political Filtering in Primary Reporting**: Authoritarian regimes may withhold disaster casualty figures from international bodies, impacting ground-truth inclusion.

UNSEEN accounts for these factors by standardizing severity metrics and measuring geographic baseline reporting density.

---

## 3. Uncertainty Transparency & Visible Confidence Bounds

- **No Deterministic Declarations**: Model outputs must never be presented as absolute truth. Every estimated coverage probability $\hat{P}_{e,o}$ must be accompanied by uncertainty bounds derived from calibration and bootstrap variance.
- **Explicit Confidence Intervals**: Anomaly reports display confidence intervals alongside point estimates to prevent overconfidence in low-sample regimes.

---

## 4. Human-in-the-Loop Oversight

High-stakes conclusions regarding media performance must not be fully automated:
- UNSEEN is designed as an **augmented intelligence audit tool** for journalism scholars, editors, and human-rights researchers.
- Any flagged media blind spot should undergo expert human review to assess unmodeled contextual factors (e.g., editorial shifts, correspondent strikes, breaking regional conflicts).

---

## 5. Prevention of System Weaponization

There is a potential risk that hostile actors or politically motivated groups could misuse statistical anomaly flags to delegitimize independent news organizations.

To mitigate this risk:
- All source code, matching heuristics, and calibration procedures are open and transparently documented.
- Comparative audits must include matched-event counterfactuals, demonstrating how the outlet treated similar events across historical cohorts.
- Outlets are evaluated against their own historical editorial standards and geographic scope, rather than an arbitrary universal baseline.
