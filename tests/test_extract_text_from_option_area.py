import pytest
import numpy as np

from app.extract_text_from_option_area import extract_text_from_option_area
from app.load_image import load_image
from app.point import Point



@pytest.fixture
def image():
    image = load_image(path='./tests/fixtures/parts/part_img_1.png')
    if image is None:
        pytest.skip('Image is None, so skip the test.')
    return image



def test_extract_text_from_option_area(image, mocker):
    expected = 'expected text'
    mocker.patch('app.extract_text_from_option_area.extract_text', return_value=expected)
    got = extract_text_from_option_area(image=image)
    assert got == expected



def test_extract_text_from_option_area_when_ticked_area_width_is_bigger_than_image_width(image):
    ticked_area_width = 2000
    with pytest.raises(ValueError, match='larger than image width'):
        extract_text_from_option_area(image=image, ticked_area_width=ticked_area_width)



def test_extract_text_from_option_area_when_image_is_none():
    with pytest.raises(ValueError, match='Image is None'):
        extract_text_from_option_area(image=None)  # type: ignore[arg-type]



def test_extract_text_from_option_area_when_cropping_return_none(mocker, image):
    mock_crop_image = mocker.patch('app.extract_text_from_option_area.crop_image', return_value=None)

    with pytest.raises(ValueError, match='Failed to crop image'):
        extract_text_from_option_area(image=image)

    args, kwargs = mock_crop_image.call_args

    img_arg = kwargs['image'] if kwargs else args[0]
    pt1_arg = kwargs['pt1'] if kwargs else args[1]
    pt2_arg = kwargs['pt2'] if kwargs else args[2]
    assert isinstance(img_arg, np.ndarray)
    assert isinstance(pt1_arg, Point)
    assert isinstance(pt2_arg, Point)
    mock_crop_image.assert_called_once()

