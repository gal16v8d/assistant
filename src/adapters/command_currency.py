"""Adapt the websearch command to the required action."""

from typing import Any

from actions import open_webpage, CURRENCY_SYMBOLS
from consts import const
from processor.input_processor import get_user_input


def open_webpage_currency_args(**kwargs: dict[str, Any]) -> str:
    """
    Opens a webpage based on the user's input.
    """
    webpage_currency_name = get_user_input(
        request_value_t=const.TEXT_CURRENCY_MSG,
        request_value_v=const.VOICE_CURRENCY_MSG,
        error_msg=const.NO_CURRENCY_MSG,
        **kwargs,
    )

    return open_webpage(webpage_currency_name.lower(), CURRENCY_SYMBOLS)
