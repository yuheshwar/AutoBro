from providers.stt.base import STTProvider
import numpy as np


class WhisperSTTProvider(STTProvider):
    def transcribe(self, audio: np.ndarray, sample_rate: int) -> str:
        raise NotImplementedError
