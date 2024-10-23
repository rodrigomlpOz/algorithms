### Problem Statement
Given an array `nums` of integers and an integer `k`, which represents the size of a sliding window, find the maximum value in each sliding window of size `k` as the window moves from left to right across the array.

### Function Definition
```python
def maxSlidingWindowHeap(nums, k):
    """
    Finds the maximum value in each sliding window of size k using a max-heap.
    
    Args:
    nums (List[int]): The list of integers.
    k (int): The size of the sliding window.
    
    Returns:
    List[int]: A list containing the maximum values for each sliding window.
    """
```

### Function Call Examples
```python
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindowHeap(nums, k))  # Expected output: [3, 3, 5, 5, 6, 7]
```

### High-Level Solution
1. **Edge Case Handling**: If `nums` is empty or `k` is zero, return an empty list.
2. **Heap Initialization**: Use a max-heap (implemented with negative values to simulate max behavior using Python's `heapq`, which is a min-heap by default) to store the values along with their indices.
3. **Iterate Over the Array**:
   - Push each element onto the heap with its negative value to maintain max-heap behavior.
   - Remove elements from the heap if their indices fall outside the current sliding window.
   - Once the sliding window is fully within bounds (when `i >= k - 1`), add the maximum element (negating the top of the heap) to the result list.
4. **Return the Result List**: After processing all elements, the list contains the maximum values for each sliding window.

This approach ensures efficient management of the heap for dynamic maximum retrieval as the sliding window progresses through the array.
