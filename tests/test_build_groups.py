from app.build_groups import build_groups
from app.area import Area
from app.point import Point



def test_build_groups1():
    lst1: list[Area] = [
        Area(pt1=Point(28, 27), pt2=Point(1193, 68)), 
        Area(pt1=Point(29, 90), pt2=Point(1158, 141)), 
        Area(pt1=Point(28, 153), pt2=Point(1217, 202)), 
        Area(pt1=Point(27, 214), pt2=Point(1150, 265)),
        Area(pt1=Point(28, 276), pt2=Point(947, 327)), 
        Area(pt1=Point(256, 459), pt2=Point(1135, 504)), 
        Area(pt1=Point(255, 515), pt2=Point(1048, 561)), 
        Area(pt1=Point(256, 700), pt2=Point(1037, 745)), 
        Area(pt1=Point(256, 756), pt2=Point(978, 803)), 
        Area(pt1=Point(49, 935), pt2=Point(1042, 1086))
    ]
    expected = [
        Area(pt1=Point(28, 27), pt2=Point(947, 327)), 
        Area(pt1=Point(256, 459), pt2=Point(1048, 561)), 
        Area(pt1=Point(256, 700), pt2=Point(978, 803)), 
        Area(pt1=Point(49, 935), pt2=Point(1042, 1086))
    ]

    got = build_groups(lines=lst1)
    assert isinstance(got, list) is True
    assert got == expected



def test_build_groups2():
    lst2: list[Area] = [
        Area(pt1=Point(28, 27), pt2=Point(1193, 68)), 
    ]
    expected = [
        Area(pt1=Point(28, 27), pt2=Point(1193, 68)),
    ]
    got = build_groups(lines=lst2)
    assert got == expected


def test_build_groups3():
    lst3: list[Area] = []
    expected = []
    got = build_groups(lines=lst3)
    assert got == expected


def test_build_groups4():
    lst4: list[Area] = [
        Area(pt1=Point(28, 27), pt2=Point(1193, 68)), 
        Area(pt1=Point(28, 100), pt2=Point(1193, 150)),
        Area(pt1=Point(28, 220), pt2=Point(1193, 270)), 
    ]
    expected = [
        Area(pt1=Point(28, 27), pt2=Point(1193, 150)),
        Area(pt1=Point(28, 220), pt2=Point(1193, 270)), 
    ]
    got = build_groups(lines=lst4)
    assert got == expected


def test_build_groups5():
    lst4: list[Area] = [
        Area(pt1=Point(28, 27), pt2=Point(1193, 68)), 
        Area(pt1=Point(28, 133), pt2=Point(1193, 150)),
        Area(pt1=Point(28, 220), pt2=Point(1193, 270)), 
    ]
    expected = [
        Area(pt1=Point(28, 27), pt2=Point(1193, 68)), 
        Area(pt1=Point(28, 133), pt2=Point(1193, 150)),
        Area(pt1=Point(28, 220), pt2=Point(1193, 270)), 
    ]
    got = build_groups(lines=lst4)
    assert got == expected
