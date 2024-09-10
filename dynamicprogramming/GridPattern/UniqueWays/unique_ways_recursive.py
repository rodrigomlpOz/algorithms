def uniquePaths(m, n):
    """
    Recursive function to calculate the number of unique paths in an m x n grid.

    Args:
    m : int : Number of rows in the grid.
    n : int : Number of columns in the grid.

    Returns:
    int : The number of unique paths from top-left to bottom-right.
    """
    # Base Case: If there's only one row or one column, there's only one path (all right or all down)
    if m == 1 or n == 1:
        return 1

    # Recursive Case: The total number of unique paths is the sum of the unique paths from
    # the cell above (m-1, n) and the cell to the left (m, n-1).
    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)

# Example test
m = 3
n = 3
print(uniquePaths(m, n))  # Output: 6
