"""Shortcut to access all actions."""

from actions.ai_prompt import (
    get_ai_image_response,
    get_ai_image_response_v3,
    get_ai_text_response,
)
from actions.joke import get_joke
from actions.stock import get_stock_price
from actions.time import ask_time
from actions.websearch import (
    open_webpage,
    top_anime,
    CURRENCY_SYMBOLS,
    CRYPTO_SYMBOLS,
    WEB_PAGE_SYMBOLS,
)
from actions.weekday import weekday

__all__ = [
    "ask_time",
    "get_ai_image_response",
    "get_ai_image_response_v3",
    "get_ai_text_response",
    "get_joke",
    "get_stock_price",
    "open_webpage",
    "top_anime",
    "weekday",
    "CRYPTO_SYMBOLS",
    "CURRENCY_SYMBOLS",
    "WEB_PAGE_SYMBOLS",
]
