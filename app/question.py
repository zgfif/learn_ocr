from dataclasses import dataclass



@dataclass(frozen=True)
class Question:
    text: str
    options: str
