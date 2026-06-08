from typing import Literal


def classify(transcript: str) -> Literal["chat", "action", "browser", "memory"]:
    raise NotImplementedError
