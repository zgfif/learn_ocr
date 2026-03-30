import pytest

from pathlib import Path
from cv2.typing import MatLike

from app.has_template import has_template
from app.load_image import load_image


BASE_PATH: Path = Path(__file__).resolve().parent.parent
FIXTURES_PATH: Path = BASE_PATH / "fixtures" / "parts"
TEMPLATES_PATH: Path = BASE_PATH.parent / "img"



def func():
    return 'aaa'


def load_img(
    base_path: Path, 
    filename: str
) -> MatLike:
    full_path = base_path / filename
    image = load_image(str(full_path))
    if image is None:
        raise FileNotFoundError(f"Cannot load image: {full_path}")
    return image



def _load_from(base_path: Path, request: pytest.FixtureRequest) -> MatLike:
    try:
        return load_img(base_path=base_path, filename=request.param)
    except FileNotFoundError as e:
        pytest.skip(str(e))


@pytest.fixture
def image(request: pytest.FixtureRequest) -> MatLike:
    return _load_from(base_path=FIXTURES_PATH, request=request)



@pytest.fixture
def template(request: pytest.FixtureRequest) -> MatLike:
    return _load_from(base_path=TEMPLATES_PATH, request=request)



@pytest.mark.parametrize(
    "image, template, expected", 
    [
        ("part_img_0.png", "ticked.png", False),
        ("part_img_0.png", "unticked.png", False),
        ("part_img_1.png", "ticked.png", False),
        ("part_img_1.png", "unticked.png", True),
        ("part_img_2.png", "ticked.png", True),
        ("part_img_2.png", "unticked.png", False),
        ("part_img_3.png", "ticked.png", True),
        ("part_img_3.png", "unticked.png", False),
    ],
    ids=[
        "img_0 ticked -> False",
        "img_0 unticked -> False",
        "img_1 ticked -> False",
        "img_1 unticked -> True",
        "img_2 ticked -> True",
        "img_2 unticked -> False",
        "img_3 ticked -> True",
        "img_3 unticked -> False",
    ],
    indirect=["image", "template"],
)
def test_has_template(
    image: MatLike, 
    template: MatLike, 
    expected: bool
) -> None:
    assert has_template(image, template) is expected, "Unexpected result for template match."
