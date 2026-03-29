from cv2.typing import MatLike

from app.option import Option
from app.extract_text_from_option_area import extract_text_from_option_area


ERR_EMPTY_TEXT: str = 'Return an Option object with extracted text and correctness flag.'


def build_option(
    image: MatLike,
    correctness: bool
    ) -> Option:
    """
    Return the Option object containing text and correctness.

    Parameters
    ----------
        image : MatLike
            Image containing a single answer option area.
        correctness : bool
            Whether the option is correct.
    
    Returns
    ------
    Option
    
    Raises
    ------
    ValueError
        If extracted text is empty.
    """
    text = extract_text_from_option_area(image)
    if text == '':
        raise ValueError(ERR_EMPTY_TEXT)
    return Option(text=text, correctness=correctness)
