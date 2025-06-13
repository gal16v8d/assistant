"""Command AI Adapter to required action."""

from typing import Any

from actions import (
    get_ai_image_response,
    get_ai_image_response_v3,
    get_ai_text_response,
)
from consts import const
from processor.input_processor import get_user_input


def get_ai_text_args(**kwargs: dict[str, Any]) -> str:
    """
    Returns the AI text response based on the input type.
    """
    ai_text = get_user_input(
        request_value_t=const.TEXT_AI_MSG,
        request_value_v=const.VOICE_AI_MSG,
        error_msg=const.NO_AI_TEXT_MSG,
        **kwargs
    )

    return get_ai_text_response(ai_text)


def get_ai_image_args(**kwargs: dict[str, Any]) -> str:
    """
    Returns the AI image response based on the input type.
    """
    ai_text = get_user_input(
        request_value_t=const.TEXT_AI_MSG,
        request_value_v=const.VOICE_AI_MSG,
        error_msg=const.NO_AI_TEXT_MSG,
        **kwargs
    )
    title = get_user_input(
        request_value_t=const.TITLE_AI_TEXT_MSG,
        request_value_v=const.TITLE_AI_VOICE_MSG,
        error_msg=const.NO_AI_TITLE_MSG,
        **kwargs
    )
    model = get_user_input(
        request_value_t=const.MODEL_AI_TEXT_MSG,
        request_value_v=const.MODEL_AI_VOICE_MSG,
        error_msg=const.NO_AI_MODEL_MSG,
        **kwargs
    )
    if model == "v3":
        return get_ai_image_response_v3(ai_text, title)
    return get_ai_image_response(ai_text, title)
