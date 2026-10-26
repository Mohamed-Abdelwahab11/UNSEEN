"""Smoke tests verifying that the UNSEEN package and submodules import cleanly."""

import importlib


def test_package_version_and_exports():
    import unseen

    assert hasattr(unseen, "__version__")
    assert unseen.__version__ == "0.1.0"
    assert hasattr(unseen, "setup_logging")


def test_submodules_import():
    submodules = [
        "unseen.data",
        "unseen.retrieval",
        "unseen.matching",
        "unseen.features",
        "unseen.models",
        "unseen.counterfactual",
        "unseen.anomaly",
        "unseen.calibration",
        "unseen.explainability",
        "unseen.evaluation",
        "unseen.visualization",
    ]
    for mod_name in submodules:
        mod = importlib.import_module(mod_name)
        assert mod is not None
