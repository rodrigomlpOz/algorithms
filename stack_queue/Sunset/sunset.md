## Problem Statement


You are given an array of buildings where each building is represented by its height. Imagine you are facing these buildings from the west (left side of the array). A building has a view of the sunset if all the buildings to its west (left) are shorter than it.

You are asked to return the indices of the buildings that have a view of the sunset, in reverse order (as seen from the sunset).

### Example:

Input: [3, 7, 4, 5, 6]
Output: [4, 3, 1]

def buildings_with_sunset_view(heights):
    """
    Determine which buildings have a view of the sunset.

    :param heights: List of integers representing building heights
    :return: List of integers representing indices of buildings with sunset view
    """

### Constraints:

- The input list `heights` will contain positive integers.
- The length of the input list `heights` will be at least 1.

### Function Signature:

```python
def buildings_with_sunset_view(heights):
    """
    Determine which buildings have a view of the sunset.

    :param heights: List of integers representing building heights
    :return: List of integers representing indices of buildings with sunset view
    """
```

### Example:

```python
# Example 1
heights = [3, 7, 4, 5, 6]
print(buildings_with_sunset_view(heights))  # Output: [4, 3, 1]


# Example 2
heights = [1, 2, 3, 4, 5]
print(buildings_with_sunset_view(heights))  # Output: [4]
```

### Explanation:

- For the first example, the buildings with indices 4, 3, and 1 have a view of the sunset because they are taller than all the buildings to their left.
    
- For the second example, only the building with index 4 has a view of the sunset because it is the tallest.            


### Approach:

1. Initialize an empty list to store the indices of buildings with a view of the sunset.
2. Iterate through the `heights` list from left to right.
3. For each building, check if it is taller than the last building in the list.
4. If it is, add its index to the list.
5. Return the list of indices in reverse order.


### Implementation:

```python
def buildings_with_sunset_view(heights):
    stack = []
    for i, height in enumerate(heights):
        while stack and height >= heights[stack[-1]]:
            stack.pop()
            
        