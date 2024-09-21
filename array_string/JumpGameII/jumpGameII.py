def jump(nums: list[int]) -> int:
    jumps, current_end, farthest = 0, 0, 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps
