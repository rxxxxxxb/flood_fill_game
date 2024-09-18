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
                
    