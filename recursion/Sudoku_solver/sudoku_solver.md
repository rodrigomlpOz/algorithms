### Problem Statement

Write a function to solve a 9x9 Sudoku puzzle. The Sudoku board is a 2D list of characters where empty cells are represented by the character `'.'`. The function should modify the board in place to fill in the solution according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine 3x3 sub-grids must contain the digits `1-9` without repetition.

You may assume that the given Sudoku puzzle is valid and has only one solution.

### Function Definition

```python
def solveSudoku(board):
    """
    Solves the given Sudoku puzzle in place.
    
    Args:
    board (List[List[str]]): A 2D list representing the Sudoku board where 
                             '.' indicates an empty cell.
                             
    Returns:
    None: The board is modified in place with the solution.
    """
    pass  # Implementation goes here
```

### Example Function Calls

```python
# Example 1
sudoku_board_1 = [
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

solveSudoku(sudoku_board_1)
for row in sudoku_board_1:
    print(row)
# The board should now be completely filled with the correct solution.

# Example 2
sudoku_board_2 = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."]
]

solveSudoku(sudoku_board_2)
for row in sudoku_board_2:
    print(row)
# The board should now be completely filled with the correct solution.
```

### Requirements:
- Modify the given Sudoku board in place.
- Ensure the solution adheres to all Sudoku rules (row, column, and sub-grid constraints).