from typing import List


class FloodFillGameManager:
    def __init__(self, board: List[List[int]]):
        """
        Initialize the flood fill game manager with the given board.
        
        :param board: The board to solve.
        """
        self.board = board
        self.n = len(board)

    def _is_in_bounds(self, x: int, y: int) -> bool:
        """
        Check if a given coordinate is within the bounds of the board.
        
        :param x: Row index.
        :param y: Column index.
        :return: True if (x, y) is within the bounds of the board, False otherwise.
        """
        return 0 <= x < self.n and 0 <= y < self.n


    def play_move(self, new_color: int):
        """
        Make a move by choosing a new color, which changes the connected region
        of tiles starting from the origin (0, 0).
        
        :param new_color: The color to change the connected region to.
        """
        origin_color = self.board[0][0]
        if origin_color != new_color:
            self._flood_fill(0, 0, origin_color, new_color)

    def is_solved(self) -> bool:
        """
        Check if the entire board has been filled with the same color.
        
        :return: True if the board is fully solved (all tiles have the same color).
        """
        first_color = self.board[0][0]
        return all(tile == first_color for row in self.board for tile in row)
    
    def _flood_fill(self, x: int, y: int, original_color: int, new_color: int):
        """
        Perform the flood fill algorithm starting from (x, y), changing the color from
        original_color to new_color on connected tiles.
        
        :param x: Row index of the starting tile.
        :param y: Column index of the starting tile.
        :param original_color: The original color that will be changed.
        :param new_color: The color to change the connected tiles to.
        """
        # If out of bounds or the color does not match the original color, return
        if not self._is_in_bounds(x, y) or self.board[x][y] != original_color:
            return
        
        # Change the color
        self.board[x][y] = new_color
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            dx, dy = direction 
            new_x = x + dx
            new_y = y + dy
            if self._is_in_bounds(new_x, new_y):
                 if self.board[new_x][new_y] == original_color:
                     self._flood_fill(new_x, new_y, original_color, new_color)
