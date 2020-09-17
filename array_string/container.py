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
        