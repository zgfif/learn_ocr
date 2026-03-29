from app.image_type import ImageType
from app.invalid_image_error import InvalidImageError


ERR_IMAGE_HAS_BOTH: str = (
    'Invalid image: both ticked and unticked templates detected.'
)


def detect_image_type(
    has_ticked: bool, 
    has_unticked: bool
) -> ImageType:
    """
    Detect the ImageType (OPTION or QUESTION).

    Parameters
    ----------
    has_ticked : bool
        Indicates whether a ticked template is present in the image.
    has_unticked : bool
        Indicates whether an unticked template is present in the image.  
    
    Returns
    -------
    ImageType
    
    Raises
    ------
    InvalidImageError
        if both ticked and unticked templates are detected.
    """
    if has_ticked and has_unticked:
        raise InvalidImageError(ERR_IMAGE_HAS_BOTH)
    
    return ImageType.OPTION if (has_ticked or has_unticked) else ImageType.QUESTION
