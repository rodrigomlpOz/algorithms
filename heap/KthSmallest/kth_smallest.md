### Problem: Find the Kth Smallest Element in an Array

We are tasked with finding the **Kth smallest element** in an unsorted array. One efficient way to solve this problem is by utilizing a **heap**.

### High-Level Solution:

1. **Using a Max-Heap**:
   - The idea is to maintain a **max-heap** of size **K** that holds the smallest **K** elements from the array.
   - As we traverse the array, for each new element, we check if it is smaller than the largest element in the heap (the root of the heap).
   - If the new element is smaller, we remove the largest element (root of the heap) and insert the new element into the heap.
   - After processing all elements, the largest element in the heap will be the Kth smallest element in the array.

2. **Using Python's Min-Heap**:
   - Python’s `heapq` implements a **min-heap** by default. To adapt this for the **Kth smallest element**, we can:
     - Add the first **K** elements of the array into the heap.
     - For each subsequent element, if it is smaller than the largest element in the heap, we replace the largest element with the new one (using `heappushpop()`).
   - Once all elements are processed, the root of the heap contains the Kth smallest element.

### Solution Outline:

1. **Heap Initialization**:
   - First, insert the first **K** elements from the array into a heap. This can be done in **O(K)** time.

2. **Heap Maintenance**:
   - For each of the remaining elements in the array (from index **K** onwards), compare the element with the root of the heap:
     - If the element is larger, it does not affect the K smallest elements, so we skip it.
     - If the element is smaller than the largest element in the heap, replace the root with this element.
   - This step takes **O(log K)** time for each of the remaining elements in the array.

3. **Final Result**:
   - Once all elements have been processed, the root of the heap contains the Kth smallest element.

### Time Complexity:
- **Heap Initialization**: O(K) to build a heap with the first **K** elements.
- **Processing Remaining Elements**: O((n - K) * log K), where **n** is the size of the array and **K** is the size of the heap. Each operation on the heap (push or pop) takes **O(log K)** time.
- **Total Time Complexity**: O(K + (n - K) * log K), which simplifies to **O(n * log K)**.

### Space Complexity:
- **Space Complexity**: O(K), since we are maintaining a heap of size **K** at any given time.

### Function Calls:

#### Example 1:
```python
arr = [12, 3, 5, 7, 19]
k = 2

# The 2nd smallest element is 5
# Expected Output: 5
```

#### Example 2:
```python
arr = [1, 23, 12, 9, 30, 2, 50]
k = 3

# The 3rd smallest element is 9
# Expected Output: 9
```
