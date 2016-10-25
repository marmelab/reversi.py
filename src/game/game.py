from .board import Board


class Game:

    def __init__(self):

        self.board = Board()

    def start(self):

        print("\n######### GAME STARTED ############\n")

        print(self.board.render())
        print(self.print_score())
        print(self.board.render(self.board.get_legal_moves(self.board.CELL_WHITE)))
        #print(self.board.render(self.board.get_legal_moves(self.board.CELL_BLACK)))

    def print_score(self):

        cell_distribution = self.board.compute_cell_distribution()
        print("\n#### SCORE (WHITE: {0}, BLACK: {1}) ####\n".format(cell_distribution[self.board.CELL_WHITE], cell_distribution[self.board.CELL_BLACK]))
