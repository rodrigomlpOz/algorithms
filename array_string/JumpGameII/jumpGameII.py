def jump(nums: list[int]) -> int:
    jumps = 0         # Count the number of jumps
    current_end = 0    # Farthest point we can reach with the current jump
    farthest = 0       # Farthest point we can reach overall
    
    for i in range(len(nums) - 1):
        # Update the farthest point we can reach from this index
        farthest = max(farthest, i + nums[i])
        
        # If we reach the end of the current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest
        
        # If we've already reached or exceeded the last index
        if current_end >= len(nums) - 1:
            break
    
    return jumps
