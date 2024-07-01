'''
In Phase 2, both pointers will indeed meet. The key idea here is that once a cycle is detected in Phase 1, the cycle's entrance (which is the duplicate number) can be found by moving both pointers one step at a time starting from the head and the intersection point, respectively. Here's the logic behind it:

After detecting the cycle in Phase 1, the distance from the start of the array to the cycle's entrance is equal to the distance from the intersection point to the cycle's entrance.
Thus, by resetting one pointer to the start of the array and keeping the other at the intersection point, both pointers will meet at the cycle's entrance (the duplicate number) when moved one step at a time.
'''

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
