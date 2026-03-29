import pytest

from app.process_image_part import process_image_part
from app.option import Option
from app.load_image import load_image




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
def ticked():
    image = load_image('./img/ticked.png')
    if image is None:
        pytest.skip('Can not load image.')
    return image


@pytest.fixture
def unticked():
    image = load_image('./img/unticked.png')
    if image is None:
        pytest.skip('Can not load image.')
    return image




def test_process_image_part1(image1, ticked, unticked):
    expected = Option(
        text='Anordnung zum erneuten Ablegen einer theoretischen Fahrerlaubnisprüfung', 
        correctness=False
    )
    got = process_image_part(
        image=image1,
        ticked_template=ticked,
        unticked_template=unticked
    )
    assert got == expected


def test_process_image_part0(image0, ticked, unticked):
    expected: str = 'Sie befinden sich in der Probezeit und sind bisher nicht auffällig geworden. '\
        'Welche Folgen können eintreten, wenn Sie an dem Verkehrszeichen „Halt. '\
            'Vorfahrt gewähren.“ nicht anhalten und dadurch andere Verkehrsteilnehmer gefährden?'

    got = process_image_part(
        image=image0,
        ticked_template=ticked,
        unticked_template=unticked
    )
    assert got == expected



def test_process_image_part_when_none(ticked, unticked):
    with pytest.raises(ValueError):
        process_image_part(
            image=None,   # type: ignore[arg-type]
            ticked_template=ticked,
            unticked_template=unticked
        )
