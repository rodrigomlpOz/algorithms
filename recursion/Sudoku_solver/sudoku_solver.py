def solveSudoku(board):
    def isValid(board, row, col, num):
        # Check if 'num' is not in the current row
        for i in range(9):
            if board[row][i] == num:
                return False

        # Check if 'num' is not in the current column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check if 'num' is not in the current 3x3 box
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_row_start + i][box_col_start + j] == num:
                    return False

        return True

    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    # Try placing numbers 1-9
                    for num in '123456789':
                        if isValid(board, row, col, num):
                            board[row][col] = num
                            # Recursively try to solve the rest of the board
                            if solve(board):
                                return True
                            # Backtrack if the solution is not valid
                            board[row][col] = '.'
                    return False
        return True

    # Start solving the Sudoku
    solve(board)

# Example usage
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solveSudoku(sudoku_board)
for row in sudoku_board:
    print(row)
