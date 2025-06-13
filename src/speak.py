"""This module provides a simple text-to-speech functionality using pyttsx3."""

from typing import Any
import pyttsx3


# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(text: str) -> Any:
    """
    Speaks the given text using the text-to-speech engine.
    """
    # For debugging purposes
    print(f"Speaking: {text}")

    engine.say(text)
    engine.runAndWait()
