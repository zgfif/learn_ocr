from cv2.typing import MatLike

from app.types import Coordinates
from app.fetch_match_map import fetch_match_map
from app.fetch_locations import fetch_locations
from app.group_rectangles import group_rectangles




def find_template_coordinates(
        image: MatLike | None, 
        template: MatLike | None
) -> list[Coordinates]:
    """
    Fetch coordinates of template in the image.

    Parameters
    ----------
    image : MatLike | None
        Source image.
    template : MatLike | None
        Template to search for.

    Returns
    -------
    list
        Returns a list of (x, y) coordinates. Returns an empty list if no matches are found.
    """
    if image is None or template is None:
        return []

    match_map = fetch_match_map(image=image, template=template)
    locations = fetch_locations(match_map)
    print(locations)
    
    h, w = template.shape[:2]  # type: ignore[attr-defined]
    
    # build the list of rectangles.
    rects: list[tuple[int, int, int, int]] = []

    ys, xs = locations

    if len(xs) == 0:
        return []

    for x, y in zip(xs, ys):
        # Duplicate rectangles because group_rectangles requires at least 2
        # overlapping rectangles to form a group (OpenCV behavior).
        rect = (int(x), int(y), w, h)
        rects.extend([rect, rect])
    
    # group close rectangles.
    grouped_rects = group_rectangles(rectangles=rects)

    return [(int(x), int(y)) for x, y, *_ in grouped_rects]
