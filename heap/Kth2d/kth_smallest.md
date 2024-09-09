### Problem Statement:
Given a matrix where each row and column is sorted in ascending order, find the `k`-th smallest element in the matrix. The matrix dimensions are `n x n`.

### Example:
**Input:**
```python
matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
```

**Output:**
```
13
```

**Explanation:**
The elements of the matrix in sorted order are:  
`[1, 5, 9, 10, 11, 12, 13, 13, 15]`.  
The 8th smallest element is `13`.

---

### High-Level Solution Using a Min-Heap:

1. **Heap Initialization:**
   - Start by pushing the smallest element in the matrix (top-left corner) into a heap. This is because the matrix is sorted row-wise and column-wise, so this element will always be the smallest.
   - Track the position `(i, j)` of the element being pushed into the heap.

2. **Heap Operations:**
   - Pop the smallest element from the heap, which is the current smallest element in the matrix.
   - After removing an element from the heap:
     - If possible, push the next element from the same row into the heap.
     - If possible, push the element below the current element (from the next row) into the heap.
   - Repeat this process `k` times to find the `k`-th smallest element.

3. **Final Result:**
   - The element popped during the `k`-th iteration of the loop is the `k`-th smallest element in the matrix.

---

### High-Level Explanation:

1. **Matrix Structure:**
   - The matrix is sorted both row-wise and column-wise. This allows us to efficiently extract the smallest elements by using a heap.

2. **Heap Operations:**
   - Initially, the smallest element `matrix[0][0]` is pushed into the heap.
   - For every smallest element popped from the heap, we explore the next possible elements:
     - The element to the right in the same row.
     - The element directly below in the same column.
   - We continue this process until we find the `k`-th smallest element.

3. **Final Answer:**
   - The element popped during the `k`-th iteration of the loop is the `k`-th smallest element in the matrix.

---

### Time Complexity:
- **Pushing and popping from the heap:** Each push and pop operation takes **O(log m)**, where `m` is the number of elements in the heap. Since at most `2k` elements can be pushed to the heap (one for each row and column combination), the complexity of heap operations is **O(k log k)**.
  
- **Total Complexity:**  
  The time complexity is **O(k log k)**, which is efficient given the constraints of the problem.

### Space Complexity:
- The space complexity is **O(k)**, since at most `k` elements are in the heap at any given time.

This approach ensures efficient extraction of the `k`-th smallest element in a sorted matrix using a heap.
