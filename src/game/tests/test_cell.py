import unittest
from ..cell import new_cell, get_symbol, get_types, extract_positions, TYPE_WHITE, TYPE_EMPTY, TYPE_BLACK


class TestCell(unittest.TestCase):

    def test_new_cell_should_return_cell_dict(self):
        self.assertEqual(new_cell(42, 24, TYPE_WHITE), {'x': 42, 'y': 24, 'type': TYPE_WHITE})

    def test_get_symbol_should_return_cell_symbol(self):
        self.assertEqual(get_symbol(new_cell(0, 0, TYPE_BLACK)), "○")
        self.assertEqual(get_symbol(new_cell(0, 0, TYPE_WHITE)), "●")

    def test_get_symbol_should_return_empty_string_for_type_empty(self):
        self.assertEqual(get_symbol(new_cell(0, 0, TYPE_EMPTY)), " ")

    def test_get_types_should_return_all_types(self):
        self.assertEqual(get_types(), {TYPE_WHITE, TYPE_BLACK, TYPE_EMPTY})

    def test_extract_positions_should_return_a_list_of_position_tuples_from_cells(self):
        self.assertEqual(extract_positions([new_cell(42, 41, TYPE_EMPTY), new_cell(42, 1, TYPE_BLACK)]), [(42, 41), (42, 1)])
