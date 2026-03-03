import cv2
from app.view_image import ViewImage
from app.cropping_points import CROPPING_POINTS
from app.cv_cropping import CvCropping



images = ('./IMG_4731.png', './IMG_4732.png',)

cropped_images = []

for image in images:
    image = cv2.imread(image)
    cropped = CvCropping(image=image).perform(
        CROPPING_POINTS[0], 
        CROPPING_POINTS[1]
    )
 
    
