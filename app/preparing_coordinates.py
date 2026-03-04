from app.area import Area
from app.point import Point



class PreparingCoordinates:
    def __init__(self, lines: list[Area]) -> None:
        self.lines = lines


    def perform(self) -> list[Area]:
        modified_lines = []

        for line in self.lines:
            new_line = Area(Point(x=0, y=line.pt1.y - 5), Point(x=1250, y=line.pt2.y + 50))
            modified_lines.append(new_line)
        return modified_lines
