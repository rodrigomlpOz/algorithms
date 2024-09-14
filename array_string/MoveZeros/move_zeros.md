### Problem Statement

**Move Zeroes**

Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

### Function Signature
```python
def moveZeroes(nums: List[int]) -> None:
    pass
```

### Constraints
- The length of the array is in the range [1, 10^4].
- Each element in the array is an integer in the range [-2^31, 2^31 - 1].

### Example
```python
# Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

# Example 2:
Input: nums = [0,0,1]
Output: [1,0,0]
```

### High-Level Approach
1. **Initialize a Pointer**: Start with a pointer (`lastNonZeroFoundAt`) that tracks the position of the last non-zero element found.
2. **First Pass**: Iterate through the array. For each non-zero element found, move it to the position indicated by `lastNonZeroFoundAt`, then increment `lastNonZeroFoundAt`.
3. **Second Pass**: After the first pass, all non-zero elements are shifted to the front of the array in their original order. Now, fill the rest of the array with zeros starting from the position of `lastNonZeroFoundAt` to the end of the array. 

This approach ensures that all zeros are moved to the end while maintaining the relative order of non-zero elements, and it does so in-place without needing extra space for another array.
