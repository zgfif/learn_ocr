class GroupedLines:
    def __init__(self, lines: list) -> None:
        self.lines = lines


    def fetch(self) -> list:
        """
        Return the list of grouped lines.
        """
        units_list = []

        unit = self.lines[0]

        for line in self.lines:
            if line.pt1.close_to(unit.pt2):
                unit.pt2 = line.pt2
            else:
                units_list.append(line)
                unit = line
        return units_list
