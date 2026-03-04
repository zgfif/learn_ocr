class Point:
    CLOSENESS_THRESHOLD: int = 63

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


    def close_to(self, other: object) -> bool:
        """
        Return True if space between y axis <= threshold (px).
        """
        if isinstance(other, Point):
            return abs(other.y - self.y) <= self.CLOSENESS_THRESHOLD
        return NotImplemented
        

    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'
    

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    
