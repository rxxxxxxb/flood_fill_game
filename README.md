# The Flood Fill Game :

The Flood Fill Game is played on a square board with colored tiles. The goal is to change the color of the entire board to a single color. You start from the top-left corner and can change the color of the tiles connected to that corner by choosing a new color. Each time you pick a color, all the connected tiles with the same color as the top-left corner will change to the new color you chose. The game continues until all the tiles on the board are the same color. 

The challenge is to do this in as few moves as possible!

> Basically, It works similarly to a paint-bucket tool in MS paint, which changes all connected areas of the same color to a new color.


## Approach :
We will use 3 classes :
- Generating the board
- Responsible for running and checking the game 
- Responsible for the strategy 

## To-Do :
- Make a flood-fill-solver algorithm 