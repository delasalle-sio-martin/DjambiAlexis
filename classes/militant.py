from classes.pion import Pion


class Militant(Pion):
    """
    the militant kills by occupying the square of a piece (capture by replacement).
    He places the corpse on an unoccupied cell of his choice, except on the central cell
    A militant cannot kill a chief in power
    """

    def available_moves(self):
        pass

    def after_move(self):
        pass

    def image(self):
        return "assets/militant.png"
