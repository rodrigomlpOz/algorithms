### Problem Description:

You want to find the integer square root of a given number `num`. The integer square root is the largest integer `x` such that `x * x <= num`. For example, the integer square root of 300 is 17, because \( 17^2 = 289 \) and \( 18^2 = 324 \), which exceeds 300.

### Example:

```plaintext
Input: num = 300
Output: 17
```

### Function Signature:

```python
def val_equal_index(num: int) -> int:
    pass
```

### Function Call:

```python
num = 300
ans = val_equal_index(num)
print(ans)  # Expected output: 17
```

### High-Level Approach:

1. **Binary Search Logic:**
    - The problem can be solved using binary search, as the function \( f(x) = x^2 \) is monotonically increasing.
    - We aim to find the largest integer `mid` such that \( mid^2 \leq num < (mid+1)^2 \).

2. **Steps:**
    - Initialize two pointers, `l` (low) and `h` (high), representing the search space.
    - Calculate the midpoint `mid`.
    - Check if \( mid^2 \) is less than or equal to `num` and \( (mid+1)^2 \) is greater than `num`. If true, return `mid`.
    - If \( mid^2 \) is greater than `num`, narrow the search space to the left half by updating `h = mid - 1`.
    - Otherwise, search the right half by updating `l = mid + 1`.

3. **Edge Cases:**
    - The input `num` might be very small (e.g., 0 or 1).
    - The input `num` might be a perfect square.
