### Problem Statement: Game of Life

**Problem Description:**

The Game of Life is a cellular automaton devised by the mathematician John Horton Conway. Given a board with `m x n` cells, each cell has an initial state: live (represented by `1`) or dead (represented by `0`). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following rules:

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying these rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the `m x n` grid board, return the next state.

**Constraints:**

- `m == board.length`
- `n == board[i].length`
- 1 <= m, n <= 25
- `board[i][j]` is `0` or `1`.

def game_of_life(board):
    """
    Updates the board to the next state according to the Game of Life rules.
    """
    pass

Here's the requested structure with only function definitions and function calls, no implementation:

### Function Definitions:

```python
def count_neighbours(board, row, col):
    """
    Counts the number of live neighbors around the cell at position (row, col).
    """
    pass

def game_of_life(board):
    """
    Updates the board to the next state according to the Game of Life rules.
    """
    pass
```

### Function Calls:

```python
# Example board
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

# Call the game_of_life function to update the board
game_of_life(board)

# Call count_neighbours for an example position
count_neighbours(board, 1, 1)
```
### High-Level Approach

1. **State Definitions:**
   - `DEAD = 0`: Cell is initially dead.
   - `ALIVE = 1`: Cell is initially alive.
   - `ALIVE_TO_DEAD = 2`: Cell was alive but will die in the next state.
   - `DEAD_TO_ALIVE = 3`: Cell was dead but will become alive in the next state.

2. **Neighbor Count Function:**
   - Define a function `count_neighbours` to count live neighbors around a given cell.
   - Use a list of direction tuples to check all eight possible neighbors.

3. **Update Board States:**
   - Iterate through each cell in the board.
   - Apply the rules of the Game of Life to determine the next state of each cell, using `ALIVE_TO_DEAD` and `DEAD_TO_ALIVE` to track changes.

4. **Finalize States:**
   - Iterate through the board again to finalize the states: convert `ALIVE_TO_DEAD` to `DEAD` and `DEAD_TO_ALIVE` to `ALIVE`.
