"""This module provides a function to get the current stock price for a given stock name."""

from typing import Final
import yfinance as yf

STOCK_SYMBOLS: Final[dict[str, str]] = {
    # BVC
    "bogota": "BOGOTA.CL",
    "bolivar": "GRUPOBOLIVAR.CL",
    "bvc": "BVC.CL",
    "celsia": "CELSIA.CL",
    "corfi": "CORFICOLCF.CL",
    "ecopetrol": "ECOPETROL.CO",
    "exito": "EXITO.CL",
    "isa": "ISA.CL",
    "mineros": "MINEROS.CL",
    "pfargos": "PFGRUPOARG.CL",
    "pfaval": "PFAVAL.CL",
    "pfcibest": "PFCIBEST.CL",
    "pfdavi": "PFDAVIGRP.CL",
    "pfsura": "PFGRUPSURA.CL",
    "promigas": "PROMIGAS.CL",
    "sqmbco": "SQMBCO.CL",
    "terpel": "TERPEL.CL",
    # International
    "bbva": "BBVA",
    "bond": "BND",
    "circle": "CRCL",
    "gev": "GEV",
    "gold": "GLDM",
    "meli": "MELI",
    "nee": "NEE",
    "nu": "NU",
    "o": "O",
    "pwr": "PWR",
    "qqq": "QQQ",
    "schd": "SCHD",
    "silver": "SLV",
    "soxx": "SOXX",
    "tip": "TIP",
    "vigi": "VIGI",
    "vrt": "VRT",
    "vwo": "VWO",
    "xle": "XLE",
    "xlp": "XLP",
}


def get_stock_price(stock_name: str) -> str:
    """
    Returns the current stock price for the given stock name.
    """
    stock_symbol = STOCK_SYMBOLS.get(stock_name.lower())

    if not stock_symbol:
        return f"Stock '{stock_name}' not found in the portfolio. Current portfolio includes: {', '.join(STOCK_SYMBOLS.keys())}."

    stock_info = yf.Ticker(stock_symbol)
    current_price = stock_info.info.get("regularMarketPrice")

    if current_price is None:
        return f"Could not retrieve the price for {stock_name}."

    return f"The current price of {stock_name} is ${current_price:.2f}."
