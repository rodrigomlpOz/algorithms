The **3Sum** problem is a classic algorithmic challenge commonly asked in coding interviews. Here's a breakdown of the problem and a common approach to solve it.

### Problem Statement:
Given an array of integers `nums`, find all unique triplets `(a, b, c)` in the array such that:
```
a + b + c = 0
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

### Code Example (in Python):

```python
def threeSum(nums):
    nums.sort()  # Sort the array
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the left and right pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

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
