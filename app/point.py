class Point:
    CLOSENESS_THRESHOLD: int = 63

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


    def close_to(self, other) -> bool:
        """
        Return True 
        """
        return abs(other.y - self.y) <= self.CLOSENESS_THRESHOLD

