def max_area_two_pointers(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area with current left and right
        width = right - left
        current_height = min(height[left], height[right])
        current_area = current_height * width
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example Usage
if __name__ == "__main__":
    heights = [1,8,6,2,5,4,8,3,7]
    print("Maximum Area (Two Pointers):", max_area_two_pointers(heights))  # Output: 49
