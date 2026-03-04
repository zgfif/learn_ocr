import cv2
from app.rectangle import Rectangle
from app.view_image import ViewImage
from app.area import Unit
from app.point import Point



units: list = [
        Unit(Point(0, 0), Point(1137, 294)),
        Unit(Point(49, 417), Point(420, 569)),
        Unit(Point(49, 666), Point(395, 810)),
        Unit(Point(49, 909), Point(420, 1053)),
    ]


def test_rectangle():
    image = cv2.imread('./IMG_4731.png')

    for unit in units:
        Rectangle(image=image).draw(
            pt1=unit.pt1, pt2=unit.pt2
        )

    ViewImage(image=image).perform()

