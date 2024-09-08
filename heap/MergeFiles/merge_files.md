### Problem: Merging Multiple Sorted Arrays

We are tasked with merging multiple sorted arrays into one fully sorted array. A direct approach of concatenating all arrays and sorting them would be inefficient, so we can use a **heap-based approach** for optimal efficiency.

### High-Level Solution:

1. **Heap for Merging Sorted Arrays**:
   - We can think of each sorted array as a **stream of numbers**. To merge these streams efficiently, we use a **min-heap** to keep track of the smallest current element from each array.
   - The heap allows us to repeatedly extract the smallest element across all arrays in **O(log k)** time, where **k** is the number of arrays.

2. **Step-by-Step Solution**:
   - First, initialize a heap that stores the first element of each sorted array along with the index of the array it came from.
   - Then, repeatedly extract the smallest element from the heap (this is the next element in the merged array) and insert the next element from the same array into the heap.
   - Continue this process until all elements from all arrays have been processed.

3. **Final Merged List**:
   - The result is a sorted list containing all elements from all arrays merged into a single list.

### Solution Outline:

1. **Initialize Iterators**:
   - Create an iterator for each array to sequentially fetch elements.

2. **Heap Initialization**:
   - Add the first element of each array (if it exists) to the min-heap. The heap stores tuples of the form `(value, array_index)`, where `value` is the current element, and `array_index` tracks which array the element came from.

3. **Merge Process**:
   - While the heap is not empty, pop the smallest element and append it to the result.
   - Fetch the next element from the corresponding array (from which the smallest element came) and push it into the heap.
   - Repeat the process until all arrays are fully processed.

### Time Complexity:
- **Heap Initialization**: O(k * log k), where **k** is the number of arrays, since we insert the first element of each array into the heap.
- **Processing Remaining Elements**: There are a total of **n** elements across all arrays, and for each element, we perform a **heap push/pop** operation which takes **O(log k)** time.
- **Total Time Complexity**: O(n * log k), where **n** is the total number of elements across all arrays and **k** is the number of arrays.

### Space Complexity:
- **Space Complexity**: O(k), since the heap stores at most one element from each array at any given time.

### Function Definition:

```python
import heapq

def merge_sorted_arrays(sorted_arrays):
    """
    Merges multiple sorted arrays into a single sorted array.
    
    :param sorted_arrays: List of sorted arrays to be merged.
    :return: A single merged and sorted array containing all elements.
    """
    pass  # High-level logic explained above
```

### Example Function Calls:

#### Example 1:
```python
sorted_arrays = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

# Expected Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

#### Example 2:
```python
sorted_arrays = [
    [10, 20, 30],
    [15, 25, 35],
    [5, 12, 14]
]

# Expected Output: [5, 10, 12, 14, 15, 20, 25, 30, 35]
```

### Summary:

1. **Initialize iterators** for each array.
2. **Build a heap** with the first element of each array.
3. **Pop and push elements** from the heap, always adding the smallest element from the current arrays until all arrays are processed.
4. The solution efficiently merges **k** sorted arrays into a single sorted array using a min-heap.
