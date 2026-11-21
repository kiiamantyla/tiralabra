"""Yksikkötestit tekoälyn heuristiikalle ja expectimax-algoritmille"""

import unittest
from ai import count_empty_cells, evaluate_board, expectimax, get_best_move, get_dynamic_depth

class TestAIHeuristic(unittest.TestCase):
    """Testiluokka heuristiikkafunktiolle ja expectimax-algortimille"""

    def setUp(self):
        self.full_board = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2]
        ]

        self.board = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

    def test_count_empty_cells(self):
        """Testaa tyhjien ruutujen laskemisen"""
        self.assertEqual(count_empty_cells(self.board), 15)
        self.assertEqual(count_empty_cells(self.full_board), 0)

    def test_evaluate_empty_cells(self):
        """Testaa, että tyhjistä ruuduista saa paremmat pisteet"""
        bad_board = [
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 2, 2, 2]
        ]

        score_good = evaluate_board(self.board)
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

    def test_dynamic_depth(self):
        """Testaa hakusyvyyden muuttumisen"""
        self.assertEqual(get_dynamic_depth(self.board, 3), 3)

        five_empty_board = [
            [2, 4, 2, 4],
            [4, 0, 4, 2],
            [0, 4, 0, 4],
            [4, 0, 4, 0]
        ]
        self.assertEqual(get_dynamic_depth(five_empty_board, 3), 4)

        two_empty_board = [
            [2, 0, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 0, 2]
        ]
        self.assertEqual(get_dynamic_depth(two_empty_board, 3), 5)

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
        move = get_best_move(self.full_board, depth=1)
        self.assertIsNone(move)

    def test_expectimax_depth_zero(self):
        """Testaa expectimax-algoritmia syvyydellä 0"""
        val = expectimax(self.board, depth=0, is_player=True)
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
        """Testaa expectimax-algortimia chance-solmulla"""
        val = expectimax(self.board, depth=1, is_player=False)
        self.assertIsInstance(val, float)

    def test_expectimax_no_valid_moves_with_max_node(self):
        """Testaa expectimax-algoritmia max-solmulla kun ei ole valideja siirtoja"""
        val = expectimax(self.full_board, depth=1, is_player=True)
        self.assertIsInstance(val, float)

    def test_expectimax_chance_node_no_empty_cells(self):
        """Testaa expectimax-algoritmia chance-solmulla kun ei ole valideja siirtoja"""
        val = expectimax(self.full_board, depth=1, is_player=False)
        self.assertIsInstance(val, float)
