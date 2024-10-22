### Problem Statement:

You are given two lists of non-overlapping intervals, **A** and **B**, where each interval is represented as `[start, end]` and both lists are already sorted based on the start times of the intervals. Write a function to merge the two lists of intervals into a single list of non-overlapping intervals, such that the intervals are sorted by start times and any overlapping intervals are merged.

### Example:

```python
A = [[1, 5], [10, 14], [16, 18]]
B = [[2, 6], [8, 10], [11, 20]]

Output: [[1, 6], [8, 20]]
```

**Explanation**:
- Intervals `[1, 5]` and `[2, 6]` overlap, so they are merged into `[1, 6]`.
- Intervals `[10, 14]` and `[8, 10]` overlap, so they are merged into `[8, 14]`.
- Intervals `[8, 14]` and `[11, 20]` overlap, so they are merged into `[8, 20]`.

### Function Definition:

```python
def mergeIntervals(A, B):
    """
    This function merges two lists of sorted, non-overlapping intervals into a single list of non-overlapping intervals.
    
    :param A: List[List[int]] - First sorted list of intervals.
    :param B: List[List[int]] - Second sorted list of intervals.
    :return: List[List[int]] - Merged list of non-overlapping intervals.
    """
    pass
```

### Function Calls:

```python
A = [[1, 5], [10, 14], [16, 18]]
B = [[2, 6], [8, 10], [11, 20]]
print(mergeIntervals(A, B))  # Expected output: [[1, 6], [8, 20]]

A = [[1, 3], [5, 7]]
B = [[2, 4], [6, 8]]
print(mergeIntervals(A, B))  # Expected output: [[1, 4], [5, 8]]

A = [[1, 2], [3, 4]]
B = [[5, 6]]
print(mergeIntervals(A, B))  # Expected output: [[1, 2], [3, 4], [5, 6]]
```

### High-Level Solution:

1. **Initialize Two Pointers**:
   - Start with two pointers: `i` for list **A** and `j` for list **B**. These pointers will traverse the lists.

2. **Traverse and Compare**:
   - At each step, compare the start times of the current intervals from **A** and **B**. Add the interval with the smaller start time to the result list, but also check if it overlaps with the last interval in the result.

3. **Merge Overlapping Intervals**:
   - If an interval overlaps with the last one added to the result list, merge the intervals by updating the end time.
   - Continue this process until one of the lists is fully processed.

4. **Process Remaining Intervals**:
   - After finishing one of the lists, add the remaining intervals from the other list to the result list, merging any overlapping intervals as needed.

5. **Return the Merged List**:
   - Return the result list, which contains all the merged and non-overlapping intervals.

### Detailed Solution (Two-pointer approach):


### Time Complexity:
- **O(n + m)**: The algorithm processes each interval in **A** and **B** exactly once.
- **Space Complexity**: **O(n + m)**, where `n` and `m` are the sizes of the input lists **A** and **B**, since the result will contain all merged intervals.