from .board import Board

def start():

    print("\n######### GAME STARTED ############\n")

    board = Board()

    print(board.render())
    print(print_score(board))
    print(board.render(board.get_legal_moves(board.CELL_WHITE)))
    print(board.get_flipped_disks_for_move(3, 2, board.CELL_WHITE))
    #print(board.render(board.get_legal_moves(board.CELL_BLACK)))

def print_score(board):

    cell_distribution = board.compute_cell_distribution()
    print("\n#### SCORE (WHITE: {0}, BLACK: {1}) ####\n".format(cell_distribution[board.CELL_WHITE], cell_distribution[board.CELL_BLACK]))
