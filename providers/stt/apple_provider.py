from providers.stt.base import STTProvider
import numpy as np


class AppleSTTProvider(STTProvider):
    def transcribe(self, audio: np.ndarray, sample_rate: int) -> str:
        raise NotImplementedError
