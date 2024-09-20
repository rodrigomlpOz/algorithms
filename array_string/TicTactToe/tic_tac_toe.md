## Problem Statement

**Design Tic-Tac-Toe**

Design a `TicTacToe` class that allows players to play the Tic-Tac-Toe game on an `n x n` board. The class should be able to initialize the board and handle a player's move, updating the board state, and checking if there's a winner after each move.

**Example:**
```
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
```

## High-Level Approach

1. **Initialize Data Structures**:
    - Create variables to store the sum of moves for each row, each column, and the two diagonals.
    - Initialize these variables in the constructor.

2. **Handle Player Move**:
    - For each move, update the corresponding row, column, and possibly diagonal sums based on the player's move.
    - Use `+1` for player 1 and `-1` for player 2 to track the sums.
    - After updating, check if the absolute value of any of these sums equals `n`, which indicates a win.

3. **Return the Result**:
    - If a win condition is met, return the player number.
    - If no win condition is met, return 0 indicating no one wins yet.

## Function Signature

```python
class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        pass

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        pass

toe = TicTacToe(3)

toe.move(0, 0, 1)  # Returns 0 (no one wins)
toe.move(0, 2, 2)  # Returns 0 (no one wins)
toe.move(2, 2, 1)  # Returns 0 (no one wins)
toe.move(1, 1, 2)  # Returns 0 (no one wins)
toe.move(2, 0, 1)  # Returns 0 (no one wins)
toe.move(1, 0, 2)  # Returns 0 (no one wins)
toe.move(2, 1, 1)  # Returns 1 (player 1 wins)

```
