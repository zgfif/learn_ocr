from cv2.typing import MatLike

from app.find_template_coordinates import find_template_coordinates
from app.types import Coordinates



def has_template(image: MatLike, template: MatLike) -> bool:
    """
    Check if the image contain the template.
    
    Parameters
    ----------
    image : MatLike
        source image to detect template.
    template : MatLike
        template for detecting.
    
    Returns
    -------
    bool
        True if the template was found, False -otherwise.
    """
    coords: list[Coordinates] = find_template_coordinates(
        image=image, 
        template=template
    )
    return bool(coords)
