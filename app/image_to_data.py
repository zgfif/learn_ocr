import pytesseract
import cv2
import numpy



class ImageToData:
    def __init__(self, image_path: str) -> None:
        self.image = cv2.imread(filename=image_path)


    def transform(self) -> dict:
        """
        Extract data from image.
        """
        if self.image is None:
            return {}
        
        image_rgb = self._convert_to_rgb(self.image)
        
        data = pytesseract.image_to_data(
            image_rgb, 
            output_type=pytesseract.Output.DICT
        )
        return data
    

    def _convert_to_rgb(self, image: numpy.ndarray) -> numpy.ndarray:
        """
        Return image data with RGB.
        """
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
