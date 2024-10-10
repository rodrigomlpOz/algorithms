def trap_stack(height):
    """
    Calculate the total trapped water using a stack-based approach.

    :param height: List[int] - List of non-negative integers representing elevation heights.
    :return: int - Total units of trapped water.
    """
    stack = []  # Stack to store indices
    total_water = 0
    current = 0  # Current index

    while current < len(height):
        # While stack is not empty and current height is greater than the height at the stack's top index
        while stack and height[current] > height[stack[-1]]:
            top = stack.pop()  # The index of the bottom of the trapped water

            if not stack:
                break  # No left boundary to trap water
            #stack[-1] is the left boundary
            distance = current - stack[-1] - 1  # Width between current and new top
            bounded_height = min(height[current], height[stack[-1]]) - height[top]
            trapped = distance * bounded_height
            total_water += trapped

        stack.append(current)
        current += 1

    return total_water
