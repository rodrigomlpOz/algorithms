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
