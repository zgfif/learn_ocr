from dataclasses import dataclass



@dataclass(frozen=True)
class Option:
    text: str
    correctness: bool

    def __repr__(self) -> str:
        return f'{self.text} - {self.correctness}'

