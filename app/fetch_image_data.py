import pytesseract
from cv2.typing import MatLike
import cv2
from app.ocr_data import OCRData



def fetch_image_data(image: MatLike | None, lang: str = 'deu') -> OCRData | dict:
    """
    Extract data from image return None if no image.
    """
    if image is None:
        return {}

    data = pytesseract.image_to_data(
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 
        lang=lang,
        output_type=pytesseract.Output.DICT
    )
    if not data:
        return {}
    return OCRData(**data)
