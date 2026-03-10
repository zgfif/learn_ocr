from dataclasses import dataclass
from app.option import Option


@dataclass(frozen=True)
class Question:
    text: str
    options: list[Option]
