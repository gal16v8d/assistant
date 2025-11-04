"""This module provides a function to get the current stock price for a given stock name."""

from typing import Final
import yfinance as yf


STOCK_SYMBOLS: Final[dict[str, str]] = {
    "amazon": "AMZN",
    "apple": "AAPL",
    "argos": "PFCEMARGOS.CL",
    "banbogota": "BOGOTA.CL",
    "bbva": "BBVA",
    "bolivar": "GRUPOBOLIVAR.CL",
    "bvc": "BVC.CL",
    "cibest": "PFCIBEST.CL",
    "corficolom": "CORFICOLCF.CL",
    "davivienda": "PFDAVVNDA.CL",
    "ecopetrol": "ECOPETROL.CO",
    "exito": "EXITO.CL",
    "goldetf": "GOAUCO.CL",
    "google": "GOOGL",
    "mercadolibre": "MELI",
    "meta": "META",
    "mineros": "MINEROS.CL",
    "microsoft": "MSFT",
    "nu": "NU",
    "nvidia": "NVDA",
    "paypal": "PYPL",
    "sqmbco": "SQMBCO.CL",
    "sura": "GRUPOSURA.CL",
    "terpel": "TERPEL.CL",
    "tesla": "TSLA",
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
