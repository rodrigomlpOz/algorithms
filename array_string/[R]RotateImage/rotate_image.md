## Problem Statement

**Rotate Image**

You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

**Example:**
```
Input: matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Output: [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```

## High-Level Approach

1. **Reverse the Rows**: 
    - Reverse the order of the rows in the matrix.
    - This effectively performs a 90-degree rotation if the rows were treated as columns.

2. **Transpose the Matrix**:
    - Swap elements across the diagonal.
    - Iterate through the matrix, and for each element `(i, j)` where `i < j`, swap `matrix[i][j]` with `matrix[j][i]`.
    - This converts the reversed rows into the final rotated state.

## Function Signature

```python
def rotate_image(matrix):
    pass
```
