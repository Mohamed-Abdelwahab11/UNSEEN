# Configuration Management

This directory contains configuration files for experiment tracking, model parameters, retrieval thresholds, and data pipeline orchestration in the UNSEEN framework.

## Structure

- `default.yaml`: Baseline experimental configuration containing seed definitions, matching parameters, model baselines, calibration settings, and evaluation splits.

## Usage

Configurations are loaded programmatically via `PyYAML` and can be overridden through environment variables (defined in `.env`) or command-line arguments in scripts.

```python
import yaml

with open("configs/default.yaml", "r") as f:
    config = yaml.safe_load(f)
```
