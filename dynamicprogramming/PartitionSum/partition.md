Sure! Let’s dive into **Problem 9: Partition Equal Subset Sum**. Here's a breakdown:

### Problem Description:

You are given a non-empty array `nums` containing only positive integers. You need to determine if the array can be partitioned into two subsets such that the sum of the elements in both subsets is equal.

### Constraints:
- Each element in the array is a positive integer.
- The length of the array does not exceed 200.
- The sum of elements will not exceed 10000.

### Example 1:

```text
Input: nums = [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

### Example 2:

```text
Input: nums = [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

---

### Function Definition and Calls:

```python
def canPartition(nums: list[int]) -> bool:
    # Function logic goes here
    pass

# Example Calls:
print(canPartition([1, 5, 11, 5]))  # Output: True
print(canPartition([1, 2, 3, 5]))   # Output: False
```

---

### High-Level Solution:

This problem can be reduced to a **subset sum** problem, where the target sum is half of the total sum of the array elements. Here's the high-level approach:

1. **Total Sum Check**: First, calculate the total sum of the array. If the total sum is odd, it's impossible to partition the array into two equal subsets, so return `False`.

2. **Subset Sum Problem**: If the total sum is even, the problem reduces to finding a subset of the array that sums to half of the total sum (`target = total_sum // 2`).

3. **Dynamic Programming (1D DP)**: 
   - Use a boolean DP array where `dp[i]` is `True` if a subset with sum `i` can be formed from the elements.
   - Initialize `dp[0] = True` because a subset with sum 0 can always be formed (by taking no elements).
   - For each number in the array, update the DP array by checking if the current number can help form new subset sums up to `target`.

4. **Final Check**: If `dp[target]` is `True` by the end of the process, that means there exists a subset with sum `target`, and thus the array can be partitioned into two equal subsets.


### Complexity Analysis:

- **Time Complexity**: `O(n * target)` where `n` is the length of the array and `target` is half of the total sum. Each number is processed to update the DP array up to the `target` sum.
  
- **Space Complexity**: `O(target)`. We only use a 1D DP array of size `target + 1` to store whether a specific subset sum is possible.

This approach efficiently handles the partition problem using dynamic programming.
