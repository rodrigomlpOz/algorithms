def findDuplicate(nums):
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Find the "entrance" to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    
    return hare

# Test cases
print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(findDuplicate([3, 1, 3, 4, 2]))  # Output: 3
print(findDuplicate([1, 1]))           # Output: 1
print(findDuplicate([1, 4, 6, 5, 3, 2, 4]))  # Output: 4
print(findDuplicate([5, 4, 3, 2, 1, 5]))     # Output: 5
