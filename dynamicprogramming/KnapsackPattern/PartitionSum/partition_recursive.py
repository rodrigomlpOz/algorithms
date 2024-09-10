def canPartition(nums: list[int]) -> bool:
    total_sum = sum(nums)
    
    # Step 1: If total sum is odd, return False
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    
    # Step 2: Recursive helper function to check if we can reach 'target'
    def canPartitionRecursive(i, current_sum):
        # Base case: If we hit the target sum
        if current_sum == 0:
            return True
        # If we exceed the target sum or index goes out of bounds
        if current_sum < 0 or i >= len(nums):
            return False
        
        # Choice 1: Include the current number in the subset
        if canPartitionRecursive(i + 1, current_sum - nums[i]):
            return True
        
        # Choice 2: Exclude the current number from the subset
        return canPartitionRecursive(i + 1, current_sum)
    
    # Start the recursion with the first element (index 0) and target sum
    return canPartitionRecursive(0, target)

# Example calls:
print(canPartition([1, 5, 11, 5]))  # Output: True
print(canPartition([1, 2, 3, 5]))   # Output: False
