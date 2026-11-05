"""Constants for the application."""

from typing import Final
from dotenv import dotenv_values, find_dotenv

# Assistant messages and prompts.
EXIT_MSG: Final[str] = "Thank you for using the virtual assistant. Goodbye!"
INPUT_TYPE_MSG: Final[str] = "Enter 'v' for voice input or 't' for text input: "
INVALID_INPUT_MSG: Final[str] = (
    "Invalid input type. Please enter 'v' for voice input or 't' for text input."
)
INVALID_OPTION_MSG: Final[str] = "Invalid option: "
NO_OPTION_MSG: Final[str] = "No option provided. Please try again."
TEXT_MENU_MSG: Final[str] = "Input the option: "
TRY_AGAIN_MSG: Final[str] = "Please try again."
USE_ONE_OF_THE_OPTIONS_MSG: Final[str] = "Please use one of the following options: "
WELCOME_MSG: Final[str] = (
    "Hello, I am your virtual assistant. How can I help you today?"
)

# Possible input types for the application.
TEXT_INPUT: Final[str] = "t"
VOICE_INPUT: Final[str] = "v"

# AI related constants.
NO_AI_TEXT_MSG: Final[str] = "No prompt provided. Please try again."
NO_AI_TITLE_MSG: Final[str] = "No title provided. Please try again."
TEXT_AI_MSG: Final[str] = "Input your text prompt: "
VOICE_AI_MSG: Final[str] = "Please say your text prompt."
TITLE_AI_TEXT_MSG: Final[str] = "Input the title for the image: "
TITLE_AI_VOICE_MSG: Final[str] = "Please say the title for the image."


# Stock related constants.
NO_STOCK_MSG: Final[str] = "No stock name provided. Please try again."
TEXT_STOCK_MSG: Final[str] = "Input the stock name: "
VOICE_STOCK_MSG: Final[str] = "Please say the stock name."

# Web search related constants.
NO_WEBPAGE_MSG: Final[str] = "No webpage name provided. Please try again."
TEXT_WEBPAGE_MSG: Final[str] = "Input the webpage name: "
VOICE_WEBPAGE_MSG: Final[str] = "Please say the webpage name."

# Web search related constants (For Currency).
NO_CURRENCY_MSG: Final[str] = "No currency name provided. Please try again."
TEXT_CURRENCY_MSG: Final[str] = "Input the currency name: "
VOICE_CURRENCY_MSG: Final[str] = "Please say the currency name."

# Web search related constants (For Crypto).
NO_CRYPTO_MSG: Final[str] = "No crypto id provided. Please try again."
TEXT_CRYPTO_MSG: Final[str] = "Input the crypto id: "
VOICE_CRYPTO_MSG: Final[str] = "Please say the crypto id."

# Follow-up check ups from stocks.md
BVC_TICKERS: Final[str] = "bvc_tickers"
# International target stocks
INT_STOCKS: Final[str] = "int_tickers"
# Follow-up check ups from crypto.md
CRYPTO_IDS: Final[str] = "crypto_ids"
CURR_IDS: Final[str] = "curr_ids"

BASE_CRYPTO_URL: Final[str] = "https://coinmarketcap.com/currencies/{}/"
BASE_CURR_URL: Final[str] = "https://www.google.com/search?q={}+to+cop+today"

def parse_env_tickers(env_var_name: str) -> dict[str, str]:
    env_config = dotenv_values(find_dotenv())
    env_value = env_config.get(env_var_name, "")
    result: dict[str, str] = {}
    items = [item.strip() for item in env_value.split(",") if item.strip()]

    for item in items:
        if ".CL" in item:
            key = item.split(".CL")[0].strip().lower()
        else:
            key = item.lower()

        result[key] = item

    return result

def parse_env_curr(env_var_name: str) -> list[str]:
    env_config = dotenv_values(find_dotenv())
    env_value = env_config.get(env_var_name, "")
    return [item.strip() for item in env_value.split(",") if item.strip()]

STOCK_SYMBOLS: Final[dict[str, str]] = parse_env_tickers(BVC_TICKERS) | parse_env_tickers(INT_STOCKS)

CRYPTO_SYMBOLS: Final[dict[str, str]] = {
    crypto: BASE_CRYPTO_URL.format(crypto) for crypto in parse_env_curr(CRYPTO_IDS)
}

CURRENCY_SYMBOLS: Final[dict[str, str]] = {
    curr: BASE_CURR_URL.format(curr) for curr in parse_env_curr(CURR_IDS)
}

WEB_PAGE_SYMBOLS: Final[dict[str, str]] = {
    "animeplanet": "https://www.anime-planet.com",
    "chess": "https://www.chess.com",
    "github": "https://www.github.com/gal16v8d",
    "google": "https://www.google.com",
    "wikipedia": "https://www.wikipedia.org",
    "youtube": "https://www.youtube.com",
}
