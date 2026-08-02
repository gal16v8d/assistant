"""Constants for the application."""

from typing import Final

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

# BVC target stocks
BVC_STOCKS: Final[dict[str, str]] = {
    "bogota": "BOGOTA.CL",
    "bolivar": "GRUPOBOLIVAR.CL",
    "bvc": "BVC.CL",
    "celsia": "CELSIA.CL",
    "conconcret": "CONCONCRET.CL",
    "corficolcf": "CORFICOLCF.CL",
    "ecopetrol": "ECOPETROL.CO",
    "exito": "EXITO.CL",
    "geb": "GEB.CL",
    "isa": "ISA.CL",
    "mineros": "MINEROS.CL",
    "pei": "PEI.CL",
    "pfargos": "PFGRUPOARG.CL",
    "pfaval": "PFAVAL.CL",
    "pfcibest": "PFCIBEST.CL",
    "pfdavi": "PFDAVIGRP.CL",
    "pfsura": "PFGRUPSURA.CL",
    "promigas": "PROMIGAS.CL",
    "terpel": "TERPEL.CL",
}
# International target stocks
INT_STOCKS: Final[dict[str, str]] = {
    "awk": "AWK",
    "bti": "BTI",
    "ceg": "CEG",
    "crwd": "CRWD",
    "gev": "GEV",
    "gldm": "GLDM",
    "isrg": "ISRG",
    "lite": "LITE",
    "ma": "MA",
    "main": "MAIN",
    "mrvl": "MRVL",
    "mu": "MU",
    "nbis": "NBIS",
    "nee": "NEE",
    "o": "O",
    "panw": "PANW",
    "qqqm": "QQQM",
    "sgov": "SGOV",
    "slv": "SLV",
    "soxq": "SOXQ",
    "spcx": "SPCX",
    "ura": "URA",
    "vea": "VEA",
    "voo": "VOO",
    "vrt": "VRT",
    "wdc": "WDC",
    "wm": "WM",
    "xar": "XAR",
    "xle": "XLE",
    "xlf": "XLF",
    "xli": "XLI",
    "xlp": "XLP",
    "xlv": "XLV",
    "xyl": "XYL",
}

STOCK_SYMBOLS: Final[dict[str, str]] = BVC_STOCKS | INT_STOCKS

BASE_CRYPTO_URL: Final[str] = "https://coinmarketcap.com/currencies"
CRYPTO_SYMBOLS: Final[dict[str, str]] = {
    # core macro & exchange reserve
    "btc": f"{BASE_CRYPTO_URL}/bitcoin/",
    "eth": f"{BASE_CRYPTO_URL}/ethereum/",
    "sol": f"{BASE_CRYPTO_URL}/solana/",
    "bnb": f"{BASE_CRYPTO_URL}/bnb/",
    # network utility & sec
    "trx": f"{BASE_CRYPTO_URL}/tron/",
    "xrp": f"{BASE_CRYPTO_URL}/xrp/",
    # focused innovation & infra
    "link": f"{BASE_CRYPTO_URL}/chainlink/",
    "sui": f"{BASE_CRYPTO_URL}/sui/",
    # speculative (own risk)
    "zec": f"{BASE_CRYPTO_URL}/zcash/",
}


BASE_URL_TEMPLATE = "https://www.google.com/search?q={}+to+cop+today"
CURRENCIES: Final[list[str]] = [
    "brl",
    "cad",
    "chf",
    "eur",
    "gbp",
    "jpy",
    "mxn",
    "pen",
    "usd",
    "yuan",
]
CURRENCY_SYMBOLS: Final[dict[str, str]] = {
    curr: BASE_URL_TEMPLATE.format(curr) for curr in CURRENCIES
}

WEB_PAGE_SYMBOLS: Final[dict[str, str]] = {
    "animeplanet": "https://www.anime-planet.com",
    "chess": "https://www.chess.com",
    "github": "https://www.github.com/gal16v8d",
    "google": "https://www.google.com",
    "wikipedia": "https://www.wikipedia.org",
    "youtube": "https://www.youtube.com",
}
