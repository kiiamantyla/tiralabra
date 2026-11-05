"""Yksikkötestit 2048-pelin sovelluslogiikalla"""

import unittest

from game import merge_row, move_left, move_right, move_up, move_down

class TestGameLogic(unittest.TestCase):
    """Testiluokka siirtologiikalle"""
    def setUp(self):
        self.board = [
            [2, 2, 0, 0],
            [2, 2, 0, 4],
            [0, 0, 0, 0],
            [0, 4, 0, 4]
        ]
        self.expected_score = 16

    def test_merge_row(self):
        """Testaa rivin yhdistymisen"""
        row = [2, 2, 0, 0]
        new_row, score = merge_row(row)
        self.assertEqual(new_row, [4, 0, 0, 0])
        self.assertEqual(score, 4)

    def test_move_left(self):
        """Testaa koko laudan siirtoa vasemmalle"""
        new_board, score = move_left(self.board)
        expected_board = [
            [4, 0, 0, 0],
            [4, 4, 0, 0],
            [0, 0, 0, 0],
            [8, 0, 0, 0]
        ]
        self.assertEqual(new_board, expected_board)
        self.assertEqual(score, self.expected_score)

    def test_move_right(self):
        """Testaa laudan siirtoa oikealle"""
        new_board, score = move_right(self.board)
        expected_board = [
            [0, 0, 0, 4],
            [0, 0, 4, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 8]
        ]
        self.assertEqual(new_board, expected_board)
        self.assertEqual(score, self.expected_score)

    def test_move_up(self):
        """Testaa laudan siirtoa ylöspäin"""
        new_board, score = move_up(self.board)
        expected_board = [
            [4, 4, 0, 8],
            [0, 4, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(new_board, expected_board)
        self.assertEqual(score, self.expected_score)


    def test_move_down(self):
        """Testaa laudan siirtoa alaspäin"""
        new_board, score = move_down(self.board)
        expected_board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 4, 0, 0],
            [4, 4, 0, 8]
        ]
        self.assertEqual(new_board, expected_board)
        self.assertEqual(score, self.expected_score)
