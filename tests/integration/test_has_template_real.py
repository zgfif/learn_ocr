from dataclasses import dataclass
from pathlib import Path

from cv2.typing import MatLike
import pytest

from app.has_template import has_template
from app.load_image import load_image


BASE_PATH: Path = Path(__file__).resolve().parents[1]
FIXTURES_PATH: Path = BASE_PATH / "fixtures" / "parts"
TEMPLATES_PATH: Path = BASE_PATH.parent / "img"



@dataclass
class Case:
    image: str
    template: str
    expected: bool


    def id(self) -> str:
        return f"{self.image[-6:]} | {self.template[-6:]} -> {self.expected}"



@pytest.fixture
def load():
    def _load_img(base_path: Path, filename: str) -> MatLike:
        full_path = base_path / filename
        image = load_image(str(full_path))
        if image is None:
            raise FileNotFoundError(f"Cannot load image: {full_path}")
        return image
    return _load_img



cases: list[Case] = [
    Case("part_img_0.png", "ticked.png", False),
    Case("part_img_0.png", "unticked.png", False),
    Case("part_img_1.png", "ticked.png", False),
    Case("part_img_1.png", "unticked.png", True),
    Case("part_img_2.png", "ticked.png", True),
    Case("part_img_2.png", "unticked.png", False),
    Case("part_img_3.png", "ticked.png", True),
    Case("part_img_3.png", "unticked.png", False),
]

@pytest.mark.parametrize(
    "case", 
    cases,
    ids=[c.id() for c in cases]
)
def test_has_template(case: Case, load) -> None:
    image = load(FIXTURES_PATH, case.image)
    template = load(TEMPLATES_PATH, case.template)
    got = has_template(image, template)
    assert got == case.expected, (
        f"{case.image=}:{case.template=} expected {case.expected} got {got}"
    )
