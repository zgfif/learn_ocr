from app.cv_cropping import CvCropping
import cv2
from app.view_image import ViewImage
from app.cropping_points import CROPPING_POINTS


def test_cv_cropping():
    image = cv2.imread(filename='./IMG_4732.png')
    if image is None:
        return
    cropped = CvCropping(image=image).perform(pt1=CROPPING_POINTS[0], pt2=CROPPING_POINTS[1])
    ViewImage(image=cropped).perform()
    