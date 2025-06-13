"""# This module provides a function to ask the user for the current time."""

from datetime import datetime
from typing import Any


def ask_time(**_: dict[str, Any]) -> str:
    """
    Ask the user for the current time.
    """
    current_time = datetime.now()
    return f"Time is {current_time.hour:02}:{current_time.minute:02}:{current_time.second:02}"
