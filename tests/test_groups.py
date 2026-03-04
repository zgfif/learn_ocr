from app.groups import Groups
from app.area import Area
from app.point import Point



lst: list[Area] = [
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



def test_groups():
    expected = [
        Area(pt1=Point(28, 27), pt2=Point(947, 327)), 
        Area(pt1=Point(256, 459), pt2=Point(1048, 561)), 
        Area(pt1=Point(256, 700), pt2=Point(978, 803)), 
        Area(pt1=Point(49, 935), pt2=Point(1042, 1086))
    ]

    got = Groups(lines=lst).build()
    assert isinstance(got, list) is True
    assert got == expected