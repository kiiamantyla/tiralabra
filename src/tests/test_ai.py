"""Yksikkötestit tekoälyn heuristiikalle"""

import unittest
from ai import evaluate_board

class TestAIHeuristic(unittest.TestCase):
    """Testiluokka heuristiikkafunktiolle"""

    def test_evaluate_empty_cells(self):
        """Testaa, että tyhjistä ruuduista saa paremmat pisteet"""
        good_board = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        bad_board = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 2, 2, 2]
        ]

        score_good = evaluate_board(good_board)
        score_bad = evaluate_board(bad_board)

        self.assertGreater(score_good, score_bad)

    def test_evaluate_snake(self):
        """Testaa, että käärmeheuristiikka painottaa nurkkalaattaa"""
        good_board = [
            [2048, 0, 0, 0],
            [0,    0, 0, 0],
            [0,    0, 0, 0],
            [0,    0, 0, 0]
        ]

        bad_board = [
            [0, 0, 0,    0],
            [0, 0, 0,    0],
            [0, 0, 2048, 0],
            [0, 0, 0,    0]
        ]

        score_good = evaluate_board(good_board)
        score_bad = evaluate_board(bad_board)

        self.assertGreater(score_good, score_bad)
