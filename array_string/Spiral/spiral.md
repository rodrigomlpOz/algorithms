## Problem Statement

**Spiral Order of a 2D Array**

Given a 2D array (matrix), return all elements of the matrix in spiral order.

**Example:**
```
Input: matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

## High-Level Approach

1. **Initialize Variables**: 
    - Create a list of directions representing right, down, left, and up movements.
    - Check if the matrix is empty, return an empty list if true.
    - Initialize starting coordinates `(x, y)` at the top-left of the matrix.
    - Initialize `curr_dir` to track the current direction index.
    - Initialize an empty list `ans` to store the spiral order.

2. **Traverse the Matrix**:
    - Calculate the total number of elements in the matrix.
    - Iterate through the matrix for the total number of elements:
        - Append the current element to the `ans` list.
        - Mark the current element as visited by setting it to a sentinel value (e.g., negative infinity).
        - Calculate the next coordinates using the current direction.
        - If the next coordinates are within bounds and the next cell is not visited, update the current coordinates.
        - If the next cell is out of bounds or already visited, change the direction and update the coordinates accordingly.

3. **Return the Result**:
    - Return the `ans` list containing elements in spiral order.

## Function Signature

```python
def spiral(matrix):
    pass
```
