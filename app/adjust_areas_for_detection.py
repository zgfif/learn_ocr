from typing import Sequence

from app.area import Area
from app.point import Point



# based on minimal height of pattern.
MINIMAL_AREA_HEIGHT: int = 187

# based on default image width.
DEFAULT_AREA_WIDTH: int = 1250
IMAGE_HEIGHT: int = 2796

# offsets for Point1 and Point2 of Area.
POINT1_Y_OFFSET: int = -25
POINT2_Y_OFFSET: int = 65



def adjust_areas_for_detection(
        areas: Sequence[Area],
        area_width: int = DEFAULT_AREA_WIDTH,    
) -> list[Area]:
    """
    Adjust areas for pattern detection.

    - pt1 is shifted upward by POINT1_Y_OFFSET
    - pt2 is shifted downward by POINT2_Y_OFFSET
    - ensures a minimum height of MINIMAL_AREA_HEIGHT
    - sets a fixed width of DEFAULT_AREA_WIDTH

    Returns new areas (does not mutate input).
    """
    adjusted_areas: list[Area] = []

    for area in areas:
        y1 = max(0, area.pt1.y + POINT1_Y_OFFSET)
        y2 = area.pt2.y + POINT2_Y_OFFSET

        height: int = y2 - y1

        if height < MINIMAL_AREA_HEIGHT:
            y2 = min(IMAGE_HEIGHT, y1 + MINIMAL_AREA_HEIGHT)

        adjusted_areas.append(
            Area(
                Point(x=0, y=y1), 
                Point(x=area_width, y=y2)
            )
        )
    return adjusted_areas
