from classes.pion import Pion


class Necromobile(Pion):
    """
    the necromobile acts like a diplomat but only with the dead pieces
    (whatever the origin of the dead piece is).
    """

    def available_moves(self):
        pass

    def after_move(self):
        pass

    def image(self):
        return "assets/necromobile.png"