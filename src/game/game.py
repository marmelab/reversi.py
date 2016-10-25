from .board import Board


class Game:

    def __init__(self):

        self.board = Board()

    def start(self):

        print("\n######### GAME STARTED ############\n")

        print(self.board.compute_cell_distribution())
        print(self.board.render())
        print(self.board.compute_cell_distribution())
        print(self.board.render(self.board.get_legal_moves(self.board.CELL_WHITE)))
        #print(self.board.render(self.board.get_legal_moves(self.board.CELL_BLACK)))

    def print_score(self):

        print("#### SCORE (WHITE: {0}, BLACK: {1})".format())
