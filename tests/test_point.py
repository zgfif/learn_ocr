from app.point import Point


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
