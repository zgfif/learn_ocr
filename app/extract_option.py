from cv2.typing import MatLike

from app.option import Option
from app.find_template_coordinates import find_template_coordinates
from app.extract_text_from_option_area import extract_text_from_option_area



ERR_IMAGE_NONE: str = 'Image must not be None.'
ERR_TICKED_UNTICKED_NONE: str = 'Ticked template and unticked template must not be None.'
ERR_BOTH_HAS_TICKED_UNTICKED: str = 'Has both ticked and unticked patterns'

def extract_option(
    image: MatLike, 
    ticked_template: MatLike, 
    unticked_template: MatLike
    ) -> Option | None:
    """
    Return the Option object if image has ticked template or unticked template. Else - return None.

    Parameters
    ----------
        image : MatLike
            image containing information.
        ticked_template : MatLike
            template to detect ticked element.
        unticked_template : MatLike
            template to detect unticked element.
    
    Returns
    ------
    Option | None
        Extract option from image (with text and correctness) if it has ticked or unticked pattern. Else return None.
    
    Raises
    ------
    ValueError
        If image or ticked_template or unticked_template is None.
    """
    
    if image is None:
        raise ValueError(ERR_IMAGE_NONE)

    if ticked_template is None or unticked_template is None:
        raise ValueError(ERR_TICKED_UNTICKED_NONE)
    
    has_ticked = bool(
        find_template_coordinates(
            image=image, 
            template=ticked_template
        )
    )
    has_unticked = bool(
        find_template_coordinates(
            image=image, 
            template=unticked_template
        )
    )

    if not (has_ticked or has_unticked):
        return None
    
    if has_ticked ^ has_unticked:
        correctness = has_ticked
    else:
        raise ValueError(ERR_BOTH_HAS_TICKED_UNTICKED)

    text = extract_text_from_option_area(image=image).strip()

    return Option(
        text=text,
        correctness=correctness
    )
