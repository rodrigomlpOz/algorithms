def threeSum(nums):
    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]
            
            if sum_ == 0:
                res.append([nums[i], nums[left], nums[right]])
                # Move left and right pointers to avoid duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif sum_ < 0:
                left += 1
            else:
                right -= 1
    
    return res

#Case were there were duplicated similar to 3sum
The condition `j > i + 1` is necessary because you want to skip duplicates **only after the first occurrence** of the second element (i.e., the element at index `j`). Here’s why it matters:

1. **Avoid Skipping the First Valid Occurrence**: The first occurrence of a number should be considered because it's part of a unique quadruplet. If you skip the first occurrence, you might miss valid combinations. By checking `j > i + 1`, you ensure that only subsequent duplicate values are skipped, not the first one.

2. **Maintain the Integrity of Nested Loops**: The `i` index is fixed in the outer loop, and `j` starts from `i + 1`. If `j == i + 1`, this is the first time you're selecting `arr[j]` as part of a potential quadruplet, so you don't want to skip it, even if `arr[j] == arr[j - 1]`. By using `j > i + 1`, you ensure that **duplicate values are only skipped after the first valid selection**.

### Example to illustrate:

Suppose `arr = [-1, 0, 0, 0, 1, 2]`, and you're looking for quadruplets that sum to `2`.

- When `i = 0`, `arr[i] = -1`.
- On the first iteration, `j = 1` and `arr[j] = 0`. This is a valid choice, so we continue.
- On the next iteration, `j = 2`, and `arr[j] = 0` again. Now, you don't want to reconsider this element because it's the same as `arr[j - 1]`, so you skip it to avoid repeating the same quadruplet (like `[-1, 0, 0, 2]` multiple times).
- The `j > i + 1` ensures that we skip **only the duplicate 0s after the first one**.

Without the `j > i + 1` check, you'd mistakenly skip the very first occurrence of `0`, which might be a valid part of the quadruplet.

### To summarize:
- `arr[j] == arr[j - 1]`: This ensures you're not repeating the same number twice for the second element.
- `j > i + 1`: This ensures you skip duplicates **only after the first valid occurrence** of the second element `arr[j]`, preventing duplicate quadruplets while preserving all valid unique combinations.

Let me know if that clears things up!
# def findArrayQuadruplet(arr, s):
#     if len(arr) < 4:
#         return []
    
#     ans = []
#     arr.sort()
    
#     for i in range(len(arr) - 3):
#         if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicates for the first element
#             continue
        
#         for j in range(i + 1, len(arr) - 2):
#             if j > i + 1 and arr[j] == arr[j - 1]:  # Skip duplicates for the second element
#                 continue
            
#             left = j + 1
#             right = len(arr) - 1
            
#             while left < right:
#                 curr_sum = arr[i] + arr[j] + arr[left] + arr[right]
                
#                 if curr_sum == s:
#                     ans.append([arr[i], arr[j], arr[left], arr[right]])
                    
#                     # Skip duplicates for the third element
#                     while left < right and arr[left] == arr[left + 1]:
#                         left += 1
#                     # Skip duplicates for the fourth element
#                     while left < right and arr[right] == arr[right - 1]:
#                         right -= 1
                    
#                     left += 1
#                     right -= 1
#                 elif curr_sum < s:
#                     left += 1
#                 else:
#                     right -= 1
    
#     return ans
