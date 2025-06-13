"""Interaction with web browser by ask."""

from typing import Any

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By


WEB_PAGE_SYMBOLS = {
    "animeplanet": "https://www.anime-planet.com",
    "chess": "https://www.chess.com",
    "github": "https://www.github.com/gal16v8d",
    "google": "https://www.google.com",
    "pricedolar": "https://www.google.com/search?q=dolar+today+cop",
    "priceeuro": "https://www.google.com/search?q=euro+today+cop",
    "priceyen": "https://www.google.com/search?q=yen+today+cop",
    "wikipedia": "https://www.wikipedia.org",
    "youtube": "https://www.youtube.com",
}


def open_webpage(url: str) -> str:
    """
    Open a webpage in the default web browser.

    :param url: The URL of the webpage to open.
    """
    try:
        resolved_url = WEB_PAGE_SYMBOLS.get(url)
        if not resolved_url:
            return f"URL '{url}' not in available sites. Current sites: {', '.join(WEB_PAGE_SYMBOLS.keys())}."

        webbrowser.open(resolved_url)
        return f"Opening {resolved_url} in the web browser."
    except Exception as e:
        print(f"An error occurred while trying to open the webpage: {e}")
        return f"Failed to open {url}. Please check the URL and try again."


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
