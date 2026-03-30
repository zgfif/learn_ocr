from cv2.typing import MatLike

from app.fetch_match_map import fetch_match_map
from app.fetch_locations import fetch_locations
from app.group_rectangles import group_rectangles
from app.types import Coordinates


ERR_DOES_NOT_HAVE_SHAPE: str = "Template does not have shape attribute."



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
    list[Coordinates]
        List of (x, y) coordinates of template matches (top-left corner).
        Returns an empty list if no matches are found.
    """
    if image is None or template is None:
        return []

    match_map = fetch_match_map(image=image, template=template)
    locations = fetch_locations(match_map)

    if not hasattr(template, "shape"):
        raise ValueError(ERR_DOES_NOT_HAVE_SHAPE)

    h, w = template.shape[:2]  # type: ignore[attr-defined]
    
    # build the list of rectangles.
    rects: list[tuple[int, int, int, int]] = []

    ys, xs = locations

    if len(xs) == 0:
        return []

    # Duplicate rectangles because group_rectangles requires at least 2
    # overlapping rectangles to form a group (OpenCV behavior).
    rects = [rect for x, y in zip(xs, ys) for rect in [(int(x), int(y), w, h)] * 2]

    # group close rectangles.
    grouped_rects = group_rectangles(rectangles=rects)

    return [(int(x), int(y)) for x, y, *_ in grouped_rects]
