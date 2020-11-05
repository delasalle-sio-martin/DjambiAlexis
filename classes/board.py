from classes.boardcell import BoardCell
from classes.assassin import Assassin
from classes.chief import Chief
from classes.diplomate import Diplomat
from classes.militant import Militant
from classes.reporter import Reporter
from classes.necromobile import Necromobile
from classes.color import Color
from tkinter import *
from PIL import Image, ImageTk

class Board:

    clickedCell = None

    def __init__(self, dimensions):
        self.dimensions = dimensions
        cells = []
        for x in range(self.dimensions[0]):
            row = []
            for y in range(self.dimensions[1]):
                row.append(BoardCell([]))
            cells.append(row)
        self.cells = cells

    # Il faudrait revoir ensuite cette génération
    def generateFourPlayerSet(self, board):

        # Création des différentes couleurs
        green = Color("Green", "#01D758")
        blue = Color("Blue", "#0131B4")
        red = Color("Red", "#DB1702")
        yellow = Color("Yellow", "#FCDC12")

        # Création d'un board 9x9

        self.board = Board((9, 9))

        # Initialisation pièces jaunes
        chiefYellow = Chief((0, 0), yellow)
        board.cells[0][0].pions = [chiefYellow]
        assassinYellow = Assassin((0, 1), yellow)
        board.cells[0][1].pions = [assassinYellow]
        militantYellow = Chief((0, 2), yellow)
        board.cells[0][2].pions = [militantYellow]
        reporterYellow = Reporter((1, 0), yellow)
        board.cells[1][0].pions = [reporterYellow]
        diplomatYellow = Diplomat((1, 1), yellow)
        board.cells[1][1].pions = [diplomatYellow]
        militantYellow2 = Militant((1, 2), yellow)
        board.cells[1][2].pions = [militantYellow2]
        militantYellow3 = Militant((2, 0), yellow)
        board.cells[2][0].pions = [militantYellow3]
        militantYellow4 = Militant((2, 1), yellow)
        board.cells[2][1].pions = [militantYellow4]
        necromobileYellow = Necromobile((2, 2), yellow)
        board.cells[2][2].pions = [necromobileYellow]

        # Initialisation pièces vertes
        militantGreen = Chief((0, 6), green)
        board.cells[0][6].pions = [militantGreen]
        assassinGreen = Assassin((0, 7), green)
        board.cells[0][7].pions = [assassinGreen]
        chiefGreen = Chief((0, 8), green)
        board.cells[0][8].pions = [chiefGreen]
        militantGreen2 = Militant((1, 6), green)
        board.cells[1][6].pions = [militantGreen2]
        diplomatGreen = Diplomat((1, 7), green)
        board.cells[1][7].pions = [diplomatGreen]
        reporterGreen = Reporter((1, 8), green)
        board.cells[1][8].pions = [reporterGreen]
        necromobileGreen = Necromobile((2, 6), green)
        board.cells[2][6].pions = [necromobileGreen]
        militantGreen3 = Militant((2, 7), green)
        board.cells[2][7].pions = [militantGreen3]
        militantGreen4 = Militant((2, 8), green)
        board.cells[2][8].pions = [militantGreen4]

        # Initialisation pièces bleues
        chiefBlue = Chief((6, 0), blue)
        board.cells[6][0].pions = [chiefBlue]
        assassinBlue = Assassin((6, 1), blue)
        board.cells[6][1].pions = [assassinBlue]
        militantBlue = Chief((6, 2), blue)
        board.cells[6][2].pions = [militantBlue]
        reporterBlue = Reporter((7, 0), blue)
        board.cells[7][0].pions = [reporterBlue]
        diplomatBlue = Diplomat((7, 1), blue)
        board.cells[7][1].pions = [diplomatBlue]
        militantBlue2 = Militant((7, 2), blue)
        board.cells[7][2].pions = [militantBlue2]
        militantBlue3 = Militant((8, 0), blue)
        board.cells[8][0].pions = [militantBlue3]
        militantBlue4 = Militant((8, 1), blue)
        board.cells[8][1].pions = [militantBlue4]
        necromobileBlue = Necromobile((8, 2), blue)
        board.cells[8][2].pions = [necromobileBlue]

        # Initialisation pièces rouges

        militantRed = Chief((6, 6), red)
        board.cells[6][6].pions = [militantRed]
        assassinRed = Assassin((6, 7), red)
        board.cells[6][7].pions = [assassinRed]
        chiefRed = Chief((6, 8), red)
        board.cells[6][8].pions = [chiefRed]
        militantRed2 = Militant((7, 6), red)
        board.cells[7][6].pions = [militantRed2]
        diplomatRed = Diplomat((7, 7), red)
        board.cells[7][7].pions = [diplomatRed]
        reporterRed = Reporter((7, 8), red)
        board.cells[7][8].pions = [reporterRed]
        necromobileRed = Necromobile((8, 6), red)
        board.cells[8][6].pions = [necromobileRed]
        militantRed3 = Militant((8, 7), red)
        board.cells[8][7].pions = [militantRed3]
        militantRed4 = Militant((8, 8), red)
        board.cells[8][8].pions = [militantRed4]

    #Déplacer une partie de l'initBoard dans boardcell pour que ça fonctionne
    def move(self, destinationX, destinationY, fenetre, board):
        selectedPion = self.clickedCell.pions[0]
        beforeMovementPion = selectedPion.position
        selectedPion.position = (destinationX, destinationY)
        self.cells[destinationX][destinationY].pions = [selectedPion]
        self.cells[destinationX][destinationY].initBoard(fenetre, destinationX, destinationY, board)

        self.clickedCell.pions[0] = None
        self.clickedCell.initBoard(fenetre, beforeMovementPion[0], beforeMovementPion[1], board)

    def initBoard(self, fenetre):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if len(self.cells[i][j].pions) > 0:
                    for k in range(len(self.cells[i][j].pions)):
                        image = Image.open(self.cells[i][j].pions[k].image())
                        image = image.resize((50, 50))
                        imageBoard = ImageTk.PhotoImage(image)
                        btn = Button(fenetre, image=imageBoard,
                                      bg=self.cells[i][j].pions[k].color.code)
                        btn.image = imageBoard

                else:
                    image = Image.open("assets/blank.png")
                    image = image.convert("RGBA")
                    image = image.resize((50, 50))
                    imageBoard = ImageTk.PhotoImage(image)
                    btn = Button(fenetre, image=imageBoard)
                    btn.image = imageBoard

                btn.grid(row=i, column=j)
