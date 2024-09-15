import unittest
from unittest.mock import patch
from src.board_generator import BoardGenerator


class TestBoardGenerator(unittest.TestCase):
    
    def test_generate_random_board(self):
        n, m = 6, 3
        board_generator = BoardGenerator(n, m)
        board = board_generator.generate_random_board()
        self.assertEqual(len(board), n)
        self.assertTrue(all(len(row) == n for row in board))
        for row in board:
            for tile in row:
                self.assertTrue(0 <= tile < m)
    
    @patch('builtins.print')
    def test_display_board_6x6(self, mock_print):
        board = [
            [0, 1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1, 0]
        ]
        BoardGenerator.display_board(board)
        mock_print.assert_any_call("\nCurrent board state:")
        mock_print.assert_any_call("0 1 2 3 4 5")
        mock_print.assert_any_call("5 4 3 2 1 0")

    @patch('builtins.print')
    def test_display_board(self, mock_print):
        board = [[0, 1], [2, 1]]
        BoardGenerator.display_board(board)
        mock_print.assert_any_call("\nCurrent board state:")
        mock_print.assert_any_call("0 1")
        mock_print.assert_any_call("2 1")

if __name__ == '__main__':
    unittest.main()