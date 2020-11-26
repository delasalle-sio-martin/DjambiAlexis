from tkinter import *
from classes.board import Board, generateFourPlayerSet

if __name__ == '__main__':
    fenetre = Tk()
    board = Board((9, 9))
    generateFourPlayerSet()
    board.initBoard(fenetre)
    fenetre.mainloop()
