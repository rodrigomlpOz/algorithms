class TicTacToe:
    '''
    Example:
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
    '''

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row = [0] * self.n # row sum
        self.col = [0] * self.n # column sum
        self.diag = 0 # diagonal sum, x=y
        self.rev_diag = 0 # reversed diagonal sum, y = -x + n - 1

    def move(self, row, col, player):
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
        move = 1 if player==1 else -1
        self.row[row] += move # update row sum
        self.col[col] += move # update column sum
        if row == col: # if diagonal, x = y
            self.diag += move # update diagonal sum
        if self.n - 1 - row == col: # if reversed diagonal, y = -x + n - 1
            self.rev_diag += move # update reversed diagonal sum
        if (abs(self.rev_diag) == self.n or abs(self.diag) == self.n or abs(self.row[row]) == self.n) or (abs(self.col[col]) == self.n):
            return player
        return 0