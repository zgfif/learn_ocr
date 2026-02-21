import pytesseract
from PIL import Image




def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    return pytesseract.image_to_string(Image.open(filename))
