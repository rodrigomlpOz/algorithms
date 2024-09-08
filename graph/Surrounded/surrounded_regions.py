def paint(maze, x, y):
    """
    Modifies the given 2D grid by flipping surrounded 'O' regions to 'X'.
    
    :param maze: A 2D list where 'X' represents a wall and 'O' represents regions that could be flipped.
    :param x: The starting x-coordinate (not necessary for this solution but kept for context).
    :param y: The starting y-coordinate (not necessary for this solution but kept for context).
    """
    
    def explore(maze, x, y):
        """
        Perform DFS to mark all 'O' cells connected to the current 'O' cell.

        :param maze: The 2D grid representing the board.
        :param x: The current row index.
        :param y: The current column index.
        """
        # If the current cell is out of bounds or not 'O', stop the exploration.
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == "O"):
            return
        # Mark the current 'O' cell as visited by setting it to 'S'.
        maze[x][y] = "S"
        
        # Explore all 4 possible directions (right, down, left, up) from the current cell.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dir in directions:
            explore(maze, x + dir[0], y + dir[1])
    
    # Get the dimensions of the board.
    num_rows, num_cols = len(maze), len(maze[0])
    
    # Step 1: Mark all 'O' cells connected to the boundary.
    # Explore from the first and last column for every row.
    for i in range(num_rows):
        if maze[i][0] == "O":
            explore(maze, i, 0)  # Left boundary.
        if maze[i][num_cols - 1] == "O":
            explore(maze, i, num_cols - 1)  # Right boundary.
    
    # Explore from the first and last row for every column.
    for j in range(num_cols):
        if maze[0][j] == "O":
            explore(maze, 0, j)  # Top boundary.
        if maze[num_rows - 1][j] == "O":
            explore(maze, num_rows - 1, j)  # Bottom boundary.
    
    # Step 2: Flip all remaining 'O' cells to 'X' (since they are surrounded).
    for i in range(num_rows):
        for j in range(num_cols):
            if maze[i][j] == "O":
                maze[i][j] = "X"  # Flip surrounded 'O' to 'X'.
    
    # Step 3: Revert the marked 'S' cells back to 'O' (as they are boundary-connected).
    for i in range(num_rows):
        for j in range(num_cols):
            if maze[i][j] == "S":
                maze[i][j] = "O"  # Restore boundary-connected cells.

    print("hello")
