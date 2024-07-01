### Problem Statement: Increasing Triplet Subsequence

**Problem Description:**

Given an integer array `nums`, determine if there exists a triplet of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If such a triplet exists, return `true`; otherwise, return `false`.

**Constraints:**

- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

**Example:**
```python
Input: nums = [1, 2, 3, 4, 5]
Output: True
Explanation: There exists a triplet (1, 2, 3).

Input: nums = [5, 4, 3, 2, 1]
Output: False
Explanation: No such triplet exists.
```

### High-Level Approach

To solve this problem efficiently with a time complexity of O(n) and space complexity of O(1), we can follow these steps:

1. **Initialization:**
   - Use two variables, `c1` and `c2`, initialized to infinity (`float('inf')`), to track the smallest and the second smallest elements encountered so far in the array.

2. **Iterate Through the Array:**
   - Traverse the array and update `c1` if the current element is less than or equal to `c1`.
   - If the current element is greater than `c1` but less than or equal to `c2`, update `c2`.
   - If the current element is greater than both `c1` and `c2`, a triplet satisfying the condition is found, so return `True`.

3. **Return Result:**
   - If the iteration completes without finding such a triplet, return `False`.

This approach ensures that we effectively find the increasing triplet by maintaining two markers (`c1` and `c2`) and looking for a third element that is larger than both.

### Explanation:

- **c1**: Keeps track of the smallest element found so far.
- **c2**: Keeps track of the second smallest element that comes after `c1`.
- When a number larger than both `c1` and `c2` is found, it indicates the presence of an increasing triplet subsequence.

By following this strategy, the algorithm can efficiently determine the presence of an increasing triplet subsequence in linear time.
