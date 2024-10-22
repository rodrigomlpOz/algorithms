def subarraySum(nums, k):
    """
    Finds the number of continuous subarrays whose sum equals k.
    
    Args:
    nums (List[int]): The list of integers.
    k (int): The target sum.
    
    Returns:
    int: The number of subarrays that sum up to k.
    """
    count = 0
    cumulative_sum = 0
    prefix_sum_count = {0: 1}  # Initialize with 0 sum having one count
    
    for num in nums:
        cumulative_sum += num
        
        # Check if there is a previous prefix sum that matches current_sum - k
        if (cumulative_sum - k) in prefix_sum_count:
            count += prefix_sum_count[cumulative_sum - k]
        
        # Update the count of the current cumulative_sum in the hash map
        if cumulative_sum in prefix_sum_count:
            prefix_sum_count[cumulative_sum] += 1
        else:
            prefix_sum_count[cumulative_sum] = 1
    
    return count

# Example usage
nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # Expected output: 2
