"""Yksikkötestit tekoälyn heuristiikalle"""

import unittest
from ai import evaluate_board, expectimax, get_best_move

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

    def test_get_best_move_returns_valid_move(self):
        """Testaa, että palautuu sallittu suunta tai None"""
        board = [
            [2, 4, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        move = get_best_move(board, depth=2)
        self.assertIn(move, ["left", "right", "up", "down", None])

    def test_get_best_move_can_merge(self):
        """Testaa, että tekoäly osaa siirtää laattoja, kun siirtoja on tarjolla"""
        board = [
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        move = get_best_move(board, depth=2)
        self.assertEqual(move, "left")

    def test_get_best_move_no_moves(self):
        """Testaa tilannetta, jossa valideja siirtoja ei ole"""
        full_board = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2]
        ]

        move = get_best_move(full_board, depth=1)
        self.assertIsNone(move)

    def test_expectimax_depth_zero(self):
        """Testaa expectimax-algoritmia syvyydellä 0"""
        board = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        val = expectimax(board, depth=0, is_player=True)
        self.assertIsInstance(val, float)

    def test_expectimax_max_node(self):
        """Testaa expectimax-algortimia max-solmulla"""
        board = [
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        val = expectimax(board, depth=1, is_player=True)
        self.assertIsInstance(val, float)

    def test_expectimax_chance_node(self):
        """Testaa expectimax-algortimia max-solmulla"""
        board = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        val = expectimax(board, depth=1, is_player=False)
        self.assertIsInstance(val, float)

    def test_expectimax_no_valid_moves_with_max_node(self):
        """Testaa expectimax-algoritmia max-solmulla kun ei ole valideja siirtoja"""
        full_board = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2]
        ]

        val = expectimax(full_board, depth=1, is_player=True)
        self.assertIsInstance(val, float)

    def test_expectimax_chance_node_no_empty_cells(self):
        """Testaa expectimax-algoritmia chance-solmulla kun ei ole valideja siirtoja"""
        full_board = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2]
        ]

        val = expectimax(full_board, depth=1, is_player=False)
        self.assertIsInstance(val, float)