def maxSubArray(nums: List[int]) -> int:
    # Initialize the current and global max to the first element
    current_max = global_max = nums[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Update current_max to either the current element alone or the current element + previous current_max
        current_max = max(nums[i], current_max + nums[i])
        
        # Update global_max to the maximum of itself and current_max
        global_max = max(global_max, current_max)
    
    return global_max