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
    "corfi": "CORFICOLCF.CL",
    "ecopetrol": "ECOPETROL.CO",
    "exito": "EXITO.CL",
    "isa": "ISA.CL",
    "mineros": "MINEROS.CL",
    "pei": "PEI.CL",
    "pfargos": "PFGRUPOARG.CL",
    "pfaval": "PFAVAL.CL",
    "pfcibest": "PFCIBEST.CL",
    "pfdavi": "PFDAVIGRP.CL",
    "pfsura": "PFGRUPSURA.CL",
    "promigas": "PROMIGAS.CL",
    "sqmbco": "SQMBCO.CL",
    "terpel": "TERPEL.CL",
    "tin": "TIN.CL"
}
# International target stocks
INT_STOCKS: Final[dict[str, str]] = {
    "aaoi": "AAOI",
    "bti": "BTI",
    "cgw": "CGW",
    "cibr": "CIBR",
    "copx": "COPX",
    "gev": "GEV",
    "gold": "GLDM",
    "iemg": "IEMG",
    "isrg":"ISRG",
    "keyence": "KYCCF",
    "lite": "LITE",
    "ma": "MA",
    "main": "MAIN",
    "mrvl": "MRVL",
    "nbis": "NBIS",
    "nee": "NEE",
    "o": "O",
    "pwr": "PWR",
    "qqqm": "QQQM",
    "sgov": "SGOV",
    "silver": "SLV",
    "sndk": "SNDK",
    "soxq": "SOXQ",
    "ufo": "UFO",
    "ura": "URA",
    "vea": "VEA",
    "vigi": "VIGI",
    "voo": "VOO",
    "vrt": "VRT",
    "wdc": "WDC",
    "wm": "WM",
    "xar": "XAR",
    "xbi": "XBI",
    "xle": "XLE",
    "xlf": "XLF",
    "xli": "XLI",
    "xlp": "XLP",
    "xlv": "XLV",
}

STOCK_SYMBOLS: Final[dict[str, str]] = BVC_STOCKS | INT_STOCKS

BASE_CRYPTO_URL: Final[str] = "https://coinmarketcap.com/currencies"
CRYPTO_SYMBOLS: Final[dict[str, str]] = {
    "btc": f"{BASE_CRYPTO_URL}/bitcoin/",
    "eth": f"{BASE_CRYPTO_URL}/ethereum/",
    "xrp": f"{BASE_CRYPTO_URL}/xrp/",
    "bnb": f"{BASE_CRYPTO_URL}/bnb/",
    "sol": f"{BASE_CRYPTO_URL}/solana/",
    "trx": f"{BASE_CRYPTO_URL}/tron/",
    "zec": f"{BASE_CRYPTO_URL}/zcash/",
}


BASE_URL_TEMPLATE = "https://www.google.com/search?q={}+to+cop+today"
CURRENCIES: Final[list[str]] = ["brl", "cad", "chf", "eur", "gbp", "jpy", "mxn", "pen", "usd", "yuan"]
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
