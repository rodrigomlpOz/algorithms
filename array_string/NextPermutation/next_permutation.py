def next_permutation(nums):
    n = len(nums)
    # Step 1: Find the first decreasing element from the right
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:  # If we found such a pair
        # Step 2: Find the element just larger than nums[i] to swap
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Swap the pivot with the element just larger than it
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 3: Reverse the numbers from i + 1 to end of the list
    nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
nums = [1, 2, 3]
next_permutation(nums)
print(nums)  # Output: [1, 3, 2]
