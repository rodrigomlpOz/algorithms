### Problem: Maze Solver (EPI 18.1)

We need to find a path through a maze starting from the bottom-left corner of the maze and ending at a specified point `(e)`. The maze is represented by a 2D grid where:
- `0` represents a passable path.
- `1` represents an obstacle.

The goal is to return a path from the starting point to the end point, or indicate that no path exists.

### High-Level Solution:

1. **DFS-Based Search**:
   - Use **depth-first search (DFS)** to explore the maze recursively, starting from the bottom-left corner.
   - Explore all four possible directions (up, down, left, right) from the current cell.

2. **Boundary and Validity Checks**:
   - Ensure that all recursive calls stay within the bounds of the maze.
   - Avoid revisiting already visited cells to prevent loops.
   - Skip over obstacles (cells with value `1`).

3. **Backtracking**:
   - If a path is found to be invalid (a dead end), backtrack by removing the last step and trying another direction.
   - Continue exploring until either a path is found or all possibilities are exhausted.

4. **Track Path and Visited Cells**:
   - Maintain a list to track the current path and a set to track visited cells.
   - When the end point is reached, return the path.

### Function Definition:

```python
def maze_solve(maze, e):
    """
    Finds a path from the bottom-left corner of the maze to the end point (e).
    
    :param maze: 2D list representing the maze, where 0 is a path and 1 is an obstacle.
    :param e: Tuple (x, y) representing the end point of the maze.
    """
    pass  # High-level logic explained above
```

### Function Calls:

#### Example 1:
```python
maze = [ 
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
]

maze_solve(maze, (0, len(maze[0]) - 1))  # Expected to find a valid path or indicate no path exists.
```

#### Example 2:
```python
maze = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 0, 1]
]

maze_solve(maze, (2, 2))  # Expected to find a valid path or indicate no path exists.
```

### Time Complexity:
- **Time Complexity**: O(n), where `n` is the total number of cells in the maze. Each cell is visited at most once.

### Space Complexity:
- **Space Complexity**: O(n), where `n` is the number of cells, due to the recursion stack and the space used to track visited cells and the path.
