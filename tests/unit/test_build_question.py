import pytest
from app.build_question import build_question, ERR_CAN_NOT_PROCESS_IMAGE, ERR_NO_OPITONS, ERR_NO_QUESTION
from app.option import Option


PROCESS_IMAGE_PART: str = 'app.build_question.process_image_part'


@pytest.fixture
def fake_parts():
    return [object(), object(), object(), object()]


@pytest.fixture
def fake_template():
    return object()


def test_process_image_parts_can_not_process_image(mocker, fake_parts, fake_template):
    mocker.patch(
        PROCESS_IMAGE_PART, 
        side_effect=[
            'question',
            None,
            'option',
            'opiton,'
        ]
    )
    with pytest.raises(ValueError, match=ERR_CAN_NOT_PROCESS_IMAGE):
        build_question(fake_parts, fake_template, fake_template)


def test_process_image_parts_when_no_options(mocker, fake_parts, fake_template):
    mocker.patch(
        PROCESS_IMAGE_PART, side_effect=[
            'question',
            'question',
            'option',
            'opiton,'
            ]
    )
    with pytest.raises(ValueError, match=ERR_NO_OPITONS):
        build_question(fake_parts, fake_template, fake_template)


def test_process_image_parts_when_no_question(mocker, fake_parts, fake_template):
    mocker.patch(
        PROCESS_IMAGE_PART, side_effect=[
            Option(text='abc', correctness=True),
            Option(text='edf', correctness=False),
            Option(text='auf', correctness=True),
            Option(text='www', correctness=False),
            ]
    )
    with pytest.raises(ValueError, match=ERR_NO_QUESTION):
        build_question(fake_parts, fake_template, fake_template)