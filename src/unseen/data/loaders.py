"""Base data loading and validation abstractions for UNSEEN."""

from __future__ import annotations

import abc
from collections.abc import Iterator
from pathlib import Path

from unseen.data.schemas import MediaOutlet, NewsArticle, RealWorldEvent


class BaseEventLoader(abc.ABC):
    """Abstract base class for ingesting ground-truth real-world events."""

    def __init__(self, data_path: str | Path) -> None:
        self.data_path = Path(data_path)

    @abc.abstractmethod
    def load(self) -> list[RealWorldEvent]:
        """Load and return all validated real-world event objects."""
        raise NotImplementedError

    @abc.abstractmethod
    def stream(self) -> Iterator[RealWorldEvent]:
        """Stream real-world events lazily to conserve memory."""
        raise NotImplementedError


class BaseNewsLoader(abc.ABC):
    """Abstract base class for loading media outlet news metadata."""

    def __init__(self, data_path: str | Path) -> None:
        self.data_path = Path(data_path)

    @abc.abstractmethod
    def load(self) -> list[NewsArticle]:
        """Load and return all validated news articles."""
        raise NotImplementedError

    @abc.abstractmethod
    def stream(self) -> Iterator[NewsArticle]:
        """Stream news articles lazily."""
        raise NotImplementedError


class BaseOutletRegistry(abc.ABC):
    """Abstract repository managing monitored media organizations."""

    @abc.abstractmethod
    def get_outlet(self, outlet_id: str) -> MediaOutlet | None:
        """Fetch outlet metadata by ID."""
        raise NotImplementedError

    @abc.abstractmethod
    def list_outlets(self) -> list[MediaOutlet]:
        """List all registered media outlets."""
        raise NotImplementedError
