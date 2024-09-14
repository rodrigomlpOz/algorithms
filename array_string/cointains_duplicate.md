### Problem Statement:
Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

### Function Definition:
```python
def contains_duplicate(nums: list[int]) -> bool:
    # Function to determine if there are any duplicate integers in the list
```

### Function Calls:
```python
# Example 1
nums1 = [1, 2, 3, 3]
print(contains_duplicate(nums1))  # Output: True

# Example 2
nums2 = [1, 2, 3, 4]
print(contains_duplicate(nums2))  # Output: False
```

### High-Level Description:
1. **Objective**: The goal is to check whether any element in the array `nums` appears more than once.
2. **Approach**:
   - Initialize an empty set `seen` to track the elements we have already encountered.
   - Loop through each element in the array.
     - If the current element is already in the set `seen`, return `true` (indicating a duplicate exists).
     - If not, add the element to the set.
   - If no duplicates are found after checking all elements, return `false`.
3. **Efficiency**:
   - Time Complexity: O(n), where n is the number of elements in the array. Each element is checked once.
   - Space Complexity: O(n) due to the set used to store elements.

