import pytesseract
import cv2
from numpy import ndarray



class ImageData:
    def __init__(self, image: ndarray) -> None:
        self.image = image


    def extract(self) -> dict:
        """Extract data from image."""
        if self.image is None:
            return {}
        
        image_rgb = self._convert_to_rgb(self.image)
        
        data = pytesseract.image_to_data(
            image=image_rgb, 
            lang='deu',
            output_type=pytesseract.Output.DICT
        )
        return data
    

    def _convert_to_rgb(self, image: ndarray) -> ndarray:
        """Return image data with RGB."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
