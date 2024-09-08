### Problem: Sort Approximately Sorted Array

We are tasked with sorting an approximately sorted array, where every element is at most **K** positions away from its final sorted position. In other words, the array is nearly sorted, and we need to sort it efficiently.

### High-Level Solution:

1. **Heap Approach**:
   - The key observation here is that any element in the array can only be misplaced by at most **K** positions. This allows us to maintain a **min-heap** of size **K** to always keep track of the smallest elements that might need to be placed in their correct position.
   
2. **Step-by-Step Solution**:
   - First, initialize a **min-heap** with the first **K** elements of the sequence. These **K** elements are the candidates for the smallest element in the final sorted order.
   
   - After the heap is initialized, for each new element in the sequence, push it into the heap and pop the smallest element. The popped element is guaranteed to be in its correct position because the heap always contains **K** elements, and the new element we push ensures that no elements are misplaced by more than **K** positions.
   
   - Once the sequence is exhausted, we extract all the remaining elements from the heap and append them to the result. These elements are the largest remaining in sorted order.

3. **Final Sorted List**:
   - The result list will contain the sorted sequence once all the heap operations are complete.

### Time Complexity:
- **Heap Initialization**: O(K) to build a heap of size **K**.
- **Processing Remaining Elements**: For each of the remaining **n - K** elements, we push an element into the heap and pop the smallest element, each taking **O(log K)** time. This step takes **O((n - K) * log K)**.
- **Total Time Complexity**: O((n - K) * log K + K * log K) ≈ O(n * log K), where **n** is the total number of elements in the sequence.

### Space Complexity:
- **Space Complexity**: O(K), since the heap size is maintained at **K** at any given point.

### Function Definition:

```python
import heapq

def sort_approximately_sorted_array(sequence, k):
    """
    Sorts a nearly sorted sequence where each element is at most K positions 
    away from its sorted position.
    
    :param sequence: List of elements in the approximately sorted array.
    :param k: Maximum distance an element is displaced from its sorted position.
    :return: A fully sorted list.
    """
    pass  # High-level logic explained above
```

### Function Calls:

#### Example 1:
```python
sequence = [3, -1, 2, 6, 4, 5, 8]
k = 2

# Expected Output: [-1, 2, 3, 4, 5, 6, 8]
```

#### Example 2:
```python
sequence = [10, 9, 8, 7, 4, 70, 60, 50]
k = 4

# Expected Output: [4, 7, 8, 9, 10, 50, 60, 70]
```

### How It Works:
- By using a heap of size **K**, we ensure that every element pushed into the result is the smallest possible one that is guaranteed to be in the correct position.
- As we process the sequence and maintain a heap, the output is progressively built in sorted order, and we finalize by extracting any leftover elements from the heap.
