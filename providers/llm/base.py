from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def ask(self, transcript: str, screenshot_b64: str, history: list[dict]) -> str: ...
