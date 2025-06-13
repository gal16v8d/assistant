"""assistant will listen to the user and respond accordingly"""

from builtins import input, callable
from typing import Any, Final

from actions import (
    ask_time,
    get_joke,
    top_anime,
    weekday,
)
from adapters import (
    get_ai_image_args,
    get_ai_text_args,
    get_stock_args,
    open_webpage_args,
)
from consts import const
from processor.input_processor import get_user_input
from speak import speak


class Assistant:

    def __init__(self):
        self.status = "Running"

    def end_assistant(self, **_: dict[str, Any]) -> str:
        """
        Finish the virtual assistant.
        """
        self.status = "Stopped"
        return const.EXIT_MSG


if __name__ == "__main__":
    speak(const.WELCOME_MSG)
    assistant = Assistant()

    choose_input = input(const.INPUT_TYPE_MSG).strip().lower()
    while choose_input not in (const.VOICE_INPUT, const.TEXT_INPUT):
        speak(const.INVALID_INPUT_MSG)
        choose_input = input(const.INPUT_TYPE_MSG).strip().lower()

    APP_OPTIONS: Final[dict[str, callable]] = {
        "ai image": get_ai_image_args,
        "ai text": get_ai_text_args,
        "exit": assistant.end_assistant,
        "joke": get_joke,
        "stock": get_stock_args,
        "time": ask_time,
        "top anime": top_anime,
        "web search": open_webpage_args,
        "weekday": weekday,
    }

    while assistant.status == "Running":
        speak(f"{const.USE_ONE_OF_THE_OPTIONS_MSG} {', '.join(APP_OPTIONS.keys())}")

        user_input = get_user_input(
            request_value_t=const.TEXT_MENU_MSG,
            error_msg=const.NO_OPTION_MSG,
            choose_input=choose_input,
        )

        if user_input in APP_OPTIONS:
            speak(APP_OPTIONS[user_input](choose_input=choose_input))
        else:
            speak(f"{const.INVALID_OPTION_MSG}'{user_input}'. {const.TRY_AGAIN_MSG}")
