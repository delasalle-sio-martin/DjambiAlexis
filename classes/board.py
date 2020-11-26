from classes.boardcell import BoardCell
from classes.assassin import Assassin
from classes.chief import Chief
from classes.diplomate import Diplomat
from classes.militant import Militant
from classes.reporter import Reporter
from classes.necromobile import Necromobile
from classes.color import Color
from tkinter import *


class Board:
    clickedCell = None

    def __init__(self, dimensions: (int, int)):
        self.dimensions = dimensions
        cells = []
        for x in range(self.dimensions[0]):
            row = []
            for y in range(self.dimensions[1]):
                row.append(BoardCell([]))
            cells.append(row)
        self.cells = cells

    # FIXME : Il faudrait revoir ensuite cette génération
    def generateFourPlayerSet(self):
        """
        Generate a board 9x9 with all the pieces
        :return:
        """

        green = Color("Green", "#01D758")
        blue = Color("Blue", "#0131B4")
        red = Color("Red", "#DB1702")
        yellow = Color("Yellow", "#FCDC12")

        board = Board((9, 9))

        board.cells[0][0].pions = [Chief((0, 0), yellow)]
        board.cells[0][1].pions = [Assassin((0, 1), yellow)]
        board.cells[0][2].pions = [Militant((0, 2), yellow)]
        board.cells[1][0].pions = [Reporter((1, 0), yellow)]
        board.cells[1][1].pions = [Diplomat((1, 1), yellow)]
        board.cells[1][2].pions = [Militant((1, 2), yellow)]
        board.cells[2][0].pions = [Militant((2, 0), yellow)]
        board.cells[2][1].pions = [Militant((2, 1), yellow)]
        board.cells[2][2].pions = [Necromobile((2, 2), yellow)]

        board.cells[0][6].pions = [Militant((0, 6), green)]
        board.cells[0][7].pions = [Assassin((0, 7), green)]
        board.cells[0][8].pions = [Chief((0, 8), green)]
        board.cells[1][6].pions = [Militant((1, 6), green)]
        board.cells[1][7].pions = [Diplomat((1, 7), green)]
        board.cells[1][8].pions = [Reporter((1, 8), green)]
        board.cells[2][6].pions = [Necromobile((2, 6), green)]
        board.cells[2][7].pions = [Militant((2, 7), green)]
        board.cells[2][8].pions = [Militant((2, 8), green)]

        board.cells[6][0].pions = [Chief((6, 0), blue)]
        board.cells[6][1].pions = [Assassin((6, 1), blue)]
        board.cells[6][2].pions = [Militant((6, 2), blue)]
        board.cells[7][0].pions = [Reporter((7, 0), blue)]
        board.cells[7][1].pions = [Diplomat((7, 1), blue)]
        board.cells[7][2].pions = [Militant((7, 2), blue)]
        board.cells[8][0].pions = [Militant((8, 0), blue)]
        board.cells[8][1].pions = [Militant((8, 1), blue)]
        board.cells[8][2].pions = [Necromobile((8, 2), blue)]

        board.cells[6][6].pions = [Militant((6, 6), red)]
        board.cells[6][7].pions = [Assassin((6, 7), red)]
        board.cells[6][8].pions = [Chief((6, 8), red)]
        board.cells[7][6].pions = [Militant((7, 6), red)]
        board.cells[7][7].pions = [Diplomat((7, 7), red)]
        board.cells[7][8].pions = [Reporter((7, 8), red)]
        board.cells[8][6].pions = [Necromobile((8, 6), red)]
        board.cells[8][7].pions = [Militant((8, 7), red)]
        board.cells[8][8].pions = [Militant((8, 8), red)]

    def move(self, destination_x: int, destination_y: int, window: Tk, board):
        """

        :param destination_x:
        :param destination_y:
        :param window:
        :param board:
        :return:
        """
        selectedPion = self.clickedCell.pions[0]
        beforeMovementPion = selectedPion.position
        selectedPion.position = (destination_x, destination_y)
        self.cells[destination_x][destination_y].pions = [selectedPion]
        self.cells[destination_x][destination_y].initBoard(window, destination_x, destination_y, board)

        self.clickedCell.pions[0] = None
        self.clickedCell.initBoard(window, beforeMovementPion[0], beforeMovementPion[1], board)

    # def initBoardTest(self, fenetre):
    #     for i in range(len(self.cells)):
    #         for j in range(len(self.cells[i])):
    #             if len(self.cells[i][j].pions) > 0:
    #                 for k in range(len(self.cells[i][j].pions)):
    #                     image = Image.open(self.cells[i][j].pions[k].image())
    #                     image = image.resize((50, 50))
    #                     imageBoard = ImageTk.PhotoImage(image)
    #                     btn = Button(fenetre, image=imageBoard,
    #                                  bg=self.cells[i][j].pions[k].color.code)
    #                     btn.image = imageBoard
    #
    #             else:
    #                 image = Image.open("assets/blank.png")
    #                 image = image.convert("RGBA")
    #                 image = image.resize((50, 50))
    #                 imageBoard = ImageTk.PhotoImage(image)
    #                 btn = Button(fenetre, image=imageBoard)
    #                 btn.image = imageBoard
    #
    #             btn.grid(row=i, column=j)

    def onClickedCell(self, x: int, y: int, window: Tk):
        """

        :param x:
        :param y:
        :param window:
        :return:
        """
        if self.clickedCell is None:
            if len(self.cells[x][y].pions) > 0:
                self.clickedCell = self.cells[x][y]
            else:
                self.move(x, y, window, self)
                self.clickedCell = None

    def initBoard(self, fenetre: Tk):
        """

        :param fenetre:
        :return:
        """
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                cell.initBoard(fenetre, i, j, self)
