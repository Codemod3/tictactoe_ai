<h1 align center>  Tictactoe project </h1>
<h2>This program uses the minimax algorithm to make sure the computer never loses<br></h2>

## Understanding
There are two main files in this project: runner.py and tictactoe.py. tictactoe.py contains all of the logic for playing the game, and for making optimal moves. runner.py contains all of the code to run the graphical interface for the game. Once you have run the runner.py you will be able to play against your AI! <br>

The function initial_state returns the starting state of the board. For this problem, we’ve chosen to represent the board as a list of three lists (representing the three rows of the board), where each internal list contains three values that are either X, O, or EMPTY.

## Function description

<ul> The player function takes a board state as input, and return which player’s turn it is (either X or O).
<li>In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.</li>
<li>Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).</li></ul><br>
  
<ul>
The actions function returns a set of all of the possible actions that can be taken on a given board.
<li>Each action represents a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).</li>
<li>Possible moves are any cells on the board that do not already have an X or an O in them.</li>
</ul><br>

<ul>
The result function takes a board and an action as input, and returns a new board state, without modifying the original board.
<li>If action is not a valid action for the board,exception is raised.</li>
<li>The returned board is the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.</li>
<li>Importantly, the original board is left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. So a deep copy of the board is made.
</li>
</ul><br>

<ul>The winner function accepts a board as input, and return the winner of the board if there is one.
<li>If the X player has won the game, function returns X. If the O player has won the game, function returns O.</li>
<li>One can win the game with three of their moves in a row horizontally, vertically, or diagonally.</li>
<li>If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function returns None.</li></ul>
<br>
<ul>  
The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.
<li>If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function returns True.</li>
<li>Otherwise, the function returns False if the game is still in progress.</li>
</ul>
  <br>
<ul>The utility function accepts a terminal board as input and output the utility of the board.
<li>If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.</li>
<li>Utility will only be called on a board if terminal(board) is True.</li>
</ul>
  <br>
<ul>The minimax function takes a board as input, and return the optimal move for the player to move on that board.
<li>The move returned is the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.</li>
<li>If the board is a terminal board, the minimax function returns None.</li></ul><br>
