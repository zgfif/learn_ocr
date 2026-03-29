import pytest

from app.build_option import build_option, ERR_EMPTY_TEXT
from app.option import Option


EXTRACT_TEXT_FROM_OPTION_AREA: str = 'app.build_option.extract_text_from_option_area'


@pytest.fixture
def fake_image():
    return object()



def test_build_option(mocker, fake_image):
    mocker.patch(EXTRACT_TEXT_FROM_OPTION_AREA, return_value='text')
    got = build_option(fake_image, True)
    assert got == Option(text='text', correctness=True)


def test_build_option_when_no_text(mocker, fake_image):
    mocker.patch(EXTRACT_TEXT_FROM_OPTION_AREA, return_value='')
    with pytest.raises(ValueError, match=ERR_EMPTY_TEXT):
        build_option(fake_image, True)
    

