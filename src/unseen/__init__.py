"""UNSEEN: Counterfactual Intelligence for Auditing Systematic Media Omission.

B.Sc. Graduation Project (Project ID: 27DSAI).
Applied Domain: Media Intelligence and Journalism Analytics.
"""

from __future__ import annotations

import logging
import os
import sys

__version__ = "0.1.0"
__author__ = "Mohamed Abdelwahab"
__all__ = ["__version__", "__author__", "setup_logging"]


def setup_logging(
    level: str | int | None = None,
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
) -> logging.Logger:
    """Configure standardized logging across the UNSEEN framework.

    Args:
        level: Logging level (e.g., 'INFO', 'DEBUG', logging.INFO).
               Defaults to UNSEEN_LOG_LEVEL env var or 'INFO'.
        log_format: Standard formatting string for log messages.

    Returns:
        Root UNSEEN logger instance.
    """
    if level is None:
        level = os.getenv("UNSEEN_LOG_LEVEL", "INFO").upper()

    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=[logging.StreamHandler(sys.stdout)],
        force=True,
    )

    logger = logging.getLogger("unseen")
    logger.debug("UNSEEN logger initialized at level %s", level)
    return logger
