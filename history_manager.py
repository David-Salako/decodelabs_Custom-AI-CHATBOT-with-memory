"""
This manages the in-memory conversation history array.

it also implements two things straight from the project brief:
1. The Structural Validation Gate -- reject empty/whitespace-only input
   before it reaches the API (prevents a 400 Bad Request crash).
2. The Sliding Window Algorithm -- FIFO-prune the oldest turns once the
   history grows past a safe size, so long sessions never blow the
   model's context window.
"""

from dataclasses import dataclass


@dataclass
class Turn:
    role: str  # "user" or "model"
    text: str


class ChatHistory:
    def __init__(self, max_turns: int = 20):
        # max_turns counts individual turns (user + model combined).
        # 20 turns ~= 10 full exchanges kept live in context.
        self.max_turns = max_turns
        self._turns: list[Turn] = []

    def add_user(self, text: str) -> None:
        self._turns.append(Turn(role="user", text=text))
        self._enforce_window()

    def add_model(self, text: str) -> None:
        self._turns.append(Turn(role="model", text=text))
        self._enforce_window()

    def _enforce_window(self) -> None:
        """FIFO truncation: drop the oldest turns once we exceed max_turns."""
        overflow = len(self._turns) - self.max_turns
        if overflow > 0:
            self._turns = self._turns[overflow:]

    def get_turns(self) -> list[Turn]:
        return list(self._turns)

    def clear(self) -> None:
        self._turns = []

    def turn_count(self) -> int:
        return len(self._turns)

    @staticmethod
    def validate_input(raw: str):
        """Returns cleaned text, or None if it's empty/whitespace-only."""
        cleaned = raw.strip()
        return cleaned if cleaned else None