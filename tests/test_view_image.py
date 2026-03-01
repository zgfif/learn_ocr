from app.view_image import ViewImage
from app.rectangle import Rectangle
import cv2



def test_view_image():
    image = cv2.imread('./IMG_4731.png')
    if image is None:
        return
    image = Rectangle(image=image).draw(pt1=(10, 10), pt2=(50, 50))
    image = Rectangle(image=image).draw(pt1=(70, 70), pt2=(150, 150))
    ViewImage(image=image).perform()
