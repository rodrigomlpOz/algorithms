### Problem Statement:
A **peak element** is an element that is strictly greater than its neighbors. Given a 0-indexed integer array `nums`, find a peak element and return its index. If the array contains multiple peaks, return the index of any one of the peaks.

You can assume that `nums[-1] = -∞` and `nums[n] = -∞` where `n` is the length of `nums`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in **O(log n)** time.

### Function Definition:
```python
def findPeakElement(nums: list[int]) -> int:
    pass
```

### Function Calls:

```python
# Test cases
print(findPeakElement([1, 2, 3, 1]))  # Expected output: 2 (index of element 3)
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Expected output: 5 or 1
```

### High-Level Solution:

1. **Binary Search Setup**: 
   - We will use binary search to efficiently find the peak element.
   - Start by initializing two pointers `left` and `right` to the start and end of the array.

2. **Binary Search Loop**:
   - Calculate the middle index `mid`.
   - Compare the middle element with its right neighbor:
     - If `nums[mid] > nums[mid + 1]`, the peak lies on the left side (including `mid`), so we reduce the search space by setting `right = mid`.
     - If `nums[mid] < nums[mid + 1]`, the peak lies on the right side, so we move `left = mid + 1`.
   - Continue narrowing down the search space until `left == right`.

3. **Return the Peak**:
   - When the loop ends, the pointers `left` and `right` will converge to the index of a peak element. Return this index as the result.

### Detailed Solution:

1. **Initialization**: Start with two pointers: `left = 0` and `right = len(nums) - 1`.
2. **Binary Search**: In each iteration:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] > nums[mid + 1]`, move `right` to `mid` (peak is on the left).
   - Otherwise, move `left` to `mid + 1` (peak is on the right).
3. **Return**: Once the pointers converge, `left` will be the index of the peak element. Return `left`.