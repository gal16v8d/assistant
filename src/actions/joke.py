"""Return a random joke."""

from typing import Any
import pyjokes


def get_joke(**_: dict[str, Any]) -> str:
    """
    Returns a random joke in English.
    """
    return pyjokes.get_joke("en")
