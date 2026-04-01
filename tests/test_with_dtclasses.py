import pytest
from dataclasses import dataclass



@dataclass
class Case:
    a: int
    b: int
    expected: int
    id: str



cases: list[Case] = [
    Case(a=2, b=3, expected=5, id='simple sum 2 + 3'),
    Case(a=6, b=4, expected=10, id='sum 6 + 4'),
]



@pytest.mark.parametrize("case", cases, ids=[c.id for c in cases])
def test_add(case: Case) -> None:
    assert case.a + case.b == case.expected


