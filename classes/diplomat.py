from classes.pion import Pion


class Diplomat(Pion):
    """
    the diplomat can move another living piece by occupying its square
    (of course, he can only move the pieces of the other players).
    The piece is placed on any unoccupied cell
    """
    def available_moves(self):
        pass

    def after_move(self):
        pass

    def image(self):
        return "assets/diplomate.png"