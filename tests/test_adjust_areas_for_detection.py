from app.adjust_areas_for_detection import adjust_areas_for_detection
from app.area import Area
from app.point import Point



def test_adjast_areas_for_detection_when_three_areas():
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
            Point(0, 0),
            Point(1250, 187)
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
    got = adjust_areas_for_detection(areas=areas)
    assert expected == got



def test_adjanst_areas_for_detection_when_no_areas():
    assert adjust_areas_for_detection([]) == []
