### Problem Statement:
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If the target is not found in the array, return `[-1, -1]`.

You must write an algorithm with **O(log n)** runtime complexity.

### Function Definition:
```python
def searchRange(nums: list[int], target: int) -> list[int]:
    pass
```

### Example Function Calls:
```python
print(searchRange([5, 7, 7, 8, 8, 10], 8))  # Expected output: [3, 4]
print(searchRange([5, 7, 7, 8, 8, 10], 6))  # Expected output: [-1, -1]
print(searchRange([], 0))  # Expected output: [-1, -1]
```

### High-Level Solution:
Since the array is sorted and we need to find the first and last position of a target element, the problem can be solved using **binary search**. The key is to perform **two binary searches**:
1. **First binary search** to find the leftmost (starting) position of the target.
2. **Second binary search** to find the rightmost (ending) position of the target.

The time complexity must be **O(log n)**, and binary search is ideal for this as it reduces the search space by half in each iteration.

### Detailed Steps:
1. **Binary Search for the First Position**:
   - Use binary search to find the first occurrence of the target. Once we find an occurrence, we continue searching the left side to ensure it is the first occurrence.
   
2. **Binary Search for the Last Position**:
   - Similarly, use binary search to find the last occurrence of the target. Once we find an occurrence, we continue searching the right side to ensure it is the last occurrence.
   
3. **Edge Cases**:
   - If the array is empty, return `[-1, -1]`.
   - If the target is not found, return `[-1, -1]`.

### Python Solution:


### Explanation:
1. **`findFirst` Function**:
   - We perform binary search to find the first occurrence of the target.
   - Once we find the target at `mid`, we continue searching the left half to find if there's an earlier occurrence.
   
2. **`findLast` Function**:
   - We perform binary search to find the last occurrence of the target.
   - Once we find the target at `mid`, we continue searching the right half to find if there's a later occurrence.
   
3. **Edge Handling**:
   - If no first occurrence is found (i.e., `findFirst` returns `-1`), the target does not exist in the array, so we return `[-1, -1]`.
   - Otherwise, we return the positions `[first, last]`.

### Time Complexity:
- **O(log n)**: The binary search function runs in O(log n) for both the first and last position searches. Since both are run independently, the overall complexity remains O(log n).

### Example Runs:

1. **Example 1:**
   - Input: `nums = [5, 7, 7, 8, 8, 10]`, `target = 8`
   - Output: `[3, 4]`
   - Explanation: The target `8` appears at index 3 and 4.

2. **Example 2:**
   - Input: `nums = [5, 7, 7, 8, 8, 10]`, `target = 6`
   - Output: `[-1, -1]`
   - Explanation: The target `6` does not exist in the array.

3. **Example 3:**
   - Input: `nums = []`, `target = 0`
   - Output: `[-1, -1]`
   - Explanation: The array is empty, so the target cannot be found.