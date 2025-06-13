"""Function to resolve the weekday from a date string."""

import datetime
from typing import Any, Final

WEEK_DAYS: Final[dict[int, str]] = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def weekday(**_: dict[str, Any]) -> str:
    """
    Ask the user for the day of the week and respond accordingly.
    """
    current_day = datetime.date.today().weekday()
    return f"Current day is: {WEEK_DAYS.get(current_day, 'Unknown day')}"
