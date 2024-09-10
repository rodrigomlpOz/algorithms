The **Maximum Subarray** problem is a classic dynamic programming problem, often solved using **Kadane's Algorithm**.

### Problem Statement:
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Example:

```plaintext
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

### Function Definition:
```python
def maxSubArray(nums: List[int]) -> int:
    """
    This function finds the contiguous subarray within an array which has the largest sum.

    Args:
    nums: List[int] - The input array of integers.

    Returns:
    int - The sum of the maximum subarray.
    """
```

### Function Calls:
```python
# Test case 1
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))  # Output: 6

# Test case 2
nums = [1]
print(maxSubArray(nums))  # Output: 1

# Test case 3
nums = [5,4,-1,7,8]
print(maxSubArray(nums))  # Output: 23
```

### High-Level Solution (Kadane’s Algorithm):
Kadane’s Algorithm is an efficient approach to solving the **Maximum Subarray** problem using dynamic programming principles. The key idea is to iterate through the array while keeping track of:
1. The maximum subarray sum ending at the current index (`current_max`).
2. The overall maximum subarray sum found so far (`global_max`).

At each index, we decide whether to:
- Continue the current subarray (add the current element to the existing subarray).
- Start a new subarray (the current element itself is greater than adding it to the existing subarray).

### Steps:
1. Initialize `current_max` and `global_max` to the first element of the array.
2. For each subsequent element in the array:
   - Update `current_max` by taking the maximum of either the current element alone or the current element plus `current_max`.
   - Update `global_max` if `current_max` is greater than `global_max`.
3. Return `global_max`.


### Explanation:

1. **Initialization**:
   - `current_max`: Keeps track of the maximum sum of the subarray ending at the current index.
   - `global_max`: Keeps track of the maximum sum of any subarray found so far.

2. **Iteration**:
   - For each element `nums[i]`, we decide whether to:
     - Add the current element to the previous subarray (`current_max + nums[i]`).
     - Start a new subarray with just the current element (`nums[i]`).
   - Update `current_max` with the maximum of these two choices.

3. **Updating `global_max`**:
   - After each iteration, update `global_max` to be the maximum of `global_max` and `current_max`.

4. **Return the Result**:
   - After processing all elements, return `global_max`, which holds the maximum subarray sum.

### Time Complexity:
- **O(n)**: We only iterate through the array once.

### Space Complexity:
- **O(1)**: We only use a few variables (`current_max` and `global_max`), so the space complexity is constant.

---

This approach ensures that the maximum subarray sum is found in linear time, making it highly efficient even for large arrays.

Let me know if you need further explanations or variations of this problem!