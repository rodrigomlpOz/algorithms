def searchRange(nums: list[int], target: int) -> list[int]:
    # Helper function to find the first position of target
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first_position = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_position = mid  # Record the potential first occurrence
                right = mid - 1  # Continue searching the left part
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first_position
    
    # Helper function to find the last position of target
    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last_position = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last_position = mid  # Record the potential last occurrence
                left = mid + 1  # Continue searching the right part
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last_position
    
    # Find the first and last position using the helper functions
    first = findFirst(nums, target)
    if first == -1:  # If first occurrence is not found, target does not exist
        return [-1, -1]
    
    last = findLast(nums, target)
    
    return [first, last]
