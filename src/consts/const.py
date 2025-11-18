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
MODEL_AI_TEXT_MSG: Final[str] = "Please choose the AI model (gemini or v3): "
MODEL_AI_VOICE_MSG: Final[str] = "Please say the AI model (gemini or v3)."
NO_AI_MODEL_MSG: Final[str] = "No AI model provided. Please try again."
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
