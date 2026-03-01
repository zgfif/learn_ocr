from numpy import ndarray
from app.types import Coordinates
from cv2 import rectangle



class Rectangle:
    COLOR: tuple = (0, 255, 0)
    THICKNESS: int = 2

    def __init__(self, image: ndarray) -> None:
        self.image = image


    def draw(self, pt1: Coordinates, pt2: Coordinates) -> ndarray:
        """Draw rectangle by coordinates on the image and return the image."""
        rectangle(
            img=self.image, 
            pt1=pt1, pt2=pt2, 
            color=self.COLOR, 
            thickness=self.THICKNESS
        )
        return self.image
