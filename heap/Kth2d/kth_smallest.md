**Problem Statement:**

Given an n x n matrix where each row and each column is sorted in ascending order, find the k-th smallest element in the matrix.

**Example:**

```python
Input:
matrix = [
   [1, 5, 9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

Output:
13

Explanation: The elements of the matrix in sorted order are [1, 5, 9, 10, 11, 12, 13, 13, 15].
```

---

**Function Definition:**

```python
def kthSmallest(matrix, k):
    """
    Finds the k-th smallest element in a n x n sorted matrix.

    Args:
    matrix (List[List[int]]): The n x n matrix with sorted rows and columns.
    k (int): The order of the smallest element to find.

    Returns:
    int: The k-th smallest element in the matrix.
    """
    # Implementation goes here
```

---

**Function Calls:**

```python
# Example usage:
matrix = [
   [1, 5, 9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

print(kthSmallest(matrix, k))  # Output should be 13
```

---

**High-Level Solution:**

To solve this problem efficiently, we can utilize the properties of the sorted matrix. Here are two common approaches:

### 1. Min-Heap Approach

**Idea:**

- Use a min-heap to keep track of the smallest elements.
- Initially, insert the first element of each row into the heap.
- Extract the minimum element from the heap k times.

**Algorithm:**

1. Initialize a min-heap.
2. Insert the first element of each row into the heap along with its coordinates (row and column indices).
3. Initialize a counter to keep track of the number of elements extracted.
4. While the counter is less than k:
   - Extract the smallest element from the heap.
   - Increment the counter.
   - If there is a next element in the same row, insert it into the heap.
5. After k extractions, the last extracted element is the k-th smallest.

**Time Complexity:** O(k log n), where n is the number of rows (since the heap size is at most n).

**Space Complexity:** O(n), for storing elements in the heap.
