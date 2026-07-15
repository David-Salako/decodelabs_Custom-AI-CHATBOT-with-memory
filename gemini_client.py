"""
Thin wrapper around the Gemini API that turns a ChatHistory into the
role/parts payload the SDK expects, and sends it as a single stateful
transaction (the "Terminal Append Sequence" from the brief).
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from history_manager import ChatHistory

load_dotenv()

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

SYSTEM_INSTRUCTION = (
    "You are a helpful, friendly assistant. Keep answers concise unless "
    "the user asks for detail. You have access to the full conversation "
    "history below -- use it to stay consistent and remember what the "
    "user has told you."
)


def _get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Copy .env.example to .env and add "
            "your key from Google AI Studio."
        )
    return genai.Client(api_key=api_key)


def _history_to_contents(history: ChatHistory) -> list[types.Content]:
    """Converts our Turn objects into the SDK's Content(role, parts) shape."""
    return [
        types.Content(role=turn.role, parts=[types.Part(text=turn.text)])
        for turn in history.get_turns()
    ]


def send_message(history: ChatHistory, user_message: str, model: str = DEFAULT_MODEL) -> str:
    """
    Appends the user's message to history, sends the full history array
    to Gemini, appends the model's reply, and returns the reply text.
    """
    client = _get_client()

    history.add_user(user_message)
    contents = _history_to_contents(history)

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.7,
        ),
    )

    reply_text = response.text
    history.add_model(reply_text)
    return reply_text
