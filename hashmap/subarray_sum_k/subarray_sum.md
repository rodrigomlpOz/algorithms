### Problem Statement

Given an array of integers `nums` and an integer `k`, write a function to find the number of continuous subarrays whose sum equals `k`.

### Function Definition

```python
def subarraySum(nums, k):
    """
    Finds the number of continuous subarrays whose sum equals k.
    
    Args:
    nums (List[int]): The list of integers.
    k (int): The target sum.
    
    Returns:
    int: The number of subarrays that sum up to k.
    """
    pass  # Implementation goes here
```

### Example Function Calls

```python
# Example 1
nums1 = [1, 1, 1]
k1 = 2
result1 = subarraySum(nums1, k1)
print(result1)  # Expected output: 2
# Explanation: There are two subarrays that sum up to 2: [1, 1] (index 0 to 1) and [1, 1] (index 1 to 2).

# Example 2
nums2 = [3, 4, 7, 2, -3, 1, 4, 2]
k2 = 7
result2 = subarraySum(nums2, k2)
print(result2)  # Expected output: 4
# Explanation: There are four subarrays that sum up to 7: [3, 4], [7], [4, 2, -3, 1, 3], and [2, -3, 7].

# Example 3
nums3 = [1, 2, 3]
k3 = 3
result3 = subarraySum(nums3, k3)
print(result3)  # Expected output: 2
# Explanation: The subarrays that sum up to 3 are [1, 2] and [3].
```

### Requirements:
- The function should return an integer representing the number of subarrays that sum up to `k`.
- Subarrays must be continuous, and order matters.

Let's walk through an example step by step using the high-level approach to solve the "Subarray Sum Equals K" problem.

### Example
- Given: `nums = [1, 2, 3]` and `k = 3`.
- Goal: Find the number of continuous subarrays that sum up to `3`.

### Step-by-Step Execution

1. **Initialization:**
   - `cumulative_sum = 0` (this keeps track of the sum of elements from the start to the current index).
   - `count = 0` (this counts the number of subarrays with sum equal to `k`).
   - `prefix_sum_count = {0: 1}` (a hash map that stores how many times each cumulative sum has been seen, initialized with `{0: 1}` to account for cases where the subarray itself equals `k`).

2. **Iterate Through the Array:**

   - **Index 0 (`nums[0] = 1`):**
     - Update `cumulative_sum`: `cumulative_sum += 1` → `cumulative_sum = 1`.
     - Check if `(cumulative_sum - k) = (1 - 3) = -2` exists in `prefix_sum_count`. It does not, so no subarray ending at index 0 sums to `3`.
     - Update the hash map: `prefix_sum_count[1] = 1`.
     - Hash map state: `{0: 1, 1: 1}`.
     - `count` remains `0`.

   - **Index 1 (`nums[1] = 2`):**
     - Update `cumulative_sum`: `cumulative_sum += 2` → `cumulative_sum = 3`.
     - Check if `(cumulative_sum - k) = (3 - 3) = 0` exists in `prefix_sum_count`. It does, and the value associated with `0` is `1`, indicating that one subarray ending at index 1 sums to `3`.
     - Update `count`: `count += 1` → `count = 1`.
     - Update the hash map: `prefix_sum_count[3] = 1`.
     - Hash map state: `{0: 1, 1: 1, 3: 1}`.

   - **Index 2 (`nums[2] = 3`):**
     - Update `cumulative_sum`: `cumulative_sum += 3` → `cumulative_sum = 6`.
     - Check if `(cumulative_sum - k) = (6 - 3) = 3` exists in `prefix_sum_count`. It does, and the value associated with `3` is `1`, indicating that one subarray ending at index 2 sums to `3`.
     - Update `count`: `count += 1` → `count = 2`.
     - Update the hash map: `prefix_sum_count[6] = 1`.
     - Hash map state: `{0: 1, 1: 1, 3: 1, 6: 1}`.

3. **Final Result:**
   - The `count` is `2`, indicating that there are two subarrays in `nums` that sum to `3`:
     - `[1, 2]` (from index 0 to 1).
     - `[3]` (from index 2).

### Key Points Illustrated:
- **Cumulative Sum Calculation:** This running total helps identify subarrays by subtracting previous cumulative sums.
- **Hash Map Usage:** The hash map tracks how many times each cumulative sum occurs, allowing us to determine if there's a matching sum difference.
- **Efficient Counting:** By looking up `(cumulative_sum - k)` in the hash map, we can quickly find subarrays that sum to `k` without having to check each subarray explicitly.

This step-by-step process demonstrates how the algorithm uses cumulative sums and a hash map to efficiently find subarrays that sum up to a given target.