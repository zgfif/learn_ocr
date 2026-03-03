from numpy import ndarray
from app.point import Point


class CvCropping:
    def __init__(self, image: ndarray) -> None:
        self.image = image

    def perform(self, pt1: Point, pt2: Point) -> ndarray:
        """Return cropped image"""
        return self.image[ pt1.y:pt2.y, pt1.x:pt2.x]
