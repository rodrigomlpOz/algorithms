Here is the problem statement, function definition, example function calls, and a high-level solution for **"Maximum Sum Subarray of Size K"**.

### Problem Statement:
Given an array of integers and a number `k`, find the maximum sum of any contiguous subarray of size `k`.

### Function Definition:
```python
def max_sum_subarray_of_size_k(k: int, arr: list[int]) -> int:
    pass
```

### Example Function Calls:
```python
# Test case 1
print(max_sum_subarray_of_size_k(3, [2, 1, 5, 1, 3, 2]))  # Output: 9 (subarray [5, 1, 3])

# Test case 2
print(max_sum_subarray_of_size_k(2, [2, 3, 4, 1, 5]))  # Output: 7 (subarray [3, 4])

# Test case 3
print(max_sum_subarray_of_size_k(4, [1, 2, 3, 4, 5, 6]))  # Output: 18 (subarray [3, 4, 5, 6])
```

### High-Level Solution:
1. **Initialize variables:**
   - Start with a variable `window_sum` to keep track of the sum of the current window, initialized to 0.
   - Use a variable `max_sum` to store the maximum sum encountered, initialized to negative infinity or 0.

2. **Expand the window:**
   - Iterate through the array, adding each element to `window_sum`.

3. **Check the window size:**
   - When the number of elements in the window reaches `k`, update `max_sum` with the maximum value between the current `max_sum` and `window_sum`.

4. **Slide the window:**
   - Subtract the element that is leaving the window (i.e., the element at the left end of the window).
   - Move the left side of the window forward by one position.

5. **Continue sliding until the end of the array is reached.**

6. **Return the maximum sum found (`max_sum`).**

### Final Solution Code:
Here is how the implementation would look:

```python

```

### Example Walkthrough:
For the array `[2, 1, 5, 1, 3, 2]` with `k = 3`:

1. **Initial window:** `[2, 1, 5]` → Sum = 8 → `max_sum = 8`
2. **Slide the window:** `[1, 5, 1]` → Sum = 7 → `max_sum = 8`
3. **Slide the window:** `[5, 1, 3]` → Sum = 9 → `max_sum = 9`
4. **Slide the window:** `[1, 3, 2]` → Sum = 6 → `max_sum = 9`

The function returns `9` as the maximum sum for a subarray of size `3`.