from typing import Sequence

from app.area import Area
from app.point import Point



# based on minimal height of pattern.
MINIMAL_AREA_HEIGHT: int = 187

# based on default image width.
DEFAULT_AREA_WIDTH: int = 1250

# offsets for Point1 and Point2 of Area.
POINT1_Y_OFFSET: int = -25
POINT2_Y_OFFSET: int = 65




def increase_areas(areas: Sequence[Area]) -> list[Area]:
    """
    Perform offsetting the points of each area for correct patterns detecting.
    The first point is offseted up, the second point - down.

    Parameters
    ----------
    areas : Sequence[Area]
        the sequence of areas. Each area has two points (pt1 and pt2).

    Returns
    -------
        The list of areas with increased parameters.
    """
    new_areas: list[Area] = []

    for area in areas:
        y1 = area.pt1.y + POINT1_Y_OFFSET
        y2 = area.pt2.y + POINT2_Y_OFFSET

        if (y2 - y1) < MINIMAL_AREA_HEIGHT:
            y2 = y1 + MINIMAL_AREA_HEIGHT
                
        new_areas.append(
            Area(
                Point(x=0, y=y1), 
                Point(x=1250, y=y2)
            )
        )
    return new_areas
