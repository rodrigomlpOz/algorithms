### Container With Most Water

#### Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that holds the most water. Return the maximum amount of water a container can store.

#### Examples
- Input: `height = [1,8,6,2,5,4,8,3,7]`
  - Output: `49`
- Input: `height = [1,1]`
  - Output: `1`

#### Constraints
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

#### Function Signature
```python
def maxArea(height: List[int]) -> int:
```

#### High-Level Algorithm
1. **Initialization**:
   - Set two pointers `i` and `j` at the beginning and end of the `height` array.
   - Initialize `max_area` to a very small value.
2. **Two-pointer Technique**:
   - While `i` is less than `j`:
     - Calculate the width of the container as `j - i`.
     - Determine the height of the container by taking the minimum of `height[i]` and `height[j]`.
     - Calculate the current area as `width * height`.
     - Update `max_area` if the current area is larger.
     - Move the pointer pointing to the shorter line inward, because moving the taller line inward would not increase the area.
3. **Output**:
   - Return the `max_area`.

