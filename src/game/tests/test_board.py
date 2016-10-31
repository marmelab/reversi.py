import unittest
from ..board import validate_board_size, get_empty_cells, get_departure_cells, get_cell_distribution, apply_cell_change
from ..board import new_board, get_leading_player_type, render, is_even, get_legal_cell_changes, can_type_apply_cell_change
from ..board import is_legal_cell_change, is_full, get_flipped_cells_from_cell_change
from ..cell import new_cell, TYPE_EMPTY, TYPE_BLACK, TYPE_WHITE
from ..matrix import render as matrix_render


class TestBoard(unittest.TestCase):

    def test_new_board_should_raise_exception_on_invalid_size(self):
        with self.assertRaises(ValueError):
            new_board(5, 6)
        with self.assertRaises(ValueError):
            new_board(2, 2)

    def test_new_board_should_return_valid_game_matrix(self):
        board = new_board(4, 4)
        expected_board = [
            [new_cell(0, 0, TYPE_EMPTY), new_cell(1, 0, TYPE_EMPTY), new_cell(2, 0, TYPE_EMPTY), new_cell(3, 0, TYPE_EMPTY)],
            [new_cell(0, 1, TYPE_EMPTY), new_cell(1, 1, TYPE_BLACK), new_cell(2, 1, TYPE_WHITE), new_cell(3, 1, TYPE_EMPTY)],
            [new_cell(0, 2, TYPE_EMPTY), new_cell(1, 2, TYPE_WHITE), new_cell(2, 2, TYPE_BLACK), new_cell(3, 2, TYPE_EMPTY)],
            [new_cell(0, 3, TYPE_EMPTY), new_cell(1, 3, TYPE_EMPTY), new_cell(2, 3, TYPE_EMPTY), new_cell(3, 3, TYPE_EMPTY)]
        ]
        self.assertEqual(board, expected_board)

    def test_is_even_should_return_false_with_odd_and_true_with_even_number(self):
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(2), True)

    def test_validate_board_size_should_raise_valueerror_on_odd_size(self):
        with self.assertRaises(ValueError):
            validate_board_size(5, 6)
        with self.assertRaises(ValueError):
            validate_board_size(6, 5)

    def test_validate_board_size_should_raise_valueerror_on_size_smaller_than_four(self):
        with self.assertRaises(ValueError):
            validate_board_size(2, 2)

    def test_validate_board_size_should_not_raise_error_on_valid_size(self):
        try:
            validate_board_size(4, 4)
        except:
            self.fail("validate_board_size() raised Error unexpectedly!")

    def test_get_empty_cells_should_return_a_matrix_of_cell_with_empty_type(self):
        cells = get_empty_cells(2, 3)
        expected_cells = [
            new_cell(0, 0, TYPE_EMPTY), new_cell(1, 0, TYPE_EMPTY),
            new_cell(0, 1, TYPE_EMPTY), new_cell(1, 1, TYPE_EMPTY),
            new_cell(0, 2, TYPE_EMPTY), new_cell(1, 2, TYPE_EMPTY)
        ]
        self.assertEqual(cells, expected_cells)

    def test_get_departure_cells_should_return_the_four_base_cells(self):
        matrix = [[None for x in range(2)] for y in range(2)]
        cells = get_departure_cells(matrix)
        expected_cells = [
            new_cell(0, 0, TYPE_BLACK),
            new_cell(1, 1, TYPE_BLACK),
            new_cell(0, 1, TYPE_WHITE),
            new_cell(1, 0, TYPE_WHITE)
        ]
        sort_position = lambda item: item['x'] + item['y']
        self.assertEqual(sorted(expected_cells, key=sort_position), sorted(cells, key=sort_position))

    def test_get_cell_distribution_should_not_return_incremented_dict_on_empty_matrix(self):
        distribution = get_cell_distribution([])
        expected_distribution = distribution = {TYPE_WHITE: 0, TYPE_BLACK: 0, TYPE_EMPTY: 0}
        self.assertEqual(distribution, expected_distribution)

    def test_get_cell_distribution_should_return_incremented_dict_on_filled_matrix(self):
        distribution = get_cell_distribution([
            [new_cell(0, 0, TYPE_EMPTY)],
            [new_cell(0, 0, TYPE_BLACK), new_cell(0, 0, TYPE_BLACK)],
            [new_cell(0, 0, TYPE_WHITE)]
        ])
        expected_distribution = distribution = {TYPE_WHITE: 1, TYPE_BLACK: 2, TYPE_EMPTY: 1}
        self.assertEqual(distribution, expected_distribution)

    def test_get_leading_player_type_should_return_max_scored_type(self):
        matrix = [[new_cell(0, 0, TYPE_BLACK), new_cell(0, 0, TYPE_WHITE), new_cell(0, 0, TYPE_WHITE)]]
        self.assertEqual(get_leading_player_type(matrix), TYPE_WHITE)

    def test_render_should_render_board_with_cell_types_characters(self):
        matrix = [[new_cell(0, 0, TYPE_WHITE), new_cell(0, 1, TYPE_BLACK), new_cell(0, 2, TYPE_EMPTY)]]
        expected_matrix = [["●", "○", " "]]
        self.assertEqual(render(matrix), matrix_render(expected_matrix))

    def test_render_should_render_board_with_proposal_positions(self):
        matrix = [[new_cell(0, 0, TYPE_WHITE), new_cell(0, 1, TYPE_BLACK), new_cell(0, 2, TYPE_EMPTY)]]
        expected_matrix = [["●", "○", "0"]]
        proposal_positions = [(0, 2)]
        self.assertEqual(render(matrix, proposal_positions), matrix_render(expected_matrix))

    def test_apply_cell_change_should_not_mutate_matrix_and_return_false_with_an_invalid_cell_type(self):
        base_matrix = [[new_cell(0, 0, TYPE_WHITE), new_cell(1, 0, TYPE_BLACK)]]
        mutated_matrix = base_matrix
        self.assertEqual(apply_cell_change(mutated_matrix, new_cell(1, 0, TYPE_EMPTY)), False)
        self.assertEqual(mutated_matrix, base_matrix)

    def test_apply_cell_change_should_not_mutate_matrix_and_return_false_with_an_invalid_cell(self):
        base_matrix = [[new_cell(0, 0, TYPE_WHITE), new_cell(1, 0, TYPE_BLACK), new_cell(2, 0, TYPE_EMPTY)]]
        mutated_matrix = base_matrix
        self.assertEqual(apply_cell_change(mutated_matrix, new_cell(2, 0, TYPE_BLACK)), False)
        self.assertEqual(mutated_matrix, base_matrix)

    def test_apply_cell_change_should_mutate_matrix_and_return_true_with_a_valid_cell(self):
        mutated_matrix = [[new_cell(0, 0, TYPE_WHITE), new_cell(1, 0, TYPE_BLACK), new_cell(2, 0, TYPE_EMPTY)]]
        expected_matrix = [[new_cell(0, 0, TYPE_WHITE), new_cell(1, 0, TYPE_WHITE), new_cell(2, 0, TYPE_WHITE)]]
        self.assertEqual(apply_cell_change(mutated_matrix, new_cell(2, 0, TYPE_WHITE)), True)
        self.assertEqual(mutated_matrix, expected_matrix)

    def test_get_legal_cell_changes_should_return_a_dict_for_each_cell_type(self):
        matrix = [[new_cell(0, 0, TYPE_EMPTY)]]
        self.assertEqual(get_legal_cell_changes(matrix), {TYPE_WHITE: [], TYPE_BLACK: []})

    def test_get_legal_cell_changes_should_return_a_list_of_cells_for_each_types(self):
        """
        1 = w, 0 = b, _ = e
        1 0 _
        _ 1 0
        1 0 _
        """
        matrix = [
            [new_cell(0, 0, TYPE_WHITE), new_cell(1, 0, TYPE_BLACK), new_cell(2, 0, TYPE_EMPTY)],
            [new_cell(0, 1, TYPE_EMPTY), new_cell(1, 1, TYPE_WHITE), new_cell(2, 1, TYPE_BLACK)],
            [new_cell(0, 2, TYPE_WHITE), new_cell(1, 2, TYPE_BLACK), new_cell(2, 2, TYPE_EMPTY)]
        ]
        self.assertEqual(get_legal_cell_changes(matrix), {
            TYPE_WHITE: [new_cell(2, 0, TYPE_WHITE), new_cell(2, 2, TYPE_WHITE)],
            TYPE_BLACK: [new_cell(0, 1, TYPE_BLACK)]
        })

    def test_can_type_apply_cell_change_should_return_false_if_there_is_no_possible_cell_changes_for_type(self):
        matrix = [[new_cell(0, 0, TYPE_WHITE), new_cell(1, 0, TYPE_WHITE), new_cell(2, 0, TYPE_EMPTY)]]
        self.assertEqual(can_type_apply_cell_change(matrix, TYPE_WHITE), False)

    def test_can_type_apply_cell_change_should_return_true_if_there_is_possible_cell_changes_for_type(self):
        matrix = [[new_cell(0, 0, TYPE_WHITE), new_cell(1, 0, TYPE_BLACK), new_cell(2, 0, TYPE_EMPTY)]]
        self.assertEqual(can_type_apply_cell_change(matrix, TYPE_WHITE), True)

    def test_is_legal_cell_change_should_return_false_for_invalid_cell_change(self):
        self.assertEqual(is_legal_cell_change([], new_cell(0, 42, TYPE_WHITE)), False)
        self.assertEqual(is_legal_cell_change([[new_cell(0, 0, TYPE_EMPTY)]], new_cell(0, 0, TYPE_EMPTY)), False)

    def test_is_legal_cell_change_should_return_false_for_cell_change_in_another_filled_cell(self):
        matrix = [[new_cell(0, 0, TYPE_WHITE)]]
        self.assertEqual(is_legal_cell_change(matrix, new_cell(0, 0, TYPE_WHITE)), False)

    def test_is_legal_cell_change_should_return_false_for_illegal_cell_change(self):
        matrix = [[new_cell(0, 0, TYPE_WHITE), new_cell(1, 0, TYPE_EMPTY)]]
        self.assertEqual(is_legal_cell_change(matrix, new_cell(1, 0, TYPE_WHITE)), False)
        self.assertEqual(is_legal_cell_change(matrix, new_cell(1, 0, TYPE_BLACK)), False)

    def test_is_legal_cell_change_should_return_true_for_legal_cell_change(self):
        matrix = [[new_cell(0, 0, TYPE_BLACK), new_cell(1, 0, TYPE_WHITE), new_cell(2, 0, TYPE_EMPTY)]]
        self.assertEqual(is_legal_cell_change(matrix, new_cell(2, 0, TYPE_BLACK)), True)

    def test_is_full_should_return_false_for_not_full_filled_board(self):
        matrix = [[new_cell(0, 0, TYPE_EMPTY)]]
        self.assertEqual(is_full(matrix), False)

    def test_is_full_should_return_false_for_full_filled_board(self):
        matrix = [[new_cell(0, 0, TYPE_WHITE)]]
        self.assertEqual(is_full(matrix), True)

    def test_get_flipped_cells_from_cell_change_should_return_an_empty_list_for_cell_change_in_an_already_filled_cell(self):
        matrix = [[new_cell(0, 0, TYPE_WHITE)]]
        self.assertEqual(get_flipped_cells_from_cell_change(matrix, new_cell(0, 0, TYPE_BLACK)), [])

    def test_get_flipped_cells_from_cell_change_should_return_all_flipped_cell_from_valid_cell_change(self):
        matrix = [
            [new_cell(0, 0, TYPE_WHITE), new_cell(1, 0, TYPE_BLACK), new_cell(2, 0, TYPE_EMPTY)],
            [new_cell(0, 1, TYPE_EMPTY), new_cell(1, 1, TYPE_WHITE), new_cell(2, 1, TYPE_BLACK)],
            [new_cell(0, 2, TYPE_WHITE), new_cell(1, 2, TYPE_BLACK), new_cell(2, 2, TYPE_WHITE)]
        ]
        self.assertEqual(get_flipped_cells_from_cell_change(matrix, new_cell(2, 0, TYPE_WHITE)), [new_cell(1, 0, TYPE_WHITE), new_cell(2, 1, TYPE_WHITE)])
