from .color import UNDERLINE, colorize
from .cell import new_cell, get_symbol, get_types, TYPE_WHITE, TYPE_BLACK, TYPE_EMPTY, extract_positions
from .matrix import new_matrix, draw_cells, get_size as get_matrix_size, get_cell as get_matrix_cell
from .vector import get_directionnal_vectors, vector_add


def new_board(xSize, ySize):
    """ Create a new board matrix from x/y sizes """

    validate_board_size(xSize, ySize)

    matrix = new_matrix(xSize, ySize)
    draw_cells(matrix, get_empty_cells(xSize, ySize) + get_departure_cells(matrix))

    return matrix


def is_even(x):
    return x % 2 == 0


def validate_board_size(xSize, ySize):
    """ Validate board size, size must be even to draw departure cells """

    if not is_even(xSize) or not is_even(ySize):
        raise ValueError("Board x/y size must be even.")
    if ySize < 4 or xSize < 4:
        raise ValueError("Board must have 4 rows or columns at least")


def get_empty_cells(xSize, ySize):
    """ Return a set of empty cells to apply on board """

    empty_cells = []

    for yPos in range(0, ySize):
        for xPos in range(0, xSize):
            empty_cells.append(new_cell(xPos, yPos, TYPE_EMPTY))

    return empty_cells

def get_departure_cells(matrix):
    """ Return departure cells from board """

    xSize, ySize = get_matrix_size(matrix)

    x_middle = int(xSize/2)
    y_middle = int(ySize/2)

    return [
        new_cell(x_middle, y_middle, TYPE_BLACK),
        new_cell(x_middle - 1, y_middle - 1, TYPE_BLACK),
        new_cell(x_middle - 1, y_middle, TYPE_WHITE),
        new_cell(x_middle, y_middle - 1, TYPE_WHITE)
    ]


def get_cell_distribution(matrix):
    """ Return cell value distribution grouped by type """

    distribution = {TYPE_WHITE: 0, TYPE_BLACK: 0, TYPE_EMPTY: 0}

    for row in matrix:
        for cell in row:
            distribution[cell['type']] += 1

    return distribution


def get_leading_player_type(matrix):

    distribution = get_cell_distribution(matrix)

    if(distribution[TYPE_WHITE] > distribution[TYPE_BLACK]):
        return TYPE_WHITE

    return TYPE_BLACK


def is_full(matrix):
    return get_cell_distribution(matrix)[TYPE_EMPTY] == 0


def render(matrix, proposal_positions=[]):
    """ Render board as string """

    xSize, ySize = get_matrix_size(matrix)
    known_types = get_types()

    character = ""
    board_render = "_" * (xSize * 2 + 1) + "\n"

    for row_idx, row in enumerate(matrix):
        board_render += "|"
        for cell_idx, cell in enumerate(row):
            cell_position = extract_positions([cell])[0]
            if cell_position in proposal_positions:
                character = str(proposal_positions.index(cell_position))
            elif cell['type'] in known_types:
                character = get_symbol(cell)
            board_render += colorize(character, UNDERLINE) + "|"
        board_render += "\n"

    return board_render


def get_flipped_cells_from_cell_change(matrix, cell):
    """ Return a set of flipped cells from cell change """

    flipped_cells = []
    empty_cell = new_cell(0, 0, TYPE_EMPTY)
    xPos, yPos, cType = cell['x'], cell['y'], cell['type']

    if not get_matrix_cell(matrix, xPos, yPos)['type'] is TYPE_EMPTY:
        return []

    # Loop over all possibles directions (except null vector)
    for vector in get_directionnal_vectors():
        (x, y) = vector_add((xPos, yPos), vector)
        vector_flipped_cells = []

        # While there's no empty cell, same color disk or border, go forward
        while get_matrix_cell(matrix, x, y, empty_cell)['type'] not in [TYPE_EMPTY, cType]:
            vector_flipped_cells.append(new_cell(x, y, cType))
            (x, y) = vector_add((x, y), vector)

        # If the're flipped disks and last cell has same type, it's ok
        last_cell = get_matrix_cell(matrix, x, y, empty_cell)
        if len(vector_flipped_cells) > 0 and last_cell['type'] is cType:
            flipped_cells += vector_flipped_cells

    return flipped_cells


def is_legal_cell_change(matrix, cell):
    return len(get_flipped_cells_from_cell_change(matrix, cell)) > 0


def can_type_apply_cell_change(matrix, cType):
    return len(get_legal_cell_changes(matrix)[cType]) > 0


def get_legal_cell_changes(matrix):
    """ Return legal cell changes for each types """

    legal_cell_changes = {TYPE_WHITE: [], TYPE_BLACK: []}
    xSize, ySize = get_matrix_size(matrix)

    for cType in [TYPE_WHITE, TYPE_BLACK]:
        for yPos in range(0, ySize):
            for xPos in range(0, xSize):
                cell_change = new_cell(xPos, yPos, cType)
                if is_legal_cell_change(matrix, cell_change):
                    legal_cell_changes[cType].append(cell_change)

    return legal_cell_changes


def apply_cell_change(matrix, cell):
    """ Attempt to place cell in the board """

    if not is_legal_cell_change(matrix, cell):
        return False

    flipped_cells = get_flipped_cells_from_cell_change(matrix, cell)
    draw_cells(matrix, [cell] + flipped_cells)

    return True
