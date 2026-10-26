"""Base model interfaces for outlet-specific expected coverage prediction."""

from __future__ import annotations

import abc
from pathlib import Path
from typing import Any


class BaseCoverageModel(abc.ABC):
    """Abstract interface for modeling P(outlet covers event | features)."""

    def __init__(self, random_seed: int = 42) -> None:
        self.random_seed = random_seed
        self.is_fitted = False

    @abc.abstractmethod
    def fit(self, X: Any, y: Any, **kwargs: Any) -> BaseCoverageModel:
        """Fit the expected coverage model on feature matrix X and binary targets y."""
        raise NotImplementedError

    @abc.abstractmethod
    def predict_proba(self, X: Any) -> Any:
        """Predict expected coverage probability P(Y=1 | X).

        Returns:
            1D array-like of predicted probabilities bounded in [0.0, 1.0].
        """
        raise NotImplementedError

    def predict(self, X: Any, threshold: float = 0.5) -> list[int]:
        """Generate binary coverage predictions based on decision threshold."""
        probas = self.predict_proba(X)
        return [1 if p >= threshold else 0 for p in probas]

    @abc.abstractmethod
    def save(self, file_path: str | Path) -> None:
        """Serialize model weights and metadata to disk."""
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def load(cls, file_path: str | Path) -> BaseCoverageModel:
        """Load serialized model from disk."""
        raise NotImplementedError
