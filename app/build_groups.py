from app.area import Area
from operator import attrgetter



def build_groups(lines: list[Area]) -> list[Area]:
    """
    Sort lines by starting point and merge consecutive ones
    whose endpoints are close.
    """
    if not lines:
        return []

    lines = sorted(lines, key=attrgetter("pt1.y"))

    result: list[Area] = []

    start, end = lines[0].pt1, lines[0].pt2
    
    for line in lines[1:]:
        if line.pt1.close_to(end):
            end = line.pt2
        else:
            result.append(Area(start, end))
            start, end = line.pt1, line.pt2

    result.append(Area(start, end))

    return result
