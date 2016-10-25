from .color import UNDERLINE, colorize
from .move import new_move
from itertools import product
import operator


class Board:

    """ Reversi Board """

    CELL_EMPTY = "empty"
    CELL_BLACK = "black"
    CELL_WHITE = "white"

    def __init__(self, rows=8, columns=8):

        """ Rows / Columns count must be even for placing the departure discs in the center of the board """

        is_even = lambda x: x % 2 == 0

        if not is_even(rows) or not is_even(columns):
            raise ValueError("Board rows and columns count must be set with an even number.")
        if rows < 4 or columns < 4:
            raise ValueError("Board must have 4 rows or columns at least")

        self.cells = []
        self.rows = rows
        self.columns = columns

        self._init_board()

    def place_disk(self, color, proposal_index):

        """ Place disk at the given position for color """

        proposal_map = self.get_legal_moves(color)
        row, column = proposal_map[proposal_index]

        flipped_positions = self.get_flipped_positions_for_move(new_move(row, column, color))

        self.cells[row][column] = color

        for flipped_position in flipped_positions:
            self.cells[flipped_position[0]][flipped_position[1]] = color

    def inverse_color(self, color):
        if color == self.CELL_WHITE:
            return self.CELL_BLACK

        return self.CELL_WHITE

    def compute_cell_distribution(self):

        """ Compute current cell distribution by type """

        score = {self.CELL_WHITE: 0, self.CELL_BLACK: 0, self.CELL_EMPTY: 0}

        for row in self.cells:
            for col in row:
                score[col] += 1

        return score

    def is_full(self):
        return self.compute_cell_distribution()[self.CELL_EMPTY] == 0

    def render(self, proposals=[]):

        """ Render current board """

        character = ""
        board_render = "_" * (self.columns * 2 + 1) + "\n"

        for rowidx, row in enumerate(self.cells):
            board_render += "|"
            for colidx, col in enumerate(row):
                if col == self.CELL_WHITE:
                    character = "●"
                elif col == self.CELL_BLACK:
                    character = "○"
                elif (rowidx, colidx) in proposals:
                    character = str(proposals.index((rowidx, colidx)))
                else:
                    character = " "
                board_render += colorize(character, UNDERLINE) + "|"
            board_render += "\n"

        return board_render

    def get_legal_moves(self, color):
        """ Return all possibles positions in an array of tuples """

        allowed_positions = []

        for rowidx, row in enumerate(self.cells):
            for colidx, col in enumerate(row):
                if self.is_legal_move(new_move(rowidx, colidx, color)):
                    allowed_positions.append((rowidx, colidx))

        return allowed_positions

    def is_legal_move(self, move):
        return len(self.get_flipped_positions_for_move(move)) > 0

    def get_flipped_positions_for_move(self, move):
        global_flipped_positions = []
        row, column, color = move['row'], move['column'], move['color']

        if not self.get_cell_value(row, column) == self.CELL_EMPTY:
            return []

        # Vector addition
        vector_add = lambda v1, v2: tuple(map(operator.add, v1, v2))

        # Create directionnal vectors
        direction_vectors = product((-1, 0, 1), (-1, 0, 1))

        # Loop over all possibles directions (except null vector)
        for vector in (vectors for vectors in direction_vectors if not vectors == (0, 0)):
            (x, y) = vector_add((row, column), vector)
            local_flipped_positions = []

            # While there's no empty cell, same color disk or border, go forward
            while self.get_cell_value(x, y) not in [None, self.CELL_EMPTY, color]:
                local_flipped_positions.append((x, y))
                (x, y) = vector_add((x, y), vector)

            # If the're flipped disks and last position is same color, it's ok
            if len(local_flipped_positions) > 0 and self.get_cell_value(x, y) == color:
                global_flipped_positions += local_flipped_positions

        return global_flipped_positions

    def get_cell_value(self, row, column):
        try:
            return self.cells[row][column]
        except IndexError:
            return None

    def populate_from_positions_array(self, positions):

        """ Populate the current board with given positions """

        self._check_positions_array_validity(positions)

        for rowidx, row in enumerate(positions):
            for colidx, col in enumerate(row):
                self.cells[rowidx][colidx] = col

    def _check_positions_array_validity(self, positions):

        """Ensure that given positions match the current board configuration"""

        rowlen = len(positions)

        if not rowlen == self.rows:
            raise ValueError("Invalid rows count for board population. {0} given, {1} expected.".format(rowlen, self.rows))

        for rowidx, row in enumerate(positions):
            if not len(row) == self.columns:
                raise ValueError("Invalid columns count for board population at {0} row".format(rowidx))

    def _init_board(self):

        """ Init board with default reversi configuration """

        self.cells = [[self.CELL_EMPTY for x in range(self.columns)] for y in range(self.rows)]

        row_middle = int(self.rows/2)
        column_middle = int(self.columns/2)

        self.cells[row_middle][column_middle] = self.CELL_BLACK
        self.cells[row_middle - 1][column_middle - 1] = self.CELL_BLACK
        self.cells[row_middle - 1][column_middle] = self.CELL_WHITE
        self.cells[row_middle][column_middle - 1] = self.CELL_WHITE
