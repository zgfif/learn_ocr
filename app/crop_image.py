from numpy import ndarray
from app.point import Point
from cv2.typing import MatLike



def crop_image(
        image: MatLike | None,
        pt1: Point, 
        pt2: Point
) -> MatLike | None:
    """
    Crop image using two points. 
    Return cropped image or None if image is not set.
    """
    if image is None:
        return None

    # sort coordinates in right order
    x1, x2 = sorted([pt1.x, pt2.x])
    y1, y2 = sorted([pt1.y, pt2.y])

    return image[y1:y2, x1:x2]
