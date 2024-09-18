def rotate_image(matrix):
    """
    Rotates the given n x n 2D matrix by 90 degrees clockwise in-place.

    Parameters:
    matrix (List[List[int]]): A 2D list representing the image to be rotated.

    Returns:
    None: The function modifies the input matrix directly.
    """
    n = len(matrix)  # Determine the size of the matrix (n x n)
    
    # Step 1: Reverse the order of the rows in the matrix.
    # This flips the matrix vertically.
    matrix.reverse()
    
    # Step 2: Transpose the matrix.
    # Transposing switches the element at position (i, j) with the element at (j, i).
    # This effectively mirrors the matrix over its main diagonal.
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
