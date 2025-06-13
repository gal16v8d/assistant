"""Adapt the stock command to the required action."""

from typing import Any

from actions import get_stock_price
from consts import const
from processor.input_processor import get_user_input


def get_stock_args(**kwargs: dict[str, Any]) -> str:
    """
    Returns the stock name based on the input type.
    """
    stock_name = get_user_input(
        request_value_t=const.TEXT_STOCK_MSG,
        request_value_v=const.VOICE_STOCK_MSG,
        error_msg=const.NO_STOCK_MSG,
        **kwargs
    )

    return get_stock_price(stock_name.lower())
