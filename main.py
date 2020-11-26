from tkinter import *
from classes.board import Board

if __name__ == '__main__':
    fenetre = Tk()
    board = Board((9, 9))
    board.generateFourPlayerSet()
    board.initBoard(fenetre)
    fenetre.mainloop()
