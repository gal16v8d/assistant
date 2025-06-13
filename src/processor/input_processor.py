from builtins import input
from typing import Any

from consts import const
from listen import listen
from speak import speak


def _process_user_input(**kwargs: dict[str, Any]) -> Any | None:
    """
    Get user input based on the chosen input type.
    If the input type is voice, it will listen for the input.
    If the input type is text, it will prompt for input.
    """
    assistant_input = kwargs.get("choose_input", const.TEXT_INPUT).strip().lower()
    if assistant_input == const.VOICE_INPUT:
        if "request_value_v" in kwargs:
            speak(kwargs.get("request_value_v"))
        value = listen()
    else:
        value = input(kwargs.get("request_value_t")).strip()
    return value


def get_user_input(**kwargs: dict[str, Any]) -> str:
    """
    Validate the user input.
    If the input is empty, it will prompt the user to try again
    until a valid input is provided.
    """
    error_msg = kwargs.get("error_msg")
    result = _process_user_input(**kwargs)

    while not result:
        speak(error_msg)
        result = _process_user_input(**kwargs)
    return str(result)
