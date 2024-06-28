def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i = 0
    j = len(height) - 1
    max_area = float('-inf')
    while i < j:
        width = (j - i)
        curr_height = min(height[i], height[j])
        curr_contained_water = (width * curr_height)
        max_area = max(curr_contained_water, max_area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(maxArea([1,1]))                # Output: 1
print(maxArea([4,3,2,1,4]))          # Output: 16
print(maxArea([1,2,1]))              # Output: 2
print(maxArea([2,3,4,5,18,17,6]))    # Output: 17
print(maxArea([1,2,4,3]))            # Output: 4
