from providers.tts.base import TTSProvider


class MacOSSayTTSProvider(TTSProvider):
    def speak(self, text: str) -> None:
        raise NotImplementedError

    def stop(self) -> None:
        raise NotImplementedError
