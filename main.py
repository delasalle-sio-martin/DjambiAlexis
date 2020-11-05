from tkinter import *
from classes.boardclass import Board

if __name__ =='__main__':

    board = Board((9, 9))
    fenetre = Tk()
    fenetre.title = "Djambi"
    board.generateFourPlayerSet(board)
    board.initBoard(fenetre)
    fenetre.mainloop()