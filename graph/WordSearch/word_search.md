### Problem: Word Search (Leetcode 79)

The goal is to determine if a given word exists in a 2D grid of characters. You can construct the word by moving horizontally or vertically, but you cannot revisit the same cell more than once in the current search path.

### Problem Definition:
- **Input**:
  - A 2D board of characters.
  - A word that needs to be found in the board.
  
- **Output**:
  - Return `True` if the word exists in the board, otherwise return `False`.

### High-Level Solution:

1. **Depth-First Search (DFS)**:
   - We can use DFS to search for the word starting from every cell in the grid. For each character in the word, we recursively explore its neighboring cells (up, down, left, right) to see if the remaining portion of the word can be constructed.

2. **Boundary and Character Match Check**:
   - At each step of the recursion, ensure that the current cell contains the expected character from the word.
   - Also, ensure that we don't go out of bounds or revisit a cell that has already been used in the current search path.

3. **Backtracking**:
   - To avoid revisiting the same cell in the current path, we mark the cell as visited by replacing its value temporarily (e.g., with a special character like `'*'`).
   - After exploring all possible directions, we restore the original value of the cell to ensure other paths can use it if needed.

4. **Starting DFS From Every Cell**:
   - Since the word can start from any cell, we initiate a DFS search from every cell in the grid.

### Function Definition:

```python
def word_search(board, word):
    """
    Determines if the word exists in the 2D board by searching horizontally or vertically.
    
    :param board: 2D list of characters representing the grid.
    :param word: The word to be found.
    :return: True if the word exists in the board, otherwise False.
    """
    pass  # High-level logic explained above
```

### Steps in the Solution:

1. **DFS Function**:
   - This recursive function checks if the current cell matches the first character of the word and then explores the neighboring cells for the rest of the word.

2. **Exploring Directions**:
   - From each cell, move in four possible directions: up, down, left, and right. For each valid direction, continue the DFS search for the remaining characters in the word.

3. **Backtracking**:
   - Mark the cell as visited by replacing its value with a temporary marker (e.g., `'*'`) and restore it after the recursive calls.

4. **Main Loop**:
   - Start a DFS search from each cell in the board. If the DFS finds the word, return `True`. If no valid path is found after all DFS calls, return `False`.

### Function Calls:

#### Example 1:
```python
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"

ans = word_search(board, word)
print(ans)  # Expected Output: False
```

#### Example 2:
```python
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "SEE"

ans = word_search(board, word)
print(ans)  # Expected Output: True
```

### Time Complexity:
- **Time Complexity**: O(N * M * 4^L), where:
  - **N** is the number of rows in the board.
  - **M** is the number of columns in the board.
  - **L** is the length of the word.
  - At each cell, there are up to 4 possible directions to explore, and we do this for each letter in the word.

### Space Complexity:
- **Space Complexity**: O(L), where **L** is the length of the word. This accounts for the recursion stack depth, which will be at most the length of the word.

This approach efficiently uses DFS and backtracking to determine whether the word can be found in the board.
