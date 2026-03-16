from app.fetch_match_map import fetch_match_map
from app.load_image import load_image
from numpy import ndarray
from pytest import raises



def test_fetch_match_map():
    image = load_image('./tests/fixtures/IMG_4731.png')
    template = load_image('./img/checked.png')
    assert image is not None
    assert template is not None
    got = fetch_match_map(image=image, template=template)
    assert isinstance(got, ndarray)
    assert len(got) == image.shape[0] - template.shape[0] + 1
    assert len(got[0]) == image.shape[1] - template.shape[1] + 1
    assert len(got[-1]) == image.shape[1] - template.shape[1] + 1

    assert got.ndim == 2



def test_fetch_match_map_with_raising():
    template = load_image('./tests/fixtures/IMG_4731.png')
    image = load_image('./img/checked.png')
    assert image is not None
    assert template is not None

    with raises(ValueError) as excinfo:
        fetch_match_map(image=image, template=template)
    assert 'Template size (' in str(excinfo.value)