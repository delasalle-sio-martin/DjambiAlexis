from classes.pion import Pion


class Chief(Pion):
    """
    The chief kills and places the corpse in the same way as the militant.
    """

    def available_moves(self):
        pass

    def after_move(self):
        pass

    def image(self):
        return "assets/chief.png"
