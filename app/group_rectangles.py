from typing import cast

import cv2
import numpy as np
from numpy.typing import NDArray



def group_rectangles(
        rectangles: list[tuple[int, int, int, int]], 
        grouping_threshold: int = 1, 
        eps: float = 0.2
) -> NDArray[np.integer]:
    """
    Group rectangles with close attributes (x, y, w, h).

    Parameters
    ----------
    rectangles : list[tuple[int, int, int, int]]
        List of rectangles in format (x, y, w, h).
    grouping_threshold : int
        Minimum number of rectangles required to form a group.
    eps : float
        Relative difference between rectangles to merge them.   
        For example eps=0.2 means rectangles must differ by less than 20%.
    Returns
    -------
    NDArray[np.integer]
        Array of grouped rectangles with shape (N, 4).
    """
    if not rectangles:
        return np.empty((0, 4), dtype=np.int32)
    if grouping_threshold < 0:
        raise ValueError('grouping_threshold must be >= 0')
    
    rects, _ = cv2.groupRectangles(
        rectList=rectangles, 
        groupThreshold=grouping_threshold, 
        eps=eps
    )
    return cast(NDArray[np.integer], rects)
