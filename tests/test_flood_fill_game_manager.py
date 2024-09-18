import unittest
from src.flood_fill_game_manager import FloodFillGameManager

class TestFloodFillGame(unittest.TestCase):
    
    def test_is_solved(self):
        board_solved = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        board_unsolved = [[1, 1, 1, 2], [1, 1, 1, 0], [1, 1, 3, 1], [1, 1, 1, 1]]
        game_solved = FloodFillGameManager(board_solved)
        game_unsolved = FloodFillGameManager(board_unsolved)
        self.assertTrue(game_solved.is_solved())
        self.assertFalse(game_unsolved.is_solved())

    def test_flood_fill(self):
        board = [[0, 0, 0], [1, 1, 1]]
        game = FloodFillGameManager(board)
        game.play_move(1)
        expected_board = [[1, 1, 0], [1, 1, 1]]
        self.assertEqual(game.board, expected_board)

if __name__ == '__main__':
    unittest.main()