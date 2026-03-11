from app.point import Point
from pytest import raises



def test_point1():
    p1 = Point(0, 0)
    p2 = Point(0, 244)
    assert p1.close_to(p2) is False


def test_point2():
    p1 = Point(0, 244)
    p2 = Point(27, 244)
    assert p1.close_to(p2) is True


def test_point3():
    p1 = Point(0, 244)
    p2 = Point(27, 310)
    assert p1.close_to(p2) is False


def test_point4():
    p1 = Point(0, 244)
    p2 = Point(0, 244)
    assert (p1 == p2) is True


def test_point5():
    p1 = Point(0, 244)
    p2 = Point(0, 243)
    assert (p1 == p2) is False


def test_point6():
    p1 = Point(0, 244)
    p2 = Point(1, 244)
    assert (p1 == p2) is False


def test_point7():
    message: str = "Coordinates must be integers"
    with raises(TypeError) as excinfo:
        Point('2', 1) # type: ignore[arg-type]
    assert message in str(excinfo.value)


def test_point8():
    message: str = "Coordinates must be integers"
    with raises(TypeError) as excinfo:
        Point(2, '1') # type: ignore[arg-type]
    assert message in str(excinfo.value)



def test_point9():
    p1 = Point(0, 244)
    p2 = 'abc'
    assert (p1 == p2) is False
