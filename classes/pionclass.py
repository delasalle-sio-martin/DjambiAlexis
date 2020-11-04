from abc import ABC,abstractmethod

class Pion(ABC):

    def __init__(self, position, color):
        self.alive = True
        self.position = position
        self.color = color

    @abstractmethod
    def available_moves(self):
        pass

    @abstractmethod
    def after_move(self):
        pass

