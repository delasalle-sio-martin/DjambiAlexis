from classes.boardclass import Board
from classes.assassinclass import Assassin
from classes.chiefclass import Chief
from classes.diplomatclass import Diplomat
from classes.militantclass import Militant
from classes.reporterclass import Reporter
from classes.necromobile import Necromobile
from tkinter import *

if __name__ =='__main__':

    #Création d'un board 9x9

    board = Board((9, 9))

    #Initialisation pièces jaunes
    chiefYellow = Chief((0, 0), "Yellow")
    board.cells[0][0].pions = [chiefYellow]
    assassinYellow = Assassin((0, 1), "Yellow")
    board.cells[0][1].pions = [assassinYellow]
    militantYellow = Chief((0, 2), "Yellow")
    board.cells[0][2].pions = [militantYellow]
    reporterYellow = Reporter((1, 0), "Yellow")
    board.cells[1][0].pions = [reporterYellow]
    diplomatYellow = Diplomat((1, 1), "Yellow")
    board.cells[1][1].pions = [diplomatYellow]
    militantYellow2 = Militant((1, 2), "Yellow")
    board.cells[1][2].pions = [militantYellow2]
    militantYellow3 = Militant((2, 0), "Yellow")
    board.cells[2][0].pions = [militantYellow3]
    militantYellow4 = Militant((2, 1), "Yellow")
    board.cells[2][1].pions = [militantYellow4]
    necromobileYellow = Necromobile((2, 2), "Yellow")
    board.cells[2][2].pions = [necromobileYellow]

    #Initialisation pièces vertes
    militantGreen = Chief((0, 6), "Green")
    board.cells[0][6].pions = [militantGreen]
    assassinGreen = Assassin((0, 7), "Green")
    board.cells[0][7].pions = [assassinGreen]
    chiefGreen = Chief((0, 8), "Green")
    board.cells[0][8].pions = [chiefGreen]
    militantGreen2 = Militant((1, 6), "Green")
    board.cells[1][6].pions = [militantGreen2]
    diplomatGreen = Diplomat((1, 7), "Green")
    board.cells[1][7].pions = [diplomatGreen]
    reporterGreen = Reporter((1, 8), "Green")
    board.cells[1][8].pions = [reporterGreen]
    necromobileGreen = Necromobile((2, 6), "Green")
    board.cells[2][6].pions = [necromobileGreen]
    militantGreen3 = Militant((2, 7), "Green")
    board.cells[2][7].pions = [militantGreen3]
    militantGreen4 = Militant((2, 8), "Green")
    board.cells[2][8].pions = [militantGreen4]

    #Initialisation pièces bleues
    chiefBlue = Chief((6, 0), "Blue")
    board.cells[6][0].pions = [chiefYellow]
    assassinBlue = Assassin((6, 1), "Blue")
    board.cells[6][1].pions = [assassinBlue]
    militantBlue = Chief((6, 2), "Blue")
    board.cells[6][2].pions = [militantBlue]
    reporterBlue = Reporter((7, 0), "Blue")
    board.cells[7][0].pions = [reporterBlue]
    diplomatBlue = Diplomat((7, 1), "Blue")
    board.cells[7][1].pions = [diplomatBlue]
    militantBlue2 = Militant((7, 2), "Blue")
    board.cells[7][2].pions = [militantBlue2]
    militantBlue3 = Militant((8, 0), "Blue")
    board.cells[8][0].pions = [militantBlue3]
    militantBlue4 = Militant((8, 1), "Blue")
    board.cells[8][1].pions = [militantBlue4]
    necromobileBlue = Necromobile((8, 2), "Blue")
    board.cells[8][2].pions = [necromobileBlue]

    #Initialisation pièces rouges

    militantRed = Chief((6, 6), "Red")
    board.cells[6][6].pions = [militantRed]
    assassinRed = Assassin((6, 7), "Red")
    board.cells[6][7].pions = [assassinRed]
    chiefRed = Chief((6, 8), "Red")
    board.cells[6][8].pions = [chiefRed]
    militantRed2 = Militant((7, 6), "Red")
    board.cells[7][6].pions = [militantRed2]
    diplomatRed = Diplomat((7, 7), "Red")
    board.cells[7][7].pions = [diplomatRed]
    reporterRed = Reporter((7, 8), "Red")
    board.cells[7][8].pions = [reporterRed]
    necromobileRed = Necromobile((8, 6), "Red")
    board.cells[8][6].pions = [necromobileRed]
    militantRed3 = Militant((8, 7), "Red")
    board.cells[8][7].pions = [militantRed3]
    militantRed4 = Militant((8, 8), "Red")
    board.cells[8][8].pions = [militantRed4]

    #Ajout des pièces dans le board

    for i in range(len(board.cells)):
        for j in range(len(board.cells[i])):
            for k in range(len(board.cells[i][j].pions)):
                print(board.cells[i][j].pions[k].__class__.__name__, end=' ')
                print(board.cells[i][j].pions[k].color)
        else:
            print(i, end=',')
            print(j, end=',')
            print('vide')


    fenetre = Tk()
    champ_label = Label(fenetre, text="Djambi")
    champ_label.pack()
    for r in range(9):
        for c in range(9):
            Label(fenetre, text='R%s/C%s' % (r, c)).grid(row=r, column=c)
    fenetre.mainloop()