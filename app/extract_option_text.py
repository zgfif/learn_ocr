from cv2.typing import MatLike
from app.point import Point
from app.crop_image import crop_image
from app.extract_text import extract_text


DEFAULT_TICKED_AREA_WIDTH: int = 220


def extract_option_text(
        image: MatLike, 
        ticked_area_width: int = DEFAULT_TICKED_AREA_WIDTH,
) -> str:
    """
    Return option text from image with ticking box.
    """
    y, x = image.shape[:2]
    # crop image to get rid of ticking box.
    image_without_ticking_area = crop_image(
        image=image,
        pt1=Point(ticked_area_width, 0), 
        pt2=Point(x, y),
    )
    if image_without_ticking_area is None:
        return ''
    return extract_text(image=image_without_ticking_area)
