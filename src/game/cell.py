
TYPE_EMPTY = "empty"
TYPE_WHITE = "white"
TYPE_BLACK = "black"


def new_cell(xPos, yPos, type=TYPE_EMPTY):
    return {'x': xPos, 'y': yPos, 'type': type}


def get_symbol(cell):
    """ Return cell symbol from cell type """

    if cell['type'] == TYPE_BLACK:
        return "○"
    if cell['type'] == TYPE_WHITE:
        return "●"

    return " "


def get_types():
    return set([TYPE_WHITE, TYPE_BLACK, TYPE_EMPTY])


def extract_positions(cells):
    return list(map(lambda cell: (cell['x'], cell['y']), cells))
