from PIL.Image import Image
from pytesseract import image_to_string



class Text:
    def __init__(self, image: Image, lang: str = 'deu') -> None:
        self.image = image
        self.lang = lang
    

    def extract(self) -> str:
        """
        Recognize and return the text from the image object.
        """
        return image_to_string(
            image=self.image, 
            lang=self.lang
        )
