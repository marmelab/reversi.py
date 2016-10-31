import unittest
import sys
from io import StringIO
from ..game import print_score, print_ask_board, get_reverse_player_type
from ..cell import new_cell, TYPE_WHITE, TYPE_EMPTY, TYPE_BLACK
from ..color import colorize as c, UNDERLINE as u


class TestGame(unittest.TestCase):

    def test_print_score_should_output_score_disclaimer(self):
        stdout_ = sys.stdout
        stream = StringIO()
        sys.stdout = stream
        print_score({TYPE_WHITE: 13, TYPE_BLACK: 37, TYPE_EMPTY: 42})
        sys.stdout = stdout_
        self.assertEqual(stream.getvalue(), "\n#### SCORE (WHITE: 13, BLACK: 37) ####\n\n")

    def test_get_reverse_player_type_should_return_reverse_cell_type(self):
        self.assertEqual(get_reverse_player_type(TYPE_WHITE), TYPE_BLACK)
        self.assertEqual(get_reverse_player_type(TYPE_BLACK), TYPE_WHITE)
