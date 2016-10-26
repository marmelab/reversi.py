from .board import new_board, render, get_cell_distribution, get_legal_cell_changes, is_full, apply_cell_change, can_type_apply_cell_change, get_leading_player_type
from .cell import TYPE_WHITE, TYPE_BLACK, extract_positions

def start():
    print("\n######### GAME STARTED ############\n")

    try:

        board = new_board(8, 8)
        current_type = TYPE_WHITE

        print_board(board)

        while not is_full(board):

            reverse_player_type = get_reverse_player_type(current_type)
            if not can_type_apply_cell_change(board, reverse_player_type):
                print("\n Opponent can't play, play again ! \n")

            else:
                current_type = reverse_player_type

            print_score(get_cell_distribution(board))
            print_ask_board(board, current_type)

            while not apply_cell_change_from_ask_position(board, current_type):
                print("Invalid position, try again")

        print("\n")
        print_board(board)
        print("\n#### {0} PLAYER WIN !! ####\n".format(get_leading_player_type(board)))

    except KeyboardInterrupt:

        print("\n\nBye bye, hope to see you again !\n\n")

def apply_cell_change_from_ask_position(board, cType):
    """ Ask for position and attempt tp apply cell change """

    try:
        position = int(input("Player ({0}) which position ? ".format(cType)))
        legal_changes = get_legal_cell_changes(board)
        return apply_cell_change(board, legal_changes[cType][position])
    except ValueError:
        return False
    except IndexError:
        return False


def get_reverse_player_type(cType):
    """ Get type from reverse player from type """

    if cType == TYPE_WHITE:
        return TYPE_BLACK

    return TYPE_WHITE


def print_ask_board(board, cType):
    """ Print board with cell change possibilities from type """

    legal_changes = get_legal_cell_changes(board)
    print(render(board, extract_positions(legal_changes[cType])))


def print_board(board):
    """ Print board render """

    print(render(board))


def print_score(cell_distribution):
    """ Show score from cell_distribution as string """

    print("\n#### SCORE (WHITE: {0}, BLACK: {1}) ####\n".format(
        cell_distribution[TYPE_WHITE],
        cell_distribution[TYPE_BLACK]
    ))
