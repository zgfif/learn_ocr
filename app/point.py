class Point:
    CLOSENESS_THRESHOLD: int = 63


    def __init__(self, x: int, y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Coordinates must be integers")

        self.x = x
        self.y = y


    def close_to(self, other: object) -> bool:
        """
        Return True if the vertical distance to another Point is within the closeness threshold.
        """
        if isinstance(other, Point):
            return abs(other.y - self.y) <= self.CLOSENESS_THRESHOLD
        return False


    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'


    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented
