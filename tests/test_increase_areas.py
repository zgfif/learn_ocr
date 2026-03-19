from app.increase_areas import increase_areas
from app.area import Area
from app.point import Point



def test_increase_areas():
    areas: list[Area] = [
        Area(
            Point(20, 20),
            Point(1230, 60)
        ),
        Area(
            Point(20, 140),
            Point(1230, 180)
        ),
        Area(
            Point(20, 250),
            Point(1230, 290)
        ),
    ]

    expected: list[Area] = [
        Area(
            Point(0, -5),
            Point(1250, 182)
        ),
        Area(
            Point(0, 115),
            Point(1250, 302)
        ),
        Area(
            Point(0, 225),
            Point(1250, 412)
        ),
    ]

    got = increase_areas(areas=areas)
    print(got)
    assert expected == got

