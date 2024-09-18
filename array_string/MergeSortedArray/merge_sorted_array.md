### Problem Definition:

You are given two sorted arrays `nums1` and `nums2`, where `nums1` has a length that is sufficient to accommodate all elements from both arrays (i.e., the size of `nums1` is `m + n`, where `m` is the number of elements in `nums1`, and `n` is the number of elements in `nums2`). The task is to merge `nums2` into `nums1` as one sorted array **in-place**.

### Function Definition:

```python
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merges two sorted arrays, nums1 and nums2, into nums1 in-place.
    
    :param nums1: List[int] - The first sorted list, with a size of m + n
    :param m: int - The number of elements in nums1
    :param nums2: List[int] - The second sorted list
    :param n: int - The number of elements in nums2
    :return: None - Modifies nums1 in-place
    """
    # Your code here
```

### Approach:

The trick here is to merge the arrays **from the end** to avoid overwriting elements in `nums1` before they are moved. We use three pointers:
- `p1` points to the last element of the first `m` elements of `nums1`.
- `p2` points to the last element of `nums2`.
- `p` points to the last position in `nums1` (which is `m + n - 1`).

Starting from the end of `nums1`, we compare the elements from `nums1` and `nums2`, placing the larger element at position `p` and then decrementing the appropriate pointer. This way, we can merge the arrays without needing additional space.

### Code Implementation:


### Explanation:

1. **Initialization:**
   - `p1` starts from the last valid element of `nums1` (i.e., `m - 1`).
   - `p2` starts from the last element of `nums2` (i.e., `n - 1`).
   - `p` starts from the last position in `nums1`, which is `m + n - 1`.

2. **Merging from the End:**
   - Compare `nums1[p1]` and `nums2[p2]`. Place the larger of the two at `nums1[p]`.
   - Decrement the respective pointer (`p1` or `p2`), as well as `p`.

3. **Handling Remaining Elements:**
   - If `nums2` has remaining elements after the main loop, copy them into `nums1` (this happens if all elements of `nums1` have been merged already).
   - There’s no need to move remaining elements from `nums1` because they are already in their correct positions.

### Example Calls:

#### Example 1:
```python
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
```

#### Example 2:
```python
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]
```

#### Example 3:
```python
nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]
```

### Time and Space Complexity:

- **Time Complexity:** `O(m + n)` since we iterate through both `nums1` and `nums2` exactly once.
- **Space Complexity:** `O(1)` because we modify `nums1` in-place and do not use any additional space.

This approach ensures that the two sorted arrays are merged efficiently without extra memory usage, which is crucial for problems that require in-place solutions.
