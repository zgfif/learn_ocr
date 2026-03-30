import pytest
from typing import Sequence

from app.find_template_coordinates import find_template_coordinates
from app.load_image import load_image
from app.types import Coordinates



def close(
    p1: Coordinates, 
    p2: Coordinates, 
    tol: int = 2
) -> bool:
    """
    Return True if points are within tolerance.
    """
    return abs(p1[0] - p2[0]) <= tol and abs(p1[1] - p2[1]) <= tol



def assert_points_are_close(
    got: Sequence[Coordinates], 
    expected: Sequence[Coordinates], 
    tol: int = 2
) -> None:
    assert len(got) == len(expected)
    assert all(any(close(g, e, tol) for g in got) for e in expected)



@pytest.fixture
def image_4731():
    """
    Return IMG_4731.png as NDArray.
    """
    image = load_image(path='./tests/fixtures/IMG_4731.png')
    if image is None:
        pytest.skip('Test image not found.')
    return image



@pytest.fixture
def image_4732():
    """
    Return IMG_4732.png as NDArray.
    """
    image = load_image(path='./tests/fixtures/IMG_4732.png')
    if image is None:
        pytest.skip('Test image not found.')
    return image



@pytest.fixture
def ticked():
    """
    Return ticked.png as NDArray
    """
    ticked_image = load_image(path='./img/ticked.png')
    if ticked_image is None:
        pytest.skip('Test image not found.')
    return ticked_image



@pytest.fixture
def unticked():
    """
    Return unticked.png as NDArray
    """
    unticked_image = load_image(path='./img/unticked.png')
    if unticked_image is None:
        pytest.skip('Test image not found.')
    return unticked_image



@pytest.fixture
def logo():
    """
    Return youtube_logo.jpg as NDArray
    """
    logo = load_image(path='./img/youtube_logo.jpg')
    if logo is None:
        pytest.skip('Test image not found.')    
    return logo



def test_one_object_on_image(image_4731, ticked) -> None:
    got = find_template_coordinates(
        image=image_4731, 
        template=ticked,
    )
    expected = [(37, 404),]
    assert_points_are_close(got, expected)



def test_two_objects_on_image(image_4732, ticked) -> None:
    got = find_template_coordinates(
        image=image_4732, 
        template=ticked,
    )
    expected = [(37, 894), (37, 1136),]
    assert_points_are_close(got, expected)



def test_when_invalid_path_to_image(logo) -> None:
    got = find_template_coordinates(
        image=load_image(''),
        template=logo,
    )
    assert got == []



def test_when_invalid_path_to_template(image_4732) -> None:
    got = find_template_coordinates(
        image=image_4732, 
        template=load_image(''),
    )
    assert got == []



def test_when_can_not_find_template(image_4732, logo) -> None:
    got = find_template_coordinates(
        image=image_4732, 
        template=logo,
    )
    assert got == []



def test_bug_from_4731(unticked) -> None:
    got = find_template_coordinates(
        image=load_image('./tests/fixtures/part_with_bug.png'), 
        template=unticked,
    )
    assert len(got) == 1
    x, y = got[0]
    assert x > 0
    assert y > 0
