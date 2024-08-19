### Problem Description
Given a 2D binary matrix `matrix`, where each row is sorted in non-decreasing order (i.e., all 0s appear before 1s), your task is to find the index of the leftmost column that contains a 1. If there is no such column, return `inf`.

The matrix is structured such that:
- Each element is either 0 or 1.
- Each row is sorted, with 0s on the left and 1s on the right.

### Function Definitions
1. **`def binarySearch(A: List[int]) -> int:`**  
   This function performs a binary search on a sorted list `A` to find the leftmost index of the target value `1`. If `1` is found, it returns the index; otherwise, it returns an index indicating where `1` would be if it existed.

2. **`def leftmost_one(matrix: List[List[int]]) -> int:`**  
   This function takes a 2D binary matrix as input and iterates through each row, using the `binarySearch` function to determine the leftmost index of `1` across all rows. It returns the smallest index where `1` appears in the matrix.

### Function Calls
```python
# Example usage:
matrix = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 1]
]

result = leftmost_one(matrix)
print(result)  # Output should indicate the leftmost column with 1.
```

### High-Level Approach
1. **Binary Search (`binarySearch` function):**
   - The goal of this function is to efficiently locate the first occurrence of `1` in a sorted row using binary search.
   - By iterating while `lo < hi`, the mid-point is calculated, and the search space is adjusted depending on whether the mid value is less than the target (`1`) or not.
   - The loop narrows down the search until it finds the smallest index where `1` appears.

2. **Iterating Over Rows (`leftmost_one` function):**
   - The matrix is processed row-by-row.
   - For each row, the `binarySearch` function is used to determine the leftmost index of `1`.
   - The minimum index among all rows is tracked to find the leftmost column containing `1`.

3. **Edge Cases to Consider:**
   - The matrix may contain only `0`s.
   - There could be rows with no `1`s, which need to be handled appropriately.

This approach leverages binary search to efficiently locate the first `1` in each row, making the overall solution more optimized compared to a simple linear search.
