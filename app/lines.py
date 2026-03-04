from app.point import Point
from app.area import Area



class Lines:
    LEVEL: int = 4

    def __init__(self, data: dict) -> None:
        self.data = data


    def coordinates(self) -> list[Area]:
        """
        Return the list with coordinates of lines.
        """
        lst = []

        words_count = len(self.data['level'])
        
        for i in range(words_count):
            if self.data['level'][i] == self.LEVEL:
                (x, y , w, h)  = self.data['left'][i],self.data['top'][i], self.data['width'][i], self.data['height'][i]
                
                line = Area(
                    Point(x, y), 
                    Point(x + w, y + h)
                )

                lst.append(line)

        return lst