from app.cropping import Cropping
from PIL import Image



def test_first_cropping():
    image = Image.open(fp='./IMG_4731.png')
    assert image.size == (1290, 2796)
    cropped = Cropping(image=image).perform(start_coord=(0, 0), end_coord=(1290, 50))
    assert cropped.size == (1290, 50)


def test_second_cropping():
    image = Image.open(fp='./IMG_4732.png')
    cropped = Cropping(image=image).perform(start_coord=(0, 40), end_coord=(1290, 50))
    assert cropped.size == (1290, 10)
