import random
from src.board_generator import BoardGenerator


def main():
    """
    Main function to run the flood fill game. 
    """
    
    # Game configuration
    board_size = 6  # Board size (6 x 6)
    num_colors = 3  # Number of colors
    
    # Generate the board
    board_generator = BoardGenerator(board_size, num_colors)
    board = board_generator.generate_random_board()

    # Display the initial board
    board_generator.display_board(board)
        


if __name__ == "__main__":
    main()
    
    
    
    
    
    