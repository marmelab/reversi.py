from .board import Board
from .move import new_move


def start():
    print("\n######### GAME STARTED ############\n")

    board = Board()
    current_color = board.CELL_BLACK

    print(board.render())

    while not board.is_full():

        print_score(board)
        print_ask_board(board, current_color)

        position_choice = ask_position(current_color)

        while not board.place_disk(current_color, position_choice):
            print("Invalid position, try again")
            position_choice = ask_position(current_color)

        current_color = get_reverse_color(current_color)

    #print("{0} WINS !".format(winner))


def ask_position(color):
    return int(input("Player ({0}) which position ?".format(color)))


def print_ask_board(board, color):
    print(board.render(board.get_legal_moves(color)))


def print_score(board):
    cell_distribution = board.compute_cell_distribution()
    print("\n#### SCORE (WHITE: {0}, BLACK: {1}) ####\n".format(cell_distribution[board.CELL_WHITE], cell_distribution[board.CELL_BLACK]))


def get_reverse_color(color):
    return Board.CELL_BLACK if color == Board.CELL_WHITE else Board.CELL_WHITE
