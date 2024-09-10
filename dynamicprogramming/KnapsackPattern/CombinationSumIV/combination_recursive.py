def combinationSum4_recursive(nums: List[int], target: int) -> int:
    # Base cases
    if target == 0:
        return 1  # There's exactly one way to achieve target 0 (by using no numbers)
    if target < 0:
        return 0  # No way to achieve a negative target
    
    total_ways = 0
    # For each number in nums, try to include it and solve for the reduced target
    for num in nums:
        if num <= target:
            total_ways += combinationSum4_recursive(nums, target - num)
    
    return total_ways
