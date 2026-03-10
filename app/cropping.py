from numpy import ndarray
from app.point import Point



class Cropping:
    def __init__(self, image: ndarray) -> None:
        self.image = image


    def perform(self, pt1: Point, pt2: Point) -> ndarray | None:
        """
        Crop image by two points and return cropped image as ndarrry object. If no image - return None.
        """
        if self.image is None:
            return
        
        return self.image[
            pt1.y:pt2.y, 
            pt1.x:pt2.x
        ]
