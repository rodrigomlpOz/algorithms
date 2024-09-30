Here’s the **Summary Ranges** problem with the problem definition and high-level solution explanation, but without the detailed implementation. Instead, I’ve included the function definition and several function calls with `print` statements as you requested.

### Problem: 228. Summary Ranges

**Problem Statement:**
You are given a sorted unique integer array `nums`.

A range `[a, b]` is the set of all integers from `a` to `b` (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a, b]` in the list should be output as:
- `"a->b"` if `a != b`
- `"a"` if `a == b`

**Example 1:**
```
Input: nums = [0, 1, 2, 4, 5, 7]
Output: ["0->2", "4->5", "7"]
Explanation: The ranges are:
[0, 2] --> "0->2"
[4, 5] --> "4->5"
[7, 7] --> "7"
```

### High-Level Solution:
1. **Initialize variables:** Start with an empty list to store ranges and track the start of the current range.
2. **Iterate through the array:** For each number, check if it is consecutive from the previous number. If it's not, close the current range and start a new one.
3. **Form the ranges:** If the start and end of the range are the same, store it as a single number. Otherwise, store it as `"a->b"`.
4. **Return the ranges:** After iterating through the array, return the list of formatted ranges.

### Function Definition (Skeleton):
```python
def summaryRanges(nums):
    # High-level idea:
    # 1. Track the start of each range.
    # 2. If numbers are consecutive, continue the range.
    # 3. If not consecutive, close the range and start a new one.
    pass
```

### Function Calls with Print Statements:
```python
# Test Case 1
nums1 = [0, 1, 2, 4, 5, 7]
print(f"Input: {nums1}")
print(f"Output: {summaryRanges(nums1)}")
# Expected Output: ["0->2", "4->5", "7"]

# Test Case 2
nums2 = [0, 2, 3, 4, 6, 8, 9]
print(f"Input: {nums2}")
print(f"Output: {summaryRanges(nums2)}")
# Expected Output: ["0", "2->4", "6", "8->9"]

# Test Case 3
nums3 = []
print(f"Input: {nums3}")
print(f"Output: {summaryRanges(nums3)}")
# Expected Output: []

# Test Case 4
nums4 = [-1]
print(f"Input: {nums4}")
print(f"Output: {summaryRanges(nums4)}")
# Expected Output: ["-1"]

# Test Case 5
nums5 = [0]
print(f"Input: {nums5}")
print(f"Output: {summaryRanges(nums5)}")
# Expected Output: ["0"]
```

This version includes:
1. **Problem Definition** to explain what needs to be solved.
2. **High-Level Solution** to describe the approach for solving the problem.
3. **Function Definition Skeleton** where the actual code should be written.
4. **Function Calls with `print` statements** for multiple test cases, demonstrating expected outputs.