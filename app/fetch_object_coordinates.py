import numpy as np
from app.types import Coordinates
from cv2.typing import MatLike
from app.fetch_match_map import fetch_match_map
from app.fetch_locations import fetch_locations
from app.group_rectangles import group_rectangles


PATTERN_SIZE: tuple[int, int] = (120, 120)



def fetch_object_coordinates(
        image: MatLike | None, 
        pattern: MatLike | None
) -> list[Coordinates] | None:
    """
    Return the list of coordinates of found objects (by pattern) on image.
    """
    if image is None or pattern is None:
        return None

    match_map = fetch_match_map(image=image, template=pattern)
    locations = fetch_locations(match_map)
    
    rects = []
    
    h, w = PATTERN_SIZE
 
    for pt in np.column_stack((locations[1], locations[0])):
        # Формируем список прямоугольников [x, y, w, h]
        rects.append([int(pt[0]), int(pt[1]), w, h])
        rects.append([int(pt[0]), int(pt[1]), w, h]) # Добавляем дважды (нужно для работы функции)
    
    # Группируем близкие прямоугольники
    grouped_rects = group_rectangles(rectangles=rects)

    return [(int(x), int(y)) for x, y, _, _ in grouped_rects]    
