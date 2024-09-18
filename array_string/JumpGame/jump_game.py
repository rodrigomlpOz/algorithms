def canJump(nums: list[int]) -> bool:
    # Track the farthest index that can be reached
    max_reach = 0
    
    # Iterate through the nums array
    for i in range(len(nums)):
        # If the current index is beyond the max reachable index, return False
        if i > max_reach:
            return False
        
        # Update the max reachable index
        max_reach = max(max_reach, i + nums[i])
        
        # If we can reach or exceed the last index, return True
        if max_reach >= len(nums) - 1:
            return True
    
    # If the loop completes and we didn't return True, return False
    return False
