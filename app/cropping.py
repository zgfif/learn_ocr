from numpy import ndarray
from app.point import Point



class Cropping:
    def __init__(self, image: ndarray | None) -> None:
        self.image = image


    def perform(self, pt1: Point, pt2: Point) -> ndarray | None:
        """
        Crop image using two points. 
        Return cropped image or None if image is not set.
        """
        if self.image is None:
            return None

        # sort coordinates in right order
        x1, x2 = sorted([pt1.x, pt2.x])
        y1, y2 = sorted([pt1.y, pt2.y])

        return self.image[y1:y2, x1:x2]
