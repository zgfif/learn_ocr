from app.fetch_image_data import fetch_image_data
import cv2
from app.ocr_data import OCRData



def test_fetch_image_data():
    image = cv2.imread('./tests/fixtures/IMG_4731.png')
    assert image is not None
    data = fetch_image_data(image=image)
    # print(data)
    assert isinstance(data, OCRData)


def test_fetch_image_data2():
    image = cv2.imread('')
    assert image is None
    got = fetch_image_data(image=image) # type: ignore[arg-type]
    assert got == {}
