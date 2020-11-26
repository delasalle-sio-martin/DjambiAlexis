from classes.pion import Pion


class Assassin(Pion):
    """
    the assassin kills in the same way as the militant
    but places the corpse in the square he comes from.
    """

    def available_moves(self):
        pass

    def after_move(self):
        pass

    def image(self):
        return "assets/assassin.png"
