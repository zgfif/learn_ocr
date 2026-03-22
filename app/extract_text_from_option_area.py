from cv2.typing import MatLike
from app.point import Point
from app.crop_image import crop_image
from app.extract_text import extract_text


DEFAULT_TICKED_AREA_WIDTH: int = 220
DEFAULT_LANG: str = 'deu'



def extract_text_from_option_area(
    image: MatLike, 
    ticked_area_width: int = DEFAULT_TICKED_AREA_WIDTH,
    lang: str = DEFAULT_LANG,
    config: str = ''
) -> str:
    """
    Parameters
    ----------
    image : MatLike
        Source image.
    ticked_area_width : int
        width of ticked area in px. Default is 220.
    lang : str
        language for OCR, default is 'deu' German.
    config : str
        Tesseract OCR config string.
    
    Returns
    -------
    str
        normalized text.
    
    Raises
    -----
    ValueError
        If image is None, crop fails, or ticked_area_width is invalid.
    """
    if image is None:
        raise ValueError('Image is None')

    height, width = image.shape[:2]

    if ticked_area_width >= width:
        raise ValueError('larger than image width')

    # crop image to get rid of ticking box.
    cropped = crop_image(
        image=image,
        pt1=Point(ticked_area_width, 0), 
        pt2=Point(width, height)
    )
    if cropped is None:
        raise ValueError('Failed to crop image')

    return extract_text(
        image=cropped, 
        lang=lang, 
        config=config
    ) 
