from .color import UNDERLINE, colorize


def new_matrix(xSize, ySize, value=None):
    return [[value for x in range(xSize)] for y in range(ySize)]


def draw_cell(matrix, cell):
    matrix[cell['y']][cell['x']] = cell


def draw_cells(matrix, cells=[]):
    for cell in cells:
        draw_cell(matrix, cell)


def get_size(matrix):
    """ We suppose that matrix x len is the same everywhere """

    rows_count = len(matrix)

    if rows_count is 0:
        return (0, 0)

    return (len(matrix[0]), rows_count)


def get_cell(matrix, xPos, yPos, default=None):
    """ Return cell value, return default if no one is find """

    try:
        # Disable negative index functionnality
        if yPos < 0 or xPos < 0:
            raise IndexError
        return matrix[yPos][xPos]
    except LookupError:
        return default


def render(matrix):

    xSize, ySize = get_size(matrix)
    render_str = "_" * (xSize * 2 + 1) + "\n"

    for row in matrix:
        render_str += "|"
        for val in row:
            render_str += '%5s' % colorize(val, UNDERLINE) + "|"
        render_str += "\n"

    return render_str
