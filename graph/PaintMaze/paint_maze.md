### Problem: Paint the Maze (EPI 18.2)

The task is to change the color of a connected region in a 2D matrix (maze) starting from a given point `(x, y)`. The region consists of all cells that are connected either horizontally or vertically and have the same initial color as the cell at `(x, y)`.

<img width="643" alt="image" src="https://github.com/user-attachments/assets/5e402a7c-d185-4492-8bd5-17a04fbe8f64">


### High-Level Solution:

1. **Identify the Region**:
   - The region is composed of cells connected either horizontally or vertically that share the same initial color as the starting point.

2. **Recursive Flood Fill**:
   - We perform a recursive depth-first search (DFS) from the given point `(x, y)` to explore the entire connected region. As we explore, we change the color of each cell in the region to the opposite color.
   - We need to stop the recursion when we either hit a boundary of the maze or encounter a cell that does not belong to the region (i.e., a cell that has a different color).

3. **Check Four Directions**:
   - From any cell, we can move to its neighbors in four possible directions: up, down, left, and right. We recursively apply the color change to any neighboring cell that shares the same initial color.

### Function Definition:

```python
def paint(maze, x, y):
    """
    Changes the color of the region starting from the point (x, y) in the maze.
    
    :param maze: A 2D matrix representing the maze, where 0 and 1 are different colors.
    :param x: The row index from where painting starts.
    :param y: The column index from where painting starts.
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
    [0, 0, 1, 0]
]

paint(maze, len(maze) - 1, 0)

# Expected Output: The maze will be painted, and changes will be made to connected regions starting at (3, 0).
```

#### Example 2:
```python
maze = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 0, 1]
]

paint(maze, 0, 1)

# Expected Output: The region starting from (0, 1) and connected to other 0's will change color.
```

### Time Complexity:
- **Time Complexity**: O(n), where `n` is the number of cells in the maze. Each cell is visited at most once.
  
### Space Complexity:
- **Space Complexity**: O(n), due to the recursive call stack when visiting each cell in the region.
