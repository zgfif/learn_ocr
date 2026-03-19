import pytest
import numpy as np
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
        tol: int = 2):
    assert len(got) == len(expected)
    assert all(any(close(g, e, tol) for g in got) for e in expected)



@pytest.fixture
def image_4731():
    """
    Return IMG_4731.png as NDArray
    """
    image = load_image(path='./tests/pytest.fixtures/IMG_4731.png')
    if image is None:
        pytest.skip('Test image not found.')
    return image



@pytest.fixture
def image_4732():
    """
    Return IMG_4732.png as NDArray
    """
    image = load_image(path='./tests/pytest.fixtures/IMG_4732.png')
    if image is None:
        pytest.skip('Test image not found.')
    return image



@pytest.fixture
def checked():
    """
    Return checked.png as NDArray
    """
    checked_image = load_image(path='./img/checked.png')
    if checked_image is None:
        pytest.skip('Test image not found.')
    return checked_image



@pytest.fixture
def unchecked():
    """
    Return unchecked.png as NDArray
    """
    unchecked_image = load_image(path='./img/unchecked.png')
    if unchecked_image is None:
        pytest.skip('Test image not found.')
    return unchecked_image


@pytest.fixture
def logo():
    """
    Return youtube_logo.jpg as NDArray
    """
    logo = load_image(path='./img/youtube_logo.jpg')
    if logo is None:
        pytest.skip('Test image not found.')    
    return logo



def test_one_object_on_image(image_4731, checked):
    got = find_template_coordinates(
        image=image_4731, 
        template=checked,
    )
    expected = [(37, 404),]
    assert_points_are_close(got, expected)



def test_two_objects_on_image(image_4732, checked):
    got = find_template_coordinates(
        image=image_4732, 
        template=checked,
    )
    expected = [(37, 894), (37, 1136),]
    assert_points_are_close(got, expected)



def test_when_invalid_path_to_image(logo):
    got = find_template_coordinates(
        image=load_image(''), 
        template=logo,
    )
    assert got == []



def test_when_invalid_path_to_template(image_4732):
    got = find_template_coordinates(
        image=image_4732, 
        template=load_image(''),
    )
    assert got == []



def test_when_can_not_find_template(image_4732, logo):
    got = find_template_coordinates(
        image=image_4732, 
        template=logo,
    )
    assert got == []



def test_bug_from_4731(unchecked):
    got = find_template_coordinates(
        image=load_image('./tests/fixtures/part_with_bug.png'), 
        template=unchecked,
    )
    assert len(got) == 1
    x, y = got[0]
    assert x > 0
    assert y > 0


def test_mocking_fetch_locations(mocker, image_4731, unchecked):
    return_value = (
        np.array([403, 404, 405]), 
        np.array([37, 37, 37])
    )
    mocker.patch('app.find_template_coordinates.fetch_locations', return_value=return_value)
    got = find_template_coordinates(
        image=image_4731,
        template=unchecked
    )
    assert_points_are_close(got, expected=[(37, 404)])


