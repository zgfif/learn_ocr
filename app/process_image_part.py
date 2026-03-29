from cv2.typing import MatLike

from app.option import Option
from app.detect_option_correctness import detect_option_correctness
from app.detect_image_type import detect_image_type
from app.build_option import build_option
from app.extract_question_text import extract_question_text
from app.image_type import ImageType
from app.find_template_coordinates import find_template_coordinates
from app.types import Coordinates



def process_image_part(
    image: MatLike, 
    ticked_template: MatLike, 
    unticked_template: MatLike
    ) -> str | Option:
    """
    Process image and return Option object if image has ticked or unticked patterns. 
    If it has only text return text.

    Parameters
    ----------
    image : MatLike
        loaded image to extract.
    ticked_template : MatLike
        template to find ticked template on image.
    unticked_template : MatLike
        template to find unticked template on image.

    Returns
    -------
    str | Option | None
        if the type is 'question' extract string from image.
        If the type is 'option' return Option object or None. 
    
    Raises
    ------
    ValueError
        if image_type neither 'option' nor 'question'.
    """
    ticked_coordinates: list[Coordinates] = find_template_coordinates(image, ticked_template)
    unticked_coordinates: list[Coordinates] = find_template_coordinates(image, unticked_template)

    has_ticked = bool(ticked_coordinates)
    has_unticked = bool(unticked_coordinates)

    image_type = detect_image_type(has_ticked, has_unticked)

    if image_type == ImageType.OPTION:
        correctness = detect_option_correctness(has_ticked, has_unticked)
        return build_option(image, correctness)

    return extract_question_text(image)
