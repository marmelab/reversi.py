def new_matrix(xSize, ySize, value=None):
    return [[value for x in range(xSize)] for y in range(ySize)]


def draw_cell(matrix, cell):
    matrix[cell['x']][cell['y']] = cell


def draw_cells(matrix, cells=[]):
    for cell in cells:
        draw_cell(matrix, cell)


def get_size(matrix):
    """ We suppose that matrix x len is the same everywhere """

    rows_count = len(matrix)

    if(rows_count == 0):
        return (0, 0)

    return (len(matrix[0]), rows_count)


def get_cell(matrix, xPos, yPos):
    """ Return cell value, return None if no one is find """

    try:
        return matrix[xPos][yPos]
    except IndexError:
        return None
