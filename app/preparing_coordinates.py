from app.area import Area
from app.point import Point



class PreparingCoordinates:
    MINIMAL_BLOCK_HEIGHT: int = 182


    def __init__(self, lines: list[Area]) -> None:
        self.lines = lines


    def perform(self) -> list[Area]:
        modified_lines = []

        for line in self.lines:
            y1 = line.pt1.y - 25
            y2 = line.pt2.y + 65

            if y2 - y1 < self.MINIMAL_BLOCK_HEIGHT:
                # print('small block', y2 - y1)
                y2 = y2 + (self.MINIMAL_BLOCK_HEIGHT - y2) + 5
            
            new_line = Area(Point(x=0, y=y1), Point(x=1250, y=y2))
            
            modified_lines.append(new_line)
        return modified_lines
