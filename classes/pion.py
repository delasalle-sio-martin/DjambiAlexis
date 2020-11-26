from abc import ABC, abstractmethod
from classes.color import Color


class Pion(ABC):
    """
    Pion is an abstract class (ABC) that will be used by the others pawns
    """

    def __init__(self, position: (int, int), color: Color):
        self.alive = True
        self.position = position
        self.color = color

    @abstractmethod
    def available_moves(self):
        pass

    @abstractmethod
    def after_move(self):
        pass

    @abstractmethod
    def image(self):
        """
        Represent the path to the icon of a pawn used on the board
        :return:
        """
        return "assets/blank.png"
