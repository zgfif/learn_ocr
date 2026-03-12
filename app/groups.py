from app.area import Area



class Groups:
    def __init__(self, lines: list[Area]) -> None:
        self.lines = lines
    

    def build(self) -> list[Area]:
        """
        Group consecutive lines that are close together and return the list of grouped Areas.
        """        
        if not self.lines:
            return []

        groups: list[Area] = []
        
        current_group = self.lines[0]

        for line in self.lines[1:]:
            if line.pt1.close_to(current_group.pt2):
                current_group.pt2 = line.pt2
            else:
                groups.append(current_group)
                current_group = line

        groups.append(current_group)

        return groups
