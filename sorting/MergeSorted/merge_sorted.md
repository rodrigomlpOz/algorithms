### Problem Statement

You are given two sorted arrays:
- `A` of size `m + n` where the first `m` elements are sorted, and the remaining `n` elements are zeros (reserved space for merging).
- `B` of size `n` where all `n` elements are sorted.

The task is to merge array `B` into `A` so that the resulting array remains sorted. The merged result should be placed in array `A`.

### Function Definition

```python
def intersection(A, m, B, n):
    """
    Merges two sorted arrays A and B into array A.
    
    Args:
    A : list
        A sorted array of size m + n, where the first m elements are sorted and
        the remaining n elements are zeros (reserved space for merging).
    m : int
        The number of valid elements in array A.
    B : list
        A sorted array of size n.
    n : int
        The number of elements in array B.
        
    Returns:
    None. (The result is merged in place into A)
    """
```

### High-Level Implementation

1. **Pointers Initialization**: 
   Initialize two pointers `a` and `b` that point to the last valid elements in arrays `A` and `B` respectively. Also, initialize a `write_idx` pointer to the last position in array `A` (i.e., index `m + n - 1`).
   
2. **Compare and Merge**: 
   Iterate through both arrays starting from the end:
   - If the current element in `A` is larger, move it to the `write_idx` position.
   - Otherwise, move the current element from `B` to `write_idx`.
   - Decrease the respective pointers (`a` or `b`) and the `write_idx` after each operation.

3. **Remaining Elements of B**: 
   If any elements in `B` are left (i.e., `b` is not yet exhausted), copy the remaining elements into `A`.

4. **In-Place Merge**: 
   The merge happens in place in array `A`, so no additional space is used beyond the input.



### Explanation of Example
Given `arr1 = [5, 13, 17, 0, 0, 0, 0, 0]` and `arr2 = [3, 7, 11, 19]`, after merging, the resulting array will be `[3, 5, 7, 11, 13, 17,
