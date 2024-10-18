### Problem: 452. Minimum Number of Arrows to Burst Balloons

**Problem Statement:**
There are spherical balloons taped to a flat wall represented by the XY-plane. The balloons are given as a 2D integer array `points`, where `points[i] = [xstart, xend]` represents a balloon with its horizontal diameter stretching between `xstart` and `xend`.

An arrow can be shot vertically (in the positive y-direction) from any point along the x-axis. A balloon is burst by an arrow shot at `x` if `xstart <= x <= xend`. The goal is to find the minimum number of arrows that must be shot to burst all the balloons.

**Example 1:**
```
Input: points = [[10, 16], [2, 8], [1, 6], [7, 12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2, 8] and [1, 6].
- Shoot an arrow at x = 11, bursting the balloons [10, 16] and [7, 12].
```

**Example 2:**
```
Input: points = [[1, 2], [3, 4], [5, 6], [7, 8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
```

**Example 3:**
```
Input: points = [[1, 2], [2, 3], [3, 4], [4, 5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1, 2] and [2, 3].
- Shoot an arrow at x = 4, bursting the balloons [3, 4] and [4, 5].
```

### High-Level Solution:
1. **Sort the balloons:** Sort the intervals by the end coordinate (`xend`). This helps in efficiently finding the next arrow position.
2. **Greedy approach:** After shooting an arrow at the end of the first balloon, continue checking the next balloons. If a balloon overlaps with the current arrow position, you do not need a new arrow. Otherwise, shoot a new arrow.
3. **Count the number of arrows needed.**

### Full Implementation:

```python
def findMinArrowShots(points):
    pass
```

### Function Calls with Test Cases:

```python
# Test Case 1
points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(f"Input: {points1}")
print(f"Output: {findMinArrowShots(points1)}")
# Expected Output: 2

# Test Case 2
points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(f"Input: {points2}")
print(f"Output: {findMinArrowShots(points2)}")
# Expected Output: 4

# Test Case 3
points3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(f"Input: {points3}")
print(f"Output: {findMinArrowShots(points3)}")
# Expected Output: 2

# Test Case 4 (Edge Case: No balloons)
points4 = []
print(f"Input: {points4}")
print(f"Output: {findMinArrowShots(points4)}")
# Expected Output: 0

# Test Case 5
points5 = [[1, 10], [2, 3], [4, 8], [5, 6]]
print(f"Input: {points5}")
print(f"Output: {findMinArrowShots(points5)}")
# Expected Output: 2
```

### Explanation of the Solution:
1. **Sort the balloons:** We first sort the intervals based on the `xend` value. This ensures that we always consider the interval that ends the earliest when shooting an arrow, which helps minimize the number of arrows.
   
2. **Shoot arrows:** 
   - We start by shooting an arrow at the end of the first interval.
   - For each subsequent interval, if its `xstart` is greater than the current arrow's position, we shoot a new arrow at the end of that interval. If not, the current arrow can burst the current balloon as well, and we don't need to shoot a new arrow.

3. **Edge Cases:**
   - **Empty input (`points = []`):** If there are no balloons, we return 0.
   - **Non-overlapping intervals:** If the balloons do not overlap, we shoot one arrow for each balloon.

### Time Complexity:
- Sorting the intervals takes `O(n log n)`, where `n` is the number of intervals (balloons).
- The loop to iterate through the intervals is `O(n)`.
- Hence, the overall time complexity is `O(n log n)`.
