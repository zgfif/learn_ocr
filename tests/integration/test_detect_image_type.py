import pytest

from app.detect_image_type import detect_image_type, ERR_IMAGE_HAS_BOTH
from app.image_type import ImageType
from app.invalid_image_error import InvalidImageError



@pytest.mark.parametrize('has_ticked, has_unticked, image_type', 
    [
        (False, False, ImageType.QUESTION),
        (True, False, ImageType.OPTION),
        (False, True, ImageType.OPTION),
    ],
    ids=[
        'no_templates -> QUESTION',
        'ticked_only -> OPTION',
        'unticked_only -> OPTION'
    ]
)
def test_detect_image_type_valid_cases(
    has_ticked: bool, 
    has_unticked: bool, 
    image_type: ImageType
) -> None:
    assert detect_image_type(has_ticked, has_unticked) == image_type



def test_detect_image_type_raises_when_both_present() -> None:
    with pytest.raises(InvalidImageError) as excinfo:
        detect_image_type(True, True)
    assert str(excinfo.value) == ERR_IMAGE_HAS_BOTH
