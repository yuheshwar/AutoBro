from providers.llm.base import LLMProvider


class OllamaLLMProvider(LLMProvider):
    def ask(self, transcript: str, screenshot_b64: str, history: list[dict]) -> str:
        raise NotImplementedError
