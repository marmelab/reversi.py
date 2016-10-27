import unittest
from ..matrix import new_matrix, draw_cell, draw_cells, get_size, get_cell, render
from ..cell import new_cell, TYPE_WHITE
from ..color import colorize as c, UNDERLINE as u


class TestMatrix(unittest.TestCase):

    def test_new_matrix_should_return_matrix(self):
        expected_matrix = [[None, None], [None, None], [None, None]]
        matrix = new_matrix(2, 3, None)
        self.assertEqual(expected_matrix, matrix)

    def test_draw_cell_should_mute_matrix(self):
        matrix = [[None, None], [None, None], [None, None]]
        cell = new_cell(1, 0, TYPE_WHITE)
        expected_matrix = [[None, cell], [None, None], [None, None]]
        draw_cell(matrix, cell)
        self.assertEqual(matrix, expected_matrix)

    def test_draw_cells_should_mute_matrix_from_cells(self):
        matrix = [[None, None], [None, None], [None, None]]
        cell1 = new_cell(1, 1, TYPE_WHITE)
        cell2 = new_cell(0, 0, TYPE_WHITE)
        expected_matrix = [[cell2, None], [None, cell1], [None, None]]
        draw_cells(matrix, [cell1, cell2])
        self.assertEqual(matrix, expected_matrix)

    def test_get_size_should_return_matrix_size_from_first_row_only(self):
        matrix = [[0, 0, 0], [0, 0, 0, 0], [0, 0]]
        expected_size = (3, 3)
        self.assertEqual(get_size(matrix), expected_size)

    def test_get_cell_should_return_cell_value(self):
        matrix = [[0, 0, 0], [0, 0, 0, 1], [0, 0]]
        self.assertEqual(get_cell(matrix, 3, 1), 1)

    def test_get_cell_should_return_default_cell_value_on_indexerror(self):
        matrix = [[0]]
        self.assertEqual(get_cell(matrix, 42, 42, ':)'), ':)')

    def test_render_should_return_rendered_matrix_as_string(self):
        matrix = [["1", "2"], ["0", "3"]]
        # Second arg represent the terminal rendering of the expected render result
        self.assertEqual(render(matrix), "_____\n|" + c("1", u)  + "|" + c("2", u)  + "|\n|" + c("0", u)  + "|" + c("3", u)  + "|\n")
