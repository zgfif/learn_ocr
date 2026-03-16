from cv2.typing import MatLike
import cv2
import numpy as np



def fetch_match_map(
    image: MatLike, 
    template: MatLike,
    method: int = cv2.TM_CCOEFF_NORMED,
) -> np.ndarray:
    """
    Compute a template matching score map.

    Parameters
    ----------
    image : MatLike
        Source image.
    template : MatLike
        Template to search for.
    method : int
        OpenCV template matching method.
    
    Returns
    -------
    ndarray
        2D similarity map produced by cv2.matchTemplate.
    
    Raises
    ------
    ValueError
        If template size is larger than the image.

    """
    h_img, w_img = image.shape[:2]
    h_templ, w_templ = template.shape[:2]

    if h_templ > h_img or w_templ > w_img:
        raise ValueError(f'Template size ({h_templ}, {w_templ}) must not exceed '
                         f'image size ({h_img}, {w_img}).')
    return cv2.matchTemplate(
        image=image, 
        templ=template,
        method=method
    )
