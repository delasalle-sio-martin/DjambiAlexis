from classes.pion import Pion


class Reporter(Pion):
    """
    the reporter kills by occupying one of the four squares next to the square of the piece he wants to kill
    (he cannot kill diagonally)
    The corpse stays in his square; the reporter can only kill at the end of his move.
    """
    def available_moves(self):
        pass

    def after_move(self):
        pass

    def image(self):
        return "assets/reporter.png"
