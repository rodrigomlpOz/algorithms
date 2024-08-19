### Problem Description:

Given a sorted and rotated array, the goal is to find the index of the smallest element in the array. This element represents the point where the rotation occurs.

### Example:

```plaintext
Input: [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
Output: 4  # The index of the smallest element, 103
```

### Explanation:

- The input array is originally sorted but has been rotated at some pivot unknown to you. The smallest element is the pivot point in the rotated array.
- The problem is to find the index of this smallest element using binary search.

### Function Signature:

```python
def val_equal_index(arr: List[int]) -> int:
    pass
```

### Function Call:

```python
arr = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
result = val_equal_index(arr)
print(result)  # Expected output: 4 (index of 103)
```

### High-Level Approach:

1. **Binary Search Logic:**
    - The array is sorted and rotated, so it contains two increasing sequences separated by the smallest element (the pivot).
    - Utilize binary search to find this pivot.

2. **Steps:**
    - Start by initializing two pointers, `l` and `h`, at the start and end of the array.
    - Calculate the midpoint (`mid`).
    - Depending on the comparison between `arr[mid]` and `arr[h]`, decide whether to move left or right.
    - The loop continues until the two pointers converge, indicating the position of the smallest element.

3. **Edge Cases:**
    - The array might have only one element.
    - The array might not be rotated at all (completely sorted).

The solution employs binary search, resulting in an efficient `O(log n)` time complexity.
