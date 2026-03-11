from app.point import Point
from pytest import raises
import pytest



def test_point1():
    p1 = Point(0, 0)
    p2 = Point(0, 244)
    assert not p1.close_to(p2)


def test_point2():
    p1 = Point(0, 244)
    p2 = Point(27, 244)
    assert p1.close_to(p2)


def test_point3():
    p1 = Point(0, 244)
    p2 = Point(27, 310)
    assert not p1.close_to(p2)


def test_point4():
    p1 = Point(0, 244)
    p2 = Point(0, 244)
    assert p1 == p2


def test_point5():
    p1 = Point(0, 244)
    p2 = Point(0, 243)
    assert p1 != p2


def test_point6():
    p1 = Point(0, 244)
    p2 = Point(1, 244)
    assert p1 != p2


@pytest.mark.parametrize("coordinates", [
    ('2', 1),
    (1, '2'),
])
def test_point_raising_error(coordinates):
    message: str = "Coordinates must be integers"
    with raises(TypeError) as excinfo:
        Point(*coordinates)
    assert message in str(excinfo.value)


def test_point9():
    p1 = Point(0, 244)
    p2 = 'abc'
    assert p1 != p2


def test_point10():
    p1 = Point(0, 0)
    p2 = Point(0, Point.CLOSENESS_THRESHOLD)
    assert p1.close_to(p2)


def test_point11():
    p1 = Point(0, 0)
    p2 = Point(0, Point.CLOSENESS_THRESHOLD + 1)
    assert not p1.close_to(p2)

