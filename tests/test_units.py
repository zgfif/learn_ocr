# from app.grouped_lines import Units
# from tests.fixtures.img_4731_full_lines import lines
# from app.area import Unit
# from app.point import Point


# def test_units():    
#     expected = [
#         Unit(Point(0, 0), Point(1137, 294)),
#         Unit(Point(49, 417), Point(420, 569)),
#         Unit(Point(49, 666), Point(395, 810)),
#         Unit(Point(49, 909), Point(420, 1053)),
#     ]

#     got = Units(lines=lines).fetch()

#     assert len(got) == 4
#     assert expected == got
