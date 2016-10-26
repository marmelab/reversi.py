from .board import new_board, render
from .cell import TYPE_WHITE, TYPE_BLACK


def start():
    print("\n######### GAME STARTED ############\n")

    board = new_board(8, 8)
    print(board)
    print(render(board))


def ask_position(cType):
    return int(input("Player ({0}) which position ?".format(cType)))


def print_ask_board(board, cType):
    legal_changes = get_legal_cell_changes(board)

    from_type_filter = (lambda c: x['type'] == cType)

    legal_changes_from_type = filter(from_type_filter, legal_changes)
    print(board.render(board, legal_cell_changes_from_type))


def print_score(cell_distribution):
    """ Show score from cell_distribution as string """

    score = [cell_distribution[TYPE_WHITE], cell_distribution[TYPE_BLACK]]
    print("\n#### SCORE (WHITE: {0}, BLACK: {1}) ####\n".format(scores))
