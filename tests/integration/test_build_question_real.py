import pytest

from pathlib import Path
from cv2.typing import MatLike

from app.build_question import build_question, ERR_CAN_NOT_LOAD_TEMPLATES
from app.load_image import load_image
from app.option import Option
from app.question import Question



FIXTURES_PATH: Path = Path(__file__).parents[1].joinpath('fixtures')
PATTERNS_PATH: Path = Path(__file__).parents[2].joinpath('img')


question_text: str = (
    "Sie befinden sich in der Probezeit und sind bisher "\
    "nicht auffällig geworden. Welche Folgen können eintreten, wenn Sie an "\
    "dem Verkehrszeichen „Halt. Vorfahrt gewähren.“ nicht anhalten und "\
    "dadurch andere Verkehrsteilnehmer gefährden?"
)



parts1_paths: list[tuple[str, str]] = [
    ('parts', 'part_img_0.png'),
    ('parts', 'part_img_1.png'),
    ('parts', 'part_img_2.png'),
    ('parts', 'part_img_3.png'),
]



def load_from(base_path: Path, *parts: str):
    path = str(base_path.joinpath(*parts))
    image = load_image(path)
    if image is None:
        pytest.skip('can not load image')
    return image



def load_images(images_paths: list[tuple[str, str]]) -> list[MatLike]:
    images: list = []
    for image_path in images_paths:
        image = load_from(FIXTURES_PATH, *image_path)
        images.append(image)
    return images



def load_template(path: str) -> MatLike:
    return load_from(PATTERNS_PATH, path)



@pytest.fixture
def parts1() -> list[MatLike]:
    return load_images(parts1_paths)



@pytest.fixture
def ticked_template() -> MatLike:
    return load_template('ticked.png')



@pytest.fixture
def unticked_template() -> MatLike:
    return load_template('unticked.png')



@pytest.fixture
def question1() -> Question:
    return Question(
        text=question_text,
        options=[
            Option(text='Anordnung zum erneuten Ablegen einer theoretischen Fahrerlaubnisprüfung', correctness=False),
            Option(text='Anordnung zur Teilnahme an einem Aufbauseminar für Fahranfänger', correctness=True),
            Option(text='Eintrag in das Fahreignungsregister', correctness=True),
        ]
    )



def test_process_image_parts_when_no_ticked_template(parts1, unticked_template):
    with pytest.raises(ValueError, match=ERR_CAN_NOT_LOAD_TEMPLATES):
        build_question(parts1, None, unticked_template)   # type: ignore[arg-type]



def test_process_image_parts_when_no_unticked_template(parts1, ticked_template):
    with pytest.raises(ValueError, match=ERR_CAN_NOT_LOAD_TEMPLATES):
        build_question(parts1, ticked_template, None)   # type: ignore[arg-type]



def test_process_image_parts_when_no_both_templates(parts1):
    with pytest.raises(ValueError, match=ERR_CAN_NOT_LOAD_TEMPLATES):
        build_question(parts1, None, None)   # type: ignore[arg-type]



def test_process_image_parts_correct(parts1, ticked_template, unticked_template, question1):
    got = build_question(
        parts1, 
        ticked_template, 
        unticked_template
    )
    assert got == question1
