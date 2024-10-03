The **3Sum** problem is a classic algorithmic challenge commonly asked in coding interviews. Here's a breakdown of the problem and a common approach to solve it.

### Problem Statement:
Given an array of integers `nums`, find all unique triplets `(a, b, c)` in the array such that:
```
def threeSum(nums):
    # Implementation here


# Example 1
nums1 = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]

# Example 2
nums2 = [0, 1, 1]
print(threeSum(nums2))  # Output: []

# Example 3
nums3 = [0, 0, 0]
print(threeSum(nums3))  # Output: [[0, 0, 0]]
```
and avoid including duplicate triplets.

### Approach:

1. **Sort the Array:** First, sort the array. This helps in avoiding duplicates and makes it easier to use the two-pointer technique.
   
2. **Traverse the Array:** Loop through each element in the array and treat it as a fixed element. Then, use the two-pointer technique to find pairs of elements after the current element that sum up to the negative of the fixed element.
   
3. **Two-pointer Technique:** After fixing one element, use two pointers (`left` and `right`):
   - `left` starts from the element right after the fixed element.
   - `right` starts from the end of the array.
   - Adjust the pointers based on the sum of the triplet.
     - If the sum is less than zero, move the `left` pointer to the right to increase the sum.
     - If the sum is greater than zero, move the `right` pointer to the left to decrease the sum.

4. **Avoid Duplicates:** Skip over duplicate values for the fixed element and the left pointer to avoid counting the same triplet multiple times.

### Time Complexity:
- Sorting the array takes **O(n log n)**.
- The two-pointer traversal for each element takes **O(n)**.
- Overall time complexity is **O(n^2)**.

### Example:

```python
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
```

**Output:**

```
[[-1, -1, 2], [-1, 0, 1]]
```

This code efficiently finds all unique triplets in the array that sum to zero, avoiding duplicates using sorting and two-pointer technique.
