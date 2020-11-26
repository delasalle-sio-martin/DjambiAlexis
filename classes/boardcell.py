from tkinter import *
from PIL import Image, ImageTk


class BoardCell:
    """
    Class used to symbolize one cell, in which it is possible to put a pawn
    """

    def __init__(self, pions: []):
        self.pions = pions
        self.btn = None

    # FIXME : Something doesn't work here, and only creates white squares.
    def initBoard(self, fenetre: Tk, x: int, y: int, board):
        """
        Allows us to put a visual on each pawn placed in the board
        :param fenetre:
        :param x:
        :param y:
        :param board:
        :return:
        """
        if self.pions and self.pions[0]:
            pion = self.pions[0]
            image = Image.open(pion.image())
            image = image.resize((50, 50))
            imageBoard = ImageTk.PhotoImage(image)
            btn_color = pion.color.code
        else:
            image = Image.open("assets/blank.png")
            image = image.convert("RGBA")
            image = image.resize((50, 50))
            imageBoard = ImageTk.PhotoImage(image)
            btn_color = "#FFFFFF"

        self.btn = Button(fenetre, image=imageBoard,
                          bg=btn_color, command=lambda: board.onClickedCell(x, y, fenetre))
        self.btn.image = image
        self.btn.grid(row=x, column=y)
