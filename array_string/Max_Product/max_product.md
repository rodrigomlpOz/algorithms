## Problem Statement

**Maximum Product Subarray**

Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

**Example:**
```
Input: nums = [2, 3, -2, 4]
Output: 6
Explanation: [2, 3] has the largest product 6.
```

**Example:**
```
Input: nums = [-2, 0, -1]
Output: 0
Explanation: The result cannot be 2, because [-2, -1] is not a subarray.
```

## High-Level Approach

1. **Initialize Variables**:
    - `global_max` to store the maximum product found so far, initialized to the first element of `nums`.
    - `local_max` and `local_min` to store the maximum and minimum products ending at the current position, both initialized to the first element of `nums`.

2. **Iterate Through the Array**:
    - Starting from the second element, iterate through the array.
    - If the current element is negative, swap `local_max` and `local_min` because multiplying by a negative flips the signs, potentially making the maximum smaller and the minimum larger.
    - Update `local_max` to be the maximum of the current element itself and the product of `local_max` with the current element.
    - Update `local_min` to be the minimum of the current element itself and the product of `local_min` with the current element.
    - Update `global_max` to be the maximum of `global_max` and `local_max`.

3. **Return the Result**:
    - Return `global_max`, which contains the maximum product of any contiguous subarray.

## Function Signature

```python
def maxProduct(nums):
    pass
```
