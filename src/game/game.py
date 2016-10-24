from .board import Board

class Game:

    def __init__(self):

        self.board = Board()

    def start(self):

        print("\n######### GAME STARTED ############\n")

        print(self.board.compute_score())
        self.board.render()
