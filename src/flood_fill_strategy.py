import random

class FloodFillStrategy:
    """
    Implements flood fill strategies for selecting colors in a tile-based game.

    """    
    def __init__(self, board: list[list[int]]):
        """
        Initializes the FloodFillStrategy object with the provided game board.
        
        Parameters:
        -----------
        board : list of lists
            The game board represented as a 2D list where each value is a color (integer).
        """
    
        self.board_size = len(board)
        self.board = board
    
    def choose_random(self, num_colors: int) -> int:
        """
        Randomly selects a color from the available set of colors.
        
        Parameters:
        -----------
        num_colors : int
            The total number of available colors.
        
        Returns:
        --------
        int
            A random integer representing a color between 0 and num_colors - 1.
        """
        return random.randint(0, num_colors - 1) 
        
    def get_user_color_choice(self, num_colors, move_number):
        """
        Function to get and validate user input for color choice.
        
        Parameters:
        -----------
        num_colors: The total number of available colors.
        move_number: The current move number (for displaying in the prompt).

        Returns:
        --------
        The user's chosen color.
        """
        while True:
            try:
                new_color = int(input(f"Move {move_number}: Enter a color (0 to {num_colors - 1}): "))
                if 0 <= new_color < num_colors:
                    return new_color
                else:
                    print(f"Invalid input. Please enter a number between 0 and {num_colors - 1}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
    def _is_in_bounds(self, x, y):
        """
        Check if the given coordinates (x, y) are within the bounds of the board.

        Args:
            x (int): The x-coordinate (row index) of the tile.
            y (int): The y-coordinate (column index) of the tile.

        Returns:
            bool: True if the coordinates are within the board boundaries, 
        """ 
        return 0 <= x < self.board_size and 0 <= y < self.board_size            
    
    def choose_best_color(self, num_colors):
        """
        Choose the best color to maximize the number of connected tiles 
        adjacent to the origin (tile at position (0, 0)). 

        The algorithm uses a breadth-first search (BFS) to explore tiles 
        adjacent to the origin and counts how many neighboring tiles 
        share each color. It then greedily selects the color with the 
        maximum number of adjacent tiles. In case of a tie, it chooses 
        the color with the lowest numerical value.

        Args:
            num_colors (int): The total number of distinct colors on the board.

        Returns:
            int: The color (represented by an integer) that maximizes the 
                number of adjacent tiles connected to the origin. If there is 
                a tie, the color with the lowest rank is returned.
        """
        initial_tile_color = self.board[0][0]
        
        # Directional offsets to move (right, down, left, up)
        direction_offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        
        # Dictionary to store the count of adjacent colors and count 0 as default 
        color_count = {color: 0 for color in range(num_colors)}
        
        # Use a queue to perform a BFS-like approach to find adjacent tiles
        visited = set((0, 0)) # Marking the first tile as visited 
        queue = [(0, 0)]  # Adding the first tile in the queue 
        
        best_color = initial_tile_color 
        max_count = -1
        
        while queue:
            x, y = queue.pop(0)
            
            for dx, dy in direction_offsets:
                new_x, new_y = x + dx, y + dy
                
                if self._is_in_bounds(new_x, new_y) and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y)) 
                    adjacent_color = self.board[new_x][new_y]
                    
                    if adjacent_color != initial_tile_color:
                        color_count[adjacent_color] += 1
                    else:
                        queue.append((new_x, new_y)) 

        # Find the color with the maximum count
        for color, count in color_count.items():
            if count > max_count:
                best_color = color
                max_count = count
            elif count == max_count and color < best_color:
                best_color = color

        return best_color            
                
        