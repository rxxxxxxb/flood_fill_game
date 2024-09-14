import random
from typing import List


class BoardGenerator:
    def __init__(self, n: int, m: int):
        """
        Initialize the board generator with a given size and number of colors.
        
        :param n: The size of the board (n x n).
        :param m: The number of distinct colors.
        """
        self.n = n
        self.m = m

    def generate_random_board(self) -> List[List[int]]:
        """
        Generate a random board with n x n tiles and m distinct colors.
        
        :return: A 2D list representing the board with random colors.
        """
        board = []
    
        for _ in range(self.n):
            row = [
                random.randint(0, self.m - 1)  # Assign a random color (0 to m-1) for each tile
                for _ in range(self.n)          # Generate 'n' columns for each row
            ]
            board.append(row)
                
        return board
    
    @staticmethod
    def display_board(board: List[List[int]]):
        """
        Display the current state of the game board.
        
        :param board: The board to display.
        """
        print("\nCurrent board state:")
        for row in board:
            print(" ".join(str(tile) for tile in row))
        