import random
from src.flood_fill_strategy import FloodFillStrategy
from src.flood_fill_game_manager import FloodFillGameManager
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

    game = FloodFillGameManager(board)

    # Display the initial board
    board_generator.display_board(board)
    
    # Initialize solcing strategy 
    strategy = FloodFillStrategy(board)

    moves = 0

    while not game.is_solved():
        moves += 1
        
        # Get user input for the new color
        # new_color = strategy.choose_random(num_colors) # Choose random for simplicity 
        # new_color = strategy.get_user_color_choice(num_colors,moves)
        new_color = strategy.choose_best_color(num_colors)

        # Play the move and update the board
        game.play_move(new_color)
        board_generator.display_board(board)

    print(f"Game solved in {moves} moves!")


if __name__ == "__main__":
    main()