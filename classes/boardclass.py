from classes.boardcellclass import BoardCell

class Board:

    def __init__(self, dimensions):
        self.dimensions = dimensions
        cells = []
        for x in range(self.dimensions[0]):
            row = []
            for y in range(self.dimensions[1]):
                row.append(BoardCell([]))
            cells.append(row)
        self.cells = cells

    def move(self):
        pass