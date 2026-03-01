class LineBlocks:
    LEVEL: int = 4


    def __init__(self, data: dict) -> None:
        self.data = data


    def fetch(self) -> list:
        """
        Return the list with coordinates of lines.
        """
        lst = []
        words_count = len(self.data['level'])
        
        # lines_count = 0
        for i in range(words_count):
            if self.data['level'][i] == self.LEVEL:
                (x, y , w, h)  = self.data['left'][i],self.data['top'][i], self.data['width'][i], self.data['height'][i]
                line = ((x, y), (x + w, y + h))
                lst.append(line)

        return lst