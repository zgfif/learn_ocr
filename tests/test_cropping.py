import cv2
from app.cropping import Cropping
from app.view_image import ViewImage
from app.full_text_points import FULL_TEXT_POINTS



def test_cropping():
    image = cv2.imread(filename='./IMG_4732.png')
    
    if image is None:
        return

    cropped = Cropping(image=image).perform(
        pt1=FULL_TEXT_POINTS.pt1, 
        pt2=FULL_TEXT_POINTS.pt2
    )
    
    if not cropped:
        return
    ViewImage(image=cropped).perform()


    