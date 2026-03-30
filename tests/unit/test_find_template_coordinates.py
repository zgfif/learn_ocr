import pytest

from app.find_template_coordinates import find_template_coordinates, ERR_DOES_NOT_HAVE_SHAPE



@pytest.fixture
def fake_image() -> object:
    return object()



@pytest.fixture
def fake_template() -> object:
    return object()



def test_raise_value_error(mocker, fake_image, fake_template) -> None:
    mocker.patch('app.find_template_coordinates.fetch_match_map')
    mocker.patch('app.find_template_coordinates.fetch_locations')
    with pytest.raises(ValueError, match=ERR_DOES_NOT_HAVE_SHAPE):
        find_template_coordinates(fake_image, fake_template)
