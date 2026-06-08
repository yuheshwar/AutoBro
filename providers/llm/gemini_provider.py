from providers.llm.base import LLMProvider


class GeminiLLMProvider(LLMProvider):
    def ask(self, transcript: str, screenshot_b64: str, history: list[dict]) -> str:
        raise NotImplementedError
