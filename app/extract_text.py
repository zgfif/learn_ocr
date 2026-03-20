import pytesseract
from cv2.typing import MatLike

from app.normalize_string import normalize_string


DEFAULT_LANG: str = 'deu'


def extract_text( 
    image: MatLike, 
    lang: str = DEFAULT_LANG,
    config: str | None = None
) -> str:
    """
    Extract and normalize text from image.

    Parameters
    ----------
    image : MatLike
        Target loaded image.
    lang : str
        Language for OCR (default is 'deu' - German).
    config : str | None
        Optional Tesseract config string.

    Returns
    -------
    str
        normalized extracted text.

    Raises
    ------
    ValueError
        if image is None.
    RuntimeError
        if something went wrong during text extracting.
    """
    if image is None:
        raise ValueError('Image must not be None.')

    try:
        raw_text = pytesseract.image_to_string(
            image=image, 
            lang=lang,
            config=config or ''
        )
    except pytesseract.TesseractError as e:
        raise RuntimeError(f'OCR failed (lang={lang}): {e}') from e
    result = normalize_string(raw_text)
    return result or ''
