import cv2
import pytesseract
from cv2.typing import MatLike
from app.ocr_data import OCRData



def fetch_image_data(image: MatLike | None, lang: str = 'deu') -> OCRData | None:
    """
    Extract data from image return None if no image.
    """
    if image is None:
        return None
    
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    data = pytesseract.image_to_data(
        image=rgb_image, 
        lang=lang,
        output_type=pytesseract.Output.DICT
    )

    return OCRData(**data)
