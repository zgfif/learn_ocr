from app.view_image import ViewImage
from app.rectangle import Rectangle
import cv2
from app.point import Point



def test_view_image():
    image = cv2.imread('./tests/fixtures/IMG_4731.png')
    if image is None:
        return
    image = Rectangle(image=image).draw(pt1=Point(10, 10), pt2=Point(50, 50))
    if image is None:
        return
    image = Rectangle(image=image).draw(pt1=Point(70, 70), pt2=Point(150, 150))
    if image is None:
        return
    vi = ViewImage(image=image)

    assert isinstance(vi, ViewImage)
