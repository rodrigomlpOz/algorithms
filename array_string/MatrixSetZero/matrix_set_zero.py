from types import List

def setZeroes(matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    # Step 1: Determine if the first row or first column needs to be zero
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Step 2: Use the first row and column as markers for other rows and columns
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Step 3: Set matrix cells to zero based on the markers
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(1, cols):
                matrix[i][j] = 0

    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(1, rows):
                matrix[i][j] = 0

    # Step 4: Handle the first row and first column separately
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0