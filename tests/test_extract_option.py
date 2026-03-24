import pytest
from pathlib import Path

from app.extract_option import extract_option
from app.load_image import load_image
from app.option import Option
from app.extract_option import ERR_IMAGE_NONE, ERR_TICKED_UNTICKED_NONE, ERR_BOTH_HAS_TICKED_UNTICKED



TESTS_PATH = Path(__file__).parent
FIXTURES_PATH: Path = TESTS_PATH / 'fixtures'
PATTERNS_PATH: Path = TESTS_PATH.parent / 'img'


FIND_TEMPLATE_COORDS: str = 'app.extract_option.find_template_coordinates'
EXTRACT_TEXT_FROM_OPTION_AREA: str = 'app.extract_option.extract_text_from_option_area'


def load_image_from(base_path: Path, *parts: str):
    path = str(base_path.joinpath(*parts))
    image = load_image(path)
    if image is None:
        pytest.skip('Image not loaded.')
    return image



@pytest.fixture
def option_image_1():
    return load_image_from(FIXTURES_PATH, 'parts', 'part_img_1.png')


@pytest.fixture
def option_image_2():
    return load_image_from(FIXTURES_PATH, 'parts', 'part_img_2.png')


@pytest.fixture
def ticked_template():
    return load_image_from(PATTERNS_PATH, 'ticked.png')


@pytest.fixture
def unticked_template():
    return load_image_from(PATTERNS_PATH, 'unticked.png')


@pytest.fixture
def fake_image():
    return object()


@pytest.fixture
def fake_template():
    return object()


def test_extract_option_1(option_image_1, ticked_template, unticked_template):
    expected = Option(
        text='Anordnung zum erneuten Ablegen einer theoretischen Fahrerlaubnisprüfung',
        correctness=False
    )
    got = extract_option(
        image=option_image_1, 
        ticked_template=ticked_template, 
        unticked_template=unticked_template
    )
    assert got == expected



def test_extract_option_2(option_image_2, ticked_template, unticked_template):
    expected = Option(
        text='Anordnung zur Teilnahme an einem Aufbauseminar für Fahranfänger', 
        correctness=True
    )
    got = extract_option(
        image=option_image_2, 
        ticked_template=ticked_template, 
        unticked_template=unticked_template
    )
    assert got == expected



def test_extract_option_when_image_is_none(ticked_template, unticked_template):
    with pytest.raises(ValueError, match=ERR_IMAGE_NONE):
        extract_option(
            image=None,   # type: ignore[arg-type]
            ticked_template=ticked_template, 
            unticked_template=unticked_template
        )



@pytest.mark.parametrize('ticked_template, unticked_template', [
    (object(), None),
    (None, object()),
    (None, None)
])
def test_extract_option_invalid_templates(option_image_1, ticked_template, unticked_template):
    with pytest.raises(ValueError, match=ERR_TICKED_UNTICKED_NONE):
        extract_option(
            image=option_image_1, 
            ticked_template=ticked_template,
            unticked_template=unticked_template
        )



def test_extract_option_return_none(mocker, fake_image, fake_template):
    mocker.patch(FIND_TEMPLATE_COORDS, return_value=[])
    got = extract_option(fake_image, fake_template, fake_template)
    assert got is None



def test_extract_option_when_has_ticked_and_unticked_coordinates(mocker, fake_image, fake_template):
    ticked_coordinates = [(10, 11)] # ticked
    unticked_coordinates = [(3, 5)] # unticked
    
    mocker.patch(
        FIND_TEMPLATE_COORDS,
        side_effect=[ticked_coordinates, unticked_coordinates]
    )
    with pytest.raises(ValueError, match=ERR_BOTH_HAS_TICKED_UNTICKED):
        extract_option(fake_image, fake_template, fake_template)



def test_extract_option_when_has_only_ticked(mocker, fake_image, fake_template):
    expected = Option(text='Option 1', correctness=True)

    ticked_coordinates = [(10, 11)] # ticked
    unticked_coordinates = []  # unticked
    
    mocker.patch(
        FIND_TEMPLATE_COORDS, 
        side_effect=[ticked_coordinates, unticked_coordinates]
    )
    mocker.patch(
        EXTRACT_TEXT_FROM_OPTION_AREA, 
        return_value='Option 1'
    )
    got = extract_option(fake_image, fake_template, fake_template)
    assert got == expected



def test_extract_option_when_has_only_unticked(mocker, fake_image, fake_template):
    expected = Option(text='Option 2', correctness=False)

    ticked_coordinates = []
    unticked_coordinates = [(10, 11)]

    mocker.patch(
        FIND_TEMPLATE_COORDS,
        side_effect=[ticked_coordinates, unticked_coordinates]
    )
    mocker.patch(
        EXTRACT_TEXT_FROM_OPTION_AREA, 
        return_value='Option 2'
    )
    got = extract_option(fake_image, fake_template, fake_template)
    assert got == expected



def test_extract_option_when_has_no_text_and_ticked(mocker, fake_image, fake_template):
    expected = Option(text='', correctness=True)

    ticked_coordinates = [(10, 11)]
    unticked_coordinates = []

    mocker.patch(
        FIND_TEMPLATE_COORDS,
        side_effect=[ticked_coordinates, unticked_coordinates]
    )
    mocker.patch(
        EXTRACT_TEXT_FROM_OPTION_AREA, 
        return_value=''
    )
    got = extract_option(fake_image, fake_template, fake_template)
    assert got == expected