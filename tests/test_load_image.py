from app.load_image import load_image
from numpy import ndarray



def test_load_image():
    path = ''
    got = load_image(path=path)
    assert got is None


def test_load_image2():
    path = './tests/fixtures/IMG_4731.png'
    got = load_image(path=path)
    assert got is not None
    assert isinstance(got, ndarray)
