## Problem Statement: Find the Duplicate Number

### Problem Description:
Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, there is exactly one duplicate number in the array. Your task is to find and return this duplicate number.


### Constraints:
1. You must not modify the array (assume the array is read-only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n^2).
4. There is only one duplicate number in the array, but it could be repeated more than once.

### Example:
def find_duplicate(nums):
    # Function to find the duplicate number
    pass

# Test cases
nums1 = [1, 3, 4, 2, 2]
print("Output:", find_duplicate(nums1))  # Expected Output: 2

nums2 = [3, 1, 3, 4, 2]
print("Output:", find_duplicate(nums2))  # Expected Output: 3


### Notes:
- You can read more about various creative ways to solve this problem [here](https://leetcode.com/problems/find-the-duplicate-number/solution/).

### High-Level Overview:
To solve this problem efficiently, we can use a strategy inspired by cycle detection in a linked list, known as Floyd's Tortoise and Hare algorithm. Here's a high-level overview of the approach:

1. **Cycle Detection**: Treat the array as a linked list where the value at each index points to the next index. Due to the duplicate number, a cycle will exist within this list. Use two pointers (tortoise and hare) to detect the cycle.
2. **Finding the Entrance**: Once a cycle is detected, reset one of the pointers to the start of the array and move both pointers one step at a time. The point where they meet again will be the duplicate number. This works because the cycle entrance is the duplicate number causing the loop.

This method ensures that we do not modify the array, use constant extra space, and achieve a runtime complexity better than O(n^2).
