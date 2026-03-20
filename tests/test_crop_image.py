import cv2
from app.crop_image import crop_image
from app.full_text_points import FULL_TEXT_POINTS



def test_cropping():
    image = cv2.imread(filename='./tests/fixtures/IMG_4732.png')
    
    if image is None:
        return

    cropped = crop_image(
        image=image,
        pt1=FULL_TEXT_POINTS.pt1, 
        pt2=FULL_TEXT_POINTS.pt2
    )

    if cropped is None:
        return

    assert cropped.shape[0] == 2020
    assert cropped.shape[1] == 1286
