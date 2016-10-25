from .board import Board
from .move import new_move


def start():
    print("\n######### GAME STARTED ############\n")

    board = Board()
    current_color = board.CELL_BLACK

    print(board.render())

    while not board.is_full():

        print_score(board)
        print(board.render(board.get_legal_moves(current_color)))

        position_choice = input("Player ({0}) which position ?".format(current_color))
        board.place_disk(current_color, int(position_choice))

        current_color = board.CELL_BLACK if current_color == board.CELL_WHITE else board.CELL_WHITE

    #print("{0} WINS !".format(winner))

def print_score(board):
    cell_distribution = board.compute_cell_distribution()
    print("\n#### SCORE (WHITE: {0}, BLACK: {1}) ####\n".format(cell_distribution[board.CELL_WHITE], cell_distribution[board.CELL_BLACK]))
