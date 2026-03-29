from app.invalid_image_error import InvalidImageError


ERR_IMAGE_HAS_BOTH: str = 'Invalid image: both ticked and unticked templates detected.'

ERR_IS_NOT_OPTION: str = 'Invalid option: has neither ticked nor unticked patterns.'



def detect_option_correctness(has_ticked: bool, has_unticked: bool) -> bool:
    """
    Detect correctness of the option.

    Parameters
    ----------
    has_ticked : bool
        has option ticked pattern.
    has_unticked : bool
        has option unticked pattern.
    
    Raises
    ------
    InvalidImageError
        if has both ticked and unticked patterns.
        if has neither ticked nor unticked patterns.
    """
    if has_ticked and has_unticked:
        raise InvalidImageError(ERR_IMAGE_HAS_BOTH)
    
    if not has_ticked and not has_unticked:
        raise InvalidImageError(ERR_IS_NOT_OPTION)
    
    return True if has_ticked else False
