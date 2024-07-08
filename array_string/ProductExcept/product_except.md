## Problem Statement

**Product of Array Except Self**

Given an array `nums` of integers, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The problem must be solved without using division and in `O(n)` time complexity.


```python
def productExceptSelf(nums):
    pass
```

## High-Level Approach

1. **Initialize Result Array**: Start by initializing an array `output` where each element is set to 1. This array will store the final products.

2. **Left Pass**:
   - Traverse the array from left to right.
   - Keep a running product of all elements to the left of the current element.
   - Update the `output` array such that each element at index `i` contains the product of all elements to the left of `nums[i]`.

3. **Right Pass**:
   - Traverse the array from right to left.
   - Keep a running product of all elements to the right of the current element.
   - Multiply the current value of `output[i]` by this running product to get the final product of all elements except `nums[i]`.

4. **Return Result**: The `output` array now contains the desired products for each element.

This approach ensures that we achieve the solution in `O(n)` time complexity without using division, by utilizing the `output` array to store intermediate results during the two passes.
