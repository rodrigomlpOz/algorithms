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
