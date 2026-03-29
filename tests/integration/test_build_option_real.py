import pytest

from app.build_option import build_option
from app.load_image import load_image
from app.option import Option



@pytest.fixture
def image0():
    image = load_image('./tests/fixtures/parts/part_img_0.png')
    if image is None:
        pytest.skip('Can not load image.')
    return image


@pytest.fixture
def image1():
    image = load_image('./tests/fixtures/parts/part_img_1.png')
    if image is None:
        pytest.skip('Can not load image.')
    return image


@pytest.fixture
def image2():
    image = load_image('./tests/fixtures/parts/part_img_2.png')
    if image is None:
        pytest.skip('Can not load image.')
    return image



@pytest.fixture
def option0():
    return Option(
        text=(
            "ıden sich in der Probezeit und sind bisher ffällig geworden. "\
            "Welche Folgen können ı, wenn Sie an dem Verkehrszeichen „Halt. "\
            "gewähren.“ nicht anhalten und dadurch /erkehrsteilnehmer gefährden?"
        ), 
        correctness=True
    )


@pytest.fixture
def option1():
    return Option(
        text='Anordnung zum erneuten Ablegen einer theoretischen Fahrerlaubnisprüfung', 
        correctness=False
    )


@pytest.fixture
def option2():
    return Option(
        text='Anordnung zur Teilnahme an einem Aufbauseminar für Fahranfänger', 
        correctness=True
    )


def test_build_option0(image0, option0) -> None:
    assert build_option(image=image0, correctness=True) == option0


def test_build_option1(image1, option1) -> None:
    assert build_option(image=image1, correctness=False) == option1


def test_build_option2(image2, option2) -> None:
    assert build_option(image=image2, correctness=True) == option2
