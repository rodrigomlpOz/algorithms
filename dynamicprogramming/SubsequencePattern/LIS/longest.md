### Problem Statement:
Given an integer array `nums`, return the length of the longest strictly increasing subsequence. A subsequence is derived by deleting some or no elements from the array without changing the order of the remaining elements.

### Function Definition:
```python
def lengthOfLIS(nums):
    pass
```

### Function Calls:
```python
# Test cases
arr1 = [10, 9, 2, 5]
print(lengthOfLIS(arr1))  # Expected output: 2 (Subsequence: [2, 5])

arr2 = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(arr2))  # Expected output: 4 (Subsequence: [2, 3, 7, 101])

arr3 = [0, 1, 0, 3, 2, 3]
print(lengthOfLIS(arr3))  # Expected output: 4 (Subsequence: [0, 1, 2, 3])

arr4 = [7, 7, 7, 7]
print(lengthOfLIS(arr4))  # Expected output: 1 (Subsequence: [7])
```

### High-Level Solution:
1. **Recursive Approach**:
   - The `max_lis` function is a recursive helper that evaluates whether to include or skip the current element `nums[idx]` when constructing an increasing subsequence.
   - **Base Case**: When the index reaches the end of the array, return `0` since there are no more elements to process.
   - **Recursive Case**:
     - If the current element `nums[idx]` is greater than `cur_max`, two choices exist:
       - Include it and move to the next element, updating the `cur_max` to `nums[idx]` and adding `1` to the result.
       - Skip it and continue searching the sequence.
     - If `nums[idx]` is not greater than `cur_max`, skip it.
   - **Initial Call**: The function starts with index `0` and an initial `cur_max` of negative infinity (`float('-inf')`), indicating that no element has been chosen yet.

2. **Inefficiency**:
   - This top-down recursive solution with two recursive calls at each step results in a time complexity of `O(2^n)`, making it impractical for larger inputs. It evaluates all possible subsequences, leading to exponential time complexity.

3. **Improvement**:
   - To improve efficiency, dynamic programming (DP) or memoization can be used to store intermediate results and avoid redundant computations.
   - Another approach is a bottom-up dynamic programming solution with a time complexity of `O(n^2)` or an optimized solution using binary search and dynamic programming with `O(n log n)` complexity.
