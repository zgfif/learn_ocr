import pytest

from app.process_image_part import process_image_part
from app.option import Option
from app.invalid_image_error import InvalidImageError


FIND_TEMPLATE_COORDS: str = 'app.process_image_part.find_template_coordinates'
EXTRACT_QUESTION_TEXT: str = 'app.process_image_part.extract_question_text'
BUILD_OPTION: str = 'app.process_image_part.build_option'


@pytest.fixture
def fake_image() -> object:
    return object()


@pytest.fixture
def option1():
    return Option(text='Option1', correctness=False)


@pytest.fixture
def option2():
    return Option(text='Option2', correctness=True)


@pytest.fixture
def question_text0():
    return 'Question text 1'


@pytest.fixture
def fake_template():
    return object()


def test_process_image_part1(mocker, fake_image, fake_template, option1):
    mocker.patch(
        FIND_TEMPLATE_COORDS, 
        side_effect=[
            [], # ticked coordinates
            [(10, 20)] # unticked coordinates
        ]
    )
    mocker.patch(BUILD_OPTION, return_value=option1)
    got = process_image_part(fake_image, fake_template, fake_template)
    assert got == option1



def test_process_image_part2(mocker, fake_image, fake_template, option2):
    mocker.patch(
        FIND_TEMPLATE_COORDS, 
        side_effect=[
            [(10, 20)], # ticked coordinates
            [] # unticked coordinates
        ]
    )
    mocker.patch(BUILD_OPTION, return_value=option2)
    got = process_image_part(fake_image, fake_template, fake_template)
    assert got == option2


def test_process_image_part_when_both_ticked_and_unticked(mocker, fake_image, fake_template):
    mocker.patch(
        FIND_TEMPLATE_COORDS, 
        side_effect=[
            [(10, 20)], # ticked coordinates
            [(30, 40)] # unticked coordinates
        ]
    )
    with pytest.raises(InvalidImageError):
        process_image_part(fake_image, fake_template, fake_template)
