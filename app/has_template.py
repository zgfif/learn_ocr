from cv2.typing import MatLike

from app import find_template_coordinates
from app.find_template_coordinates import find_template_coordinates



def has_template(image: MatLike, template: MatLike) -> bool:
    """
    Does the image has template.
    
    Parameters
    ----------
    image : MatLike
        source image to detect template.
    template : MatLike
        template for detecting.
    
    Returns
    -------
    bool
    """
    return bool(
        find_template_coordinates(
            image=image, 
            template=template
        )
    )
