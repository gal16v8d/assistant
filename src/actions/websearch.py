"""Interaction with web browser by ask."""

from typing import Any, Final

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By


CURRENCY_SYMBOLS: Final[dict[str, str]] = {
    "brl": "https://www.google.com/search?q=brl+to+cop+today",
    "chf": "https://www.google.com/search?q=chf+to+cop+today",
    "eur": "https://www.google.com/search?q=eur+to+cop+today",
    "gbp": "https://www.google.com/search?q=gbp+to+cop+today"
    "jpy": "https://www.google.com/search?q=jpy+to+cop+today",
    "mxn": "https://www.google.com/search?q=mxn+to+cop+today",
    "pen": "https://www.google.com/search?q=pen+to+cop+today",
    "usd": "https://www.google.com/search?q=usd+to+cop+today",
}

WEB_PAGE_SYMBOLS: Final[dict[str, str]] = {
    "animeplanet": "https://www.anime-planet.com",
    "chess": "https://www.chess.com",
    "github": "https://www.github.com/gal16v8d",
    "google": "https://www.google.com",
    "wikipedia": "https://www.wikipedia.org",
    "youtube": "https://www.youtube.com",
}


def open_webpage(url: str, allowed_symbols: dict[str, str]) -> str:
    """
    Open a webpage in the default web browser.

    :param url: The URL of the webpage to open.
    :param allowed_symbols: A dictionary mapping symbols to their corresponding URLs.
    :return: A message indicating the result of the operation.
    """
    try:
        resolved_url = allowed_symbols.get(url)
        if not resolved_url:
            return f"'{url}' not in available sites. Current sites: {', '.join(allowed_symbols.keys())}."

        webbrowser.open(resolved_url)
        return f"Opening {resolved_url} in the web browser."
    except Exception as e:
        print(f"An error occurred while trying to open the webpage: {e}")
        return f"Failed to open {url}. Please check the available options and try again."


def top_anime(**_: dict[str, Any]) -> str:
    """
    Open the top anime page in the web browser.
    """
    url = f"{WEB_PAGE_SYMBOLS.get('animeplanet')}anime/top-anime"
    try:
        driver = webdriver.Firefox()
        driver.get(url)
        matched_elements = driver.find_elements(By.CLASS_NAME, "tooltip")
        element_text = [element.text for element in matched_elements]
        return f"Top anime results: {', '.join(element_text)}"
    except Exception as e:
        print(f"An error occurred while trying to open the top anime page: {e}")
        return "Failed to open top anime page. Please check your browser setup."
