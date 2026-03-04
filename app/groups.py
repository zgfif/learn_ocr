from app.area import Area
from app.point import Point


class Groups:
    def __init__(self, lines: list[Area]) -> None:
        self.lines = lines
    

    def build(self) -> list:
        """Group lines into groups and return it."""
        groups = []
        
        if not self.lines:
            return groups
        
        area = self.lines[0]

        for i in range(len(self.lines)):
            if self.lines[i].pt1.close_to(area.pt2):
                area.pt2 = self.lines[i].pt2
            else:
                groups.append(area)
                area = self.lines[i]

                if i == len(self.lines) - 1:
                    groups.append(area)


        
        return groups

