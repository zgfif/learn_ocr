from app.image_data import ImageData
import cv2



def test_image_data():
    image = cv2.imread('./tests/fixtures/IMG_4731.png')

    if image is None:
        return

    data = ImageData(image=image).extract()

    assert isinstance(data, dict)
