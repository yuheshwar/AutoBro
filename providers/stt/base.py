from abc import ABC, abstractmethod
import numpy as np


class STTProvider(ABC):
    @abstractmethod
    def transcribe(self, audio: np.ndarray, sample_rate: int) -> str: ...
