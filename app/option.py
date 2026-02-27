from dataclasses import dataclass



@dataclass(frozen=True)
class Option:
    text: str
    correctness: bool
