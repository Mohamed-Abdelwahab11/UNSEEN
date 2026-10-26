# UNSEEN Testing Suite

This directory contains the unit, integration, and regression test suites for the UNSEEN framework.

## Running Tests

From the repository root:

```bash
# Run all tests
pytest tests/ -v

# Run with test coverage report
pytest --cov=unseen tests/
```

## Structure

- `conftest.py`: Shared pytest fixtures (mock events, synthetic articles, mock outlets).
- `test_package_structure.py`: Validates package exports and imports.
- `test_schemas.py`: Validates schema immutability, serialization, and typing contracts.
- `test_metrics.py`: Validates mathematical correctness of Brier score, ECE, MRR, Recall@K, and Log Loss.
