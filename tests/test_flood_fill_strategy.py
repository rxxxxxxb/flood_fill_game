import unittest
from unittest.mock import patch
from src.flood_fill_strategy import FloodFillStrategy

class TestFloodFillStrategy(unittest.TestCase):
    
    def test_choose_random(self):
        board = [[0, 1], [2, 1]]
        strategy = FloodFillStrategy(board)
        with patch('random.randint', return_value=1):
            chosen_color = strategy.choose_random(3)
            self.assertEqual(chosen_color, 1)

if __name__ == '__main__':
    unittest.main()