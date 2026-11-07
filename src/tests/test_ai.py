"""Yksikkötestit tekoälyn heuristiikalle"""

import unittest
from ai import evaluate_board

class TestAIHeuristic(unittest.TestCase):
    """Testiluokka heuristiikkafunktiolle"""

    def test_evaluate_empty_cells(self):
        """Testaa, tyhjistä ruuduista saa paremmat pisteet"""
        good_board = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        bad_board = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [0, 4, 2, 0],
            [2, 0, 0, 4]
        ]

        score_good = evaluate_board(good_board)
        score_bad = evaluate_board(bad_board)

        self.assertGreater(score_good, score_bad)
