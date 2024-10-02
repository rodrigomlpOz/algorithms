def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Compare the middle element with its next element
        if nums[mid] > nums[mid + 1]:
            # The peak is on the left side (including mid)
            right = mid
        else:
            # The peak is on the right side
            left = mid + 1
    
    # When left == right, we've found the peak element
    return left
