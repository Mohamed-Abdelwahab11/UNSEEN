"""Semantic matching interfaces for event-article pair verification."""

from __future__ import annotations

import abc

from unseen.data.schemas import NewsArticle, RealWorldEvent


class BaseEventArticleMatcher(abc.ABC):
    """Abstract interface for verifying whether an article specifically reports an event."""

    def __init__(self, default_threshold: float = 0.65) -> None:
        self.default_threshold = default_threshold

    @abc.abstractmethod
    def compute_similarity(self, event: RealWorldEvent, article: NewsArticle) -> float:
        """Compute semantic affinity score between event and article in [0.0, 1.0]."""
        raise NotImplementedError

    def is_match(
        self,
        event: RealWorldEvent,
        article: NewsArticle,
        threshold: float | None = None,
    ) -> bool:
        """Classify whether the article matches the event according to decision threshold."""
        tau = self.default_threshold if threshold is None else threshold
        return self.compute_similarity(event, article) >= tau

    def match_candidates(
        self,
        event: RealWorldEvent,
        candidates: list[NewsArticle],
        threshold: float | None = None,
    ) -> list[tuple[NewsArticle, float, bool]]:
        """Score candidate articles and label matches against threshold.

        Returns:
            List of (article, similarity_score, is_match) tuples.
        """
        results = []
        tau = self.default_threshold if threshold is None else threshold
        for article in candidates:
            score = self.compute_similarity(event, article)
            results.append((article, score, score >= tau))
        return results
