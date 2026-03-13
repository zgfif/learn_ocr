import cv2
import numpy as np
from app.types import Coordinates
from cv2.typing import MatLike
from app.fetch_match_map import fetch_match_map


THRESHOLD: float = 0.99
PATTERN_SIZE: tuple[int, int] = (120, 120)
GROUP_THRESHOLD: int = 1
EPS: float = 0.2



def fetch_object_coordinates(image: MatLike | None, pattern: MatLike | None) -> list[Coordinates] | None:
    """
    Return the list of coordinates of found objects (by pattern) on image.
    """
    if image is None or pattern is None:
        return None

    match_map = fetch_match_map(image=image, template=pattern)

    found = np.where(match_map > THRESHOLD)
    
    print(found[0])
    
    rects = []
    
    h, w = PATTERN_SIZE

    for pt in zip(*found[::-1]):
        # Формируем список прямоугольников [x, y, w, h]
        rects.append([int(pt[0]), int(pt[1]), w, h])
        rects.append([int(pt[0]), int(pt[1]), w, h]) # Добавляем дважды (нужно для работы функции)
    # Группируем близкие прямоугольники
    # groupThreshold=1 (объединять, если наложились), eps=0.2 (насколько близко)
    grouped_rects, weights = cv2.groupRectangles(rects, groupThreshold=GROUP_THRESHOLD, eps=EPS)

    elements = []
    for (x, y, w, h) in grouped_rects:
        tpl = int(x), int(y)
        elements.append(tpl)
    return elements
