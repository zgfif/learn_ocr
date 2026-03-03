from numpy import ndarray
from cv2 import rectangle
from app.point import Point



class Rectangle:
    COLOR: tuple = (0, 255, 0)
    THICKNESS: int = 2

    def __init__(self, image: ndarray) -> None:
        self.image = image


    def draw(self, pt1: Point, pt2: Point) -> ndarray:
        """Draw rectangle by coordinates on the image and return the image."""
        rectangle(
            img=self.image, 
            pt1=(pt1.x, pt1.y), 
            pt2=(pt2.x, pt2.y), 
            color=self.COLOR, 
            thickness=self.THICKNESS
        )
        return self.image
