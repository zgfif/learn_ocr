import pytest
from app.detect_option_correctness import detect_option_correctness, ERR_IMAGE_HAS_BOTH, ERR_IS_NOT_OPTION
from app.invalid_image_error import InvalidImageError



@pytest.mark.parametrize('has_ticked, has_unticked, expected', 
    [
        (True, False, True),
        (False, True, False)
    ],
    ids=[
        'ticked True and unticked False -> True', 
        'ticked False and unticked True -> False'
    ]
)
def test_option_correctness(has_ticked, has_unticked, expected):
    got = detect_option_correctness(has_ticked, has_unticked)
    assert got == expected


def test_option_correctness_has_both():
    with pytest.raises(InvalidImageError, match=ERR_IMAGE_HAS_BOTH):
        detect_option_correctness(True, True)


def test_option_correctness_has_not_any():
    with pytest.raises(InvalidImageError, match=ERR_IS_NOT_OPTION):
        detect_option_correctness(False, False)

